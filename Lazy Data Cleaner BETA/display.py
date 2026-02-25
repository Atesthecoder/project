# Importing Libraries
import tkinter as tk
from controll import controlling
from time import sleep as s


# Run on clicking run_button
def run():
    
    labels1.config(text="Running...",fg="black")
    
    
    labels2.grid()
    infer_button.grid()
    
# Displaying
def displaying(informations):
    labels1.config(text=f"{informations}", font=("Arial", 20, "bold"), fg="black")
def continue1():#after "run" it was work
    
    labels2,infer_button.destroy()#destroy un-needs
    success, message = controlling()#yours
    labels1.after(0, lambda: labels1.config(text=message, fg="green" if success else "red"))
    #in-in button
    restart.grid()
    
# Create the main window
root = tk.Tk()

# Set window title
root.title("Lazy Data Cleaner - BETA")

# Set window size & non-resizable
root.geometry("1200x600")
root.resizable(False, False)

# Labels
#  Output label

labels1 = tk.Label(root, text="OUTPUT", font=("Arial", 18, "bold"), fg="black")
labels1.grid()
# Output label2
labels2 = tk.Label(root,text=(f"This is a beta program it will be update"),font=("Arial", 18, "bold"), fg="green",)


# Buttons
#contunie button:
infer_button = tk.Button(root,text=f"if you want continue click me!!!",bg="black",command=continue1,fg="green")
#restart button
restart = tk.Button(text="re-start system",command=continue1)

#  Run button
run_button = tk.Button(root, text="RUN", font=("Arial", 40, "bold"), bg="blue", command=run)
run_button.grid()

# Main frame and main loop
mainframe = tk.Frame(root)
root.mainloop()