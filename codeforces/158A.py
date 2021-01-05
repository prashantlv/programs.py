def main():
    n,k = map(int, input().split())
    li = []
    count = 0
    li = input().split()
    for j in li:
        if int(j) > k:
            count += 1
    print(count)            
if __name__ == '__main__':
    main()

#wrong ans to test case3 FUCK THIS CONTEST