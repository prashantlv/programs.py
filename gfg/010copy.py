def main():
    arr = [1,4,3,2,6,7]
    jumps = 0
    end = 0
    farthest = 0
    for i in range(len(arr)-1):
        farthest = max(farthest,i+arr[i])
        if(i==end):
            jumps+= 1
            end = farthest
    return jumps
if __name__=="__main__":
    print(main())    
