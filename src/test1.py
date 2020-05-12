import pandas as pd 
data=pd.read_csv("E:\\CTU-13-Dataset\\CTU-13-Dataset\\CTU-13-Dataset\\8\\capture20110816-3.binetflow")
data['Label']=data.Label.str.contains("Botnet")
print(data.columns)