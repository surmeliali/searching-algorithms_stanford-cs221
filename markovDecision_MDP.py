# MARKOV_DECISION
# TRAM FAILS WITH PROBABILITY OF 0.5

## MODEL
import os

class TransportationMDP(object):
    def __init__(self, N):
        self.N = N
    def startState(self):
        return 1
    def isEnd(self, state):
        return state == self.N
    def actions(self, state):
        # Returns list of valid actions (walk or tram)
        result=[]
        if state+1<=self.N:
            result.append('walk')
        if state*2<=self.N:
            result.append('tram')
        return result
    def succProbReward(self, state, action):
        # Return list of (newState, probability, reward) triples     
        # state = s, action = a, newState = s'  
        # prob = T(s,a,s'), reward = Reward(s,a,s')
        # Reward will be -1 for walk, -2 for tram
        result=[]
        if action=='walk':
            result.append((state+1, 1, -1))
        elif action=='tram':
            result.append((state*2, 0.5, -2))
            result.append((state, 0.5, -2))    
        return result
    def discount(self):
        return 1.
    def states(self):
        return range(1, self.N+1)


def valueiteration(mdp):
    #initilaize
    V={}
    for state in mdp.states():
        V[state] = 0

    def Q(state,action):
        return sum(prob*(reward+mdp.discount()*V[newState]) for newState, prob, reward in mdp.succProbReward(state,action))

    while True:
        # Compute new values (newV) given the old values(V)
        newV = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                newV[state]=0
            else:
                newV[state]=max(Q(state,action) for action in mdp.actions(state))
        # Check for convergence --> if two value close each other, we have answ.
        if max(abs(V[state]-newV[state]) for state in mdp.states())<1e-10:
            break
        V=newV

        # read out policy
        pi={}
        for state in mdp.states():
            if mdp.isEnd(state):
                pi[state] = 'none'
            else:
                pi[state] = max((Q(state,action), action) for action in mdp.actions(state))[1]


        # Print staff out
        os.system('clear')
        print('{:15} {:15} {:15}'.format('s', 'V(s)' ,'pi(s)'))
        for state in mdp.states():
            print('{:15} {:15} {:15}'.format(state, V[state] ,pi[state]))
        input()


mdp=TransportationMDP(N=10)
#Initialize
valueiteration(mdp)




#print(mdp.actions(3))
#print(mdp.succProbReward(3,'walk'))
#print(mdp.succProbReward(3,'tram'))


""" def SuccandCost(self, state):
        # Return list of (action, newState, cost) triples
        result=[]
        if state+1<=self.N:
            result.append(('walk',state+1, 1))
        if state*2<=self.N:
            result.append(('tram',state*2, 2))
        return result"""

    

## ALGORITHMS

# ('walk', 4, 1) ('tram', 6, 2)
