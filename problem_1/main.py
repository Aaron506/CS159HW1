from MDP import MDP
import pdb


# Problem Paramters
N  = 5  # Number of parcking spots
p  = 0.05 # Probability of transitioning to a free parking spot
Cg = 4  # Cost of parking to the garage

# Initialize mdp object
printLevel = 0
mdp = MDP(N, p, Cg, printLevel)

# Build transition probability
mdp.buildTransitionMatrices()

# # Compute the matrices for the closed-loop system given the threshold of the optimal policy = N
# Ppi, Cpi = mdp.computePolicy(iThreshold = 3)

# # Evaluate the policy for Ppi and Cpi
# mdp.policyEvaluation(Ppi, Cpi)

# # Perform value iteration to compute the optimal value function
# mdp.valueIteration()

# # # Perform policy iteration to compute the optimal value function
# mdp.policyIteration()