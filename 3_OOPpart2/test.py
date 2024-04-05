import random
arr = ["Sam", "Jonathan", "Kaleab", "Sab", "Zac", "Jackson" ]
while len(arr) != 0 :
    x = random.randint(0,len(arr)-1)
    print(arr[x])
    arr.remove(arr[x])