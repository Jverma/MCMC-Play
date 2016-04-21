from numpy import genfromtxt,transpose,random,exp,mean,std,array
from numpy import histogram, histogram2d,savetxt,zeros,diag,any
import numpy
import scipy.optimize as so
import pylab
import matplotlib.mlab as mlab
from matplotlib import rc
from mpi4py import MPI
from sys import argv, exit

#----------------------------------------------------------
__author__ = ("Irshad Mohammed <creativeishu@gmail.com>")
#----------------------------------------------------------

class MCMC(object):

	def __init__(self, NumberOfSteps=100000, FittingFunctionType="Linear", \
				NumberOfParams=2, Mins=[0.0,-1.0], Maxs=[2.0,1.0], SDs=[0.5,0.5], \
				datafile="../data/Linear_m1.00_c0.00_sd0.05_size25.txt"):

		if not (NumberOfParams == len(Mins) and \
			NumberOfParams==len(Maxs) and NumberOfParams==len(SDs)):
			print "Length of Mins, Maxs and SDs should be same as NumberOfParams"
			exit()

		self.outputfilename='mcmc.output'
		self.NumberOfSteps = NumberOfSteps
		self.NumberOfParams = NumberOfParams
		self.mins = array(Mins)
		self.maxs = array(Maxs)
		self.SD = array(SDs)
		self.CovMat = diag(self.SD**2)
		self.FittingFunctionType = FittingFunctionType

		data = genfromtxt(datafile)
		self.Xdata = data[:,0]
		self.Ydata = data[:,1]
		self.Edata = data[:,2]

#----------------------------------------------------------
		
	def FirstStep(self):
		return self.mins + \
				random.random(self.NumberOfParams)*\
				(self.maxs - self.mins)

	def NextStep(self,Oldstep):
		NS = random.multivariate_normal(Oldstep,self.CovMat)
		while any(NS<self.mins) or any(NS>self.maxs):
			NS = random.multivariate_normal(Oldstep,self.CovMat)
		return NS

	def MetropolisHastings(self,Oldchi2,Newchi2):
		likelihoodratio = exp(-(Newchi2-Oldchi2)/2)
		if likelihoodratio < random.random():
			return False
		else:
			return True

	def MainChain(self):
		OldStep = self.FirstStep()
		Oldchi2 = self.chisquare(OldStep)
		outfile = open(self.outputfilename,'w')
		writestring = '%1.6f \t'*self.NumberOfParams

		multiplicity = 0
		acceptedpoints = 0
		for i in range(self.NumberOfSteps):
			multiplicity += 1
			NewStep = self.NextStep(OldStep)
			Newchi2 = self.chisquare(NewStep)

			GoodPoint = self.MetropolisHastings(Oldchi2,Newchi2)

			if not GoodPoint:
				continue
			else:
				print >>outfile, '%1.6f \t'%Newchi2,'%i \t'%multiplicity,\
								writestring%tuple(NewStep)
				acceptedpoints += 1
				multiplicity = 0
				Oldstep = NewStep
				Oldchi2 = Newchi2

		return float(acceptedpoints)/i

	def FittingFunction(self, x, a=1.0, b=1.0, c=1.0, d=1.0, e=1.0):
		if self.FittingFunctionType=="Linear":
			return a*x + b
		elif self.FittingFunctionType=="Quadratic":
			return a*x**2 + b*x + c
		else:
			print "Please enter a valid Fitting Function: Linear or Quadratic"
			exit()

	def chisquare(self, Params):
		Ytrial = self.FittingFunction(self.Xdata, *Params)
		chi2 = ((Ytrial - self.Ydata)/self.Edata)**2
		return numpy.sum(chi2)

#==============================================================================

if __name__=="__main__":
	# obj = MCMC()
	# obj.MainChain()
	chain = genfromtxt('mcmc.output')
	pylab.plot(chain[:,2], chain[:,3])
	pylab.show()

