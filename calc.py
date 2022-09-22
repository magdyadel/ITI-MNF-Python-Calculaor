import tkinter as tk
import math
import csv

calc = tk.Tk()

calc.title("Calculator ...!" )
#calc.geometry("200x300")


 # set frame showing inputs and title
top_frame = tk.Frame(calc, relief='flat', bg='#666666'
                     ).grid(row = 0)

# set frame showing all buttons
bottom_frame = tk.Frame(calc, relief='flat', bg='#666666'
                        ).grid(row=0)
# name of calculator
my_item = tk.Label(top_frame, text="Simple Calculator",font=('arial', 14), 
                   fg='white', width=26, bg='#666666')
my_item.grid(columnspan = 4 , ipadx=78)




#Global variables
res = ""
sqrtLabel = ""
color=""


#EntryLabel
entryLabel = tk.StringVar()
tk.Label(top_frame, 
         font=('futura', 25, 'bold'),
         textvariable = entryLabel, 
         fg= 'white',
         bg= '#666666',
         relief= 'flat',
         activebackground= "#666666",
         height=1, 
         width=11
         ).grid(columnspan=4, ipadx=111)

#answerLabel
answerLabel = tk.StringVar()
tk.Label(top_frame, 
         font=('futura', 25, 'bold'),
         textvariable = answerLabel,
         bg= '#666666',
         relief= 'flat',
         foreground='orange', 
         activeforeground='orange',
         height=1, width=11
         ).grid(columnspan = 4, ipadx=111)



#functions
def changeEntryLabel(entry):
    global res
    global sqrtLabel
    res = res + str(entry)
    sqrtLabel = res
    entryLabel.set(res)

def allClear():
    global res
    global sqrtLabel
    res = ""
    sqrtLabel = ""
    entryLabel.set("")
    answerLabel.set("")    

def clearEntryLabel():
    global res
    global sqrtLabel
    sqrtLabel = res
    res = ""
    entryLabel.set(res)

def evalAnswer():
    global res
    lst = []
    lst.append(res)
    try:
       eval(res)
       answer= str(eval(res)) # This line should be alligned    
                   #properly without any indentation error
       clearEntryLabel()
       answerLabel.set(answer)
       #Here we are handling the error when the expression has some SyntaxError 
       #or for that matter any Error.
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        clearEntryLabel()
        answerLabel.set("Error!")
    lst.append(answerLabel.get())
    with open('results.csv', 'a') as file:
        wRes = csv.writer(file)
        wRes.writerow(lst) 
    lst.clear()

def evalSqrt():
    global res
    global sqrtLabel
    try:
        sqrtAnswer = math.sqrt(eval(str(sqrtLabel)))
        clearEntryLabel()
        answerLabel.set(sqrtAnswer)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        try:
            sqrtAnswer = math.sqrt(eval(str(res)))
            clearEntryLabel()
            answerLabel.set(sqrtAnswer)
        #Error Handling  
        except(ValueError,SyntaxError,
               TypeError,ZeroDivisionError):
            clearEntryLabel()
            answerLabel.set("Error!")

    
def createButton(txt,x,y):
    global color
    if txt.isdigit():
      color='light blue'
    else:
      color='light red'
    btn = tk.Button(bottom_frame, font=('futura', 15, 'bold'),
              padx=16,pady=16,text = str(txt),
              fg= 'white',
              bg= '#666666',
              relief= 'flat',
              activebackground= "#666666",
              command = lambda:changeEntryLabel(txt),
              height = 2, width=6)
    if txt.isdigit():
        btn.configure(activebackground="#4d4d4d", bg='#4d4d4d')
    btn.grid(row = x , column = y)
 
    
    
    
#buttons list stores the button values
buttons = ['AC','√','%','/',
           '7','8','9','*',
           '4','5','6','-',
           '1','2','3','+',
           '','','','.']


bListCounter = 0
#loop to create buttons for the application
for i in range(4,9):
    for j in range(0,4):
        createButton(buttons[bListCounter],i,j)
        bListCounter =bListCounter + 1

#Button for AC button - clear the workspace
tk.Button(bottom_frame,font=('futura', 15, 'bold'),
          padx=16,pady=16, text = "AC",
          fg= 'white',
          bg= '#666666',
          relief= 'flat',
          activebackground= "#666666",
          command = lambda:allClear(),
          height=2, width=6
          ).grid(row = 4 , column = 0 )

#Button for SquareRoot
tk.Button(bottom_frame,font=('futura', 15, 'bold'),
          padx=16,pady=16, text = "√",
          fg= 'white',
          bg= '#666666',
          relief= 'flat',
          activebackground= "#666666",
          command = lambda:evalSqrt(),
          height=2, width=6
          ).grid(row = 4 , column = 1)

#Button for value 0 - have 2 columnspace and different dimensions
btn_0 =tk.Button(bottom_frame,font=('futura', 15, 'bold'),
          padx=16,pady=16, text = "0",
          fg= 'white',
          bg= '#666666',
          relief= 'flat',
          activebackground= "#666666",
          command = lambda:changeEntryLabel(0),
          height=2, width=15,)
btn_0.configure(activebackground="#4d4d4d", bg='#4d4d4d')
btn_0.grid(row = 8 , column = 0 , columnspan=2 )
                                   
#Button for "=" - final calc button
btn_eq = tk.Button(bottom_frame,font=('futura', 15, 'bold'),
          padx=16,pady=16, text = "=",
          fg= 'white',
          bg= '#666666',
          relief= 'flat',
          activebackground= "#666666",
          command = lambda:evalAnswer(),
          height=2, width=6)
btn_eq.configure(bg='#ff9980', activebackground='#ff9980')
btn_eq.grid(row = 8 , column = 2)

calc.mainloop() 




