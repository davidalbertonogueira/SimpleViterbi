'''Implementation example of the Viterbi algorithm (Hidden Markov Model) 
DISCLAIMER: This is a simple and easy-to-go implementation of 
this algorithm in Python. 
Its intent is not to be efficient, but educational and easy to understand. 
Modifications should be done to improve performance.
David Nogueira, 2015.11.25'''
  
import numpy
#Based on wikipedia example in Viterbi algorithm page

#Function to print the probability table of the state sequence
def printdptable(V):
    print " ".join(("%7d" % i) for i in range(len(V)))
    for y in states:
        print "%.5s: " % y + " ".join("%.7s" % ("%f" % V[t][states.index(y)]) \
        for t in range(0, len(observations)) )
        
def viterbi_emit_trans(obs, states, start_p, trans_p, emit_p):
    deltas = numpy.zeros( shape=( len(observations), len(states) ) ); 
    path = {}
    
    # Initialize base cases (t == 0)
    for y in states:
        deltas[0][states.index(y)] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
    
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        newpath = {}
        for y in states:
            #best_value = -1e-12;
            #best_state = -1;
            #for y0 in states:
            #    curr_value = \
            #    deltas[t-1][states.index(y0)] * trans_p[y0][y] * emit_p[y][obs[t]]
            #    if curr_value > best_value or best_state < 0:
            #        best_value = curr_value
            #        best_state = y0
            #pythonic way
            (best_value, best_state) = \
            max((deltas[t-1][states.index(y0)] * trans_p[y0][y] * emit_p[y][obs[t]], y0) \
            for y0 in states)
            
            deltas[t][states.index(y)] = best_value
            newpath[y] = path[best_state] + [y]

        # Update path
        path = newpath
    
    # Return the most likely sequence
    n = len(obs) - 1
    printdptable(deltas)
    (best_value, best_state) = max((deltas[n][states.index(y)], y) for y in states)
    return (best_value, path[best_state])

def viterbi_node_edge(obs, states, node_scores, edge_scores, log=0):
    deltas = numpy.zeros( shape=( len(observations), len(states) ) ); 
    backtrack = numpy.zeros( shape=( len(observations), len(states) ) ); 
    path = {}
    
    # Initialize base cases (t == 0)
    for y in states:
        deltas[0][states.index(y)] = node_scores[0][states.index(y)] 
        path[y] = [y]
        backtrack[0][states.index(y)] = -1
    
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        newpath = {}
        for y in states:
            #best_value = -1e-12;
            #best_state = -1;
            #for y0 in states:
            #    if log == 0:
            #        curr_value = \
            #        deltas[t-1][states.index(y0)] * \
            #        edge_scores[t-1][states.index(y0)][states.index(y)]
            #    elif log == 1:
            #        curr_value = \
            #        deltas[t-1][states.index(y0)] + \
            #        edge_scores[t-1][states.index(y0)][states.index(y)]
            #    if curr_value > best_value or best_state < 0:
            #        best_value = curr_value
            #        best_state = y0
            #pythonic way
            if log == 0:
                (best_value, best_state) = \
                max((deltas[t-1][states.index(y0)] * \
                edge_scores[t-1][states.index(y0)][states.index(y)], y0) \
                for y0 in states)
            elif log == 1:
                (best_value, best_state) = \
                max((deltas[t-1][states.index(y0)] + \
                edge_scores[t-1][states.index(y0)][states.index(y)], y0) \
                for y0 in states)
                             
            if log == 0:
                deltas[t][states.index(y)] = \
                best_value * node_scores[t][states.index(y)]
            elif log == 1:
                deltas[t][states.index(y)] = \
                best_value + node_scores[t][states.index(y)]
            
            newpath[y] = path[best_state] + [y]
            backtrack[t][states.index(y)] = states.index(best_state)

        # Update path
        path = newpath   
        
    # Return the most likely sequence
    n = len(obs) - 1
    printdptable(deltas)
    (best_value, best_state) = max((deltas[n][states.index(y)], y) for y in states)
    return (best_value, path[best_state])



# ***** PROBLEM EXAMPLE VARIABLES ***** #
states              = ('Healthy', 'Fever') 
observations        = ('normal', 'cold', 'dizzy') 
start_probability   = {'Healthy': 0.6, 'Fever': 0.4} 
transition_probability = {
   'Healthy'    : {'Healthy': 0.7, 'Fever': 0.3},
   'Fever'      : {'Healthy': 0.4, 'Fever': 0.6}}
emission_probability = {
   'Healthy'    : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
   'Fever'      : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}}
# ***** PROBLEM EXAMPLE VARIABLES ***** #
 
# ***** CREATION OF NODE AND EDGE SCORE MATRICES ***** #
node_scores = numpy.zeros( shape=( len(observations), len(states) ) );  
# Initialize base cases (t == 0)
for y in states:
    node_scores[0][states.index(y)] = \
    start_probability[y] * emission_probability[y][observations[0]] 
for t in range(1, len(observations)):
    for y in states:
        node_scores[t][states.index(y)] = emission_probability[y][observations[t]] 

  
edge_scores = numpy.zeros( shape=( len(observations)-1, len(states), len(states) ) ); 
for t in range(0, len(observations)-1):
    for prev_state in range(0, len(node_scores[t])):
        for next_state in range(0, len(node_scores[t+1])):
            edge_scores[t][prev_state][next_state] = \
            transition_probability[states[prev_state]][states[next_state]]
# ***** CREATION OF NODE AND EDGE SCORE MATRICES ***** #

def example_with_emission_transition_matrices():
    return viterbi_emit_trans( observations,
                               states,
                               start_probability,
                               transition_probability,
                               emission_probability)
                               
def example2_with_node_edge_matrices_withoutlog():
    return viterbi_node_edge(  observations,
                               states, 
                               node_scores, 
                               edge_scores,
                               0)
#Example with log values. 
#This is the recommend method as it does not suffer from underflow 
#as the previous method (multiplication of probabilities 0<p(x)<1 tends to zero).                                                          
def example2_with_node_edge_matrices_withlog():
    return viterbi_node_edge(  observations,
                               states, 
                               numpy.log(node_scores), 
                               numpy.log(edge_scores),
                               1)
                               
                 
print(example_with_emission_transition_matrices())
print(example2_with_node_edge_matrices_withoutlog())
print(example2_with_node_edge_matrices_withlog())
