try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

chosen_algo = ""

class SampleApp(tk.Tk):

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
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
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
        print(chosen_algo)
        frame = self.frames[page_name]
        frame.tkraise()

    # def run_algo(self, file_num):


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg="#3FEEE6")
        self.controller = controller
        self.controller.configure(bg="#3FEEE6")
        myLabel = tk.Label(self, text="Chose an algorithm:", font=("Courier", 20), bg="#3FEEE6", fg="black")
        Button1 = tk.Button(self, text="Longest Common Subsequence", width=50, command=lambda: controller.show_frame("PageOne", "Longest Common SubSequence"))
        Button2 = tk.Button(self, text="Shortest Common SuperSequence", width=50, command=lambda: controller.show_frame("PageOne", "Shortest Common SuperSequence"))
        Button3 = tk.Button(self, text="Longest Increasing SubSequence", width=50, command=lambda: controller.show_frame("PageOne", "Longest Increasing SubSequence"))
        Button4 = tk.Button(self, text="The Levenshtein Distance", width=50, command=lambda: controller.show_frame("PageTwo", "The Levenshtein Distance"))
        Button5 = tk.Button(self, text="Matrix Chain Multiplication", width=50, command=lambda: controller.show_frame("PageTwo", "Matrix Chain Multiplication"))
        Button6 = tk.Button(self, text="0-1 Knapsack Problem", width=50, command=lambda: controller.show_frame("PageThree", "0-1 Knapsack Problem"))
        Button7 = tk.Button(self, text="Partition Problem", width=50, command=lambda: controller.show_frame("PageTwo", "Partition Problem"))
        Button8 = tk.Button(self, text="Rod Cutting", width=50, command=lambda: controller.show_frame("PageThree", "Rod Cutting"))
        Button9 = tk.Button(self, text="Coin Change Problem", width=50, command=lambda: controller.show_frame("PageThree", "Coin Change Problem"))
        Button10 = tk.Button(self, text="Word Break Problem", width=50, command=lambda: controller.show_frame("PageFour", "Word Break Problem"))

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
    global chosen_algo
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#3FEEE6")
        self.controller = controller
        label = tk.Label(self, text="Chose a file", font=("Courier", 20), bg="#3FEEE6", fg="black")
        button = tk.Button(self, text="Go back", command=lambda: controller.show_frame("StartPage"))
        button.pack(side="top", anchor="nw")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="File 1", command = lambda: controller.run_algo(1))
        button2 = tk.Button(self, text="File 2", command = lambda: controller.run_algo(2))
        button3 = tk.Button(self, text="File 3", command = lambda: controller.run_algo(3))
        button1.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#3FEEE6")
        self.controller = controller
        label = tk.Label(self, text="Chose a file", font=("Courier", 20), bg="#3FEEE6", fg="black")
        button = tk.Button(self, text="Go back", command=lambda: controller.show_frame("StartPage"))
        button.pack(side="top", anchor="nw")
        label.pack(side="top", fill="x", pady=10)

        button4 = tk.Button(self, text="File 4", command = lambda: controller.run_algo(4))
        button5 = tk.Button(self, text="File 5", command = lambda: controller.run_algo(5))
        button7 = tk.Button(self, text="File 7", command = lambda: controller.run_algo(7))
        button4.pack(pady=5)
        button5.pack(pady=5)
        button7.pack(pady=5)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#3FEEE6")
        self.controller = controller
        label = tk.Label(self, text="Chose a file", font=("Courier", 20), bg="#3FEEE6", fg="black")
        button = tk.Button(self, text="Go back", command=lambda: controller.show_frame("StartPage"))
        button.pack(side="top", anchor="nw")
        label.pack(side="top", fill="x", pady=10)

        button6 = tk.Button(self, text="File 6", command = lambda: controller.run_algo(6))
        button8 = tk.Button(self, text="File 8", command = lambda: controller.run_algo(8))
        button9 = tk.Button(self, text="File 9", command = lambda: controller.run_algo(9))
        button6.pack(pady=5)
        button8.pack(pady=5)
        button9.pack(pady=5)

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#3FEEE6")
        self.controller = controller
        label = tk.Label(self, text="Chose a file", font=("Courier", 20), bg="#3FEEE6", fg="black")
        button = tk.Button(self, text="Go back", command=lambda: controller.show_frame("StartPage"))
        button.pack(side="top", anchor="nw")
        label.pack(side="top", fill="x", pady=10)

        button10 = tk.Button(self, text="File 10", command = lambda: controller.run_algo(10))
        button10.pack(pady=5)


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("400x400")
    app.mainloop()