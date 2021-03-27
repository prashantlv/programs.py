def decideJump(arr,n,currentPos=0):
    if arr[currentPos] == 0:
        return -1
    else:    
        maxSteps = arr[currentPos]
        minJump=1
        while maxSteps > 0:
            minJump = min(minJump, 1+decideJump(arr,n,currentPos+maxSteps))
            currentPos += minJump
            maxSteps -= 1
        return minJump     

if __name__ =="__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = decideJump(arr,n)
    print(result)
