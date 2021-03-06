def main(li):
    count = Counter(li)
    return count.most_common(1)[0][0] 

if __name__ == '__main__':
    from collections import Counter
    li = list(map(int, input().split()))

    print(main(li))
