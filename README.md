![DOI](https://zenodo.org/badge/534699890.svg)
# Dimensionality Reduction and Cluster identification of SARS-CoV-2 extracted features
## Exercise with a ~5% subsample of GISAID 

Supporting materials for paper: Unsupervised identification of significant lineages of SARS-CoV-2 through scalable machine learning methods.

1. Install environment:\
conda env create --file dimredcovid19.yml

2. If there are throubles installing PaCMAP module, install module ANNOY with the WHL file:\
pip install annoy-1.17.0-cp310-cp310-win_amd64.whl

3. Extract the folder 'GISAID_Subsample' from file GISAID_Subsample.7z within the same folder

4. Activate environment and run jupyter notebook:\
conda activate dimredcovid19
jupyter notebook

5. Follow the jupyter notebook for more instructions:\
Dimensionality_Reduction_Covid19.ipynb

## Interactive plots of paper: Unsupervised identification of significant lineages of SARS-CoV-2 through scalable machine learning methods.
Figure 1: 3d PaCMAP projection and clustering analysis of genetic topology of roughly 5.7 million sequences extracting $3mc$ feature. Plotting only 1% due to graphic processing costs.
1. [Top: Coulored by Scorpio labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/3MC_PaCMAP_1pctProjectionGISAID_ColouredBy-scorpio.html)
2. [Bottom-left: Coloured by HDBSCAN labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/3MC_PaCMAP_1pctProjectionGISAID_ColouredBy-hdbscan.html)
3. [Bottom-right: Coloured by CLASSIX labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/3MC_PaCMAP_1pctProjectionGISAID_ColouredBy-classix.html)

Figure 2: 3d PaCMAP projection of specific structural protein regions for about 5.7 million sequences, generated using 3mc. Coulored by Scorpio labelling. Plotting only 1% due to graphic processing costs.
1. [Gen S](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/3MC_S_PaCMAP_1pctProjectionGISAID_ColouredBy-scorpio.html)
2. [Gen N](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/3MC_N_PaCMAP_1pctProjectionGISAID_ColouredBy-scorpio.html)
3. [Gen M](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/3MC_M_PaCMAP_1pctProjectionGISAID_ColouredBy-scorpio.html)
4. [Gen E](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/3MC_E_PaCMAP_1pctProjectionGISAID_ColouredBy-scorpio.html)

## Interactive plots of Suplemmentary Information of paper: : Unsupervised identification of significant lineages of SARS-CoV-2 through scalable machine learning methods.

Figure S1: 3d PaCMAP projection (parameters: $NB=51$, $MN=0.25$ and $FP=4$) of the whole GISAID dataset extracting the $env$ feature
1. [Top: Coulored by Scorpio labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/ENVk3_PaCMAP_1pctProjectionGISAID_ColouredBy-scorpio.html)
2. [Bottom-left: Coloured by HDBSCAN labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/ENVk3_PaCMAP_1pctProjectionGISAID_ColouredBy-hdbscan.html)
3. [Bottom-right: Coloured by CLASSIX labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/ENVk3_PaCMAP_1pctProjectionGISAID_ColouredBy-classix.html)

Figure S2: 3d PaCMAP projection (parameters: $NB=51$, $MN=0.25$ and $FP=2$) of the whole GISAID dataset extracting the $3mnv$ feature
1. [Top: Coulored by Scorpio labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/3MNV_PaCMAP_1pctProjectionGISAID_ColouredBy-scorpio.html)
2. [Bottom-left: Coloured by HDBSCAN labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/3MNV_PaCMAP_1pctProjectionGISAID_ColouredBy-hdbscan.html)
3. [Bottom-right: Coloured by CLASSIX labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/3MNV_PaCMAP_1pctProjectionGISAID_ColouredBy-classix.html)

Figure S3: 3d PaCMAP projection (parameters: $NB=51$, $MN=1$ and $FP=4$) of the whole GISAID dataset extracting the $anv$ feature
1. [Top: Coulored by Scorpio labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/ANV_PaCMAP_1pctProjectionGISAID_ColouredBy-scorpio.html)
2. [Bottom-left: Coloured by HDBSCAN labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/ANV_PaCMAP_1pctProjectionGISAID_ColouredBy-hdbscan.html)
3. [Bottom-right: Coloured by CLASSIX labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/ANV_PaCMAP_1pctProjectionGISAID_ColouredBy-classix.html)

Figure S4: 3d PaCMAP projection (parameters: $NB=51$, $MN=1$ and $FP=2$) of the whole GISAID dataset extracting the $nv$ feature
1. [Top: Coulored by Scorpio labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/NV_PaCMAP_1pctProjectionGISAID_ColouredBy-scorpio.html)
2. [Bottom-left: Coloured by HDBSCAN labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/NV_PaCMAP_1pctProjectionGISAID_ColouredBy-hdbscan.html)
3. [Bottom-right: Coloured by CLASSIX labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/NV_PaCMAP_1pctProjectionGISAID_ColouredBy-classix.html)

Figure S5: 3d PaCMAP projection (parameters: $NB=51$, $MN=50$ and $FP=4$) of the whole GISAID dataset extracting the $wmrv$ feature
1. [Top: Coulored by Scorpio labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/WMRV_PaCMAP_1pctProjectionGISAID_ColouredBy-scorpio.html)
2. [Bottom-left: Coloured by HDBSCAN labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/WMRV_PaCMAP_1pctProjectionGISAID_ColouredBy-hdbscan.html)
3. [Bottom-right: Coloured by CLASSIX labelling](https://raw.githack.com/robcah/dimredcovid19/main/3d_PaCMAP_Projections/WMRV_PaCMAP_1pctProjectionGISAID_ColouredBy-classix.html)