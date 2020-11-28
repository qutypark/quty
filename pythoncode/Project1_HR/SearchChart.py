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



