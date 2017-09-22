import numpy 
import os
os.listdir(".")
os.chdir('/Users/zoeloh/Desktop/Intro_Biocom_ND_319_Tutorial5')
data = numpy.loadtxt(fname="test.dat",delimiter=" ")
data

data[:,0]==0

data[;,0]>2

data[data[:,0]>2,:]
