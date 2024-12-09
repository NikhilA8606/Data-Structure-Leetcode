    https://www.naukri.com/code360/problems/star-triangle_6573671?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems
    Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Triangle.

Example:
Input: ‘N’ = 3

Output: 

  *
 ***
*****

def nStarTriangle(n: int) -> None:
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(' ', end='')
        # Print stars
        for j in range(2 * i + 1):
            print('*', end='')
        # Move to the next line
        print()

    
    