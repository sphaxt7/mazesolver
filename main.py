from graphics import *
from cell import Cell

def main():
    win = Window(800, 600)
    # l = Line(Point(0, 0), Point(800, 600))
    # win.draw_line(l, "black")

    cell = Cell(win)
    cell.draw(50, 50, 100, 100)
    
    win.wait_for_close()

main()