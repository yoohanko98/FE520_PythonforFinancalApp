# FE520 - Homework 3
# Author: Yoohan Ko
# "I pledge my honor I have abided by the Stevens Honor System"

# create a class called LCG whose instance can generate random numbers by Linear Congruential Generator algorithm
class LCG:
    def __init__(self, seed, multiplier, increment, modulus):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus

    # function to get the seed
    def getSeed(self):
        return self.seed

    # function to set the seed
    def setSeed(self, newseed):
        self.seed = newseed

    # function to initialize the generator (start form the seed)
    def initGenerator(self):
        self.prev_num = (self.multiplier * self.seed + self.increment) % self.modulus
        return self.prev_num / self.modulus

    # function to give me the next random number
    def nextNum(self):
        self.temp_num = self.prev_num
        self.prev_num = (self.multiplier * self.temp_num + self.increment) % self.modulus
        return self.prev_num / self.modulus

    # function to give me a sequence (list) of random number, length should be passed by argument
    def getSequence(self, length):
        num_sequence = []
        if length > 1:
            num_sequence.append(self.initGenerator())
        for i in range(1, length):
            num_sequence.append(self.nextNum())
        return num_sequence

# print("Creating LCG instance:")
# myLCG = LCG(1, 1103515245, 12345, 4294967296)
# print(myLCG.getSeed())
# print(myLCG.getSequence(10))

class SCG(LCG):
    def __init__(self, seed, multiplier, increment, modulus):
        if seed % 4 != 2:
            print("The condition of Seed mod 4 = 2 has not been satisfied. The result of seed mod 4 is: " + str(seed % 4))
            exit()
        super().__init__(seed, multiplier, increment, modulus)

    # overriding the inherited function to give me the next random number using the different recurrence relation
    def nextNum(self):
        self.temp_num = self.prev_num
        self.prev_num = (self.temp_num * (self.temp_num + self.increment)) % self.modulus
        return self.prev_num / self.modulus

print("Creating SCG instance:")
mySCG = SCG(2, 1103515245, 12345, 4294967296)
print(mySCG.getSeed())
print(mySCG.getSequence(10))

