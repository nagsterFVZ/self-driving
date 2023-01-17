import curses
from control.esc import Esc
from control.servo import Servo

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            Servo.increment(5)
        elif char == curses.KEY_LEFT:
            Servo.increment(-5)
        elif char == curses.KEY_UP:
            Esc.incControl(int(5))
        elif char == curses.KEY_DOWN:
            Esc.incControl(int(-5))
        elif char == 49: # 1
            Esc.cal_phase_1()
        elif char == 50: # 2
            Esc.cal_phase_2()
        elif char == 122: # Z
            Esc.safe()
        elif char == 120: # X
            Esc.arm()
finally:
    # shut down cleanly
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
