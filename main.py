#Marc Paul
#Implementation of a simple agent

import random

    
class Agent:
    #This agent will have a name, age, and an X and Y position
    def __init__(self, name, age, locationX, locationY):
        self.__name__ = name
        self.age = age
        self.locationX = locationX
        self.locationY = locationY
    
    #If we want to change the name
    def setName(self, name):
        self.__name__ = name
    #If we want to get the name
    def getName(self):
        return self.__name__

    #Moves the agent to a random location
    def MoveLocationRandom(self):
        #Gives a random X, Y value between 0 and 2000
        randomX = random.randint(0,2000)
        randomY = random.randint(0,2000)
        
        #This is a function to make the X value either + 1 or - 1
        #Until the X value is the same as the random value
        while(self.locationX != randomX):
            if(self.locationX < randomX):
                self.locationX += 1
            else:
                self.locationX -= 1
        #This is a function to make the Y value either +1 or -1
        #Until the Y value is the same as the random value.
        while(self.locationY != randomY):
            if(self.locationY < randomY):
                self.locationY += 1
            else:
                self.locationY -= 1
    #Turns the Y value into Y - 1    
    def LocationSouth(self):
        self.locationY = self.locationY - 1
    
    #If temp is less than the agent's age then add 1 to the X,Y, and temp value
    def MoveLocationBasedOnAge(self):
        temp = 0
        while(temp < self.age):
            self.locationX = self.locationX + 1
            self.locationY = self.locationY + 1
            temp = temp + 1
            
        
def main():
    ai = Agent( "John", 54, 0, 0)
    print("The ai agents intial name is: " + ai.getName())
    ai.setName("Bob")
    print("The name of the ai agent after being changed is: " + ai.getName())
    print("The age of the ai agent is:", ai.age)
    ai.MoveLocationRandom()
    print("The location on the x-axis of the ai agent after a random location move is:", ai.locationX)
    print("The location on the y-axis of the ai agent after a random location move is:", ai.locationY)
    ai.LocationSouth()
    print("The location of the ai agent after going south is:", ai.locationY)
    ai.MoveLocationBasedOnAge()
    print("The location on the x-axis of the ai agent after moving based on age is:", ai.locationX)
    print("The location on the y-axis of the ai agent after moving based on age is:", ai.locationY)


main()