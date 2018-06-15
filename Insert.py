def Insertion():
    seq=[74,32,89,55,22,64]
    s=Sort(seq,0)
    print s


def Sort(seq,k):
    if(len(seq)==k):
        return seq
    else:
        while(k<len(seq)):
            
            pos=k
            while(pos>0 and seq[pos]<seq[pos-1]):
                (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
                pos=pos-1
            return Sort(seq,k+1)
        
