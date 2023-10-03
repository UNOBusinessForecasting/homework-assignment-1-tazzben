import pandas as pd
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing
 
data = pd.read_csv("https://github.com/dustywhite7/Econ8310/raw/master/AssignmentData/Assignment2/assignment2.csv")

#check type and convert "Timestamp" to pd datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
 
#Set index and variable 'trips'
x = data['trips']
x.index = data['Timestamp']
x.index.freq = x.index.inferred_freq
 
#model specification
model = ExponentialSmoothing(x, trend='add', seasonal='mul', damped_trend=True)
modelFit = model.fit()
pred=modelFit.forecast(744)
