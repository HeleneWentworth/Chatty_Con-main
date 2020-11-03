#Creating GUI with tkinter
import tkinter
from tkinter import *

msg = ""

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Quicksand", 12 ))

        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
         
base = Tk()
base.title("Hello")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="black", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="man")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Quicksand",16,'bold'), text="Send", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")

#EntryBox.bind("<Return>", send)
#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)
base.mainloop()































# import tkinter
# from tkinter import *


# root = Tk()

# root.title('Chatbot')


# root.geometry('400x500')

# main_menu = Menu(root)

# file_menu = Menu(root)
# file_menu.add_command(label='New..')
# file_menu.add_command(label='Save as..')
# file_menu.add_command(label='Exit')


# main_menu.add_cascade(label='File', menu = file_menu)
# main_menu.add_command(label='Edit')
# main_menu.add_command(label='Quit')
# root.config(menu=main_menu)

# chatWindow = Text(root, bd=1, bg='black', width = 50, height = 8 )
# chatWindow.place (x=6, y=6, height= 385, width= 370)



# messageWindow = Text(root, bg='black', width = 30, height=4)
# messageWindow.place (x=120, y=400, height= 88, width= 260)

# Button = Button(root, text='Send', bg='blue', activebackground='light blue', width = 12, height=5, font=('Quicksand',20))
# Button.place (x=6, y=400, height= 88, width= 120)


# scrollbar = Scrollbar(root, command=chatWindow.yview())
# scrollbar.place (x=375, y=5, height= 385)



# root.mainloop()


# def chat():
#     msg = EntryBox.get("1.0",'end-1c').strip()
#     EntryBox.delete("0.0",END)
# if msg != '':
#         ChatLog.config(state=NORMAL)
#         ChatLog.insert(END, "You: " + msg + '\n\n')
#         ChatLog.config(foreground="#442265", font=("Quicksand", 12 ))
#         res = chatbot_response(msg)
#         ChatLog.insert(END, "Bot: " + res + '\n\n')
#         ChatLog.config(state=DISABLED)
#         ChatLog.yview(END)
# base = Tk()
# base.title("Hello")
# base.geometry("400x500")
# base.resizable(width=FALSE, height=FALSE)
# #Create Chat window
# ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
# ChatLog.config(state=DISABLED)
# #Bind scrollbar to Chat window
# scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
# ChatLog['yscrollcommand'] = scrollbar.set
# #Create Button to send message
# SendButton = Button(base, font=("Quicksand",12,'bold'), text="Send", width="12", height=5,
#                     bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
#                     command= send )
# #Create the box to enter message
# EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
# #EntryBox.bind("<Return>", send)
# #Place all components on the screen
# scrollbar.place(x=376,y=6, height=386)
# ChatLog.place(x=6,y=6, height=386, width=370)
# EntryBox.place(x=128, y=401, height=90, width=265)
# SendButton.place(x=6, y=401, height=90)
# base.mainloop()