import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class DivideByZero:
    def CountNumbers(self, numbers):
        length = 1
        numbers = list(numbers)
        while length != len(numbers):
        	length = len(numbers)
        	for i in xrange(len(numbers) - 1):
        		left = numbers[i]
        		for j in xrange(i+1, len(numbers)):
        			right = numbers[j]
        			div = max(left, right) / min(left, right)
        			if div != 0 and div not in numbers:
        				numbers.append(div)
        return length

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pf 2.3.0
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("{"))
	for i in range(len(p0)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str(p0[i]))
	
	sys.stdout.write(str("}"))
	print(str("]"))
	obj = DivideByZero()
	startTime = time.clock()
	answer = obj.CountNumbers(p0)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		res = answer == p1
	
	if (not res):
		print(str("DOESN'T MATCH!!!!"))
		if (hasAnswer):
			print(str("Desired answer:"))
			print(str("\t") + str(p1))
		
		print(str("Your answer:"))
		print(str("\t") + str(answer))
	elif ((endTime - startTime) >= 2):
		print(str("FAIL the timeout"))
		res = False
	elif (hasAnswer):
		print(str("Match :-)"))
	else:
		print(str("OK, but is it right?"))
	
	print(str(""))
	return res

all_right = True
tests_disabled = False


# ----- test 0 -----
disabled = False
p0 = (9,2)
p1 = 3
all_right = (disabled or KawigiEdit_RunTest(0, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = (8,2)
p1 = 3
all_right = (disabled or KawigiEdit_RunTest(1, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = (50,)
p1 = 1
all_right = (disabled or KawigiEdit_RunTest(2, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = (1,5,8,30,15,4)
p1 = 11
all_right = (disabled or KawigiEdit_RunTest(3, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = (1,2,4,8,16,32,64)
p1 = 7
all_right = (disabled or KawigiEdit_RunTest(4, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = (6,2,18)
p1 = 7
all_right = (disabled or KawigiEdit_RunTest(5, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

if (all_right):
	if (tests_disabled):
		print(str("You're a stud (but some test cases were disabled)!"))
	else:
		print(str("You're a stud (at least on given cases)!"))
	
else:
	print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# Little John has a piece of paper with some distinct integers written on it.
# You are given a tuple (integer) numbers.
# The elements of numbers are the numbers written on John's paper.
# 
# John is now going to add some new numbers to his paper.
# While doing so, he will be using integer division.
# When doing integer division, we discard the fractional part of the result.
# In this problem, we will use "div" to denote integer division.
# For example, 15 div 5 = 3, and 24 div 5 = 4.
# 
# John will repeat the following process:
# He will look at his paper and select two distinct numbers A and B such that A is greater than B.
# He will compute C = A div B.
# If C is not written on his paper yet, he will add it to the paper.
# 
# The process will stop once there is no way for John to add a new number to his paper.
# Compute and return how many numbers will there be on John's paper at the end.
# 
# DEFINITION
# Class:DivideByZero
# Method:CountNumbers
# Parameters:tuple (integer)
# Returns:integer
# Method signature:def CountNumbers(self, numbers):
# 
# 
# NOTES
# -The return value does not depend on the order in which John adds new numbers to his paper.
# 
# 
# CONSTRAINTS
# -numbers will contain between 1 and 100 elements, inclusive.
# -Each element of numbers will be between 1 and 100, inclusive.
# -The elements in numbers will be distinct.
# 
# 
# EXAMPLES
# 
# 0)
# {9, 2}
# 
# Returns: 3
# 
# John starts with just 9 and 2 on his paper.
# He can add the number 4, because 9 div 2 = 4.
# After he adds the number 4, there will be no more numbers to add, because 9 div 4 = 2, and also 4 div 2 = 2.
# Thus, at the end John's paper will contain 3 numbers: 9, 2, and 4.
# 
# 1)
# {8, 2}
# 
# Returns: 3
# 
# 
# 
# 2)
# {50}
# 
# Returns: 1
# 
# We only have one number. There isn't anything John can do.
# 
# 3)
# {1, 5, 8, 30, 15, 4}
# 
# Returns: 11
# 
# 
# 
# 4)
# {1, 2, 4, 8, 16, 32, 64}
# 
# Returns: 7
# 
# 
# 
# 5)
# {6, 2, 18}
# 
# Returns: 7
# 
# Once John has a number on his paper, he can use it when producing new numbers.
# For example, in this case he can add 9 (computed as 18 div 2), and then add 1 (computed as 9 div 6).
# The numbers he will have at the end are 1, 2, 3, 4, 6, 9, and 18.
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pf 2.3.0!
