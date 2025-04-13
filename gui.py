import tkinter as tk
from tkinter import ttk
from tkinter import font


class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.i = 0
        self.labels = []
        # style
        self.style = ttk.Style()
        self.style.configure("GrayText.TLabel", foreground="#212121")
        self.style.configure("Green.TLabel", foreground="#00ff00")
        self.style.configure("Red.TLabel", foreground="#ff0000")
        # sample text
        self.text = "hello world"
        label_frame = ttk.Frame(self, padding=(5, 10), relief="solid")
        label_frame.pack(padx=10, pady=20, side="top")

        # make label for each char.
        for char in self.text:
            label = ttk.Label(label_frame, text=char)
            label["font"] = font.Font(family="default", size=20)
            label["style"] = "GrayText.TLabel"
            label.pack(fill=tk.BOTH, expand=True, side='left' )
            self.labels.append(label)

        label_frame.focus_set()
        label_frame.bind("<KeyRelease>", self.on_keypress)

    def on_keypress(self, event):
        # TODO: fix Space problem.
        if self.i > len(self.text) - 1:
            return

        if self.text[self.i] == event.keysym:
            self.labels[self.i].configure(style="Green.TLabel")
        else:
            self.labels[self.i].configure(style="Red.TLabel")

        self.i += 1


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        MainFrame(self).pack(fill=tk.BOTH, expand=True)

    def run(self):
        self.mainloop()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
