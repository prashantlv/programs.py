def main():
    n = int(input())
    li = []
    count = 0
    for i in range(n):
        li.append(input())

    for num in li:
        if num.count('1') > 1:
            count += 1
    print(count)        

if __name__ == '__main__':
    main()