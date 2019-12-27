# There is a robot starting at position (0, 0), the origin, on a 2D plane. 
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after
#  it completes its moves.

#The move sequence is represented by a string, and the character moves[i] 
# represents its ith move. Valid moves are R (right), L (left), U (up), and D (down).
#  If the robot returns to the origin after it finishes all of its moves, return true. 
# Otherwise, return false.

#Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

#Example 1:
#Input: "UD"
#Output: true 
#Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.


def origin_check(moves):
    first_spot = [0, 0]
    final_spot = [0, 0]
    for move in moves:
        if move == 'R':
            final_spot[0] += 1
        elif move == 'L':
            final_spot[0] -= 1
        elif move == 'U':
            final_spot[1] += 1
        elif move == 'D':
            final_spot[1] -= 1
    if final_spot == first_spot:
        print("True")
    else: 
        print("False")

da_moves = "RRUDLDUL"
origin_check(da_moves)
    

        