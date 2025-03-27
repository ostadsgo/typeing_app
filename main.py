import keyboard

class Game:
    def __init__(self, text):
        self.text = text
        self.sample_text = "the quick brown fox jumps over lazy dog."
        self.pointer_pos = 0
        self.score = 0

    def play(self):
        print(self.sample_text)
        print('^')
        keyboard.on_release(self.on_keypress)
        user_resp = input("")
        print(f"Your socre is: {self.score}")

    def on_keypress(self, event):
        pressed_key = event.name
        char_under_pointer = self.sample_text[self.pointer_pos]
        # print("Pressed Key: ", pressed_key, "Char Under Pointer", char_under_pointer )
        if pressed_key == char_under_pointer:
            self.score += 1
        self.pointer_pos += 1  # move to next char

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
