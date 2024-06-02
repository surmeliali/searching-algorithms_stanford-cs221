### 1_BACKTRACKING SEARCH CODE:

## MODEL
class TransportationProblem(object):
    def __init__(self, N):
        self.N = N
    def startState(self):
        return 1
    def isEnd(self, state):
        return state == self.N
    def SuccandCost(self, state):
        result=[]
        if state+1<=self.N:
            result.append(('walk',state+1, 1))
        if state*2<=self.N:
            result.append(('tram',state*2, 2))
        return result

## ALGORITHMS

# ('walk', 4, 1) ('tram', 6, 2)
# (action, newState, cost)


#  state(), history, cost

def backtrackingSearch(problem):
    #Dictionary because we need to track BEST SOLUTION SO FAR.
    best={
        'cost': float('+inf'),
        'history': None
    }
 
    def recurse(state, history, totalCost):
        #We have at 'state',  undergone history & accumulated total cost
        #Explore the rest of the subtree under state

        #if we are end state end it
        if problem.isEnd(state):
            # UPDATE THE BEST SOLUTION SO FAR
            # TODO!!!
            
            if totalCost<best['cost']:
                best['cost']=totalCost
                best['history']=history
            return
        # if not, we will recurse on children.
        for action, newState, cost in problem.SuccandCost(state):
            recurse(newState, history+[(action, newState, cost)],totalCost+cost)

    # First we need to call the start state as an empty, because we haven't started yet.
    recurse(problem.startState(),history=[], totalCost=0) 
    return (best['cost'], best['history'])

def printSolution(solution):
    totalCost, history = solution
    print('totalCost:{}'.format(totalCost))
    for item in history:
        print(item)

## MAIN
problem = TransportationProblem(N=10)
printSolution(backtrackingSearch(problem))

