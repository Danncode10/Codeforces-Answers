# Link: https://codeforces.com/problemset/problem/271/A
# 800 elo

# year = []
# for num in map(int, input()): # wlang slit() kase no space ang input
# 	year.append(num)
#
# # 4 digits
#
# answer = 0
# match = False
#
# while not match:
#
# 	# Convert year[] to num
#
#
# 	for i in range(4+1):
# 		for j in range(4 - i):
# 			if year[i] == year[j]:
# 				match = True
#
#
# print(year)

year = int(input())

found = False

while not found:
	duplicate = False

	# increment year:
	year += 1

	str_year = str(year)

	# print(str_year)

	for i in range(4):
		for j in range(i+1, 4): # starts at i, ends in 4
			# print(f"Comaring {str_year[i]} and {str_year[j]}")
			if str_year[i] == str_year[j]:
				duplicate = True
				break

	if not duplicate:
		found = True


print(year)







