def matching():
    # Calculate matching percentage and export it to Excel sheet
    import numpy as np
    import pandas as pd
    import os

    import xlwings as xw
    from sklearn import preprocessing


    # read data
    essc=pd.read_csv("C:/Users/local",encoding="cp932")


    # ――――――――――――――――matching percentage――――――――――――――――
    # Variance V53
    V530=pd.DataFrame((essc['V53']-XX).value_counts().sort_index()) # XX = Threshold
    V53P=[]
    V53N=[]
    for i in V530.index.values:
        if i >= 0.0:
            V53P.append(round(i,2))
        else:
            V53N.append(round(i,2))
    V53N.sort(reverse=True)

    # Variance V51
    V510=pd.DataFrame((essc['V51']-XX).value_counts().sort_index()) # XX = Threshold
    V51P=[]
    V51N=[]
    for i in V510.index.values:
        if i >= 0.0:
            V51P.append(round(i,2))
        else:
            V51N.append(round(i,2)) 
    V51N.sort(reverse=True)

    # Variance V56
    V560=pd.DataFrame((essc["V56"]-XX).value_counts().sort_index()) # XX = Threshold
    V56P=[]
    V56N=[]
    for i in V560.index.values:
        if i >= 0.0:
            V56P.append(round(i,2))
        else:
            V56N.append(round(i,2))  
    V56N.sort(reverse=True)


    # Variance V54
    V540=pd.DataFrame((essc["V54"]-XX).value_counts().sort_index())# XX = Threshold
    V54P=[]
    V54N=[]
    for i in V540.index.values:
        if i >= 0.0:
            V54P.append(round(i,2))
        else:
            V54N.append(round(i,2))  
    V54N.sort(reverse=True)

    # Variance V52
    V520=pd.DataFrame((essc["V52"]-XX).value_counts().sort_index())# XX = Threshold
    V52P=[]
    V52N=[]
    for i in V520.index.values:
        if i >= 0.0:
            V52P.append(round(i,2))
        else:
            V52N.append(round(i,2))  
    V52N.sort(reverse=True)

    #V53
    V53R=[]
    for j in (essc['V53']-XX).values:    
        for i in range(len(V53P)): 
            if j.round(2) == V53P[i]:
                a=(100/len(V53P))*(i+1)
        for k in range(1,len(V53N)):
            if j.round(2) == V53N[k]:
                a=-(100/len(V53N))*(k+1)
        V53R.append(a)   
        
    #V51
    V51R=[]
    for j in (essc["V51"]-XX).values:    
        for i in range(len(V51P)): 
            if j.round(2) == V51P[i]:
                a=(100/len(V51P))*(i+1)
        for k in range(1,len(V51N)):
            if j.round(2) == V51N[k]:
                a=-(100/len(V51N))*(k+1)
        V51R.append(a)   
    #V56
    V56R=[]
    for j in (essc['V56']-XX).values:    
        for i in range(len(V56P)):  
            if j.round(2) == V56P[i]:
                a=(100/len(V56P))*(i+1)
        for k in range(len(V56N)):
            if j.round(2) == V56N[k]:
                a=-(100/len(V56N))*(k+1)
        V56R.append(a)
        
    #V54
    V54R=[]
    for j in (essc['V54']-XX).values:    
        for i in range(len(V54P)):  
            if j.round(2) == V54P[i]:
                a=(100/len(V54P))*(i+1)
        for k in range(len(V54N)):
            if  j.round(2) == V54N[k]:
                a=-(100/len(V54N))*(k+1)
        V54R.append(a)
        
    #V52
    V52R=[]
    for j in (essc['V52']-XX).values:    
        for i in range(len(V52P)):  
            if j.round(2) == V52P[i]:
                a=(100/len(V52P))*(i+1)
        for k in range(len(V52N)):
            if j.round(2) == V52N[k]:
                a=-(100/len(V52N))*(k+1)
        V52R.append(a)
        
    justsum=[]

    #Calculate Weight  
    for i in range(essc.shape[0]):
        m=20*(V53R[i]/100)  #20 -> 100/the number of variance(= 5) 
        o=20*(V51R[i]/100)
        p=20*(V56R[i]/100)
        n=20*(V54R[i]/100)
        c=20*(V52R[i]/100)
        a=m+o+p+n+c
        justsum.append(a)

    #Normalize: because percentage should be between 0~1(100%)
    norsum=[]
    for i in range(len(justsum)):
        b=(justsum[i]-min(justsum))/(max(justsum)-min(justsum))
        norsum.append(b*100)
        
    # # # ――――――――――――――――make new dataframe――――――――――――――――
    # "result"
    c6=["ID",'V53','V51','V56','V54','V52']
    esscNew=essc[c6]
    extra=pd.DataFrame({"V53":V53R,"V51":V51R,"V56":V56R,
                        "V54":V54R,"V52":V52R,"sum":justsum,"matching":norsum})

    # label：　based on matching percentage、make label
    # ex) label= A, B, C, D -> A= 75~100 , B= 50~75 , C=25~50 , D=0~25
    label=extra['matching'].map(lambda x: "A" if 75<= x <=100 else "B" if 50<= x < 75 
                                       else "C" if 25<= x < 50 else "D") 
    extra["Label"]=label

    # sort "result"
    result=pd.concat([esscNew,extra],axis=1,sort=False)
    
    # # # ――――――――――――export dataframe to excel sheet――――――――――――――――
    sheet0=xw.sheets[0]
    sheet0.range("A7").options(index=False).value=result

    
