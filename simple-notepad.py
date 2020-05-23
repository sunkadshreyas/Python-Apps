import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename 

# function which opens file using filedialog
# deletes whatever content has been entered
# opens file in read mode and reads into variable text
# appends text at the end of text_box
def open_file():
    filepath = askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    text_box.delete("1.0",tk.END)
    with open(filepath,'r') as input_file:
        text = input_file.read()
        text_box.insert(tk.END,text)
    window.title(f"Text Editor - {filepath}")

# function which saves file
# file is opened in write mode
# the contents of text box is written into the file
def save_file():
    filepath = asksaveasfilename(defaultextension="txt",
                                 filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath,'w') as output_file:
        text = text_box.get("1.0",tk.END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")

    
window = tk.Tk()
window.title('Text Editor')

# configuring size to remain same even on expanding the window
window.rowconfigure(0,minsize=600,weight=1)
window.columnconfigure(1,minsize=600,weight=1)
  

text_box = tk.Text(window)
button_layout = tk.Frame(window)
button_open = tk.Button(master=button_layout,text="Open",command=open_file)
button_save = tk.Button(master=button_layout,text="Save As",command=save_file)

  
button_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
button_save.grid(row=1,column=0,sticky="ew",padx=5)

button_layout.grid(row=0,column=0,sticky="ns")
text_box.grid(row=0,column=1,sticky="nsew")

window.mainloop()
