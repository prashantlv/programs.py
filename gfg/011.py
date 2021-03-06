def main(li):
    count = Counter(li)
    return count.most_common(1)[0][0]  # 1 for no of element and (0,0) for a in (a,3) 

if __name__ == '__main__':
    from collections import Counter
    li = list(map(int, input().split()))

    print(main(li))
