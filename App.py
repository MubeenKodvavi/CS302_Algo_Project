import tkinter as tk
from tkinter import font as tkfont
from algorithms import LongestCommonSubSequence as LCS
from algorithms import ShortestCommonSuperSequence as SCS
from algorithms import LevenshteinDistance as LD
from algorithms import LongestIncreasingSubSequence as LIS
from algorithms import MatrixChainMultiplication as MCM
from algorithms import PartitionProblem as PP
from algorithms import CoinChange as CC
from algorithms import knapsack as k
from algorithms import RodCutting as RC
from algorithms import WordBreakProblem as WBP

chosen_algo = ""

class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        self.configure(bg="#3FEEE6")

    def show_frame(self, page_name, algorithm_name=""):
        '''Show a frame for the given page name'''
        global chosen_algo
        chosen_algo = algorithm_name
        # print(chosen_algo)
        frame = self.frames[page_name]
        frame.tkraise()

    def run_algo_sample(self):
        top = tk.Toplevel()
        top.title("Results")
        top.geometry("500x400")
        top.configure(bg="#3FEEE6")
        label_algo = tk.Label(top, text=str(chosen_algo), font=("Courier", 20), bg="#3FEEE6", fg="black")
        label_algo.pack(pady= 10)
        input = ""
        output = ""
        if(chosen_algo == "Longest Common SubSequence"):
            try:
                file1 = open("sample test cases/abc.txt", "r")
            except FileNotFoundError:
                print("File not found")
            string1 = file1.readline()
            string2 = file1.readline()
            print(string1)
            file1.close()
            input = "String1: " + str(string1) + "\nString2: " + str(string2)
            output = "Length of LCS is " + str(LCS.lcs(string1, string2))

        elif(chosen_algo == "Shortest Common SuperSequence"):
            try:
                file1 = open("sample test cases/abc.txt", "r")
            except FileNotFoundError:
                print("File not found")
            string1 = file1.readline()
            string2 = file1.readline()
            print(string1)
            file1.close()
            input = "String1: " + str(string1) + "\nString2: " + str(string2)
            output = "Length of SCS is " + str(SCS.superSeq(string1, string2, len(string1), len(string2)))
            
        elif(chosen_algo == "The Levenshtein Distance"):
            try:
                file1 = open("sample test cases/abc.txt", "r")
            except FileNotFoundError:
                print("File not found")
            string1 = file1.readline()
            string2 = file1.readline()
            print(string1)
            file1.close()
            input = "String1: " + str(string1) + "\nString2: " + str(string2)
            output = "Levenshtein(edit) distance is " + str(LD.editDistDP(string1, string2, len(string1), len(string2)))

        elif(chosen_algo == "Longest Increasing SubSequence"):
            with open("sample test cases/deg.txt", "r") as f:
                n = int(f.readline())
                line = f.readline()
                array = [int(x) for x in line.split()]
                input = "n = " + str(n) + "\narr = "
                for num in array:
                    input = input + str(num) + " "
                output = "Longest increasing subsequence length is " + str(LIS.lis(array))
                
                
            # print(string1)
            # file1.close()
            # input = "String1: " + str(string1) + "\nString2: " + str(string2)
            # output = "Levenshtein(edit) distance is " + str(LD.editDistDP(string1, string2, len(string1), len(string2)))

        elif(chosen_algo == "Matrix Chain Multiplication"):
            with open("sample test cases/deg.txt", "r") as f:
                n = int(f.readline())
                line = f.readline()
                array = [int(x) for x in line.split()]
                input = "n = " + str(n) + "\ndimensions = "
                for num in array:
                    input = input + str(num) + " "
                output = "Minimum scalar multiplications required " + str(MCM.MatrixChainOrder(array, len(array)))
        elif(chosen_algo == "0-1 Knapsack Problem"):
            with open("sample test cases/fh.txt", "r") as f:
                n = int(f.readline())
                line = f.readline()
                weights = [int(x) for x in line.split()]
                line = f.readline()
                values = [int(x) for x in line.split()]
                W = int(f.readline())
                input = "n = " + str(n) + "\nweights = "
                for num in weights:
                    input = input + str(num) + " "
                input = input + "\nvalues = "
                for num in values:
                    input = input + str(num) + " "
                input = input + "\nW = " + str(W)
                output = "Maximum value from knapsack: " + str(k.knapSack(W, weights, values, len(weights)))
        elif(chosen_algo == "Partition Problem"):
            with open("sample test cases/deg.txt", "r") as f:
                n = int(f.readline())
                line = f.readline()
                array = [int(x) for x in line.split()]
                input = "n = " + str(n) + "\narr = "
                for num in array:
                    input = input + str(num) + " "
                if PP.findPartition(array, len(array)) == True:
                    output = "Can be divided into two subsets of equal sum"
                else:
                    output = "Can not be divided into two subsets of equal sum"
        elif(chosen_algo == "Rod Cutting"):
            with open("sample test cases/fh.txt", "r") as f:
                n = int(f.readline())
                line = f.readline()
                lengths = [int(x) for x in line.split()]
                line = f.readline()
                values = [int(x) for x in line.split()]
                rodlen = int(f.readline())
                input = "n = " + str(n)
                # for num in lengths:
                #     input = input + str(num) + " "
                input = input + "\nvalues = "
                for num in values:
                    input = input + str(num) + " "
                input = input + "\nW = " + str(rodlen)
                output = "Maximum obtainable value is: " + str(RC.cutRod(values, len(values)))
        elif(chosen_algo == "Coin Change Problem"):
            with open("sample test cases/i.txt", "r") as f:
                n = int(f.readline())
                line = f.readline()
                array = [int(x) for x in line.split()]
                change = int(f.readline())
                input = "n = " + str(n) + "\ncoins = "
                for num in array:
                    input = input + str(num) + " "
                input = input +"\nChange: " +  str(change)
                output = "Ways to generate change: " + str(CC.count(array, len(array), change))
        elif(chosen_algo == "Word Break Problem"):
            with open("sample test cases/j.txt", "r") as f:
                n = int(f.readline())
                line = f.readline()
                S = [x for x in line.split()]
                Word = f.readline()
                input = "n = " + str(n) + "\nSet = "
                for num in S:
                    input = input + str(num) + " "
                input = input +"\nChange: " +  Word
                lookup = [-1] * (len(Word) + 1)
                if WBP.wordBreak(S, Word, lookup) == True:
                    output = "String can be segmented"
                else:
                    output = "String can't be segmented"
        label_inputh = tk.Label(top, text="Input:", font=("Courier", 15, "bold"), bg="#3FEEE6", fg="black")
        label_inputh.pack(pady=(5, 0))
        label_input = tk.Label(top, text = str(input), fg= 'black', bg='#3FEEE6', wraplengt=350)
        label_input.pack(pady= 5)
        label_outputh = tk.Label(top, text="Output:", font=("Courier", 15, "bold"), bg="#3FEEE6", fg="black")
        label_outputh.pack(pady=(5, 0))
        label_output = tk.Label(top, text=output, fg= 'black', bg='#3FEEE6', wraplengt=350)
        label_output.pack(pady= 5)


    def run_algo_file(self):
        pass


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg="#3FEEE6")
        self.controller = controller
        self.controller.configure(bg="#3FEEE6")
        myLabel = tk.Label(self, text="Chose an algorithm:", font=("Courier", 20), bg="#3FEEE6", fg="black")
        Button1 = tk.Button(self, text="Longest Common Subsequence", width=50, command=lambda: controller.show_frame("PageOne", "Longest Common SubSequence"))
        Button2 = tk.Button(self, text="Shortest Common SuperSequence", width=50, command=lambda: controller.show_frame("PageOne", "Shortest Common SuperSequence"))
        Button3 = tk.Button(self, text="The Levenshtein Distance", width=50, command=lambda: controller.show_frame("PageOne", "The Levenshtein Distance"))
        Button4 = tk.Button(self, text="Longest Increasing SubSequence", width=50, command=lambda: controller.show_frame("PageOne", "Longest Increasing SubSequence"))
        Button5 = tk.Button(self, text="Matrix Chain Multiplication", width=50, command=lambda: controller.show_frame("PageOne", "Matrix Chain Multiplication"))
        Button6 = tk.Button(self, text="0-1 Knapsack Problem", width=50, command=lambda: controller.show_frame("PageOne", "0-1 Knapsack Problem"))
        Button7 = tk.Button(self, text="Partition Problem", width=50, command=lambda: controller.show_frame("PageOne", "Partition Problem"))
        Button8 = tk.Button(self, text="Rod Cutting", width=50, command=lambda: controller.show_frame("PageOne", "Rod Cutting"))
        Button9 = tk.Button(self, text="Coin Change Problem", width=50, command=lambda: controller.show_frame("PageOne", "Coin Change Problem"))
        Button10 = tk.Button(self, text="Word Break Problem", width=50, command=lambda: controller.show_frame("PageOne", "Word Break Problem"))

        myLabel.pack(pady=5)
        Button1.pack(pady=5)
        Button2.pack(pady=5)
        Button3.pack(pady=5)
        Button4.pack(pady=5)
        Button5.pack(pady=5)
        Button6.pack(pady=5)
        Button7.pack(pady=5)
        Button8.pack(pady=5)
        Button9.pack(pady=5)
        Button10.pack(pady=5)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#3FEEE6")
        self.controller = controller
        label = tk.Label(self, text="Chose method to run: ", font=("Courier", 20), bg="#3FEEE6", fg="black")
        button = tk.Button(self, text="Go back", command=lambda: controller.show_frame("StartPage"))
        button.pack(side="top", anchor="nw")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Sample File", command = controller.run_algo_sample)
        button2 = tk.Button(self, text="Chose a file", command = controller.run_algo_file)
        # button3 = tk.Button(self, text="File 3", command = lambda: controller.run_algo_file(3))
        button1.pack(pady=5)
        button2.pack(pady=5)
        # button3.pack(pady=5)


if __name__ == "__main__":
    app = MyApp()
    app.geometry("500x400")
    app.title("Dynamic Programming Algorithms Solver")
    app.mainloop()