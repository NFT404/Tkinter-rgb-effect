import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a list with the colors of the rainbow
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Create the button
btn = tk.Button(root, text='RGB', bg=rainbow[0])
btn.pack()

# Function that changes the color of the button in the order of the colors of the rainbow
def change_color():
  # Get the current color of the button
  current_color = btn['bg']
  
  # If the current color of the button is the last color in the list, change the color to the first color in the list
  if current_color == rainbow[-1]:
    btn['bg'] = rainbow[0]
  # If the current color of the button is not the last color in the list, change the color to the next color in the list
  else:
    btn['bg'] = rainbow[rainbow.index(current_color) + 1]
  
  # Schedule the next change of color after one second
  root.after(1000, change_color)

# Start the color change of the button
change_color()

# Show the window
root.mainloop()
