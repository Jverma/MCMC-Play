import numpy as np 
import matplotlib.pyplot as plt 
from sys import exit

np.random.seed(250192)

def LinearData(X=np.linspace(100, 200, 25), m=1.0, c=0.0, RedStd=0.05):
	Y = (m*X + c) * np.random.normal(loc=1.0, scale=RedStd, size=len(X))
	return [X, Y, Y*(RedStd)]

def WriteLinearFile(X=np.linspace(100, 200, 25), m=1.0, c=0.0, RedStd=0.05):
	filename = 'Linear_m%1.2f_c%1.2f_sd%1.2f_size%i.txt'%(m, c, RedStd, len(X))
	data = LinearData(X, m, c, RedStd)
	np.savetxt(filename, np.transpose(np.array(data)))
	return filename




if __name__ == "__main__":
	WriteLinearFile()
