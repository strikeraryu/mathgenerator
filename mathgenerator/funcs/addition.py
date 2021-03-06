from .__init__ import *


def additionFunc(maxSum=99, maxAddend=50):
    a = random.randint(0, maxAddend)
    # The highest value of b will be no higher than the maxsum minus the first number and no higher than the maxAddend as well
    b = random.randint(0, min((maxSum - a), maxAddend))
    c = a + b
    problem = str(a) + "+" + str(b) + "="
    solution = str(c)
    return problem, solution


addition = Generator("Addition", 0, "a+b=", "c", additionFunc)
