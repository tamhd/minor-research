from iplSolver import *
from executeDatabase import *
from trainingData import *
w = [5, 5, 5]
def main():
    for trainingData in readTrainingData():
   	result = iplSolver(trainingData[0], w)
	print result
main()
