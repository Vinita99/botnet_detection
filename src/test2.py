import loaddata
import dataprep
import pickle
import numpy
import codecs

file=open('C:\\Users\\KOTRESHA\\Desktop\\Mastering-Machine-Learning-for-Penetration-Testing-master\\Chapter05\\flowdata.pickle','rb')
data=pickle.load(file,encoding="bytes")
Xdata=data[0]
Ydata=data[1]
XdataT=data[2]
YdataT=data[3]
print(XdataT)