def main():
    str = input()
    lst = []
    for letter in str:
        lst.append(letter)
        lst = set(lst)
        lst = list(lst)
    if len(lst) % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
 
if __name__ == '__main__':
    main()