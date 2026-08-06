# Introduction 
Assessing the feasibility of foundational forecasting models and analyzing when they’re best utilized for the ease of access they provide in their implementation.


# Used models
Control: Naive/seasonal naive
Traditional: SARIMA
ML Based: LightGBM, XGBoost
Deep Learning based: LSTM, NHiTS

Foundational models: TTM-1, Lag Llama, Chronos

# Hypotheses
### H<sub>1</sub>
Foundation models significantly outperform classical and ML models on small datasets.

### H<sub>2</sub>
Performance advantage decreases as dataset size increases.

### H<sub>3</sub>
Foundation models provide larger gains for long forecast horizons.

### H<sub>4</sub>
Domain-specific datasets reduce foundation model effectiveness.

### H<sub>5</sub>
When implementation effort is considered, foundation models provide higher overall value than raw accuracy alone.

### H<sub>6</sub>
Foundation forecasting models do not achieve significantly different forecasting accuracy than machine learning and deep learning models regardless of covariate availability.


# Datasets
## Favorita retail dataset
https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting
### Forecast Horizons
7/14/28 days

## M4 Finance dataset
https://github.com/Mcompetitions/M4-methods
### Forecast Horizon
2/4/8 hours for hourly observations
5/10/20 days for daily observations
4/8/12 weeks for weekly observations
3/6/12 months for monthly observations
2/4/8 quarters for quarterly observations
5/10/20 years for yearly observations

## Electricity energy dataset
https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014
### Forecast Horizon
24/168 hours


## LA traffic dataset
https://github.com/liyaguang/DCRNN
### Forecast Horizon
1/2/4 hours (12/24/48 steps of 5 minute intervals)


## FAOSTAT agricultural dataset
https://www.fao.org/faostat/en/#data/QCL
### Forecast Horizon
1/3/5 years


# Evaluation metrics
## Primary
MAE
SMAPE

## Secondary
RMSE