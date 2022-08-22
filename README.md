### Predictive Maintanance of TurboJet Engine(Classification Problem)
# Description
Prognostics and health management is an important topic in industry for predicting state of assets to avoid downtime and failures. This data set is the version of the very well known asset degradation modeling from NASA. It includes Run-to-Failure simulated data from turbo jet engines. Engine degradation simulation was carried out using C-MAPSS. Four different were sets simulated under different combinations of operational conditions and fault modes. Records several sensor channels to characterize fault evolution. The data set was provided by the Prognostics CoE at NASA Ames.

# Prediction Goal
In this dataset the goal is to predict the remaining useful life (RUL) of each engine in the test dataset. RUL is equivalent of number of flights remained for the engine after the last datapoint in the test dataset.

# Pipeline Followed For This project
![image](https://user-images.githubusercontent.com/85065063/185973862-9690b034-92ce-4cb7-bc79-556bd20657b2.png)

# Code Flow
![image](https://user-images.githubusercontent.com/85065063/185974023-47ca7735-5cf3-473c-bb2a-0b13cc30fb7b.png)

# Data Description.
The engine is operating normally at the start of each time series, and develops a fault at some point during the series. In the training set, the fault grows in magnitude until system failure. In the test set, the time series ends some time prior to system failure. The objective is to predict Remaining Useful Life (RUL).
The data are provided as a zip-compressed text file with 26 columns of numbers, separated by spaces. Each row is a snapshot of data taken during a single operational cycle, each column is a different variable. The columns correspond to:
1) unit number                           
2) time, in cycles
3) operational setting 1
……..
26) operational setting 21



