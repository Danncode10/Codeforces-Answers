'''
Task:
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
'''
n = 5
for i in range(n+1):
    print(' ' * (5-i), end='')
    print('*' * (i), end='')
    print('*' * (i-1))

for i in range(n):
    print(' ' * i, end='')
    print('*' * (n-i), end='')
    print('*' * (n-i-1))
