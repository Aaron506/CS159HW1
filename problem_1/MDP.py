import numpy as np
import pdb

class MDP(object):
	""" Markov Decision Process (MDP)
	Methods:
		- buildTransitionMatrices:
		- computePolicy:
		- valueIteration:
		- policyIteration:

	"""
	def __init__(self, N, p, Cg, printLevel):
		self.N  = N
		self.p  = p
		self.Cg = Cg
		self.printLevel = printLevel

		self.states  = 2*self.N + 2
		self.actions = 2
		self.maxIt   = 500

	def bellmanRecursion(self, s, V):
		# Bellman recursion of the value function. 
		# Recall that there are 2 actions --> First, evaluate expected cost for action 1 and action 2. Then select the best action
		
		# Hint: here you need to evaluate and store the cost for all actions a.
		cost = []
		for a in range(0, self.actions):
			C_a_s = self.C[a][s]
			P_a_s = self.P[a][s,:]
			val = ...
			cost.append(val)

		# s-th component of the value function vector
		Vn_s = ...
		# s-th component of the action vector
		An_s = ...

		return Vn_s, An_s

	def policyIteration(self):
		if self.printLevel >= 0: print("====== Start Policy Iteration")
		# Initialize list of value function vectors
		Vn = []
		iThreshold = self.N

		# Policy Iteration Loop
		for j in range(0, self.maxIt):
			# Hint: use the functions that you have already developed
			[Ppi, Cpi] = ... # First compute a policy for the threshild value iThreshold
			Vnext      = ... # Policy evaluation step
			iThreshold = ... # Policy improvement step;
			Vn.append(Vnext)

			# Check if the algorithm has converged
			if ((j>1) and np.sum(Vn[-1]-Vn[-2])==0):
				print('Policy Iteration Terminated at iteration : ',j)
				print('Park from free parking spot iThreshold = ', iThreshold)
				if self.printLevel >= 1: print('Value Function: ', Vn[-1])
				break

	def policyImprovement(self, V):
		# Initialize value function vector and action vector
		Vn = np.zeros(self.states)
		An = np.zeros(self.states)

		# Run Bellman recursion for all states
		# Notice that self.states = 2N+2 = total number of states
		# Hint: Here you need to run a for loop to update the vectors Vn \in \mathbb{R}^{self.states} and An \in \mathbb{R}^{self.states}
		...	
		

		iThreshold = self.computeIndex(An)
		return iThreshold

	def computeIndex(self, An):
		return np.argmax(An[::2])

	def valueIteration(self):
		if self.printLevel >= 0: print("====== Start Value Iteration")
		# Initialize the value function vector and action vector
		Vn = [np.zeros(self.states)]
		An = [np.zeros(self.states)]

		# Value Iteration loop
		for j in range(0, self.maxIt):
			# Initialize new value function vector and action vector
			Vnext = np.zeros(self.states)
			Anext = np.zeros(self.states)
			Vcurrent = Vn[-1]

			# Run Bellman recursion for all states using the value function vector at the previous iterate
			# Notice that self.states = 2N+2 = total number of states
			# Hint: You need to update the vectors Vnext \in \mathbb{R}^{self.states} and Anext \in \mathbb{R}^{self.states}
			for s in range(0, self.states):
				...

			Vn.append(Vnext)
			An.append(Anext)

			# Check if the algorithm has converged
			if ((j>1) and np.sum(Vn[-1]-Vn[-2])==0):
				print('Value Iteration Terminated at iteration : ',j)
				print('Park from free parking spot iThreshold = ', self.computeIndex(An[-1]))
				if self.printLevel >= 1: print('Value Function: ', Vn[-1])
				break

	def policyEvaluation(self, P, C):
		# Initialize value function
		Vn = [np.zeros(self.states)]

		# Run iterative strategy
		for j in range(0,self.maxIt):
			Vnext = ... # Hint: here you need to use only Vn[-1], P and C.
			Vn.append( Vnext )

			# Check if algorithm has converged
			if ((j>1) and np.sum(Vn[-1]-Vn[-2])==0):
				if self.printLevel >= 2: print("Policy Evaluation Terminated at iteration: ",j)
				break

		Vout = Vn[-1]
		if self.printLevel >= 2: print("Value Function:  ", Vout)
		return Vout

	def computePolicy(self,iThreshold = 0):
		# Compute the state sThreshold such that
		# if a state s <  sThreshold --> the transition probabilities are are given by the matrix self.P[0] associated with the move forward action
		# if a state s >= sThreshold --> the transition probabilities are are given by the matrix self.P[1] associated with the park action
		sThreshold = 2*iThreshold


		# You need to combine the matrices self.P[0] and self.P[1] which are assocaied 
		# with the move forward acton and parking action, respectively 
		# (hint: use the variable sThreshold and the command vstack)
		Ppi = ...

		# You need to combine the vectors self.C[0] and self.C[1] which are assocaied 
		# with the move forward acton and parking action, respectively (hint: use the variable sThreshold)
		# (hint: use the variable sThreshold and the command hstack)
		Cpi = ...

		if self.printLevel >= 3:
			print("Ppi: ")
			print(Ppi)
			print("Cpi: ", Cpi)

		return Ppi, Cpi

	def buildTransitionMatrices(self):
		# First 2*N states are assocaited with the N parking spots being free or occupied.
		# Last tow state are Garage and Theater
		P_move_forward = np.zeros((self.states, self.states))
		P_park         = np.zeros((self.states, self.states))

		# Make Theater an absorbing state
		P_move_forward[-1,-1] = 1
		P_park[-1,-1]         = 1

		# Set Transition From Garage to Theater
		P_move_forward[-2,-1] = 1
		P_park[-2,-1]         = 1


		# Move Forward
		for i  in range(0, self.N):
			i_f = 2*i  # i-th parking spot free
			i_o = 2*i+1 # i-th parking spot occupied 		
			s_n = 2*(i+1) # (i+1)-th parking spot free for (i+1) < N and garage for (i+1) = N 

			if i == self.N-1:
				P_move_forward[i_f, s_n] = ... 
				P_move_forward[i_o, s_n] = ...
			else:
				P_move_forward[i_o, s_n+0] = ... 
				P_move_forward[i_o, s_n+1] = ...
				P_move_forward[i_f, s_n+0] = ... 
				P_move_forward[i_f, s_n+1] = ...

		# Parking
		for i  in range(0, self.N):
			i_f = 2*i  # i-th parking spot free
			i_o = 2*i+1 # i-th parking spot occupied 		
			s_n = 2*(i+1) # (i+1)-th parking spot free

			if i == self.N-1:
				P_park[i_f, -1] = ...
				P_park[i_o, s_n] = ... 
			else:
				P_park[i_f, -1] = ...
				P_park[i_o, s_n+0] = ... 
				P_park[i_o, s_n+1] = ...
			
		# Compute cost vector associated with each action
		C_move_forward = np.zeros(2*self.N+2);
		C_park         = np.zeros(2*self.N+2);
	
		# Cost of being at the Garage		
		C_move_forward[-2] = self.Cg
		C_park[-2]         = self.Cg

		for i in range(0, self.N):
			i_f = 2*i # i-th parking spot free
			C_park[i_f] = ...
		
		if self.printLevel >= 2:
			print("P_move_forward:")
			print(P_move_forward)
			
			print("P_park:")
			print(P_park)

			print("C_move_forward:")
			print(C_move_forward)
			
			print("C_park:")
			print(C_park)

		self.C = [C_move_forward, C_park]
		self.P = [P_move_forward, P_park]

