def selection_Sort():
    n=raw_input("\nEnter the numbersize")
    l=[]
    for i in range(int(n)):
        x=raw_input("Enter %d element" %i)
        l.append(x)

    for i in range(len(l)):
        mini=l[i]
        for j in range(i,len(l)):
            

            if(l[j]<mini):
                mini=l[j]
        z=l.index(mini)
        l[i],l[z]=mini,l[i]


    for j in l:
        print(j),
                       
                       
                   

