from sklearn import linear_model
from sklearn import tree 
from sklearn import naive_bayes 
from sklearn import neighbors 
import dataprep
import loaddata
import test2
Xdata,Ydata,XdataT,YdataT=loaddata.loaddata('E:\\CTU-13-Dataset\\CTU-13-Dataset\\CTU-13-Dataset\\8\\capture20110816-3.binetflow')
dataprep.Prepare(Xdata,Ydata,XdataT,YdataT)