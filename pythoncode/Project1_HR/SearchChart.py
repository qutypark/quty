﻿def matching():
# Calculate matching percentage and display it to Excel sheet
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


def SearchChart():
# ID Search -> Calculated percentage and Chart will be displayed to Excel Sheet

    import numpy as np
    import pandas as pd
    import os
    import sys

    import xlwings as xw

    import matplotlib
    import matplotlib.patches as mpatches
    import matplotlib.pyplot as plt
    import japanize_matplotlib
    #for Hiragana, Gatakana, Kanji of japanese

    from scipy import stats


    import seaborn as sns
    plt.style.use("ggplot")


    #specify sheet
    sheet0=xw.sheets[0]
    sheet1=xw.sheets[1]

    #prepare Threshold
    sc5 = ["V53","V51","V56","V54","V52"]
    sc5v= [XX,XX,XX,XX,XX]
    schp= pd.DataFrame({"val":sc5v},index=sc5)

    #read data from sheet0
    df = sheet0.range("A7").options(pd.DataFrame, 
                             header=1,
                             index=False, 
                             expand='table').value

    df1=df.sort_values(by=['matching'],ascending=False)
    df1.index=(range(df1.shape[0]))

    #Result searched by ID
    a2=sheet1.range('A2').value
    
    if a2 in df1["ID"].values:
            esa2=df1[df1["ID"]==a2]
            sheet1.range('A3').clear()

    else: 
            sheet1.range("A3").value="ID doesn't exist.Please Check ID once again"
            sheet1.range("A3").api.Font.ColorIndex = 3
            sheet1.range('A5').clear()
            sheet1.range('A6').clear()
            sheet1.range('J6').clear()
            sheet1.range('C6').clear()
    
            sys.exit()

    
    esa2m=esa2[sc5].median()


    #radar chart
    sc6=["V53(+)","V51(-)","V56(+)","V54(-)","V52(+)"]
    labels=np.array(sc6)
    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    angles=np.concatenate((angles,[angles[0]]))

    schp1=np.concatenate((schp.values,[schp.values[0]]))

    esa2m1=np.concatenate((esa2m.values,[esa2m.values[0]]))

    # create backgroud radar chart:HP
    fig=plt.figure()
    ax= fig.add_subplot(111, polar=True)
    fig.set_size_inches(6,6)
    ax.set_title("radarchart")

    # Threshold radar chart 
    ax.plot(angles, schp1, 'o-', linewidth=1,label="Threshold",color="b")
    ax.set_thetagrids(angles * 180/np.pi, labels)

    # Candidate radar chart Searched By ID
    ax.plot(angles, esa2m1, 'o-', linewidth=1,label="Candidate",color="green")
    ax.fill(angles, esa2m1,"green",alpha=0.25)
    ax.set_thetagrids(angles * 180/np.pi, labels)
    ax.grid(True)
    plt.legend(loc="upper right",bbox_to_anchor=(0.1,0.1))


    sheet1.pictures.add(fig, name='radorchart', update=True,left=sheet1.range('A23').left, top=sheet1.range('A23').top)

# ――――――――――――――――Lable bar graph――――――――――――――――

    HPhist=df1[["ID","Label"]].groupby(["Label"],as_index=False).agg(lambda x:len(x.value_counts())).sort_values(by="ID",ascending=False)

    #Draw plot
    fig=plt.figure(figsize=(5,2), dpi=80)
    plt.hlines(y=HPhist.Label, xmin=0, xmax=HPhist["ID"])
    for x, y, tex in zip(HPhist["ID"], HPhist["Label"],HPhist["ID"]):
        t = plt.text(x, y, round(tex, 1), horizontalalignment='right' if x < 0 else 'left', 
                     verticalalignment='baseline', fontdict={"color":'#6259D8', 'size':12})

    # Decorations    
    plt.title('ABCDgraph', fontdict={'size':12})
    plt.yticks(HPhist.Label,HPhist.Label, fontsize=12)
    plt.grid(linestyle='--', alpha=0.3)
    plt.xlim(-10,max(HPhist["ID"])+20)
    plt.ylim(-0.25,3.5)

    sheet1.pictures.add(fig, name='Bargraph', update=True,left=sheet1.range('F11').left, top=sheet1.range('F11').top)

# ――――――――――――――――percentage and percentage bar graph――――――――――――――――

#Percentage bar with data searched By ID

    start = 0
    val=esa2["matching"].values.round(2)[0]
    default=100-esa2["matching"].values.round(2)[0]
    labels=["percentage"]

    fig, ax = plt.subplots()

    ax.broken_barh([(start, val), (val, val+default)], [0, 1], facecolors=('#6259D8', "silver"))
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 100)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_yticks([0, 1])
    ax.set_xticks([0,25, 50, 75, 100])

    ax.set_axisbelow(True) 

    ax.grid(axis='x')
    fig.set_size_inches(4,0.2)

    leg1 = mpatches.Patch(color='#6259D8', label='percentage')
    leg2 = mpatches.Patch(color="silver", label='100%')


    sheet1.pictures.add(fig, name="percentage",update=True,left=sheet1.range('F6').left, top=sheet1.range('F6').top)

    sheet1.range("J6").value = "%1f%%"%val
    sheet1.range("J6").api.Font.Size = 16
    sheet1.range("J6").api.Font.Bold = True

# ――――――――――――――――ranking and Label with data searched By ID――――――――――――――――
    per=100-stats.percentileofscore(df1['matching'], val, kind='rank')

    rank=df1[df1["ID"]==a2].index.values[0]

    sheet1.range("A5").value="among %r、ranked %r" %(df.shape[0],rank+1)
    sheet1.range("A5").api.Font.Size = 14
    sheet1.range("A5").api.Font.Bold = True

    sheet1.range("A6").value="upper　%1f%%"%per
    sheet1.range("A6").api.Font.Size = 14
    sheet1.range("A6").api.Font.Bold = True

    sheet1.range("C6").value=esa2["Label"].values[0]
    sheet1.range("C6").api.Font.Size = 14
    sheet1.range("C6").color= (233,231,249)
    sheet1.range("C6").api.Font.Bold = True
    # sheet1.range("C6").api.HorizontalAlignment = xlHAlignCenter
    # sheet1.range("C6").api.VerticalAlignment = xlHAlignCenter



