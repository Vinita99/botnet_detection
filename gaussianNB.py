from sklearn.linear_model import LogisticRegression
from sklearn import tree 
from sklearn.naive_bayes import GaussianNB 
from sklearn import neighbors
import loaddata
import dataprep
import test1,test2,test3
Xdata,Ydata,XdataT,YdataT=loaddata.loaddata('E:\\CTU-13-Dataset\\CTU-13-Dataset\\CTU-13-Dataset\\8\\capture20110816-3.binetflow')
print(Xdata)
print(Ydata)
print(XdataT)
print(YdataT)
clf = GaussianNB()
clf.fit(Xdata,Ydata)
Prediction = clf.predict(XdataT)
Score = clf.score(XdataT,YdataT)
print("The Score of the Gaussian Naive Bayes classifier is", Score * 100)