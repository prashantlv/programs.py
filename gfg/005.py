
#code
def main():
    arr = list(map(int, input().split()))
    a=[]
    for i in range(len(arr)):
        if arr[i] < 0:
            a.insert(1, arr[i])
        else:
            a.insert(len(a), arr[i])
    print(a)        

if __name__ == '__main__':
    main()
