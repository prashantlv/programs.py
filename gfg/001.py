
def reverseWord(s):
    #your code here
    a = ""
    for i in range(1,len(s)+1):
        a += s[-i]
    return a
#-------------------------------------    
#	It might work in case of array(swapping apraoch)
	#l = len(s)
    #a = s[0]
    #e = s[l-1]
	# while e>a:
    #     s[a], s[e] = s[e],s[a]
    #     a += 1
    #     e -+ 1
    # return s
#-------------------------------------	
    return s[::-1]
#------------------------------------

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1
