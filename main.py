from cleaning import Cleaning
import time

"""Main

This script allows the user to test our algorithm.

This file can also be imported as a module and contains the following
functions:

    * formatForClean - returns the good input format for Cleaning class
    * findpath - rerun the Cleaning.cleaning() method several times and only return the optimal path
    * checkpath - check if a path is true
    * setparameters - set iteration and greed interval for an input file
"""


def formatForClean(filename):
    """Used to format the input file for Cleaning class

    Parameters
    ----------
    filename : str
        The input file location

    Returns
    -------
    nx, ny, nd
        room lenth and number of robots
    grilleList
        list of string who tell walls position
    robots : dict
        'robotColor': robotPosition
    """
    f = open(filename, 'r')
    # if f.mode == 'r': #Condition to test if the file is well read
    data = []
    for line in f.readlines():
        data.append(line)
    data = [line.rstrip("\n") for line in data if line]

    # First line
    nx, ny, nd, *_ = map(int, data[0].split())

    # Room wall data
    grilleList = data[1:nx+1]
    # print('#1 ->', grilleList)
    # to have list of list of int
    grilleList = [[int(d, base=16) for d in str(number)] for number in grilleList]
    # print('#2 ->', grilleList)
    # to convert in binary
    grilleList = [["{0:04b}".format(ch) for ch in line] for line in grilleList]
    # print('#3 ->', grilleList)
    # to flat the list of lists
    grilleList = [item for sublist in grilleList for item in sublist]
    # print('#4 ->', grilleList)

    # Robots data
    robotsLines = data[nx+1:nx+1+nd]
    robots = {}  # dict {'B': 1, 'R': 4}
    for line in robotsLines:
        couleur, x, y, *_ = line.split()
        x = int(x)
        y = int(y)
        position = x*ny+y
        robots[couleur] = position

    f.close()
    return nx, ny, nd, grilleList, robots


def findpath(filename):
    """rerun the Cleaning.cleaning() method several times and only return the optimal path

    Parameters
    ----------
    filename : str
        The input file location

    Returns
    -------
    ' '.join(cheminOptimal) : str
        Optimal path
    """

    nx, ny, nd, grilleList, robots = formatForClean(filename)
    lenoptimal = nx*ny*nd
    iteration, greed1, greed2 = setparameters(filename)
    cheminOptimal = []

    for i in range(iteration):
        piece = Cleaning(nx, ny, grilleList, robots)
        chemin = piece.clean(lenoptimal, greed1, greed2)
        if(type(chemin) == list):
            if len(chemin) < lenoptimal:
                lenoptimal = len(chemin)
                cheminOptimal = chemin

    return ' '.join(cheminOptimal)


def checkpath(filename, path):
    """
    Check if some input path clean the room
    """
    nx, ny, _, grilleList, robots = formatForClean(filename)
    piece = Cleaning(nx, ny, grilleList, robots)
    return piece.check_cleaning(path)


def compute_move(filename, r, navig):
    """
    Compute some move and return robot final position
    """
    nx, ny, _, grilleList, robots = formatForClean(filename)
    piece = Cleaning(nx, ny, grilleList, robots)
    positionRobotJoueur = piece.robots[r]

    casesConnexes = piece.graph[positionRobotJoueur]
    directionPossible = {i: depl for i, depl in enumerate(casesConnexes) if depl != -1}
    navigation = piece.pointsCardinauxReverse(navig)
    caseNext = directionPossible[navigation]
    # # free the old box (we add it to its neighbors)
    piece.free(positionRobotJoueur)
    # we go in the direction of navigation as long as there is no problem
    while(caseNext != -1):
        caseCurrent = caseNext
        piece.casesPropre[caseCurrent] = 1
        caseNext = piece.graph[caseCurrent][navigation]
    # we update the robot position
    piece.robots[r] = caseCurrent
    return caseCurrent


def setparameters(filename):
    """set iteration and greed interval for an input file

    Parameters
    ----------
    filename : str
        The input file location

    Returns
    -------
    iteration
        Number of cleaning iterations
    epsilon, epsilon+gamma
        Interval for greedy method (see our report)
    """
    if filename.endswith("Case_Aspi_R_0.txt"):
        iteration = 200
        epsilon = 0.1
        gamma = 0.0
    elif filename.endswith("Case_Aspi_R_1.txt"):
        iteration = 200
        epsilon = 0.1
        gamma = 0.0
    elif filename.endswith("Case_Aspi_R_2.txt"):
        iteration = 10000
        epsilon = 0.1
        gamma = 0.0
    elif filename.endswith("Case_Aspi_R_3.txt"):
        iteration = 200000
        epsilon = 0.15
        gamma = 0.2
    elif filename.endswith("Case_Aspi_R_4.txt"):
        iteration = 60000
        epsilon = 0.15
        gamma = 0.8
    elif filename.endswith("Case_Aspi_R_5.txt"):
        iteration = 20000
        epsilon = 0.1
        gamma = 0.1
    elif filename.endswith("Case_Aspi_R_6.txt"):
        iteration = 200000
        epsilon = 0.2
        gamma = 0.1
    elif filename.endswith("Case_Aspi_R_7.txt"):
        iteration = 40000
        epsilon = 0.15
        gamma = 0.0
    else:
        iteration = 500000
        epsilon = 0.15
        gamma = 0.15

    return iteration, epsilon, epsilon+gamma


if __name__ == '__main__':
    start_time = time.perf_counter()
    cheminOptimal = findpath("input/Case_Aspi_R_0.txt")
    end_time = time.perf_counter()

    min = (end_time-start_time)//60
    sec = (end_time-start_time) % 60
    print("-----------------------------")
    print("The optimal path is : ")
    print(cheminOptimal)
    print('of size ' + str(len(cheminOptimal.split())) + ' total displacements')
    print('en ' + str('{}'.format(min)) + ' minutes and '+str('{:.2f}'.format(sec)) + ' seconds')
