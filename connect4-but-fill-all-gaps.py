#Connect 4 but fill it to the top and calculate the score at the end. Cool version.
import random
class GameBoard:
    def __init__(self, size):
        self.size=size
        self.num_entries = [0] * size
        self.items = [[0] * size for i in range(size)]
        self.points = [0] * 2

        self.save = []
   
    def num_free_positions_in_column(self, column):
        count = 0
        for j in range(len(self.items[column])):
            if self.items[column][j] == 0:
                count += 1
        return count #gives a single number, e.g: Num free items in column 1: 4

    def game_over(self):
        acount = 0
        for i in range(len(self.items)):
            for j in range(len(self.items[i])):
                if self.items[i][j] == 0:
                    acount += 1
        if acount == 0:
            return True
        else:
            return False

    def display(self):
        for i in range(len(self.items)-1,-1,-1): 
            for j in range(len(self.items[i])): 
                if self.items[j][i] == 0:
                    print("  ", end="")
                elif self.items[j][i] == 1:
                    print("o ", end="")
                else:
                    print("x ", end="")
            print("")
        sizenumfromzero = [x for x in range(self.size)]
        stringtoprint = ""
        for num in sizenumfromzero:
            stringtoprint = stringtoprint + str(num) + " "
        print("-" * (len(stringtoprint)-1))
        print(stringtoprint)
        print("Points player 1: ", self.points[0], sep="")
        print("Points player 2: ", self.points[1], sep="")


    def num_new_points(self, column, row, player):
        score = 0
        
        #horizontal straight, same row
        for z in range(column-3, column+1):
            if z >= 0: #if z exists:
                try:
                    if (player == (self.items)[z][row]) and (player == (self.items)[z+1][row]) and (player == (self.items)[z+2][row]) and (player == (self.items)[z+3][row]):
                        score += 1
                except:
                    continue

        #vertical straight, same column
        for y in range(row-3, row+1):
            if y >= 0:
                try:
                    if (player == (self.items)[column][y]) and (player == (self.items)[column][y+1]) and (player == (self.items)[column][y+2]) and (player == (self.items)[column][y+3]):
                        score += 1
                except:
                    continue

        #positive diagonal
        for x in range(-3,1):
            if ((column + x) >= 0) and ((row + x) >= 0):
                try:
                    if (player == (self.items)[column+x][row+x]) and (player == (self.items)[column+x+1][row+x+1]) and (player == (self.items)[column+x+2][row+x+2]) and (player == (self.items)[column+x+3][row+x+3]):
                        score += 1
                except:
                    continue

        #negative diagonal
        for w in range(-3,1):
            if ((column + w) >= 0) and ((row - w - 3) >= 0):
                try:
                    if (player == (self.items)[column+w][row-w]) and (player == (self.items)[column+w+1][row-w-1]) and (player == (self.items)[column+w+2][row-w-2]) and (player == (self.items)[column+w+3][row-w-3]):
                        score += 1
                except:
                    continue
        return score
    
    
    def add(self, column, player):
        if (column >= self.size) or (column < 0):
            return False
        else:
            if not self.num_entries[column] == self.size:
                self.num_entries[column] += 1 #num_entries(), e.g: [1, 3, 0]
                if 0 in self.items[column]:
                    firstavaindex = (self.items[column]).index(0)
                    if player == 1:
                        self.items[column][firstavaindex] = 1
                        temp = self.num_new_points(column, firstavaindex, player) 
                        self.points[0] += temp
                    elif player == 2:
                        self.items[column][firstavaindex] = 2
                        temp = self.num_new_points(column, firstavaindex, player)
                        self.points[1] += temp #player points, e.g: Points player 1: 2
            return True


    def free_slots_as_close_to_middle_as_possible(self):
        frommidlist = []
        if (self.size) % 2 == 0:
            largernum = int(self.size / 2)
            smallernum = largernum - 1
            while (smallernum >= 0) and (largernum < self.size):
                if self.num_free_positions_in_column(smallernum) > 0:
                    frommidlist.append(smallernum)
                if self.num_free_positions_in_column(largernum) > 0:
                    frommidlist.append(largernum)
                smallernum -= 1
                largernum += 1
        else:
            x = int(self.size / 2)
            if self.num_free_positions_in_column(x) > 0:
                frommidlist.append(x)
            ln = x - 1 #largernumber
            sn = x + 1 #smallernumber
            while (ln >= 0) and (sn < self.size):
                if self.num_free_positions_in_column(ln) > 0:
                    frommidlist.append(ln)
                if self.num_free_positions_in_column(sn) > 0:
                    frommidlist.append(sn)
                ln -= 1
                sn += 1
        return frommidlist


    def column_resulting_in_max_points(self, player):
        rownum = -1
        savedpointsforeachcolumn = [] #includes points resulted from adding player to columns with free slots
        for i in range(self.size):
            current_point = self.points[player - 1] #points of the player
            if self.num_free_positions_in_column(i) != 0: #num_free_positions_in_column(column), != 0 meaning column not full 
                rownum = self.items[i].index(0) # from that column, get zero, the empty space (row)
                self.add(i, player) #add the counter o or x
                savingpoint = self.points[player - 1] - current_point #new point - original point
                savedpointsforeachcolumn.append([i, savingpoint]) #append to savedpointsforeachcolumn, - the column and the point - this will save the point in the list b4 reseting back
                #so simulation of adding a counter, saving the point, then reseting back
                self.items[i][rownum] = 0 #make the added item empty again (back to original shape)
                self.num_entries[i] -= 1 #set back to original shape after the add()
                self.points[player - 1] = current_point #also set back the point to original too.
        
        # Find out columns which can result in maxpt and store such columns with the max_point into list of maxi 
        maxpt = 0
        maxi = []
        for j in range(len(savedpointsforeachcolumn)):
            if savedpointsforeachcolumn[j][1] > maxpt: # savedpointsforeachcolumn looks like this e.g: [[0, 0], [1, 0], [2, 0], [3, 1]]      [columns, points]
                maxpt = savedpointsforeachcolumn[j][1]
                #setting the max point avabilable
        for k in range(len(savedpointsforeachcolumn)): #check
            if savedpointsforeachcolumn[k][1] == maxpt:
                maxi.append(savedpointsforeachcolumn[k]) # all sets of lists [columns, points] with highest points (that are the same) goes in maxi

        # Use method of free_slots_as_close_to_middle_as_possible() to create a list of reference
        # and find the column of maxpt closest to the middle by referring to the reference list 
        #if all points end up being the same, the priority goes in order of free_slots_as_close_to_middle_as_possible()
        reference = self.free_slots_as_close_to_middle_as_possible() #this returns the list, e.g: [1, 2, 0, 3]
        if len(reference) > 0:
            for m in range(len(reference)):
                for n in range(len(maxi)):
                    if reference[m] == maxi[n][0]:
                        return tuple(maxi[n])
                        #select the earliest number of free_slots_as_close_to_middle_as_possible() and find from maxi that will satistfy 
                        #so find the minimum thats on both list
        else:
            return tuple([])

    
        

class FourInARow:
    def __init__(self, size):
        self.board = GameBoard(size)
    def play(self):
        print("*****************NEW GAME*****************", "Type '999' to peak the Computer's move")
        self.board.display()
        player_number = 0
        print()
        while not self.board.game_over():
            print("Player ", player_number + 1, ": ")
            if player_number == 0:
                valid_input = False
                while not valid_input:
                    try:
                        column = int(input("Please input slot: "))       
                    except ValueError:
                        print("Input must be an integer")
                    else:   
                        if (column < 0) or (column >= self.board.size) or (column == 999):
                            if column == 999: #peak
                                
                                # Choose move which maximises new points for computer (player 2)
                                (best_column, max_points) = self.board.column_resulting_in_max_points(2)
                                if max_points > 0:
                                    iii = best_column
                                else:
                                    # if no move adds new points choose move which minimises points opponent player gets
                                    (best_column, max_points) = self.board.column_resulting_in_max_points(1)
                                    if max_points > 0:
                                        iii = best_column
                                    else:
                                        # if no opponent move creates new points then choose column as close to middle as possible
                                        iii = self.board.free_slots_as_close_to_middle_as_possible()[0]
                                
                                print("For the current board, the Computer is likely to go for column", iii)
                                
                            else:
                                print("Input must be an integer in the range 0 to ", self.board.size - 1)
                        elif (self.board.num_free_positions_in_column(column) == 0):
                            print("Column ", column, "is alrady full. Please choose another one.")
                        else:
                            if self.board.add(column, player_number + 1):
                                valid_input = True
            else:
                
                # Choose move which maximises new points for computer player
                (best_column, max_points) = self.board.column_resulting_in_max_points(2)
                if max_points > 0:
                    column = best_column
                else:
                    # if no move adds new points choose move which minimises points opponent player gets
                    (best_column, max_points) = self.board.column_resulting_in_max_points(1)
                    if max_points > 0:
                        column = best_column
                    else:
                        # if no opponent move creates new points then choose column as close to middle as possible
                        column = self.board.free_slots_as_close_to_middle_as_possible()[0]

                self.board.add(column, player_number + 1)
                
                print("The Computer chooses column ", column)
            self.board.display()   
            player_number = (player_number+1) % 2
        if (self.board.points[0] > self.board.points[1]):
            print("Player 1 (circles) wins!")
        elif (self.board.points[0] < self.board.points[1]):    
            print("Player 2 (crosses) wins!")
        else:  
            print("It's a draw!")
            
next = "y"
while next == "y":
    game = FourInARow(6)
    game.play()
    next = (input("Play another round...? y/n")).lower()
    if next != "y":
        print ("see you later")
        exit ()

