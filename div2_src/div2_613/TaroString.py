import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class TaroString:
    def getAnswer(self, S):
        if S.count('C') == 1 and S.count('A') == 1 and S.count('T') == 1:
         	if S.index('C') < S.index('A') < S.index('T'):
         		return 'Possible'
        return 'Impossible'

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pf 2.3.0
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("\"") + str(p0) + str("\""))
	print(str("]"))
	obj = TaroString()
	startTime = time.clock()
	answer = obj.getAnswer(p0)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		res = answer == p1
	
	if (not res):
		print(str("DOESN'T MATCH!!!!"))
		if (hasAnswer):
			print(str("Desired answer:"))
			print(str("\t") + str("\"") + str(p1) + str("\""))
		
		print(str("Your answer:"))
		print(str("\t") + str("\"") + str(answer) + str("\""))
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
p0 = "XCYAZTX"
p1 = "Possible"
all_right = (disabled or KawigiEdit_RunTest(0, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = "CTA"
p1 = "Impossible"
all_right = (disabled or KawigiEdit_RunTest(1, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = "ACBBAT"
p1 = "Impossible"
all_right = (disabled or KawigiEdit_RunTest(2, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = "SGHDJHFIOPUFUHCHIOJBHAUINUIT"
p1 = "Possible"
all_right = (disabled or KawigiEdit_RunTest(3, p0, True, p1) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = "CCCATT"
p1 = "Impossible"
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
# 
# Cat Taro has a string S.
# He wants to obtain the string "CAT" from the string S.
# In a single turn he can choose any character and erase all occurrences of this character in S.
# He can do as many turns as he wants (possibly zero).
# 
# 
# 
# 
# You are given the string S.
# Return "Possible" (quotes for clarity) if it is possible to obtain the string "CAT" and "Impossible" otherwise.
# 
# 
# 
# DEFINITION
# Class:TaroString
# Method:getAnswer
# Parameters:string
# Returns:string
# Method signature:def getAnswer(self, S):
# 
# 
# CONSTRAINTS
# -S will contain between 1 and 50 characters, inclusive.
# -S will contain only uppercase English letters ('A'-'Z').
# 
# 
# EXAMPLES
# 
# 0)
# "XCYAZTX"
# 
# Returns: "Possible"
# 
# It is possible to obtain string "CAT" in three turns, as follows:
# 
# 
# Erase all characters 'X' (and obtain the string "CYAZT")
# 
# 
# Erase all characters 'Y' (and obtain the string "CAZT")
# 
# 
# Erase all characters 'Z' (and obtain the string "CAT")
# 
# 
# 
# 1)
# "CTA"
# 
# Returns: "Impossible"
# 
# 
# 
# 2)
# "ACBBAT"
# 
# Returns: "Impossible"
# 
# Note that whenever you are erasing a character, you must erase all its occurrences. In this case, it is not possible to erase the first 'A' and keep the second one.
# 
# 3)
# "SGHDJHFIOPUFUHCHIOJBHAUINUIT"
# 
# Returns: "Possible"
# 
# 
# 
# 4)
# "CCCATT"
# 
# Returns: "Impossible"
# 
# 
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pf 2.3.0!