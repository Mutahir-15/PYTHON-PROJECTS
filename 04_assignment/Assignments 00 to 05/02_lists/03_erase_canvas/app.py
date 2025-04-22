# Erase Canvas
import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20
NUM_ROWS = CANVAS_HEIGHT // CELL_SIZE
NUM_COLS = CANVAS_WIDTH // CELL_SIZE

# Create the main window
root = tk.Tk()
root.title("Erase Canvas")

# Create a canvas
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Create a 2D list to store the cell objects
cells = [[None for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

# Draw the grid of blue cells
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        left_x = col * CELL_SIZE
        top_y = row * CELL_SIZE
        right_x = left_x + CELL_SIZE
        bottom_y = top_y + CELL_SIZE
        # Draw a blue rectangle and store it in the 2D list
        cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="blue")
        cells[row][col] = cell

# Create the eraser (initially at (0, 0))
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

# Function to erase cells that the eraser touches
def erase_cells(event):
    # Get the eraser's current position
    eraser_coords = canvas.coords(eraser)
    left_x, top_y = eraser_coords[0], eraser_coords[1]
    right_x, bottom_y = left_x + ERASER_SIZE, top_y + ERASER_SIZE

    # Check each cell for overlap with the eraser
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            cell = cells[row][col]
            cell_coords = canvas.coords(cell)
            cell_left, cell_top = cell_coords[0], cell_coords[1]
            cell_right, cell_bottom = cell_left + CELL_SIZE, cell_top + CELL_SIZE

            # Check if the eraser overlaps with the cell
            if (left_x < cell_right and right_x > cell_left and
                top_y < cell_bottom and bottom_y > cell_top):
                canvas.itemconfig(cell, fill="white")

# Function to move the eraser with the mouse
def move_eraser(event):
    # Move the eraser to the mouse position
    x, y = event.x, event.y
    # Keep the eraser within the canvas bounds
    x = max(0, min(x, CANVAS_WIDTH - ERASER_SIZE))
    y = max(0, min(y, CANVAS_HEIGHT - ERASER_SIZE))
    canvas.coords(eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
    # Erase cells as the eraser moves
    erase_cells(event)

# Bind mouse events to the canvas
canvas.bind("<B1-Motion>", move_eraser)  # Drag with left mouse button
canvas.bind("<Button-1>", erase_cells)   # Also erase on click

# Start the application
root.mainloop()