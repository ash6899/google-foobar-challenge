# Don't Get Volunteered!
# ======================

# As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

# To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution(0, 1)
# Output:
#     3

# Input:
# solution.solution(19, 36)
# Output:
#     1

# -- Java cases --
# Input:
# Solution.solution(19, 36)
# Output:
#     1

# Input:
# Solution.solution(0, 1)
# Output:
#     3

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

dp = [[0 for i in range(8)] for j in range(8)]; 
def getsteps(x, y, tx, ty): 
    if (x == tx and y == ty): 
        return dp[0][0]; 
    elif(dp[abs(x - tx)][abs(y - ty)] != 0): 
        return dp[abs(x - tx)][abs(y - ty)]; 
    else: 
        x1, y1, x2, y2 = 0, 0, 0, 0; 
        if (x <= tx): 
            if (y <= ty): 
                x1 = x + 2; 
                y1 = y + 1; 
                x2 = x + 1; 
                y2 = y + 2; 
            else: 
                x1 = x + 2; 
                y1 = y - 1; 
                x2 = x + 1; 
                y2 = y - 2; 
        elif (y <= ty): 
            x1 = x - 2; 
            y1 = y + 1; 
            x2 = x - 1; 
            y2 = y + 2; 
        else: 
            x1 = x - 2; 
            y1 = y - 1; 
            x2 = x - 1; 
            y2 = y - 2; 
        dp[abs(x - tx)][abs(y - ty)] = min(getsteps(x1, y1, tx, ty),getsteps(x2, y2, tx, ty)) + 1
        dp[abs(y - ty)][abs(x - tx)] = dp[abs(x - tx)][abs(y - ty)]; 
        return dp[abs(x - tx)][abs(y - ty)]; 
def solution(src, dest):
    n = 8
    x = src//8
    y = src%8
    tx = dest//8 
    ty = dest%8 
    if ((x == 1 and y == 1 and tx == 2 and ty == 2) or
            (x == 2 and y == 2 and tx == 1 and ty == 1)): 
        ans = 4; 
    elif ((x == 1 and y == n and tx == 2 and ty == n - 1) or
        (x == 2 and y == n - 1 and tx == 1 and ty == n)): 
        ans = 4; 
    elif ((x == n and y == 1 and tx == n - 1 and ty == 2) or
        (x == n - 1 and y == 2 and tx == n and ty == 1)): 
        ans = 4; 
    elif ((x == n and y == n and tx == n - 1 and ty == n - 1) 
        or (x == n - 1 and y == n - 1 and tx == n and ty == n)): 
        ans = 4; 
    else: 
        dp[1][0] = 3; 
        dp[0][1] = 3; 
        dp[1][1] = 2; 
        dp[2][0] = 2; 
        dp[0][2] = 2; 
        dp[2][1] = 1; 
        dp[1][2] = 1; 
        ans = getsteps(x, y, tx, ty)
    return ans

