"""
Print without putting sting

Read an integer N.
Without using any string methods, try to print the following
    123...N
    Note that "..." represents the values in between
Input Format
The first line contains an integer N.

Output Format
Output the answer as explained in the task.

Sample Input
3

Sample Output
123
"""

n = int(input())

for i in range(1,n+1):
    print(i, end ="")
