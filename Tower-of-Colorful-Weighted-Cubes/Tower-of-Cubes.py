


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