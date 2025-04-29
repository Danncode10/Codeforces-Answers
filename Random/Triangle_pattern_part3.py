'''
     *
    ***
   *****
  *******
   *****
    ***
     *
'''

n = 5

for i in range(n):
	print(' ' * (n - i), end='')
	print('*' * i, end='')
	print('*' * (i - 1))

for i in range(n):
	print(' ' * i, end='')
	print('*' * (n - i - 1), end='')
	print('*' * (n-i))


