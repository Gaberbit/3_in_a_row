# 3 in a row puzzle solver
## This is my first public Python project!

### Goal: Solve a 3 in a row puzzle in the shortest possible time.


### Rules: 

Given an n by n board, complete each row and column such that. 
they have an equal number of blue and white squares, and.
no color is repeated three times consecutively.

### Approach:

We begin by initializing a Selenium Chrome driver,  
after doing so we define our Board class which will be used to make. 
our Board object. 

The Board class has two instance variables, board (Array) and size (Int),. 
as well as three functions, makeBoard, solveBoard, and updateBoard. 
these functions are used respectively to pull the board from, solve,. 
and push the solved board back to the webpage.

#### makeBoard funcion

When called this function starts by accessing the BrainBashers.com.  
page containing the 3 in a row puzzle select screen. It then selects. 
our chosen board size and brings up a random archived board.

We inialize a set of nested for loops, the first loop. 
creates a row Array and the second appends the color value,. 
as a character representing the last letter of the color:. 
"e" for white, "k" for black (the website defines blue squares as. 
black), and "y" for grey. 
of each sqaure in the web board to our row Array by iterating through. 
all of the xpaths of the squares on the web Board.  

Once the second loop has finished the first loop then appends. 
the newly created row Array to the board Array until the board is. 
complete. 

### solveBoard function

The solve board function utilizes four loops to solve the board. 

The first is a while loop that continues to execute while the. 
size of a set called solvedRows is less than the size of the board. 

Nested inside the first, The second loop is a for loop which. 
iterates over each row array in our board. 

Inside the second loop are two more nested for loops which iterate over. 
each square character in our rows and columns.   

Using these two nested loops we execute a series of conditional statements. 
which tell us if the square we are on is preceded, surrounded, or followed by.  
two of the same color, if it is we set it equal to a character denoting the. 
opposite color. 

after these two loops, we check if the row has all of it's blues or white's. 
and if so we set the remaining grey squares equal to the opposite color. 

Finally we check if the row is complete and of so we add it's index to the. 
solvedRows set. 

Our board should now be solved!

### updateBoard function

Our final function updates the web board by again finding all of the. 
sqaures xpaths and clicking them once to set them blue and twice to set. 
them white according to our solved board character at their given index.

The web board is now solved!!


#### Closing Remarks:
Thanks for checking out my project, I love solving 3 in a row puzzles and seeing a program. 
obliterate everyone that is throw at it is very satisfying :). 
This was a very fun first public project and I highly reccommend trying to solve this yourself. 
and improving the program to see if you can get an even faster time!






