from tkinter import Label, Tk 
import time

# Create the main application window
app_window = Tk() 

# Set the title of the window
app_window.title("Digital Clock") 

# Set the geometry (size) of the window
app_window.geometry("420x150") 

# Make the window resizable
app_window.resizable(1,1)

# Define the font, background color, foreground color, and border width for the label
text_font= ("Boulder", 68, 'bold')  # Font style, size, and weight
background = "#f2e750"  # Background color
foreground= "#363529"  # Text color
border_width = 25  # Border width around the label

# Create a Label widget with the specified properties
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 

# Place the label in the grid layout of the window
label.grid(row=0, column=1)

# Define the function to update the digital clock
def digital_clock(): 
   # Get the current time in HH:MM:SS format
   time_live = time.strftime("%H:%M:%S")

   # Update the label with the current time
   label.config(text=time_live) 

   # Schedule the next update in 200 milliseconds
   label.after(200, digital_clock)

# Start the digital clock
digital_clock()

# Enter the main event loop of the Tkinter application
app_window.mainloop()
