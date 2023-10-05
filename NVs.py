import numpy as np
from more_itertools import windowed
from collections import defaultdict # OrderedDict 
from itertools import combinations, product


def seq_creation(x, alphabet=list('ACGT')):
    '''
    Creation of random sequences
    '''
    
    return ''.join(np
                   .random
                   .choice(alphabet, 
                           x,
                          )
                  )    


def NV(seq, alphabet=list('ACGT'), db_weights=True):
    '''
    Natural Vectors
    Deng et al. 2011
    doi:10.1371/journal.pone.0017293
    Yu et al. 2013
    doi:10.1371/journal.pone.0064328
    '''

    seq = seq.upper()
    N = len(seq)
    j = 2
    weights = {'A': ['RWM', 'DHV'],
               'C': ['YSM', 'BHV'],
               'G': ['RSK', 'BDV'],
               'T': ['YWK', 'BDH']}
    def W_matrix(k, nt):
        if db_weights: 
            weight=1 if nt==k else 1/4 if nt=='N' else 0
            if not weight: 
                weights0, weights1 = weights[k]
                weight = 1/2 if nt in weights0 else 1/3 if nt in weights1 else 0
        else:
            weight = nt==k
        return weight 
    def W(k): return np.array([W_matrix(k, nt) for nt in seq])
    def T(k): return np.array([n if i else 0 for n, i in enumerate(W(k))])
    def n(k): return sum(W(k))
    def µ(k): return (sum([t*w for t, w in zip(T(k), W(k))])/n(k)) # µ=alt+230
    def D(k): return (sum((T(k)-µ(k))**j*W(k))/(n(k)**(j-1)*N**(j-1)))
    
    funcs = [['n', n], ['µ', µ], ['D', D]]
    
    nv = {}
    for name, func in funcs:
        for nt in sorted(alphabet):
            key = f'{name}_{nt}'
            nv[key] = func(nt)
            
    return nv


def ANV(seq, alphabet=list('ACGT')):
    '''
    Accumulated Natural Vectors 
    Dong et al. 2019
    '''
    
    N = len(seq)
    
    def u(k): return [k==nt for nt in seq]
    def n(k): return sum(u(k))
    def û(k): return np.cumsum(u(k), 
                    axis=0) # û = alt+0251
    def Θ(k): return sum(û(k)/N) # Θ = alt+233
    
    def µ(k): return np.mean([n for n, p in enumerate(
                    [k==nt for nt in seq], 1) if p]) # µ = alt+230
    def Ω(k): return (-n(k)*µ(k))+((N+1)*n(k)) # Ω = alt+234
    def δ(k): return Ω(k)/n(k) # δ = alt+235
    def Cov(k0, k1): return sum(((û(k0)-Θ(k0))*(û(k1)-Θ(k1))))/(n(k0)*n(k1))
    def D(k): return sum(((û(k)-Θ(k))**2))/(n(k)**2)

    funcs = [['n', n], ['δ', δ], ['D', D]]

    anv = dict()
    for name, func in funcs:
        for nt in sorted(alphabet):
            key = f'{name}_{nt}'
            anv[key] = func(nt)
            
    for nt0, nt1 in combinations(alphabet, 2):
        key = f'Cov_{nt0}{nt1}'
        anv[key] = Cov(nt0, nt1)

    return anv


def WMRV(seq, alphabet=list('ACGT')): 
    '''
    Previously called Keto-Amino-Strong Vectors (KASV) 
    and before Purine-Pyraminine-Keto Vectors (PPKV)
    Li et al. 2017
    DOI:10.1038/s41598-017-12493-2
    '''
    
    N = len(seq)
    j = 2
    
    def SW(k): return 'W' if k in 'AT' else 'S'
    def MK(k): return 'M' if k in 'AC' else 'K'
    def RY(k): return 'R' if k in 'AG' else 'Y'
    
    def T(k, s): return [n for n, p in enumerate(
                        [k==nt for nt in s]) if p]
    def n(k, s): return len(T(k, s))
    def µ(k, s): return np.mean(T(k, s))
    def D(k, s): return ((T(k,s)-µ(k,s))**j/
                      (n(k,s)**(j-1)*N**(j-1))).sum()
        
    codings = [['RY', RY],
               ['MK', MK],
               ['SW', SW]]
    
    funcs = [['n', n], ['µ', µ], ['D', D]]
    
    wmrv = dict()
    for code_alphabeth, coding in codings:
        coded_seq = list(map(coding, seq))
        for name, func in funcs:
            for nt in code_alphabeth:
                key = f'{name}_{nt}'
                wmrv[key] = func(nt, coded_seq)
            
    return wmrv
    
    
def PCNV(seq, alphabet=list('ACGT')):
    '''
    Positional Correlation Natural Vector
    He et al. 2020
    '''
    N = len(seq)
    def mask(k): return [k==nt for nt in seq]
    def P(k): return [n for n, p in enumerate(mask(k), 1) if p]
    def n(k): return len(P(k))
    def cumsum_mask(k): return np.cumsum(mask(k))
    def diff_P(k): return np.diff(P(k))
    def Un(k): return (0 if i-1<0 else P(k)[i-1] 
                       for i in cumsum_mask(k))
    def Ud(k): return (0 if i-1<0 else P(k)[i]-P(k)[i-1] 
                       if i<n(k) else N-(P(k)[-1]-1) 
                       for i in cumsum_mask(k))
    def U(k): return np.array([n/d if d!=0 else 0 
                               for n, d in zip(Un(k), Ud(k))])
    def Û(k): return sum(P(k))/N # Û = alt+0219 #U(k).sum()/N
    def diff_U(k): return U(k)-Û(k)
    def K(k): return U(k).sum()/n(k)
    def cov(k0, k1): return (((diff_U(k0)*diff_U(k1)).sum())/
                             (n(k0)*n(k1)))
    def D(k): return ((diff_U(k)**2).sum())/(n(k)**2)

    funcs = [['n', n], ['K', K], ['D', D]]

    pcnv = dict()
    for name, func in funcs:
        for nt in sorted(alphabet):
            key = f'{name}_{nt}'
            pcnv[key] = func(nt)
#             print(f'Finished: {key}')

    for nt0, nt1 in combinations(alphabet, 2):
        key = f'cov_{nt0}{nt1}'
        pcnv[key] = cov(nt0, nt1)
#         print(f'Finished: {key}')

    return pcnv

    
def KMNV(seq, k=3, alphabet=list('ACGT')):
    '''
    K-Mer Natural Vectors
    Wen et al. 2014
    http://dx.doi.org/10.1016/j.gene.2014.05.043
    '''
    
    L = len(seq)
    m = 2
    km_seq = [''.join(w) 
              for w in windowed(list(seq), k)
             ]
    words = [''.join(w) 
             for w in product(alphabet, repeat=k)
            ]

    def l(w): return np.array([n for n, p 
                               in enumerate([w==km 
                                             for km 
                                             in km_seq
                                            ]
                                           ) if p
                              ]
                             )
    def n(w): return len(l(w))
    def µ(w): return (np.mean(l(w)) 
                      if n(w)!=0 
                      else 0
                     )
    def D(w): return ((((l(w)-µ(w))**m
                       ).sum()
                       / (n(w)**(m-1)
                          *(L-k+1)**(m-1)
                         )
                      )
                      if n(w)!=0 
                      else 0
                     )

    funcs = [['n', n], ['µ', µ], ['D', D]]
    front_zeros = len(str(len(words)))
    kmer_words = sorted(words)
    
    kmnv = dict()
    for name, func in funcs:
        for word in kmer_words:
            key = f'{name}_{word}'
            kmnv[key] = func(word)
    
    return kmnv


def CMNV(seq, alphabet=list('ACGT'), with_gaps=True):
    '''
    Extended idea of Natural Vectors 
    With complete central moments: skewness and kurtosis
    Deng et al. 2011    
    doi:10.1371/journal.pone.0017293
    '''
    if not with_gaps:
        seq = seq.replace('-','')
    seq = seq.upper()
    N = len(seq)
    j_range = range(2,5)
    weights = {'A': ['RWM', 'DHV'],
               'C': ['YSM', 'BHV'],
               'G': ['RSK', 'BDV'],
               'T': ['YWK', 'BDH']}
    def W_matrix(k,nt):
        weight = 1 if nt==k else 1/4 if nt=='N' else 0
        if not weight: 
            weights0, weights1 = weights[k]
            weight = 1/2 if nt in weights0 else 1/3 if nt in weights1 else 0
        return weight 
    def W(k): return np.array([W_matrix(k, nt) for nt in seq])
    def T(k): return np.array([n if i else 0 for n, i in enumerate(W(k))])
    def n(k): return sum(W(k))
    def µ(k): return (sum([t*w for t, w in zip(T(k), W(k))])/n(k)) # µ=alt+230
    def D(k, j): return (sum((T(k)-µ(k))**j*W(k))/(n(k)**(j-1)*N**(j-1)))
    
    funcs = [['n', n], ['µ', µ]]
    
    cmnv = dict()
    for name, func in funcs:
        for nt in sorted(alphabet):
            key = f'{name}_{nt}'
            cmnv[key] = func(nt)
    
    for j in j_range:
        for nt in sorted(alphabet):
            key = f'D{j}_{nt}'
            cmnv[key] = D(nt, j)
            
    return cmnv
    

def KMC(seq, k, alphabet=list('ACGT'), with_gaps=True):
    '''
    k-mer Count
    '''
    
    if not with_gaps:
        seq = seq.replace('-','')
    seq = seq.upper()
    words = [''.join(w) for w in product(alphabet, repeat=k)]
    seq = [''.join(w) for w in windowed(list(seq), k)]
    return {key:sum([kmer==key for kmer in seq]) for key in words}
    
def KMP(seq, k, with_gaps=True):
    '''
    k-mer Probability
    '''
    
    if not with_gaps:
        seq = seq.replace('-','')
    N = len(seq)
        
    seq = seq.upper()
    
    # seq length by kmers, 1 prevent error for gaps only
    kmers_seq = max(1, N-k+1) 
    
    return {ky:float(vl)/kmers_seq for ky, vl in KMC(seq, k).items()}  

def FCGR(seq, k):
    '''
    From:
    Boštjan Cigan
    https://towardsdatascience.com/chaos-game-representation-of-a-genetic-sequence-4681f1a67e14
    data from: https://www.ncbi.nlm.nih.gov/genbank/, NC_012920.1
    '''
    
    array_size = int(np.sqrt(4**k))
    fcgr = np.zeros([array_size]*2)

    maxx = maxy = array_size
    posx = posy = 1

    for key, value in KMP(seq, k).items():
        for char in key:
            if char == "T": 
                posx += maxx / 2
            elif char == "C": 
                posy += maxy / 2
            elif char == "G":
                posx += maxx / 2
                posy += maxy / 2
            maxx /= 2
            maxy /= 2
        fcgr[-int(posy)][-int(posx)] = value
        maxx = maxy = array_size
        posx = posy = 1
        
    return fcgr

def ENV(seq, k=3, intensity_range=256):
    '''
    Extended Natural Vectors
    using Frequency Chaos Game Representation
    Wen et al. 2014
    '''
    
    N = (2**k)**2 # len(seq)
    chaos = FCGR(seq, k)
    chaos = np.nan_to_num(np.round(chaos / 
                                   np.amax(chaos)*
                                   (intensity_range-1)
                                   )
                         ).astype(int)
    X = {str(n):[] for n in range(intensity_range)}
    for y, row in enumerate(chaos):
        for x, val in enumerate(row):
            X[str(val)].append([y,x])
    
    n = {f'n_{k}':len(v) for k, v in X.items()}
    µ = {k:np.mean(v, axis=0) if len(v)!=0 else np.zeros(2) 
                                     for k, v in X.items()}
    µ1 = {f'µ1_{k}':v[0] for k, v in µ.items()}
    µ2 = {f'µ2_{k}':v[1] for k, v in µ.items()}
    X = {k:[[0,0]] if len(v)==0 else v for k, v in X.items()}

    rs = [x for x in list(product(range(3), repeat=2)) 
                                              if sum(x)==2]

    D = dict()
    for r, s in rs:
        for val in range(intensity_range):
            val = str(int(val))
            i, j = X[val][0] if len(X[val])==1 else np.array(X[val]).T
            D[f'D{r}{s}_{val}'] = (np.sum((((i-µ1[f'µ1_{val}'])**r) * 
                                          ((j-µ2[f'µ2_{val}'])**s)
                                          ) /
                                          ((n[f'n_{val}']**(r+s)) *
                                          (N**(r+s-1))
                                          )
                                         )
                                  ) if n[f'n_{val}']!=0 else 0
    ENV = dict()
    for element in [n, µ1, µ2, D]:
        ENV.update(element)
    
    return ENV