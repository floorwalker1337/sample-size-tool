import tkinter as tk
from tkinter import filedialog as fd

class GUI:
    def __init__(self):
        self.GenerateGui()
    def GenerateGui(self):
        # Root object
        self.root = tk.Tk()
        self.root.title("Sample Size Determinator")

        # Toolbar
        self.toolbar = tk.Menu(self.root)
        self.root.config(menu=self.toolbar)

        self.fileMenu = tk.Menu(self.toolbar)
        self.runMenu = tk.Menu(self.toolbar)
        self.toolbar.add_cascade(label="File", menu=self.fileMenu)
        self.toolbar.add_cascade(label="Run", menu=self.runMenu)

        # File menu options
        self.fileMenu.add_command(label="Open...", command=self.OpenFile)
        self.fileMenu.add_command(label="Exit", command=self.OnQuit)

        # Run menu options
        self.runMenu.add_command(label="Run SSD", command=self.RunSsd)
        self.runMenu.add_command(
            label="Run W/S Normality Test", command=self.RunWs)

        # Frames
        self.sampleFrame = tk.Frame(self.root)
        self.calcFrame = tk.Frame(self.root)
        self.sampleFrame.grid(column=0)
        self.calcFrame.grid(column=1)

        self.normalFrame = tk.Frame(self.calcFrame, bg="blue")
        self.ssdFrame = tk.Frame(self.calcFrame, bg="red")
        self.normalFrame.grid(row=0)
        self.ssdFrame.grid(row=1)

        # Entry fields
        self.meanField = LabelEntry(self.normalFrame, "Mean")
        self.meanField.grid(row=0)
        self.stdDevField = LabelEntry(self.normalFrame, "Std Dev")
        self.stdDevField.grid(row=1)
        self.qCalcField = LabelEntry(self.normalFrame, "q_calc")
        self.qCalcField.grid(row=2)

        # Drop down menus

        # Buttons
        
    
    def ClearEntry(self,entryToClear):
        entryToClear.delete(0,'end')
    
    def OpenFile(self):
        x = fd.askopenfile(mode="r")
        print(x)
    
    def RunWs(self):
        pass
    
    def RunSsd(self):
        pass

    def OnQuit(self):
        pass

class LabelEntry(tk.Frame):
    def __init__(self, parent, labelText):
        tk.Frame.__init__(self, parent, borderwidth=2)
        lbl = tk.Label(self, text=labelText)
        lbl.grid(row=0, column=0)
        e = tk.Entry(self, width=40)
        e.grid(row=0,column=1,columnspan=3)