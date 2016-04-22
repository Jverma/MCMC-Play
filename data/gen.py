import numpy as np 
import matplotlib.pyplot as plt 
from sys import exit

np.random.seed(250192)

def LinearData(X=np.linspace(100, 200, 25), m=1.0, c=0.0, RedStd=0.05):
	Y = (m*X + c) * np.random.normal(loc=1.0, scale=RedStd, size=len(X))
	return [X, Y, Y*(RedStd)]

def WriteLinearFile(X=np.linspace(100, 200, 25), m=1.0, c=0.0, RedStd=0.05, plot=False):
	filename = 'Linear_m%1.2f_c%1.2f_sd%1.2f_size%i.csv'%(m, c, RedStd, len(X))
	data = LinearData(X, m, c, RedStd)
	np.savetxt(filename, np.transpose(np.array(data)), delimiter=',', header='x, y, y_err')
	if plot:
		plt.errorbar(data[0], data[1], data[2], color='k', ls='', ms=14)
		plt.show()
	return filename

def QuadraticData(X=np.linspace(100, 200, 25), a=1.0, b=1.0, c=0.0, RedStd=0.05):
	Y = (a*X**2 + b*X + c) * np.random.normal(loc=1.0, scale=RedStd, size=len(X))
	return [X, Y, Y*(RedStd)]

def WriteQuadraticFile(X=np.linspace(100, 200, 25), a=1.0, b=1.0, c=0.0, RedStd=0.05, plot=False):
	filename = 'Quadratic_a%1.2f_b%1.2f_c%1.2f_sd%1.2f_size%i.csv'%(a, b, c, RedStd, len(X))
	data = QuadraticData(X, a, b, c, RedStd)
	np.savetxt(filename, np.transpose(np.array(data)), delimiter=',', header='x, y, y_err')
	if plot:
		plt.errorbar(data[0], data[1], data[2], color='k', ls='', ms=14)
		plt.show()
	return filename

#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	WriteLinearFile(plot=False)
	WriteQuadraticFile(plot=False)
