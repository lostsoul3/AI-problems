initial = ['W', 'W', 'W', 'W']
goal = ['E', 'E', 'E', 'E']
 
stack = []
stack.append(initial)
 
 
def nextState(state):
    if state == goal: return False
    farmer = state[3]
     
    #loop thru characters of state if on same side as
    #farmer test to see if farmer and it can be brought
    #across.
    for i, s in enumerate(state):
        if s == farmer:
            tryState = makeState(state, i)
            if testState(tryState) and isUnique(tryState):
                stack.append(tryState)
                return True
            
    return False       
     
def makeState(s, i):
    t = []
    for x in s: t.append(x)
    
    #farmer always crosses
    t[3] = 'E' if t[3] == 'W' else 'W'
    
    #only bring something back across the river to
    #avoid an unsafe state. 
    if t[3] == 'W':
        if not testState(t):
            t[i] = 'E' if t[i] == 'W' else 'W'
    else:
        t[i] = 'E' if t[i] == 'W' else 'W'
    return t
 
def testState(s):
    #check to see if something gets eaten
    if s[0] == s[1] and s[3] != s[0]: return False
    if s[1] == s[2] and s[3] != s[1]: return False
    return True


def isUnique(s):     
    #check to see if this state is unique. ie check for loops
    if s in stack: return False
    return True
      
      
while nextState(stack[-1]): pass
for i, x in enumerate(stack): print i, x


