from tkinter import *
from tkinter import ttk
import tkinter
import numpy as np

def eviter0(mat):#second membre non 0
     n_contraint=np.shape(mat-1)[0]#nbr ligne pour parcourir ligne
     n_collone=mat.shape[1]#nbr col pour parcourir colone
     for i in range(n_contraint-1):#-1 pour eviter parcours de z derniere ligne
            if mat[i][n_collone-1]!=0:#get indice ligne qui est diff de 0
                k=i
                break
     for j in range(n_contraint-1):
        if  mat[j][n_collone-1]==0:# precis derniere col et quelque soit ligne on cherche qui second membre =0
            mat[j] = mat[j]+mat[k]
     return mat
from fractions import Fraction as frac
def Oorder_ligne(nbrX,Order,egale):#creer list de premiere ligne x1...e1...a1... pour ligne
    list_ligne=["x"+str(i) for i in range(1,nbrX+1)]
     
    for  i in range(Order.shape[0]):
        if   Order[i]==0 or (egale[i]==0 and Order[i]==1): #<,> test genere e1....
            list_ligne.append("e"+str(i+1))
    for  i in range(Order.shape[0]):
        if Order[i]==1: #pour = ,> genere a......
            list_ligne.append("a"+str(i+1))
 
    return list_ligne
def Oorder_colone(Order,egale):#list e.. pour col sortant
    list_col=[]
    for  i in range(Order.shape[0]):
        if Order[i]==0:
         list_col.append("e"+str(i+1))  #if < alor e append dans liste
        elif Order[i]==1:
            list_col.append("a"+str(i+1)) # if >, = alors append a
    return list_col
def identite(Order,egale):#genere identité 
    z=0
    f=np.eye(np.shape(Order)[0])# pour e...
    for i in range(np.shape(Order)[0]):#
      z=z+Order[i]#savoir nbr de a
      if Order[i]==1: # if > alors modifie diag de 1 a -1
         f[i][i]=-1
      h=0 #pour  prb  indice
    for  i in range(np.shape(egale)[0]):
      if egale[i]==1: #if = alors supp e associé
         f=np.delete(f,h,1)
      else:
          h=h+1
    y=np.zeros((np.shape(Order)[0],z))#pour a.... generer des 0
    global j
    j=0
    zmin=[]
    for i in range((np.shape(Order)[0])):
        if Order[i]==1:#if = ou > alors creer 1 dans a 
           y[i][j]=Order[i]
           j=j+1
   
    return np.hstack((f,y))
def  obtenir_solution_de_base(A,B,order,egale):#stack de a,b,identit
   B=np.transpose(B)
   identit=identite(order,egale)
   tableu=np.hstack((A, identit))
   tableu=np.hstack((tableu,B))
   zero_ajou=np.zeros(np.shape(tableu)[1]-j-1)#ajout de 1 dans z associcé des a
   add=np.array([1 for i in range(j+1)])
   zero_ajou=np.concatenate((zero_ajou,add))
   tableu=np.vstack((tableu,zero_ajou))
   tableu[np.shape(tableu)[0]-1][np.shape(tableu)[1]-1]=0
   return tableu
def rasio_index(n_contraint,colone_pivo,B):
    rati=99999999999999999#suppose qu on a pas de pivot
    j=-1
    for i in range(n_contraint):
       if colone_pivo[i]>0:#pour obtenir indice de ligne pivot 
          x=B[i]/colone_pivo[i]
          if x<rati:
              rati=x
              j=i#aboir l'indice
    return j
def corrigero(mat,Order,LabelFrame,col,row):
    n_contraint=np.shape(mat-1)[0]-1
    n_collone=mat.shape[1]

    frame5=ttk.Frame(LabelFrame)
    for j in range(n_collone-1):
        Button(frame5,text=row[j],width=15).grid(row=0,column=j+1)
    Button(frame5,text="b",width=15).grid(row=0,column=n_collone)
    for i in range(n_contraint+1):
          Button(frame5,text=col[i],width=15).grid(row=i+1,column=0)
          for j in range(n_collone):
           Button(frame5,text=frac(mat[i][j]).limit_denominator(10),width=15).grid(row=i+1,column=j+1)
      
    frame5.pack()
    ttk.Label(LabelFrame,text="-------------------------------------------------------------------").pack()
    index_ligne=[]
    for  i in range(Order.shape[0]):
       if Order[i]==1:
          index_ligne.append(i)
    for i in   index_ligne:
       mat[n_contraint]=mat[n_contraint]-mat[i]

    frame5=ttk.Frame(LabelFrame)
    for j in range(n_collone-1):
        Button(frame5,text=row[j],width=15).grid(row=0,column=j+1)
    Button(frame5,text="b",width=15).grid(row=0,column=n_collone)
    for i in range(n_contraint+1):
          Button(frame5,text=col[i],width=15).grid(row=i+1,column=0)
          for j in range(n_collone):
            Button(frame5,text=frac(mat[i][j]).limit_denominator(10),width=15).grid(row=i+1,column=j+1)
      
    frame5.pack()
    ttk.Label(LabelFrame,text="-------------------------------------------------------------------").pack()
    return mat
def calculerr(mat,ligne,col,LabelFrame):
     n_contraint=np.shape(mat-1)[0]
     n_collone=mat.shape[1]
     n_contraint= n_contraint-1
     mat[n_contraint][n_collone-1]=0
     while np.min(mat[n_contraint]) <-0.00000000001  :
      index_colone_pivo=np.argmin(mat[n_contraint])
      colone_pivo=[row[index_colone_pivo] for row in mat]
      BB=[row[n_collone-1] for row in mat]
      index_ligne_pivo=rasio_index(n_contraint,colone_pivo,BB)
      if index_ligne_pivo==-1:
         frame5=ttk.Frame(LabelFrame)
         Label(frame5,text="problem nom bornee",width=15,).pack()
         frame5.pack()
         return [-1,-1]
      mat[index_ligne_pivo]= mat[index_ligne_pivo]/mat[index_ligne_pivo][index_colone_pivo]
      for i in range(n_contraint+1):
        if i !=index_ligne_pivo:
              mat[i]=mat[i]-mat[i][index_colone_pivo]*mat[index_ligne_pivo]
      col[index_ligne_pivo]=ligne[index_colone_pivo]
      
      frame5=ttk.Frame(LabelFrame)
      for j in range(n_collone-1):
        Button(frame5,text=ligne[j],width=15,).grid(row=0,column=j+1)
      Button(frame5,text="b",width=15).grid(row=0,column=n_collone)
      x=None
      for i in range(n_contraint+1):
           Button(frame5,text=col[i],width=15).grid(row=i+1,column=0)
           for j in range(n_collone):
               if i==index_ligne_pivo or j==index_ligne_pivo :
                 x="#fcff33"
               else:
                x=None
               Button(frame5,text=frac(mat[i][j]).limit_denominator(10),width=15).grid(row=i+1,column=j+1)
      
      frame5.pack()
      ttk.Label(LabelFrame,text="-------------------------------------------------------------------").pack()
    
     return [mat,col]
def corriger2(mat,z,nbr_variable,col,ligne,LabelFrame):
   col_final=np.shape(mat)[0]-1
   n_collone=mat.shape[1]

   mat=np.delete(mat,col_final,0)
   n_contraint=np.shape(mat)[1]
   zero_ajou=np.zeros(n_contraint-nbr_variable)
   z=np.concatenate((z,zero_ajou))
   mat=np.vstack((mat,z))
   for i in range(len(col)):
    if  col[i][:1]=='x':
        j=int(col[i][1:])-1
        elemnt_final=mat[col_final][j]
        mat[col_final]=mat[col_final]-elemnt_final*mat[i]
   h=0
   for i in range(len(ligne)):
      if ligne[i][:1]=='a':
        mat=np.delete(mat,h,1)
      else:
          h=h+1
   frame5=ttk.Frame(LabelFrame)
   col_final=np.shape(mat)[0]
   n_collone=mat.shape[1]
   for j in range(n_collone-1):
        Button(frame5,text=ligne[j],width=15).grid(row=0,column=j+1)
   Button(frame5,text="b",width=15).grid(row=0,column=n_collone)

   for i in range(col_final):
      Button(frame5,text=col[i],width=15).grid(row=i+1,column=0)
      for j in range(n_collone):
             Button(frame5,text=frac(mat[i][j]).limit_denominator(10),width=15).grid(row=i+1,column=j+1)
      
   frame5.pack()
   ttk.Label(LabelFrame,text="-------------------------------------------------------------------").pack()
   return mat
def calculer_final(mat,ligne,col,LabelFrame):
     n_contraint=np.shape(mat-1)[0]
     n_collone=mat.shape[1]
     x=mat[n_contraint-1][n_collone-1]
     n_contraint= n_contraint-1
     if  mat[n_contraint][n_collone-1]>0:
        mat[n_contraint][n_collone-1]=- mat[n_contraint][n_collone-1]
     while np.max(mat[n_contraint]) >0.0000000 :
      index_colone_pivo=np.argmax(mat[n_contraint])
      colone_pivo=[row[index_colone_pivo] for row in mat]
      BB=[row[n_collone-1] for row in mat]
      index_ligne_pivo=rasio_index(n_contraint,colone_pivo,BB)
      if index_ligne_pivo==-1:
         frame5=ttk.Frame(LabelFrame)
         Label(frame5,text="problem nom bornee",width=15,).pack()
         frame5.pack()
         return [-1,-1]
      mat[index_ligne_pivo]= mat[index_ligne_pivo]/mat[index_ligne_pivo][index_colone_pivo]
      for i in range(n_contraint+1):
        if i !=index_ligne_pivo:
              mat[i]=mat[i]-mat[i][index_colone_pivo]*mat[index_ligne_pivo]
      col[index_ligne_pivo]=ligne[index_colone_pivo]
     # mat[n_contraint-1][n_collone-1]=x
      frame5=ttk.Frame(LabelFrame)
      for j in range(n_collone-1):
        Button(frame5,text=ligne[j],width=15).grid(row=0,column=j+1)
      Button(frame5,text="b",width=15).grid(row=0,column=n_collone)
      for i in range(n_contraint+1):
          Button(frame5,text=col[i],width=15).grid(row=i+1,column=0)
          for j in range(n_collone):
             Button(frame5,text=frac(mat[i][j]).limit_denominator(10),width=15).grid(row=i+1,column=j+1)
      
      frame5.pack()
      ttk.Label(LabelFrame,text="-------------------------------------------------------------------").pack()
    
     return [mat,col]
A = np.array([[1,2],[1,4],[6,3]])
Order=np.array([1,1,1])
egale=np.array([0,0,0])
B= np.array([[90,120,180]])
z= np.array([-1000,-1000])
nbr_of_variable=2
ligne=Oorder_ligne(2,Order,egale)
col=Oorder_colone(Order,egale)
col.append('Z')
matrice=obtenir_solution_de_base(A,B,Order,egale)
matrice=eviter0(matrice)






def inizializza_widgetss(matrice,z,nbr_of_variable,col,ligne,Order):
        root=Tk()
        root.maxsize(900,700)
        root.minsize(900,700)
     
        frame = ttk.Frame(root, width=300, height=250)

        hscrollbar = ttk.Scrollbar(frame, orient = tkinter.HORIZONTAL)
        vscrollbar = ttk.Scrollbar(frame, orient = tkinter.VERTICAL)
        sizegrip = ttk.Sizegrip(frame)
        canvas = tkinter.Canvas(frame, bd=0, highlightthickness=0, yscrollcommand = vscrollbar.set, xscrollcommand = hscrollbar.set)
        vscrollbar.config(command =canvas.yview)
        hscrollbar.config(command =canvas.xview)


        # Add controls here
        subframe = ttk.Frame(canvas)  


        ######
        LabelFrame = ttk.Frame(subframe)
        lblins = tkinter.Label(LabelFrame, text="calcule simplex", font=("Helvetica", 12))
        lblins.pack()
        


         
        #fraame
        corrigero(matrice,Order,LabelFrame,col,ligne)
        mat=calculerr(matrice,ligne,col,LabelFrame)
        x=True
        if  type(mat[0])!=int:
           for i in range(len(mat[1])):
             if mat[1][i][:1] =='a':
              x=False
              frame5=ttk.Frame(LabelFrame)
              Label(frame5,text="problem impossible",width=15,).pack()
              frame5.pack()

           if x==True:
               c=corriger2(mat[0],z,nbr_of_variable,mat[1],ligne,LabelFrame)
               mo=calculer_final(c,ligne,col,LabelFrame)
            
               s='la solution est ' 
               z_final=0 
               print(mo)
               n_collone=mo[0].shape[1]
               print(n_collone)
               for  i in range(len(mo[1])-1):
                    if  mo[1][i][:1]=='x':
                       ind=int(mo[1][i][1:])-1
                       z_final=z_final+z[ind]*mo[0][i][n_collone-1]
                       s=s+mo[1][i]+'= '+str(frac(mo[0][i][n_collone-1]).limit_denominator(10))
                  
               s=s+'les autre x sont nulls, la fontion objectif est :'+str(frac(-z_final).limit_denominator(10))        
               print(s)        
               
              #  frame7=ttk.Frame(LabelFrame)
              #  Label(frame7,text=s,).pack()
              #  frame7.pack()
                    
                    
          
        
        ContentFrame = ttk.Frame(subframe, width = 600, height = 600)

        ButtonsFrame = ttk.Frame(subframe)
        ttk.Frame(ButtonsFrame).pack(side=LEFT, fill = X, expand=TRUE)
        
        LabelFrame.pack(side = TOP, fill = X, expand=TRUE)
        ContentFrame.pack(fill = BOTH, expand = TRUE)
        ButtonsFrame.pack(side = BOTTOM, fill = X, expand = TRUE)
      


        #### Titles
        subframe.pack(fill = tkinter.BOTH, expand = tkinter.TRUE)
        hscrollbar.pack( fill=tkinter.X, side=tkinter.BOTTOM, expand=tkinter.FALSE)
        vscrollbar.pack( fill=tkinter.Y, side=tkinter.RIGHT, expand=tkinter.FALSE)
        sizegrip.pack(in_= hscrollbar, side = BOTTOM, anchor = "se")
        canvas.pack(side = tkinter.LEFT, padx  = 5, pady  = 5, fill = tkinter.BOTH, expand= tkinter.TRUE)
        frame.pack( padx   = 5, pady  = 5, expand = True, fill = tkinter.BOTH)


        canvas.create_window(0,0, window = subframe)
        root.update_idletasks() # update geometry
        canvas.config(scrollregion = canvas.bbox("all"))
        canvas.xview_moveto(0) 
        canvas.yview_moveto(0)
        root.mainloop()


        #Packing everything

