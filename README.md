# SimpleViterbi
Implementation example of the Viterbi algorithm (Hidden Markov Model) 

DISCLAIMER: This is a simple and easy-to-go implementation of 
this algorithm in Python. 
Its intent is not to be efficient, but educational and easy to understand. 
Modifications should be done to improve performance.

Two functions are presented: one that receives emission and transition 
probabilities matrices, and another that receives nodes and edges scores matrices, 
useful for Viterbi path computation in probabilistic sequence models. 

A version of the last function is also presented using the log of the probabilities 
(rather than the probabilities themselves). 
This is the recommend approach as it does not lead to underflow, 
as it can occur in the other case.

David Nogueira, 2015.11.25
