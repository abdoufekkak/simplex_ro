from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from Function_objectif import *
from Tableu import *
from stack import *

A=[]
B=[]
Z=[]
Ord=[]
def eviter0(mat):
     n_contraint=np.shape(mat-1)[0]
     n_collone=mat.shape[1]
     for i in range(n_contraint-1):
            if mat[i][n_collone-1]!=0:
                k=i
                break
     for j in range(n_contraint-1):
        if  mat[j][n_collone-1]==0:
            mat[j] = mat[j]+mat[k]
     return mat
def addapter(A,B,order,egale):
    for i in range(np.shape(A)[0]):
          if  B[0][i]<0:
            A[i]=-A[i]
            B[0][i]=-B[0][i]
            if order[i]==1 and egale[i]==0:
                order[i]=0
            elif  order[i]==0 and egale[i]==0:
                 order[i]=1
    return [A,B,order,egale] 
    

def A_B_Z(A,B,z,bool_method,nbr_of_variable,cmb):
             B_=np.zeros((1,np.shape(A)[0]+1),dtype=float)
             A_=np.zeros((np.shape(A)[0],np.shape(A)[1]),dtype=float)
             Z_=[float(i.get()) for i in z ]
             for i in range(np.shape(A)[0]):
                B_[0][i]=float(B[i].get())
       
             for i in range(np.shape(A)[0]):
               for j in range(np.shape(A)[1]):
               
                 A_[i][j]=A[i][j].get()
       



             Order=[]
             egale=[]
             for i in Ord:
                if i.get()=="=":
                    egale.append(1)
                else :
                    egale.append(0)
                if i.get()=="<=":
                    Order.append(0)
                else :
                    Order.append(1)
             Order=np.array(Order)
             egale=np.array(egale)
           
             B_=np.zeros((1,np.shape(A)[0]),dtype=float)
             for i in range(np.shape(A)[0]):
                 B_[0][i]=float(B[i].get())
             B_= np.array(B_)
             ligne=Oorder_ligne(nbr_of_variable,Order,egale)
             col=Oorder_colone(Order,egale)
             col.append('Z')
             A_,B_,Order,egale=addapter(A_,B_,Order,egale)
             matrice=obtenir_solution_de_base(A_,B_,Order,egale) 
             matrice= eviter0(matrice)
    
             ligne=Oorder_ligne(nbr_of_variable,Order,egale)
             col=Oorder_colone(Order,egale)
             col.append('Z')
             if cmb.get()=='min':
                    Z_=np.array(Z_)
                    Z_=-Z_
                    Z_=list(Z_)
             inizializza_widgetss(matrice,Z_,nbr_of_variable,col,ligne,Order)

def creer_simlex_apartir_function_nbcontrant_nb_variable():

# this will create a label widget
 global frame
 frame=Frame(root)
 l1 = Label(frame, text = "number of contraints:",font=('Times',15,'bold'))
 l2 = Label(frame, text = "number of variables:",font=('Times',15,'bold'))
 l3 = Label(frame, text = "                                                 ",)
 l4 = Label(frame, text = "                                                 ",)
 l5 = Label(frame, text = "function objectif:",font=('Times',15,'bold'))

 # grid method to arrange labels in respective
 # rows and columns as specified
 l3.grid(row = 1, column = 1, sticky = W, pady = 20)
 l1.grid(row = 1, column = 2, sticky = W, pady = 20)
 l4.grid(row = 1, column = 3, sticky = W, pady = 20)
 l2.grid(row = 1, column = 10, sticky = W, pady = 20)
 l5.grid(row = 1, column = 0, sticky = W, pady = 20)
 # entry widgets, used to take entry from user
 e1 = Entry(frame)
 e2 = Entry(frame)

 # this will arrange entry widgets
 e1.grid(row = 5, column = 2, pady = 2)
 e2.grid(row = 5, column = 10, pady = 20)
 
 course=["max","min"]
 cmb=ttk.Combobox(frame,values=course,width=15)
 cmb.grid(column=0, row=5)
 cmb.current(0)
 btn=Button(frame,text="Click Here",bg="#B7BF9B",font=('Times',20,'bold'),command=lambda:callback())

 btn.grid(column=2, row=6)
 def callback():
          RETURN_FUNCTION_OBJECIF(int(e2.get()),root,Z,frame2,cmb)
          tableau(int(e2.get()),int(e1.get()),root,A,B,frame1,Ord)
          global BU
          BU=Button(root,text='valider',bg="#B7BF9B",font=('Times',20,'bold'),command=lambda: A_B_Z(A,B,Z,False,int(e2.get()),cmb))
          BU.pack()
        
 

 
 frame.pack()


# Create object
root = Tk()
frame1=Frame(root)

frame2=Frame(root)

root.maxsize(900,700)
root.geometry("900x700")
def tab1():
    def  tab2():
        def  tab3():
            button2.destroy()
            frame.destroy()
            frame2.destroy()
            frame1.destroy()
            BU.destroy()
            tab1()             
            
        canvas.destroy()
        button2 = Button(root, text = "return",bg="#B7BF9B",font=('Times',20,'bold'),command=tab3)
        button2.pack()
        creer_simlex_apartir_function_nbcontrant_nb_variable()
    def  tab4():
        def  tab3():
            tab1()             
        canvas.destroy()
        
    canvas = Canvas(root,width= 700, height= 700)
    global bg
    bg = ImageTk.PhotoImage(file="img.jpg")
    canvas.pack(fill= "both", expand=True)
   # Display image
    canvas.create_image(0, 0, image=bg, anchor="nw")
#Add a text in canvas
    x=canvas.create_text(470,80,fill="#F7CE5A",text="welcome to method simplex!",
                font=("arial black", 30))
    button1 = Button(root, text = "SIMPLEX METHOD",fg="#888164",bg="#C8D296",font=('Times',20,'bold'),command=tab2)

  
    button1_canvas = canvas.create_window( 280, 320,anchor = "nw",window = button1,width="330",height="100", )
    e=canvas.create_text(60,650,fill="#888164",text="   Metrane",
                font=("arial black", 20))
    e=canvas.create_text(750,650,fill="#888164",text="Abdou&Salma",
                font=("arial black", 20))

tab1()

root.mainloop()
