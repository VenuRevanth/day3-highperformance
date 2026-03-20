# day3-highperformance
Lecture notes and code examples for Day 3: High performance computing
## comments:
Here I tried to examine the run speed between vectorized numpy arrays and split numpy arrays and recombine using mpi.
## What I found
I found doing a single numpy vector operation is much faster than splitting a numpy array, and adding it using mpi4pi commands.
