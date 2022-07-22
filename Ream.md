# Problem Description
In data simulation, the problem of choosing actions with certain probability is often encountered. For example, there are now four actions: A1, A2, A3, and A4. You want to choose A1 with the probability of p(A1), and choose A2, A3, and A4 with the probability of p(A2), p(A3), and p(A4).  
How to implement this probabilistic choice problem? This repository my help you.  

# Sampling method
- We can generate a batch of "samples" according to the probability distribution, and then sample a large number of samples randomly, approximating the probability by the sampling frequency. According to the law of large numbers, the frequency will be close to the probability.
- Generating a batch of samples according to the probability distribution can also be understood as simulating its probability distribution with a batch of samples
- Still the above example: The total number of samples that can be generated is N, where the number of A1 samples is N*p1, the number of A2 samples is N*p2, the number of A3 samples is N*p3, and the number of A4 samples is N*p4.
- A large number of random sampling is performed on the generated samples, and the number of times N(An) of each data category is recorded, and finally the frequency of each data category is calculated, and the probability is approximated by the frequency. According to Uncle's Law, selection with a certain probability can only be simulated if there are enough samples.

# How to run the code
You can check the simulate.py file.
- Modify the probabilities in line 3
- Modify other parameters in line 56
- then run the code to see the result