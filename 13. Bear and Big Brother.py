# Link: https://codeforces.com/problemset/problem/791/A
# 800 elo

#Notes:
'''
a <= b
a value triple every year
b value double every year
how many full years will Limak(a) become strictly larger (strictly heavier) than Bob(b)?

'''

a,b = map(int, input().split())
ans = 0
t = 1
while True:
    a = a * 3
    b = b * 2

    if a > b:
        ans = t
        break
    t += 1 # increment

print(ans)