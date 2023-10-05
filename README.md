![DOI](https://zenodo.org/badge/534699890.svg)
# Dimensionality Reduction and Cluster identification of SARS-CoV-2 extracted features
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
