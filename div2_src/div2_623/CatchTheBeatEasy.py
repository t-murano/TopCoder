import math,string,itertools,fractions,heapq,collections,re,array,bisect,random

class CatchTheBeatEasy:
    def ableToCatchAll(self, x, y):
        xy = zip(x,y)
        xy = sorted(xy, key=lambda x:x[1])
        pre = (0,0)
        for co in xy:
        	t = co[1] - pre[1]
        	dis = abs(co[0] - pre[0])
        	if t >= dis:
        		pre = co
        	else:
        		return "Not able to catch"
        return "Able to catch"

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pf 2.3.0
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, hasAnswer, p2):
	sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("{"))
	for i in range(len(p0)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str(p0[i]))
	
	sys.stdout.write(str("}") + str(",") + str("{"))
	for i in range(len(p1)):
		if (i > 0):
			sys.stdout.write(str(","))
		
		sys.stdout.write(str(p1[i]))
	
	sys.stdout.write(str("}"))
	print(str("]"))
	obj = CatchTheBeatEasy()
	startTime = time.clock()
	answer = obj.ableToCatchAll(p0, p1)
	endTime = time.clock()
	res = True
	print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
	if (hasAnswer):
		res = answer == p2
	
	if (not res):
		print(str("DOESN'T MATCH!!!!"))
		if (hasAnswer):
			print(str("Desired answer:"))
			print(str("\t") + str("\"") + str(p2) + str("\""))
		
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
p0 = (-1,1,0)
p1 = (1,3,4)
p2 = "Able to catch"
all_right = (disabled or KawigiEdit_RunTest(0, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 1 -----
disabled = False
p0 = (-3,)
p1 = (2,)
p2 = "Not able to catch"
all_right = (disabled or KawigiEdit_RunTest(1, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 2 -----
disabled = False
p0 = (-1,1,0)
p1 = (1,2,4)
p2 = "Not able to catch"
all_right = (disabled or KawigiEdit_RunTest(2, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 3 -----
disabled = False
p0 = (0,-1,1)
p1 = (9,1,3)
p2 = "Able to catch"
all_right = (disabled or KawigiEdit_RunTest(3, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 4 -----
disabled = False
p0 = (70,-108,52,-70,84,-29,66,-33)
p1 = (141,299,402,280,28,363,427,232)
p2 = "Not able to catch"
all_right = (disabled or KawigiEdit_RunTest(4, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 5 -----
disabled = False
p0 = (-175,-28,-207,-29,-43,-183,-175,-112,-183,-31,-25,-66,-114,-116,-66)
p1 = (320,107,379,72,126,445,318,255,445,62,52,184,247,245,185)
p2 = "Able to catch"
all_right = (disabled or KawigiEdit_RunTest(5, p0, p1, True, p2) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------

# ----- test 6 -----
disabled = False
p0 = (0,0,0,0)
p1 = (0,0,0,0)
p2 = "Able to catch"
all_right = (disabled or KawigiEdit_RunTest(6, p0, p1, True, p2) ) and all_right
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
# One of the modes in the game "osu!" is called "catch the beat".
# In this mode, you control a character that catches falling fruit.
# 
# 
# 
# The game is played in the vertical plane.
# For simplicity, we will assume that both your character and all pieces of fruit are points in that plane.
# 
# 
# 
# You start the game at the coordinates (0, 0).
# Your character can only move along the x-axis.
# The maximum speed of your character is 1 unit of distance per second.
# For example, you need at least 3 seconds to move from (-2, 0) to (1, 0).
# 
# 
# 
# You are given tuple (integer)s x and y that contain initial coordinates of the fruit you should catch:
# for each valid i, there is one piece of fruit that starts at (x[i], y[i]).
# All pieces of fruit fall down with constant speed of 1 unit of distance per second.
# That is, a fruit currently located at (xf, yf) will move to (xf, yf-t) in t seconds.
# 
# 
# 
# You will catch a fruit if the character is located at the same point as the fruit at some moment in time.
# Can you catch all the fruit in the game?
# Return "Able to catch" (quotes for clarity) if you can, and "Not able to catch" otherwise.
# 
# DEFINITION
# Class:CatchTheBeatEasy
# Method:ableToCatchAll
# Parameters:tuple (integer), tuple (integer)
# Returns:string
# Method signature:def ableToCatchAll(self, x, y):
# 
# 
# CONSTRAINTS
# -x will contain between 1 and 50 elements, inclusive.
# -x and y will contain the same number of elements.
# -The elements in x will be between -1,000 and 1,000, inclusive.
# -The elements in y will be between 0 and 1,000, inclusive.
# 
# 
# EXAMPLES
# 
# 0)
# {-1, 1, 0}
# {1, 3, 4}
# 
# Returns: "Able to catch"
# 
# In order to catch all three pieces of fruit, you have to follow this schedule (always walking at 1 unit per second):
# 
# Walk left for 1 second. When you reach (-1,0), catch the fruit that started at (-1,1).
# Walk right for 2 seconds. When you reach (1,0), catch the fruit that started at (1,3).
# Walk left for 1 second. When you reach (0,0), catch the fruit that started at (0,4).
# 
# 
# 1)
# {-3}
# {2}
# 
# Returns: "Not able to catch"
# 
# The only piece of fruit cannot be caught.
# Even if you start moving left immediately, you will only reach (-2,0) by the time the fruit crosses the y axis.
# 
# 2)
# {-1, 1, 0}
# {1, 2, 4}
# 
# Returns: "Not able to catch"
# 
# 
# 
# 3)
# {0, -1, 1}
# {9, 1, 3}
# 
# Returns: "Able to catch"
# 
# You can catch the pieces of fruit in any order.
# Also note that sometimes you'll want to move slower or wait at some location.
# For example, after catching the pieces of fruit that started at (-1,1) and (1,3), you can walk to (0,0) and wait there for the third piece.
# 
# 4)
# {70,-108,52,-70,84,-29,66,-33}
# {141,299,402,280,28,363,427,232}
# 
# Returns: "Not able to catch"
# 
# 
# 
# 5)
# {-175,-28,-207,-29,-43,-183,-175,-112,-183,-31,-25,-66,-114,-116,-66}
# {320,107,379,72,126,445,318,255,445,62,52,184,247,245,185}
# 
# Returns: "Able to catch"
# 
# 
# 
# 6)
# {0,0,0,0}
# {0,0,0,0}
# 
# Returns: "Able to catch"
# 
# Different pieces of fruit may share the same position.
# You can catch all the pieces at the same time.
# 
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pf 2.3.0!
