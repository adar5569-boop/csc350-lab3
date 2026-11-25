"""CSC350 Lab 3: NumPy hands-on
Name:M Ahmad dar
Roll number:24-uon-0371

Run this file after every task:  python lab3_numpy.py
Commit after every task (git add, git commit -m "Task N done").
"""
import numpy as np

print("NumPy version:", np.__version__)

# =====================================================================
# Task 1: Creating arrays (2 marks)
# =====================================================================
print("\n=== Task 1 ===")
# 1a. Make an array `temps` with this week's temperatures:
#     31, 28, 35, 30, 33, 29, 36
#     Print it, then print its dtype, shape and size.
temp=np.array([ 31, 28, 35, 30, 33, 29, 36])
print(temp,temp.size,temp.dtype,temp.shape)
# 1b. Make `months`: the numbers 1 to 12 as a 3 x 4 table
#     (use np.arange and reshape). Print it and its shape.
month=np.arange(1,13).reshape((3,4))
print(month,month.shape)
# 1c. Print an array of five zeros, and a 2 x 3 array of ones.
print(np.zeros(5,),np.ones((2,3)))
# 1d. Make a random generator with seed 42 and roll 10 dice
#     (whole numbers from 1 to 6). Print the result.
r=np.random.default_rng(42)
print(r.integers(1,7,size=10))