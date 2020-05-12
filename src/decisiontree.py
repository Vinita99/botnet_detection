from sklearn import linear_model
from sklearn import tree 
from sklearn import naive_bayes 
from sklearn import neighbors
import loaddata
import dataprep
import test1,test2,test3
#import demo1
Xdata,Ydata,XdataT,YdataT=loaddata.loaddata('E:\\CTU-13-Dataset\\CTU-13-Dataset\\CTU-13-Dataset\\8\\capture20110816-3.binetflow')



clf = tree.DecisionTreeClassifier()
clf.fit(Xdata,Ydata)
Prediction=clf.predict(XdataT)
Score = clf.score(XdataT,YdataT)
print("Score is ",Score*100)
            
