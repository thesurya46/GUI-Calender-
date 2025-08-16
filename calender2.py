from tkinter import *
import calendar

def Calendar_See():
    try:
        get_year = int(year_entry.get())
        window = Toplevel(root)  # Create a new window on button click
        window.config(background="light green")
        window.title("Complete Year Calendar")
        window.geometry("600x600")

        
        window_content = calendar.calendar(get_year)

        
        text_area = Text(window, width=70, height=30, font=("Courier", 10, "bold"), bg="light yellow")
        text_area.insert(INSERT, window_content)
        text_area.pack(pady=20)

        
        scrollbar = Scrollbar(window)
        scrollbar.pack(side=RIGHT, fill=Y)
        text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_area.yview)

    except ValueError:
        error_label = Label(root, text="Please enter a valid year!", fg="red", bg="light blue", font=("Arial", 12, "bold"))
        error_label.grid(row=5, column=1)

root = Tk()
root.config(background="light yellow")
root.title("GUI Calendar")
root.geometry("300x200")

name = Label(root, text="All Year Calendar", bg="red", font=("Arial", 20, "bold"))
name.grid(row=0, column=1, pady=10)


year_label = Label(root, text="Enter Year", bg="purple", font=("Arial", 15, "bold"))
year_label.grid(row=1, column=0, padx=10)

year_entry = Entry(root, font=("Arial", 15))
year_entry.grid(row=1, column=1)

show_button = Button(root, text="Show Calendar", bg="green", font=("Arial", 15, "bold"), command=Calendar_See)
show_button.grid(row=2, column=1, pady=20)

root.mainloop()