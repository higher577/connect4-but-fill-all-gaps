Inspired by a university project. This version was reimplemented independently.

Worked with python on IDLE.

When the program is executed, the prompt will ask "Please input slot:" with the connect 4 board displayed, the user will play by inputing the numbers on the board.
The game rule is similar to "Connect 4", however the game finishes after all the gaps has been filled up to the brim, the player with the most points (most groups of 4) wins.
The user (Player 1, circle 'o') will verse the computer (Player 2, crosses 'x'), where its algorithm sees which columns (slot) can be slotted, and finds which column result in maximum points, 
and if the multiple column gives equal maxmum points, the priority goes to the column as close to the middle of the board.

There are 6 columns, columns 0 to 5, each can be filled with 6 counters ('o' or 'x').
if there is consequtive counters more than 4, e.g.: 'o x x x x x' <- there is 2 groups of 4, so its counts as 2 points, same for vertical, and diagonal cases.
likewise for 'x x x x x x' (3 groups of 4, so 3 points).

There is also a ‘peak’ option, which is a feature that give the user a hint when playing against the computer. 
User inputs ‘999’ to the slot instead of column inputs allowed, this will allow the user to see the hint. 
From current game board, the code calculates the next best move and tells the player what column the computer will take next.


A problem faced when coding, was when the computer gave a different input to what it said:
![image](https://github.com/user-attachments/assets/d8e0d862-8682-4ab9-befe-8f93df129ac0)

I was confused and thought the code was wrong, however, I found out that the computer chooses the best possible moves, and it changes constantly. 
The computer's prediction changes depending on what input the user puts in, so the prediction can be wrong as in the above case.
The calculation changed as the user puts in a counter in column 1.
I did not see any way to predict the user’s input which will affect the computer’s choice in the next step, so I decided to give a warning to the player, by changing the quote with meaning that prediction is a possibility.
