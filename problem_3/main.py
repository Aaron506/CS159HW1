import numpy as np
from utils import system
import pdb
import matplotlib.pyplot as plt
from ftocp import FTOCP
from matplotlib import rc
from numpy import linalg as la

# =====================================================
# Initialize system parameters
A = np.array([[1, 1],
	          [0, 1]]);
B = np.array([[0], 
			  [1]]);
C = []
x0    = np.array([-15.0,15.0])   # initial condition

# Initialize ftocp parameters
printLevel = 3
N  = 4
Q      = np.eye(2)
R      = 10*np.eye(1)
Qf     = np.eye(2)

# State constraint set X = \{ x : F_x x \leq b_x \}
Fx = np.vstack((np.eye(n), -np.eye(n)))
bx = np.array([15,15]*(2))

# Input constraint set U = \{ u : F_u u \leq b_u \}
Fu = np.vstack((np.eye(d), -np.eye(d)))
bu = np.array([5]*2)

Ff = Fx
bf = bx
# =====================================================
# Solve FTOCP and plot the solution
A = []
B = []
C = [] 
for i in range(0, N):
	A.append(np.array([[1, 0.5**i],
	          	  [0, 1]]))
	B.append(np.array([[0], 
				  	   [1]]))

	C.append(np.array([0, 0.1**i]))

ftocp = FTOCP(N, A, B, C, Q, R, Qf, Fx, bx, Fu, bu, Ff, bf, printLevel)
ftocp.solve(x0)

plt.figure()
plt.plot(ftocp.xPred[:,0], ftocp.xPred[:,1], '-ob')
plt.title('Optimal Solution for time-varying problem')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.show()