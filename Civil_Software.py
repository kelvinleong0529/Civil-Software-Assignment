import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

f = Figure(figsize=(5,5),dpi=100)
a = f.gca(projection='3d')
x = []
y = []
z = []
x_dim = 0
y_dim = 0
z_dim = 0
key = 0

def quit():
    exit(0)

def update(i):
    a.clear()
    if key == 1:
        temp = 0
        for j in range (x_dim+1):
            a.plot((x[temp],x[temp+1]),(y[temp],y[temp+1]),(z[temp],z[temp+1]))
            temp = temp + 2
        temp = 4 + (x_dim-1)*2
        for j in range (y_dim+1):
            a.plot((x[temp],x[temp+1]),(y[temp],y[temp+1]),(z[temp],z[temp+1]))
            temp = temp + 2
    elif key == 2:
        for j in range(0,len(x),x_dim+1):
            for k in range(x_dim):
                a.plot((x[j],x[j+1]),(y[j],y[j+1]),(z[j],z[j+1]))
                j = j + 1
        for j in range(1,len(x)-x_dim-1,1):
            if j!=1 and (j)%(x_dim+1)==0:
                continue
            a.plot((x[j],x[j+x_dim+1]),(y[j],y[j+x_dim+1]),(z[j],z[j+x_dim+1]))
    elif key == 3:
        for j in range(0,len(x),x_dim+1):
            for k in range(x_dim):
                a.plot((x[j],x[j+1]),(y[j],y[j+1]),(z[j],z[j+1]))
                j = j + 1
        temp = 0
        for k in range(y_dim+1):
            for j in range(1,(x_dim+1)*(z_dim+1)-x_dim-1,1):
                if j%(x_dim+1)==0:
                    continue
                a.plot((x[temp+j],x[temp+j+x_dim+1]),(y[temp+j],y[temp+j+x_dim+1]),(z[temp+j],z[temp+j+x_dim+1]))
            temp = temp + (x_dim+1)*(z_dim+1)
        for j in range(1,len(x)-(x_dim+1)*(z_dim+1),1):
            if j%(x_dim+1)==0:
                continue
            a.plot((x[j],x[j+(x_dim+1)*(z_dim+1)]),(y[j],y[j+(x_dim+1)*(z_dim+1)]),(z[j],z[j+(x_dim+1)*(z_dim+1)]))
    elif key == 4:
        temp1 = []
        temp2 = []
        for j in range(x_dim*2+1):
            if j<=x_dim:
                temp1.append(j)
            else:
                temp2.append(j)
        for j in range(len(temp1)-1):
            a.plot((x[temp1[j]],x[temp1[j+1]]),(y[temp1[j]],y[temp1[j+1]]),(z[temp1[j]],z[temp1[j+1]]))
            if j == 0:
                a.plot((x[temp1[j]],x[temp2[j]]),(y[temp1[j]],y[temp2[j]]),(z[temp1[j]],z[temp2[j]]))
            else:
                a.plot((x[temp1[j]],x[temp2[j]]),(y[temp1[j]],y[temp2[j]]),(z[temp1[j]],z[temp2[j]]))
                a.plot((x[temp1[j]],x[temp2[j-1]]),(y[temp1[j]],y[temp2[j-1]]),(z[temp1[j]],z[temp2[j-1]]))
        for j in range(len(temp2)-1):
            a.plot((x[temp2[j]],x[temp2[j+1]]),(y[temp2[j]],y[temp2[j+1]]),(z[temp2[j]],z[temp2[j+1]]))
        a.plot((x[temp1[-1]],x[temp2[-1]]),(y[temp1[-1]],y[temp2[-1]]),(z[temp1[-1]],z[temp2[-1]]))
    elif key == 5:
        temp1 = []
        temp2 = []
        temp = x_dim*2+1
        for j in range(temp):
            if j<=x_dim:
                temp1.append(j)
            else:
                temp2.append(j)
        for k in range (y_dim+1):
            for j in range(len(temp1)-1):
                a.plot((x[k*temp+temp1[j]],x[k*temp+temp1[j+1]]),(y[k*temp+temp1[j]],y[k*temp+temp1[j+1]]),(z[k*temp+temp1[j]],z[k*temp+temp1[j+1]]))
                if j == 0:
                    a.plot((x[k*temp+temp1[j]],x[k*temp+temp2[j]]),(y[k*temp+temp1[j]],y[k*temp+temp2[j]]),(z[k*temp+temp1[j]],z[k*temp+temp2[j]]))
                else:
                    a.plot((x[k*temp+temp1[j]],x[k*temp+temp2[j-1]]),(y[k*temp+temp1[j]],y[k*temp+temp2[j-1]]),(z[k*temp+temp1[j]],z[k*temp+temp2[j-1]]))
                    a.plot((x[k*temp+temp1[j]],x[k*temp+temp2[j]]),(y[k*temp+temp1[j]],y[k*temp+temp2[j]]),(z[k*temp+temp1[j]],z[k*temp+temp2[j]]))
            for j in range(len(temp2)-1):
                a.plot((x[k*temp+temp2[j]],x[k*temp+temp2[j+1]]),(y[k*temp+temp2[j]],y[k*temp+temp2[j+1]]),(z[k*temp+temp2[j]],z[k*temp+temp2[j+1]]))
            a.plot((x[k*temp+temp1[-1]],x[k*temp+temp2[-1]]),(y[k*temp+temp1[-1]],y[k*temp+temp2[-1]]),(z[k*temp+temp1[-1]],z[k*temp+temp2[-1]]))
        for k in range(y_dim):
            for j in range(len(temp1)):
                a.plot((x[k*temp+temp1[j]],x[(k+1)*temp+temp1[j]]),(y[k*temp+temp1[j]],y[(k+1)*temp+temp1[j]]),(z[k*temp+temp1[j]],z[(k+1)*temp+temp1[j]]))
            for j in range(len(temp2)):
                a.plot((x[k*temp+temp2[j]],x[(k+1)*temp+temp2[j]]),(y[k*temp+temp2[j]],y[(k+1)*temp+temp2[j]]),(z[k*temp+temp2[j]],z[(k+1)*temp+temp2[j]]))
    else:
        a.plot(x,y,1)

class Main(tk.Tk):

    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.wm_title(self,'土木工程软件大作业')
        container = tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar,tearoff=0)
        filemenu.add_command (label='Exit',command=quit)
        menubar.add_cascade(label='File',menu=filemenu)
        tk.Tk.config(self,menu=menubar)

        self.frames = {}
        for F in (HomePage,Grid,Frame2D,Frame3D,FrameStructure,Truss2D,Truss3D):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky='nsew')
        self.show_frame(HomePage)

    def grid(self,num1,num2):
        global x
        global y
        global z
        global x_dim
        global y_dim
        global key
        key = 1
        x_dim = num1
        y_dim = num2
        x.clear()
        y.clear()
        z.clear()
        temp = 1
        for i in range (num1+1):
            x.append(temp)
            x.append(temp)
            temp = temp + 1
        for i in range(num2+1):
            temp = 0
            x.append(temp)
            x.append(temp+num1+2)
        temp = 0
        for i in range (num1+1):
            y.append(temp)
            y.append(temp+num2+2)
        for i in range(num2+1):
            y.append(i+1)
            y.append(i+1)
        for i in range(len(x)):
            z.append(1)
        update(1000)
        self.show_frame(FrameStructure)

    def frame2D(self,num1,num2):
        global x
        global y
        global z
        global key
        global x_dim
        global z_dim
        key = 2
        x_dim = num1
        z_dim = num2
        x.clear()
        y.clear()
        z.clear()
        for i in range(num2+1):
            for j in range(num1+1):
                x.append(i)
        for i in range(num2+1):
            for j in range(num1+1):
                z.append(j)
        for i in range(len(x)):
            y.append(1)
        update(1000)
        self.show_frame(FrameStructure)    

    def frame3D(self,num1,num2,num3):
        global x
        global y
        global z
        global key
        global x_dim
        global y_dim
        global z_dim
        key = 3
        x_dim = num1
        z_dim = num2
        y_dim = num3
        x.clear()
        y.clear()
        z.clear()
        for k in range(num3+1):
            for i in range(num2+1):
                for j in range(num1+1):
                    x.append(i)
        for k in range(num3+1):
            for i in range(num2+1):
                for j in range(num1+1):
                    z.append(j)
        for i in range(num3+1):
            for j in range(int(len(x)/(num3+1))):
                y.append(i)
        update(1000)
        self.show_frame(FrameStructure)      

    def truss2D(self,num1):
        global x
        global y
        global z
        global key
        global x_dim
        global y_dim
        global z_dim
        key = 4
        x_dim = num1      
        x.clear()
        y.clear()
        z.clear()
        for i in range(num1+1):
            x.append(i)
            z.append(0)
            y.append(0)
        for i in range(num1):
            x.append(i+0.5)
            z.append(1)
            y.append(0)
        update(1000)
        self.show_frame(FrameStructure) 

    def truss3D(self,num1,num2):
        global x
        global y
        global z
        global key
        global x_dim
        global y_dim
        global z_dim
        key = 5
        x_dim = num1 
        y_dim = num2   
        x.clear()
        y.clear()
        z.clear()
        for j in range(num2+1):
            for i in range(num1+1):
                x.append(i)
                z.append(0)
                y.append(j)
            for k in range(num1):
                x.append(k+0.5)
                z.append(1)
                y.append(j)
        update(1000)
        self.show_frame(FrameStructure) 

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
   
class HomePage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        greeting = tk.Label(self,text="欢迎使用!")
        greeting.config(font=("Times New Roman",28,"bold"))
        greeting.pack(pady=10,padx=10)

        ins = tk.Label(self,text='请选择模板类型!')
        ins.config(font=("Courier",20))
        ins.pack()
        
        grid_but = tk.Button(self,text='轴网',width=10,height=3,command=lambda:controller.show_frame(Grid))
        grid_but.place(x=360,y=130)
        frame2D_but = tk.Button(self,text='2D 框架',width=10,height=3,command=lambda:controller.show_frame(Frame2D))
        frame2D_but.place(x=360,y=190)
        frame3D_but = tk.Button(self,text='3D 框架',width=10,height=3,command=lambda:controller.show_frame(Frame3D))
        frame3D_but.place(x=360,y=250)
        truss2D_but = tk.Button(self,text='2D 桁架',width=10,height=3,command=lambda:controller.show_frame(Truss2D))
        truss2D_but.place(x=360,y=310)
        truss3D_but = tk.Button(self,text='3D 桁架',width=10,height=3,command=lambda:controller.show_frame(Truss3D))
        truss3D_but.place(x=360,y=370)
        quit_but = tk.Button(self,text='退出',width=10,height=3,command=quit)
        quit_but.place(x=360,y=430)

class Grid(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        ins = tk.Label(self,text='请输入轴网的相关参数')
        ins.config(font=("Times New Roman",25,"bold"))
        ins.pack(pady=10,padx=10)
        ins1 = tk.Label(self,text='x方向间距数:')
        ins1.place(x=260,y=100)
        xnum = tk.Entry(self)
        xnum.place(x=360,y=100)
        ins2 = tk.Label(self,text='y方向间距数:')
        ins2.place(x=260,y=140)
        ynum = tk.Entry(self)
        ynum.place(x=360,y=140)
        home_but = tk.Button(self,text='主页',width=10,height=3,command=lambda:controller.show_frame(HomePage))
        home_but.place(x=360,y=250)
        confirm_but = tk.Button(self,text='确定',width=10,height=3,command=lambda:controller.grid(int(xnum.get()),int(ynum.get())))
        confirm_but.place(x=360,y=330)
        quit_but = tk.Button(self,text='退出',width=10,height=3,command=quit)
        quit_but.place(x=360,y=410)
        

class Frame2D(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        ins = tk.Label(self,text='请输入 2D 框架的相关参数')
        ins.config(font=("Times New Roman",25,"bold"))
        ins.pack(pady=10,padx=10)
        ins1 = tk.Label(self,text='层数:')
        ins1.place(x=260,y=100)
        xnum = tk.Entry(self)
        xnum.place(x=360,y=100)
        ins2 = tk.Label(self,text='开间数:')
        ins2.place(x=260,y=140)
        ynum = tk.Entry(self)
        ynum.place(x=360,y=140)
        home_but = tk.Button(self,text='主页',width=10,height=3,command=lambda:controller.show_frame(HomePage))
        home_but.place(x=360,y=250)
        confirm_but = tk.Button(self,text='确定',width=10,height=3,command=lambda:controller.frame2D(int(xnum.get()),int(ynum.get())))
        confirm_but.place(x=360,y=330)
        quit_but = tk.Button(self,text='退出',width=10,height=3,command=quit)
        quit_but.place(x=360,y=410)

class Frame3D(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        ins = tk.Label(self,text='请输入 3D 框架的相关参数')
        ins.config(font=("Times New Roman",25,"bold"))
        ins.pack(pady=10,padx=10)
        ins1 = tk.Label(self,text='层数:')
        ins1.place(x=260,y=100)
        xnum = tk.Entry(self)
        xnum.place(x=360,y=100)
        ins2 = tk.Label(self,text='x 方向开间数:')
        ins2.place(x=260,y=140)
        ynum = tk.Entry(self)
        ynum.place(x=360,y=140)
        ins3 = tk.Label(self,text='y 方向开间数:')
        ins3.place(x=260,y=180)
        znum = tk.Entry(self)
        znum.place(x=360,y=180)
        home_but = tk.Button(self,text='主页',width=10,height=3,command=lambda:controller.show_frame(HomePage))
        home_but.place(x=360,y=250)
        confirm_but = tk.Button(self,text='确定',width=10,height=3,command=lambda:controller.frame3D(int(xnum.get()),int(ynum.get()),int(znum.get())))
        confirm_but.place(x=360,y=330)
        quit_but = tk.Button(self,text='退出',width=10,height=3,command=quit)
        quit_but.place(x=360,y=410)

class Truss2D(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        ins = tk.Label(self,text='请输入 2D 桁架的相关参数')
        ins.config(font=("Times New Roman",25,"bold"))
        ins.pack(pady=10,padx=10)
        ins1 = tk.Label(self,text='开间数:')
        ins1.place(x=260,y=100)
        xnum = tk.Entry(self)
        xnum.place(x=360,y=100)
        home_but = tk.Button(self,text='主页',width=10,height=3,command=lambda:controller.show_frame(HomePage))
        home_but.place(x=360,y=250)
        confirm_but = tk.Button(self,text='确定',width=10,height=3,command=lambda:controller.truss2D(int(xnum.get())))
        confirm_but.place(x=360,y=330)
        quit_but = tk.Button(self,text='退出',width=10,height=3,command=quit)
        quit_but.place(x=360,y=410)

class Truss3D(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        ins = tk.Label(self,text='请输入 3D 桁架的相关参数')
        ins.config(font=("Times New Roman",25,"bold"))
        ins.pack(pady=10,padx=10)
        ins1 = tk.Label(self,text='x 方向开间数:')
        ins1.place(x=260,y=100)
        xnum = tk.Entry(self)
        xnum.place(x=360,y=100)
        ins2 = tk.Label(self,text='y 方向开间数:')
        ins2.place(x=260,y=140)
        ynum = tk.Entry(self)
        ynum.place(x=360,y=140)
        home_but = tk.Button(self,text='主页',width=10,height=3,command=lambda:controller.show_frame(HomePage))
        home_but.place(x=360,y=250)
        confirm_but = tk.Button(self,text='确定',width=10,height=3,command=lambda:controller.truss3D(int(xnum.get()),int(ynum.get())))
        confirm_but.place(x=360,y=330)
        quit_but = tk.Button(self,text='退出',width=10,height=3,command=quit)
        quit_but.place(x=360,y=410)

class FrameStructure(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        ins = tk.Label(self,text='结构模型如下所示：')
        ins.config(font=("Times New Roman",25,"bold"))
        ins.pack(pady=10,padx=10)

        home_but = tk.Button(self,text='主页',width=10,height=3,command=lambda:controller.show_frame(HomePage))
        home_but.pack()
        quit_but = tk.Button(self,text='退出',width=10,height=3,command=quit)
        quit_but.pack()

        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

        toolbar = NavigationToolbar2Tk(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)



app = Main()
app.geometry("800x520")
ani = animation.FuncAnimation(f,update,interval = 1000)
app.mainloop()