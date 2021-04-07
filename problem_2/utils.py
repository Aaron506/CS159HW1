import numpy as np
import pdb
from scipy.spatial import ConvexHull


class system(object):
	"""docstring for system"""
	def __init__(self, A, B, w_inf, x0):
		self.A     = A
		self.B     = B
		self.w_inf = w_inf
		self.x 	   = [x0]
		self.u 	   = []
		self.w 	   = []
		self.x0    = x0

		self.w_v = w_inf*(2*((np.arange(2**A.shape[1])[:,None] & (1 << np.arange(A.shape[1]))) > 0) - 1)
			
	def applyInput(self, ut):
		self.u.append(ut)
		self.w.append(np.random.uniform(-self.w_inf,self.w_inf,self.A.shape[1]))
		xnext = np.dot(self.A,self.x[-1]) + np.dot(self.B,self.u[-1]) + self.w[-1]
		self.x.append(xnext)

	def reset_IC(self):
		self.x = [self.x0]
		self.u = []
		self.w = []

