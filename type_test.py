# This is a program for testing the users typing speed
#importing libraries
import time
import random 
import curses
from curses import wrapper


def display_text(stdscr, current_text, text, wpm=0):
	stdscr.addstr(text)
	stdscr.addstr(1, 0, f"WPM: {wpm}")

	for i, char in enumerate(current_text):
		correct_char = text[i]
		color = curses.color_pair(1)
		if char != correct_char:
			color = curses.color_pair(2)

		stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    text = "It's not only writers who can benefit from this free online tool."
    current_text = []
    wpm = 0
    start_time = time.time()
    while True:
        time_elapsed = max(time.time()-start_time,1)
        wpm = round((len(current_text) / 5) / (time_elapsed / 60))

        stdscr.clear()
        display_text(stdscr,current_text,text,wpm)
        stdscr.refresh()

        if "".join(current_text) == text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
             continue

        if ord(key)==27:
            break
		
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
	        if len(current_text) > 0:
                  current_text.pop()
        elif len(current_text) < len(text):
            current_text.append(key)

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(1,0,"Welcome to this typing test\nPress any key to continue")
    stdscr.refresh()
    stdscr.getkey()




def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
        key = stdscr.getkey()
		
        if ord(key) == 27:
            break
    
wrapper(main)