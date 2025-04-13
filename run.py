import curses
import time
import random


def readfile(filename):
    with open(filename, "r") as text_file:
        texts = text_file.readlines()
    return texts


def get_random_text():
    return random.choice(readfile("sample.txt"))


def main(win):
    # colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green on black
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Red on black

    win.clear()
    text = get_random_text().strip()
    words = text.split()
    x, y = 0, 0
    win.addstr(x, y, text)
    win.move(x, y)
    win.refresh()

    accuracy = 0
    incorrect = 0
    start_time = time.time()
    max_y, max_x = win.getmaxyx()
    for i in range(len(text)):
        c = win.getch()
        if chr(c) == text[i]:
            win.attron(curses.color_pair(1))
            win.addstr(x, y, text[i])
            win.attroff(curses.color_pair(1))
        else:
            incorrect += 1
            win.attron(curses.color_pair(2))
            win.addstr(x, y, text[i])
            win.attroff(curses.color_pair(2))
        y += 1
        if y >= max_x:
            x += 1
            y = 0
        win.move(x, y)
    end_time = time.time()
    elapsed_time = end_time - start_time
    wpm = len(words) / (elapsed_time / 60)  # Calculate WPM correctly
    accuracy = (1 - (incorrect / len(text))) * 100
    win.addstr(max_y - 5, 0, f"Speed: {wpm:.2f} WPM")  # Format WPM to 2 decimal places
    win.addstr(
        max_y - 4, 0, f"Accuracy: {accuracy:.2f}%"
    )  # Format accuracy to 2 decimal places

    win.getch()


curses.wrapper(main)
