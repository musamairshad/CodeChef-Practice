# NAME: MUHAMMAD USAMA
# DIFFICULTY RATING: 238

T = int(input())
for i in range(T):
    X, Y  = input().split()
    if(int(X) + int(Y) > 6):
        print("YES")
    else:
        print("NO")