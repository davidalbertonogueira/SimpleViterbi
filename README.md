# SimpleViterbi
Implementation example of the Viterbi algorithm (Hidden Markov Model) 
DISCLAIMER: This is a simple and easy-to-go implementation of 
this algorithm in Python. 
Its intent is not to be efficient, but educational and easy to understand. 
Modifications should be done to improve performance.

Two functions are presented: one that receives emission and transition 
probabilities matrices, and another that receives nodes and edges scores matrices. 

A version of the last function is presented using the log of the probabilities 
(rather than the probabilities themselves). 
This is the recommend method as it does not lead to underflow, 
as it can occur in the other case.

David Nogueira, 2015.11.25
