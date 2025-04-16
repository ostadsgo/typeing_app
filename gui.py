import time

import tkinter as tk
from tkinter import ttk
from tkinter import font


# TODO: Make wpm calculation dynamic for each word.
class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.i = 0
        self.timer = False
        self.key_pressed = False
        self.start_time = 0
        self.end_time = 0
        self.misse_typed = 0
        self.wpms = []

        self.labels = []
        # style
        self.style = ttk.Style()
        self._style()
        # sample text
        self.text = "They are 10 types of people in the world. The poeple who knows binary and people who don't."
        self.words = self.text.split()
        self.words_num = len(self.words)

        # how many frames do we need
        frame_num = len(self.words) // 6
        frames = []
        for frame in range(frame_num):
            frames.append(ttk.Frame(relief="solid", padding=5))

        x = 0
        y = len(self.words) // len(frames)
        for frame in frames:
            frame.focus_set()
            frame.bind("<KeyRelease>", self.on_keypress)
            frame.pack(padx=0, pady=15, side="top")
            text_part = self.words[x:y]
            text_part = " ".join(text_part) + " "
            print(text_part)

            for word in text_part:
                for char in word:
                    label = ttk.Label(frame, text=char)
                    label.pack(padx=1, side="left")
                    label["font"] = font.Font(family="default", size=20)
                    label["style"] = "GrayText.TLabel"
                    self.labels.append(label)
            x = y
            y += len(self.words) // len(frames)

        self.result_var = tk.StringVar()
        self.result_var.set("Speed: ")
        elapsed_time_label = ttk.Label(self, textvariable=self.result_var)
        elapsed_time_label.pack()

        self.accu_var = tk.StringVar()
        self.accu_var.set("Acuracy: ")
        accuracy_time_label = ttk.Label(self, textvariable=self.accu_var)
        accuracy_time_label.pack()


    def _style(self):
        styles = (
            ("GrayText.TLabel", {"foreground": "#121212"}),
            ("Green.TLabel", {"foreground": "#28a745"}),
            ("Red.TLabel", {"foreground": "#dc3545", "background": "#ffffff"}),
        )
        for style, options in styles:
            self.style.configure(style, **options)

    def get_wpm(self, elapsed_time):
        # wpm = total_words_typed / time spend
        wpm = self.words_num / (elapsed_time / 60)  # Calculate WPM correctly
        self.wpms.append(wpm)
        print(self.wpms)
        wpm_avg = sum(self.wpms) / len(self.wpms)
        self.result_var.set(f"Speed: {wpm:.2f}")

    def get_accu(self):
        accuracy = (1 - (self.misse_typed / len(self.text))) * 100
        self.accu_var.set(f"Acuracy: {accuracy:.2f}%")


    def on_keypress(self, event):
        # TODO: fix Space problem.

        # Start timer when user press any key
        # claculate speed on any key pressed
        # calculate accurecy on any key press

        # start time for the first time
        if not self.timer:
            self.timer = True
            self.start_time = time.time()

        # self.elapsed_time = time.time() - self.start_time
        # self.get_wpm(self.elapsed_time)
        # stop
        if self.i > len(self.text) - 1:
            self.elapsed_time = time.time() - self.start_time
            self.get_wpm(self.elapsed_time)
            self.get_accu()
            return

        if self.text[self.i] == event.keysym:
            self.labels[self.i].configure(style="Green.TLabel")
        else:
            self.labels[self.i].configure(style="Red.TLabel")
            self.misse_typed += 1


        self.i += 1


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        MainFrame(self).pack(padx=20, pady=20, fill=tk.BOTH)

    def run(self):
        self.mainloop()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
