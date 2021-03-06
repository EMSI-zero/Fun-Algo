



class Cube:
    def __init__(self, W , front, back , left , right , top , bottom) -> None:
        """initiates a Cube object with given parameters   

        Args:
            W ([int]): wight of the cube
            front ([int]): color of front side
            back ([int]): color of back side
            left ([int]): color of left side
            right ([int]): color of right side
            top ([int]): color of top side
            bottom ([int]): color of bottom side
        """
        self.W = W
        self.sides = { 0: front , 1: back , 2: left , 3: right , 4: top , 5: bottom }
    
    
    def getSideColor(self , side):
        """get the color of the given side

        Args:
            side (int): index of the given side
            
        Returns:
            int : color of the given side
        """
        return self.sides[side]
    
    def getOppositeSide(self, side):
        """find the color of the opposite side of the cube
            sides position as { 0: front , 1: back , 2: left , 3: right , 4: top , 5: bottom }
        Args:
            side (int): given side of the cube
        
        Returns:
            int : color of the opposite side
        """
        return self.sides[(side+1) if (side%2==0) else side - 1] 
    
    def getWeight(self):
        """get weight of the cube

        Returns:
            int: weight of the cube
        """
        return self.W
    
    
    def __str__(self) -> str:
        return str(self.W)    


def sortBlocksbyWeight(blocks):
    """sorts a set of blocks by their wieght

    Args:
        blocks (list): set of blocks

    Returns:
        list: list of sorted blocks
    """
    return sorted(blocks , key=lambda b: b.getWeight())



cubes = []

numberOfBlocks = (int)(input())

for i in range(0,numberOfBlocks):
    inputStr = list(map(int , input().split()))
    cubes.append(Cube(inputStr[0], inputStr[1] ,inputStr[2] ,inputStr[3] ,inputStr[4] ,inputStr[5], inputStr[6]))
    
cubes = sortBlocksbyWeight(cubes)

#A dynamic programming table to record the highest possible tower
# with n blocks and space for recording the optimal choice for each step
T = [[[0 for i in range(0,6)]for j in range(0,numberOfBlocks)] for k in range(0,3)]
for i in range(0,numberOfBlocks):
    for j in range(0,6):
        T[0][i][j] = 1  

print(T)
#Maximum tower: max height, best starting block, best starting side
hmax = [0]*3


#fill the table for blocks and sides from the bottom block to the top for a tower of height i.
# And recording the Optimal step(top block) for each pair of blocks.

# check from cube 2 to n. 
# cube 1 is the lightest so the best possible solution is already 1.
for i in range(1,numberOfBlocks):
    # topside of cube i
    for ti in range(0,6):
        # check for cube above
        for j in reversed(range(0, i)):
            # top side of cube j
            for tj in range(0,6):
                # check if topside of i matches bottomside of j
                if(cubes[i].getSideColor(ti) == cubes[j].getOppositeSide(tj)):
                    # check if cube above has the optimal solution
                    if(T[0][j][tj] + 1 > T[0][i][ti]):
                        # print('\n\ni= ',i,'j= ',j,'\n\n')
                        # for row in range(0,numberOfBlocks):
                            # print(T[0][row])
                        # for k in range(0,numberOfBlocks):
                        #     print(T[0][:][k])  
                        T[0][i][ti] = T[0][j][tj] + 1
                        T[1][i][ti] = j # best block above cube i is cube j
                        T[2][i][ti] = tj # best bottom side for cube j is tj
                        
                        # print("T=" , T[0][i][ti])
                        
                        # put cube i as best starting block.
                        if(T[0][i][ti] > hmax[0]):
                            hmax[0] = T[0][i][ti]
                            # print("hmax=" , hmax[0])
                            hmax[1] = i # best starting block
                            hmax[2] = ti # best side for cube i
                        # input()

print(hmax)

for i in range(0,hmax[0]):
    print("block=" , hmax[1]+1 , ", side= " , hmax[2])
    next = [hmax[1] , hmax[2]]
    hmax[1] = T[1][next[0]][next[1]]
    hmax[2] = T[2][next[0]][next[1]]

                        