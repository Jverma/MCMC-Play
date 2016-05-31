import numpy as np 
import matplotlib.pyplot as plt 
from sys import exit

np.random.seed(250192)

def LinearData(X=np.linspace(-10, 10, 25), m=5.0, c=25.0, RedStd=5.0):
	delta = np.random.uniform(low=-1*RedStd, high=RedStd, size=len(X))
	# print delta
	Y = (m*X + c) + delta
	return [X, Y, delta]

def WriteLinearFile(X=np.linspace(-10, 10, 25), m=5.0, c=25.0, RedStd=5.0, plot=False):
	filename = 'Linear_m%1.2f_c%1.2f_sd%1.2f_size%i.csv'%(m, c, RedStd, len(X))
	data = LinearData(X, m, c, RedStd)
	np.savetxt(filename, np.transpose(np.array(data)), \
				delimiter=',', header='x,y,y_err', fmt='%1.5f,%1.5f,%1.5f')
	if plot:
		plt.errorbar(data[0], data[1], data[2], color='k', ls='', ms=14)
		plt.show()
	return filename

def QuadraticData(X=np.linspace(-10, 10, 25), a=5.0, b=10.0, c=25.0, RedStd=5.0):
	delta = np.random.uniform(low=-1*RedStd, high=RedStd, size=len(X))
	print delta
	Y = (a*X**2 + b*X + c) + delta
	return [X, Y, delta]

def WriteQuadraticFile(X=np.linspace(0, 20, 25), a=1.0, b=10.0, c=25.0, RedStd=25.0, plot=False):
	filename = 'Quadratic_a%1.2f_b%1.2f_c%1.2f_sd%1.2f_size%i.csv'%(a, b, c, RedStd, len(X))
	data = QuadraticData(X, a, b, c, RedStd)
	np.savetxt(filename, np.transpose(np.array(data)), \
				delimiter=',', header='x,y,y_err', fmt='%1.5f,%1.5f,%1.5f')
	if plot:
		plt.errorbar(data[0], data[1], data[2], color='k', ls='', ms=14)
		plt.show()
	return filename

#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	WriteLinearFile(plot=True)
	WriteQuadraticFile(plot=True)
