def main():
    count = 0
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(float, input().split()))
        for k in range(n-2,-1,-1):
            if a[k] == float(1):
                pass
            elif a[k] == float(0):
                count +=1
                break
            else:
                count += 1
        print(count)
        count = 0        

if __name__ == '__main__':
    main()