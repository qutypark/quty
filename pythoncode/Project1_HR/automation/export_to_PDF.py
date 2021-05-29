# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:30:40 2021
@author: PJH
"""
"""
export excel form to pdf 
"""

# integrate module below with Excel VBA button for user
def exceltopdf_ALL():
    #-------------------------0.install library----------------------------------
    import numpy as np
    import pandas as pd
    import sys
    import os

    import xlwings as xw

    import matplotlib.patches as mpatches
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    
    #　for kanji, hiragana, katakana display
    fp=FontProperties(fname=r"\ipaexg.ttf",size=16)
    fp1=FontProperties(fname=r"\ipaexg.ttf",size=12)
    fp2=FontProperties(fname=r"\ipaexg.ttf",size=10)

    
    plt.style.use("ggplot")

    #---------------------------------1. data assign------------------------------
    
    #---------------------------------1.1 excel sheet assign----------------------------
    # From user insert form sheet below
    sheet0=xw.sheets[0]
    sheet1=xw.sheets[1]
    sheet2=xw.sheets[2]
    #--------------------------------1.2 Feature assign  ----------------------
    
    #1) feature Dataframe
    dfG = sheet0.range(#excel range).options(pd.DataFrame, header=1,index=False, expand='table').value

    #2) Feauture and baseline

    gab = list(dfG.iloc[:,0].values)
    gabv = []
    for i in range (dfG.shape[0]):
        if dfG.iloc[i,1]=="P":
            v = round(dfG.iloc[i,2],1)
        elif dfG.iloc[i,1]=="N":
            v = round(abs(10-dfG.iloc[i,2]),1)
        gabv.append(v)

    gabn = []
    for i in range (dfG.shape[0]):
        if dfG.iloc[i,1]=="N":
           gabn.append(dfG.iloc[i,0])
        
    #3) baseline Dataframe
    schp= pd.DataFrame({"val":gabv},index=gab)

    df = sheet1.range(#excel range).options(pd.DataFrame, 
                             header=1,
                             index=False, 
                             expand='table').value

    df1=df.sort_values(by=['matching'],ascending=False)
    df1.index=(range(df1.shape[0]))
    
    
    #---------------------------------2. display information(Analysis result) to Excel sheet------------------------------
    
    # if error message -> delete 
    sheet2.range(#excel range).clear()
    
    for a2 in list(df1.iloc[:,0]): 
        sheet2.range(#excel range).value = a2
        esa2=df1[df1["ID"]==a2]
        esa2m=esa2[gab].median()
        for x in gabn:
                    esa2m[x]=abs(esa2m[x]-10)
    
    
        # display name
    
        sheet2.range(#excel range).value=esa2["name"].values[0]
        sheet2.range(#excel range).api.Font.Size = 14
        sheet2.range(#excel range).color= (233,231,249)
        sheet2.range(#excel range).api.Font.Bold = True
    
     
        # display radarchart
        labels=np.array(gab)
        angle=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        angles=np.concatenate((angle,[angle[0]]))
    
        schp1=np.concatenate((schp.values,[schp.values[0]]))
    
        esa2m1=np.concatenate((esa2m.values,[esa2m.values[0]]))
    
        # create backgroud radar chart:baseline
        fig=plt.figure()
        ax= fig.add_subplot(111, polar=True)
        fig.set_size_inches(6,6)
        ax.set_title("radarchart",fontproperties=fp)
    
        # baseline radar chart 
        ax.plot(angles, schp1, 'o-', linewidth=1,label="baseline",color="b")
        ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties=fp)
    
        # applicant radar chart 
        ax.plot(angles, esa2m1, 'o-', linewidth=1,label="applicant",color="green")
        ax.fill(angles, esa2m1,"green",alpha=0.25)
        ax.set_thetagrids(angles * 180/np.pi, labels,fontproperties=fp2)
        ax.grid(True)
        plt.legend(loc="upper right",prop=fp2,bbox_to_anchor=(0.1,0.1))
        plt.ylim(0.0,10.0)
    
    
        sheet2.pictures.add(fig, name='radarchart', update=True,left=sheet2.range(#excel range).left, top=sheet2.range(#excel range).top)
    
        # display bar graph for label
    
        HPhist=df1[["ID","Label"]].groupby(["Label"],as_index=False).agg(lambda x:len(x.value_counts())).sort_values(by="ID",ascending=False)
        HPhist["ID"]=HPhist["ID"].astype(int)
    
        s=HPhist["ID"].sum()
        percent=HPhist["ID"].map(lambda x:"{:.1%}".format(x/s))
        adj=[]
        for x,y in zip(HPhist["ID"],percent):
            a="%s_%s"%(x,y)
            adj.append(a)
        HPhist["countP"]=adj
    
        #Draw plot
        fig=plt.figure(figsize=(5,2), dpi=80)
        plt.hlines(y=HPhist.Label, xmin=0, xmax=HPhist["ID"])
        for x, y, tex in zip(HPhist["ID"], HPhist["Label"],HPhist["countP"]):
            t = plt.text(x, y, tex, horizontalalignment='right' if x < 0 else 'left', 
                         verticalalignment='baseline', fontdict={"color":'#6259D8', 'size':12})
    
        # Decorations    
        plt.title('graph_for_label',fontproperties=fp1)
        plt.yticks(HPhist.Label,HPhist.Label, fontsize=12)
        plt.grid(linestyle='--', alpha=0.3)
        plt.xlim(-10,max(HPhist["ID"])+60)
        plt.ylim(-0.25,3.5)
    
        sheet2.pictures.add(fig, name='Bargraph', update=True,left=sheet2.range(#excel range).left, top=sheet2.range(#excel range).top)
    
        # display matching percentage and bar graph
    
        start = 0
        val=esa2["matching"].values.round(2)[0]
        default=100-esa2["matching"].values.round(2)[0]
        labels=["matching"]
    
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
    
        leg1 = mpatches.Patch(color='#6259D8', label='matching')
        leg2 = mpatches.Patch(color="silver", label='100%')
    
    
        sheet2.pictures.add(fig, name="matching",update=True,left=sheet2.range(#excel_range).left, top=sheet2.range(#excel_range).top)
    
        sheet2.range(#excel_range).value = "%1f%%"%val
        sheet2.range(#excel_range).api.Font.Size = 16
        sheet2.range(#excel_range).api.Font.Bold = True
    
        # display ranking and Label
    
        rank=df1[df1["ID"]==a2].index.values[0]
    
        sheet2.range(#excel_range).value="%r among、%r ranked" %(df.shape[0],rank+1)
        sheet2.range(#excel_range).api.Font.Size = 14
        sheet2.range(#excel_range).api.Font.Bold = True
    
    
        sheet2.range(#excel_range).value=esa2["Label"].values[0]
        sheet2.range(#excel_range).api.Font.Size = 14
        sheet2.range(#excel_range).color= (233,231,249)
        sheet2.range(#excel_range).api.Font.Bold = True
    
        
        pdf_dir =  sheet0.range(#excel_range).value
        filename = '%s_%s.pdf' % (int(a2),esa2["name"].values[0])
        pdf_path = os.path.join(pdf_dir, filename)
        
        # ---------------------3. export excel to pdf file-------------------------------
        # if error -> display error message on excel sheet
        try:
            sheet2.api.ExportAsFixedFormat(0, pdf_path)
        except: 
            sheet2.range(#excel_range).value="cannot export file to PDF."
            sheet2.range(#excel_range).api.Font.ColorIndex = 3
            sys.exit()
    # if success -> display success message on excel sheet
    sheet2.range(#excel_range).value="successfully completed"
    sys.exit()
      
      
