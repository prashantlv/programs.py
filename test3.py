def getMaxStreaks(toss):
    heads,tails,i = 0,0,0
    # Return an array of two integers containing the maximum streak of heads and tails respectively
    ls = list(toss)
    ln = len(ls)
    while(i<ln):
        if ls[i] == 'Heads':
            if ls[i+1] == 'Heads':
                heads = heads+1
        elif ls[i] == 'Tails':
            if ls[i+1] == 'Tails':
                tails = tails+1
        else:
            pass
        i = i+1
    return [heads,tails]   

toss = ['Heads','Tails','Heads','Tails','Tails']
print(getMaxStreaks(toss))