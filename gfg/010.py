def main(l,arr):
    #numofjumps = []
    minimumjumps = 0
    for i in range(l):
        for j in range(i):
           if arr[i]>=j:
               minimumjumps += 1
    print(minimumjumps)

if __name__ =="__main__":
    l = int(input())
    arr = list(map(int, input().split()))
    main(l,arr)
