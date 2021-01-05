def shorten(li):
    newli = []
    for word in li:
        l = len(word)
        if l > 10:
            word = word[0] + str((l-2)) + word[l-1]
            newli.append(word)
        else:
            newli.append(word)
    return newli     

def main():
    n = int(input())
    li = []
    for i in range(n):
        li.append(input())

    slist = shorten(li)
    for w in slist:
        print(w)   

if __name__ == '__main__':
    main()