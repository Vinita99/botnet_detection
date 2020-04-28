from sklearn import linear_model
from sklearn import tree 
from sklearn import naive_bayes 
from sklearn import neighbors
import loaddata
import dataprep
import test1,test2,test3
#import demo1
Xdata,Ydata,XdataT,YdataT=loaddata.loaddata('E:\\CTU-13-Dataset\\CTU-13-Dataset\\CTU-13-Dataset\\8\\capture20110816-3.binetflow')


#with open("E:\\CTU-13-Dataset\\CTU-13-Dataset\\CTU-13-Dataset\\8\\capture20110816-3.binetflow", "r") as filestream:
 #   with open("answers.txt", "w") as filestreamtwo:
with open("E:\\CTU-13-Dataset\\CTU-13-Dataset\\CTU-13-Dataset\\8\\capture20110816-3.binetflow", "r") as a,open("answers.txt", "w") as b:
    for line in a:
        currentline = line.split(",")
        total = [str(currentline[0]),str(currentline[1]),str(currentline [2]),str(currentline[3]),str(currentline[4]),str(currentline [5]),str(currentline[6]),str(currentline[7]),str(currentline [8]),str(currentline[9]),str(currentline[10]),str(currentline[11]),str(currentline[12]),str(currentline[13]),str(currentline [14])]
        print(len(total))
        clf = tree.DecisionTreeClassifier()
        clf.fit(Xdata,Ydata)
        Prediction=clf.predict(total)
        Score = clf.score(total,YdataT)
        if Score>90:
            b.write(total[3])
            print(" BOT\n")
        elif Score<90 and Score>80:
            b.write(total[3])
            print("POTENTIAL BOT\n")
        else:
            b.write(total[3])
            print("NOT A BOT\n")

