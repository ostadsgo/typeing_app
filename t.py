import curses

def main(win):
    # colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green on black
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Red on black

    win.clear()
    text = "Hello world"
    x, y = 0, 0
    win.addstr(x, y, text)
    win.move(x, y)
    win.refresh()
    # curses.echo()

    correct = ""
    incorrect = ""
    for i in range(len(text)):
        c = win.getch()
        if chr(c) == text[i]:
            win.move(x, i+1)
            win.attron(curses.color_pair(1))
            win.addstr(x, i, text[i])
            win.attroff(curses.color_pair(1))
        else:
            win.move(x, i+1)
            win.attron(curses.color_pair(2))
            win.addstr(x, i, text[i])
            win.attroff(curses.color_pair(2))
    win.getch()





curses.wrapper(main)

