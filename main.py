import os
import sys
import keyboard
import getpass
import curses


class Game:
    def __init__(self, text):
        self.text = text
        self.text = "the quick brown fox jumps over lazy dog."
        self.pointer_pos = 0
        self.score = 0
        self.typed = ""

    def play(self):
        self.redraw_screen()
        keyboard.on_release(self.on_keypress)
        user_resp = input("")
        sys.exit()

    def redraw_screen(self):
        print(self.typed)
        os.system("clear")
        print(self.text)
        print(self.pointer_pos * ' ' + '^')
        print(self.typed)

    def on_keypress(self, event):
        pressed_key = event.name
        char_under_pointer = self.text[self.pointer_pos]
        self.typed += pressed_key
        if pressed_key == char_under_pointer:
            self.score += 1
        self.pointer_pos += 1  # move to next char
        self.redraw_screen()
        if len(self.typed) >= len(self.text):
            print(f"Your socre is: {self.score}")
            sys.exit()
            

class App:
    def readfile(self, filename):
        content = ""
        with open("text.txt", "r") as text_file:
            content = text_file.readlines()
        return content

    def run(self):
        text = self.readfile("text.txt")
        game = Game(text)
        game.play()

if __name__ == "__main__":
    app = App()
    app.run()
