https://www.naukri.com/code360/problems/reverse-star-triangle_6573685?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=PROBLEM

Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the Reverse N-Star Triangle.

Example:
Input: ‘N’ = 3

Output: 

*****
 ***
  *

  def nStarTriangle(n: int) -> None:
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ', end='')
        for j in range(2 * i -1):
            print('*',end='')
        print()
        

        