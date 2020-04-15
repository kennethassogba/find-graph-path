import random
verbose = False  # Set to True if you want to print cleaning step

# === Class for room to clean ===


class Cleaning(object):
    """
    The Cleaning class defines the main storage point for room to clean.
    Each room has seven fields :
    - **nx** - number of rows of the room
    - **ny** - number of columns of the room
    - **dim** - nxny
    - **grilleList** - list of string who tell walls position
    - **robots** - dict that contain robots colors and their positions
    - **casesPropre** - used to control if the room is clean
    - **graph** - stores the possible deplacements from each box
    """

    def __init__(self, nx, ny, grilleList, robots):
        self.nx = nx  # int
        self.ny = ny  # int
        self.dim = nx*ny  # int
        self.grilleList = grilleList  # list
        self.robots = robots.copy()  # dict
        self.casesPropre = [0]*self.dim  # clean box = 1 else 0
        # we generate a dict with the keys from 0 to dim-1
        # and we simply connect the related boxes
        self.graph = {i: self.voisinCaseList(i) for i in range(self.dim)}
        if(verbose):
            print("Sans murs")
            print(self.graph)
        # we place the internal walls
        for i, murs in enumerate(grilleList):
            for j, bin in enumerate(murs):
                if bin == '1':
                    self.graph[i][j] = -1
        if(verbose):
            print("Avec murs")
            print(self.graph)
        # we place the robots
        for key in robots:  # a method exist for that
            position = robots[key]
            self.casesPropre[position] = 1  # Robots clean their starting boxes
            caseVoisinRobot = self.voisinCaseList(position)
            for idc, case in enumerate(caseVoisinRobot):
                if case != -1:
                    self.graph[case][(idc+2) % 4] = -1
                    """
                    if box B is at position i about box A, ie A:[-1,B,-1,-1]
                    then A is at the position (i+2)%4 relative to B,
                    ie B:[-1,-1,-1,A]
                    """
        if(verbose):
            print("With robots")
            print(self.graph)
        if(verbose):
            print("Clean Boxes")
            print(self.casesPropre)

    def voisinCaseList(self, n):
        """
        Returns the related boxes of a 
        given box in order [W,S,E,N]
        """
        voisinsList = [-1, -1, -1, -1]
        for i in range(4):
            if i == 0:  # West
                calc = n-1
            elif i == 1:  # South
                calc = n+self.ny
            elif i == 2:  # Est
                calc = n+1
            elif i == 3:  # North
                calc = n-self.ny

            if calc < 0 or calc >= self.dim:
                calc = -1
            voisinsList[i] = calc

        if (n % self.ny == 0):  # We are on the left edge
            voisinsList[0] = -1
        elif (n % self.ny == self.ny-1):  # We are on the right edge
            voisinsList[2] = -1

        return voisinsList

    def voisinListMur(self, n):
        """
        Returns the boxes next to a given box in the 
        order [W, S, E, N] taking into account the walls
        """
        voisinlistmur = self.voisinCaseList(n)
        for j, bin in enumerate(self.grilleList[n]):
            if bin == '1':
                voisinlistmur[j] = -1
        return voisinlistmur

    def free(self, n):
        """
        When a robot moves, we 
        release the box it left empty
        """
        voisins = self.voisinListMur(n)
        for j, case in enumerate(voisins):
            if(case != -1):
                self.graph[case][(j+2) % 4] = n

    def placeRobot(self, robots):
        """
        Place the robots on the grid:
        Updates the graph according to the current position of the robots
        """
        for key in robots:
            position = robots[key]
            caseVoisinRobot = self.voisinCaseList(position)
            for idc, case in enumerate(caseVoisinRobot):
                if case != -1:
                    self.graph[case][(idc+2) % 4] = -1

    def deplRobot(self, robotJoueur, greed1, greed2):
        """
        Move a robot and return the movement made.
        Strategy : epsilon-gamma-greedy
        """
        # we recover its position
        positionRobotJoueur = self.robots[robotJoueur]
        if(verbose):
            print("positionRobotPlayer ->", positionRobotJoueur)
        # we check the possible displacements from this position
        casesConnexes = self.graph[positionRobotJoueur]
        # we isolate the possible directions
        directionPossible = {i: depl for i, depl in enumerate(casesConnexes) if depl != -1}
        if(verbose):
            print("casesConnexesPossibles", directionPossible)
        # we choose a direction among the possible according to the strategy
        lucky = random.random()  # random number in [0,1)
        if lucky < greed1:  # ->random
            navigation = random.choice(list(directionPossible.keys()))
        elif lucky >= greed1 and lucky < greed2:  # ->dirGainMin
            navigation = self.dirGainMin(positionRobotJoueur, directionPossible)
        else:  # ->dirGain
            navigation = self.dirGain(positionRobotJoueur, directionPossible)

        if(verbose):
            print("Direction ---->", navigation)

        caseNext = directionPossible[navigation]
        # -> free the old box (we add it to its neighbors)
        self.free(positionRobotJoueur)
        # we go in the direction of navigation as long as there is no problem
        while(caseNext != -1):
            caseCurrent = caseNext
            # we clean the boxes on which we pass
            self.casesPropre[caseCurrent] = 1
            caseNext = self.graph[caseCurrent][navigation]
        # we update the robot position
        self.robots[robotJoueur] = caseCurrent
        # -> take the new box (we delete at the neighbors)
        # we place the robot on the grid
        self.placeRobot(self.robots)

        return robotJoueur+self.pointsCardinaux(navigation)

    def clean(self, lenoptimal, greed1, greed2):
        """
        Cleans a grid
        """
        iter_lenoptimal = 0
        chemin = []
        if(verbose):
            print("Let's start the game")
        # until the grid is clean
        while(self.casesPropre.count(0) != 0):
            # We chose a robot randomly among those who can move
            while True:
                robotJoueur = random.choice(list(self.robots.keys()))
                if (self.graph[self.robots[robotJoueur]]).count(-1) != 4:
                    break  # check that the robot can move if not change the robot

            if(verbose):
                print("<----------- ROBOT PLAYER ->", robotJoueur)
            # we move the robot
            depl = self.deplRobot(robotJoueur, greed1, greed2)
            chemin.append(depl)
            iter_lenoptimal += 1
            if(verbose):
                print("CleanedBoxes", self.casesPropre)

            if (iter_lenoptimal > lenoptimal):
                return "------------PATH TOO LONG---------"

        return chemin

    def gainDeplacement(self, case, direction):
        """
        Determine the gain obtained (number of pieces cleaned) 
        by making a given move from a box
        """
        gain = 0
        casesPropreSuivies = []
        caseCurrent = self.graph[case][direction]
        proprete = self.casesPropre[caseCurrent]
        casesPropreSuivies.append(proprete)
        caseNext = self.graph[caseCurrent][direction]
        while caseNext != -1:
            caseCurrent = caseNext
            proprete = self.casesPropre[caseCurrent]
            casesPropreSuivies.append(proprete)
            caseNext = self.graph[caseCurrent][direction]
        gain = casesPropreSuivies.count(0)
        return gain

    def dirGain(self, positionRobotJoueur, directionPossible):
        """
        input: Possible directions of a robot.
        output: Returns the direction of maximum gain
        """

        dirOptList = []
        diropt = 0
        gainMax = 0
        for dir in directionPossible.keys():
            gain = self.gainDeplacement(positionRobotJoueur, dir)
            if(verbose):
                print("MAX -> dir {}, gain {}".format(dir, gain))
            if gain > gainMax:
                gainMax = gain

        if(verbose):
            print("gainMax", gainMax)
        for dir in directionPossible.keys():
            if self.gainDeplacement(positionRobotJoueur, dir) == gainMax:
                dirOptList.append(dir)
        diropt = random.choice(dirOptList)
        return diropt

    def dirGainMin(self, positionRobotJoueur, directionPossible):
        """
        input: Possible directions of a robot.
        output: Returns the direction of non-zero minimum gain
        """

        dirOptList = []
        gainMinList = []
        for dir in directionPossible.keys():
            gain = self.gainDeplacement(positionRobotJoueur, dir)
            if(verbose):
                print("MIN -> dir {}, gain {}".format(dir, gain))
            gainMinList.append(gain)

        gainMinList = [gain for gain in gainMinList if gain != 0]
        if gainMinList == []:
            return random.choice(list(directionPossible.keys()))

        gainMin = min(gainMinList)
        if(verbose):
            print("gainMin", gainMin)
        for dir in directionPossible.keys():
            if self.gainDeplacement(positionRobotJoueur, dir) == gainMin:
                dirOptList.append(dir)
        diropt = random.choice(dirOptList)
        return diropt

    def check_cleaning(self, path):
        """
        Check if some input path clean the room
        """
        path = path.split()
        for depl in path:
            robotJoueur = depl[0]
            navigation = self.pointsCardinauxReverse(depl[1])
            positionRobotJoueur = self.robots[robotJoueur]
            caseNext = self.graph[positionRobotJoueur][navigation]
            self.free(positionRobotJoueur)
            while(caseNext != -1):
                caseCurrent = caseNext
                # we clean the boxes on which we pass
                self.casesPropre[caseCurrent] = 1
                caseNext = self.graph[caseCurrent][navigation]
            # we update the robot position
            self.robots[robotJoueur] = caseCurrent
            # we place the robot on the grid
            self.placeRobot(self.robots)

        if self.casesPropre.count(0) != 0:
            return False
        else:
            return True

    def has_wall(self, num_case, navig):
        """
        Check if a box has a wall in the given direction
        """
        if self.grilleList[num_case][self.pointsCardinauxReverse(navig)] == '1':
            return True
        else:
            return False

    def can_move(self, r, navig):
        """
        Check if a robot can move in the given direction
        """
        if self.graph[self.robots[r]][self.pointsCardinauxReverse(navig)] == -1:
            return False
        else:
            return True

    def pointsCardinaux(self, P):
        """
        For a number between 0 and 3 returns the corresponding cardinal point 
        in accordance with the adopted nomenclature
        """
        if P == 0:
            return 'W'
        elif P == 1:
            return 'S'
        elif P == 2:
            return 'E'
        elif P == 3:
            return 'N'

    def pointsCardinauxReverse(self, P):
        """
        For a cardinal point, returns the number between 0 and 3 corresponding, 
        in accordance with the nomenclature adopted
        """
        if P == 'W':
            return 0
        elif P == 'S':
            return 1
        elif P == 'E':
            return 2
        elif P == 'N':
            return 3

    def __del__(self):
        """
        Delete copy of robots
        """
        del self.robots
