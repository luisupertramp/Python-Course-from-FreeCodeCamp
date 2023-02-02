import copy
import random
# Consider using the modules imported above.

# random.seed(95)
class Hat():

    def __init__(self, **hatContent) :
        self.contents = []
        for key,value in hatContent.items() :   # looping through all of the arguments transformed as a list of tuples
            for i in range(value) :
                self.contents.append(key)       # adding the key, 'i' amount of times. for isntance: 'red', 'red', 'red'

    def draw(self, ballsToDraw) :
        selectedBalls = []                      # list of strings to return

        if ballsToDraw < len(self.contents) :     # if the amount of balls to draw is less than the total of balls..
            for i in range(ballsToDraw) :       
                # ... append random balls to a new list and remove them from the copied list
                randomPosition = random.randint(0, len(self.contents)-1)
                selectedBalls.append(self.contents[randomPosition])
                self.contents.pop(randomPosition)
        
        else :  # ... otherwise, remove all balls
            selectedBalls = self.contents.copy()
            self.contents = []

        return selectedBalls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    copyOfBalls = copy.copy(hat.contents)
    success = 0

    for i in range(num_experiments) :           # run N amount of experiments
        drewBalls = hat.draw(num_balls_drawn)   # get the draw balls specified
        drewBalls.sort()                        # ... and sort them

        drewBallsDict = {}                      # a dictionary is created for the drew balls...
        for ball in drewBalls :
            # ... with the same format as the expected balls (a dictionary) so they can be compared 
            drewBallsDict[ball] = drewBallsDict.get(ball, 0) + 1

        foundBalls = True                       # flag to indicate that all balls were found
        for key, val in expected_balls.items() :    # looping over expected balls
            # if the expected color is (NOT) found in the drew balls, and the amount is (NOT) equal or greater...
            if not (key in drewBallsDict.keys() and drewBallsDict[key] >= val):
                foundBalls = False              # balls were not found
        
        # Then the flag is evaluated and if is still True, the counter for successful experiments increases by 1
        if foundBalls :
            success += 1

        hat.contents = copy.copy(copyOfBalls)

    return success/num_experiments

# hat1 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9, green=3)
# hat = Hat(blue=3, red=2, green=6)
# print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))
