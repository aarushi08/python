from tkinter import Tk,scrolledtext,Menu,filedialog,END,messagebox,simpledialog

root=Tk(className=" Text Editor")

#Adding scrolled text area
textArea=scrolledtext.ScrolledText(root,width=100,height=80)

#Adding functions to menu
def openFile():
    file=filedialog.askopenfile(parent=root,title='Select a text file',filetypes=(("Text File","*.txt"),("All Files","*.*")))
    root.title("-TEXT EDITOR")

    if file!=None:
        contents=file.read()
        textArea.insert('1.0',contents)
        file.close()

def saveFile():
    file=filedialog.asksaveasfile(mode='w')

    if file!=None:
        data=textArea.get('1.0',END+ '-1c')
        file.write(data)
        file.close()

def about():
    label=messagebox.showinfo("About","A Python alternative to Notepad")

def newFile():
    if len(textArea.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno("Save?","Do you want to save?"):
            saveFile()
        else:
            textArea.delete('1.0',END)
    root.title("TEXT EDITOR")

def findInFile():
    findstring=simpledialog.askstring("Find...","Enter Text")
    textData=textArea.get('1.0',END)
    occurence=textData.upper().count(findstring.upper())

    if textData.upper().count(findstring.upper())>0:
        label= messagebox.showinfo("Results",findstring+"has multiple occurences"+ str(occurence))
    else:
        label=messagebox.showinfo("Results","No match found")

def exitRoot():
    if messagebox.askyesno("Quit","Are you sure you want to quit"):
        root.destroy()


#Adding menus
menu=Menu(root)
root.config(menu=menu)
fileMenu=Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=newFile)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_command(label="Find",command=findInFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=exitRoot)

helpMenu=Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About",command=about)


textArea.pack()
root.mainloop()