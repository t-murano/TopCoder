import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class EmoticonsDiv2:
    def printSmiles(self, smiles):
        return self.calc(smiles, 0, 1000)

    def calc(self, input, count, minCount):
    	if input == 1: return count
    	for i in xrange(2, input+1):
    		if input % i == 0:
    			count += i
    			result = self.calc(input/i, count, minCount)
    			minCount = min(minCount, result)
    	return minCount




# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pf 2.3.0
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str(p0))
	print(str("]"))
	obj = EmoticonsDiv2()
	startTime = time.clock()
	answer = obj.printSmiles(p0)
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
p0 = 2
p1 = 2
all_right = (disabled or KawigiEdit_RunTest(0, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = 6
p1 = 5
all_right = (disabled or KawigiEdit_RunTest(1, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = 11
p1 = 11
all_right = (disabled or KawigiEdit_RunTest(2, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = 16
p1 = 8
all_right = (disabled or KawigiEdit_RunTest(3, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = 1000
p1 = 21
all_right = (disabled or KawigiEdit_RunTest(4, p0, True, p1) ) and all_right
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
# You are very happy because you advanced to the next round of a very important programming contest.
# You want your best friend to know how happy you are.
# Therefore, you are going to send him a lot of smile emoticons.
# You are given an integer smiles: the exact number of emoticons you want to send.
# 
# You have already typed one emoticon into the chat.
# Then, you realized that typing is slow.
# Instead, you will produce the remaining emoticons using copy and paste.
# 
# You can only do two different operations:
# 
# Copy all the emoticons you currently have into the clipboard.
# Paste all emoticons from the clipboard.
# 
# Each operation takes precisely one second.
# Copying replaces the old content of the clipboard.
# Pasting does not empty the clipboard.
# Note that you are not allowed to copy just a part of the emoticons you already have.
# 
# Return the smallest number of seconds in which you can turn the one initial emoticon into smiles emoticons.
# 
# DEFINITION
# Class:EmoticonsDiv2
# Method:printSmiles
# Parameters:integer
# Returns:integer
# Method signature:def printSmiles(self, smiles):
# 
# 
# CONSTRAINTS
# -smiles will be between 2 and 1000, inclusive.
# 
# 
# EXAMPLES
# 
# 0)
# 2
# 
# Returns: 2
# 
# First use copy, then use paste. The first operation copies one emoticon into the clipboard, the second operation pastes it into the message, so now you have two emoticons and you are done.
# 
# 1)
# 6
# 
# Returns: 5
# 
# 
# Copy. This puts one emoticon into the clipboard.
# Paste. You now have 2 emoticons in the message.
# Copy. The clipboard now contains 2 emoticons.
# Paste. You now have 4 emoticons in the message.
# Paste. You now have 6 emoticons in the message and you are done.
# 
# 
# 2)
# 11
# 
# Returns: 11
# 
# 
# 
# 3)
# 16
# 
# Returns: 8
# 
# 
# 
# 4)
# 1000
# 
# Returns: 21
# 
# 
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pf 2.3.0!