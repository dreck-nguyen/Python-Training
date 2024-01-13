# from tkinter import *
#
# window = Tk()
# window.title("My First GUI program")
# window.minsize(width=500, height=300)
#
# # Label
# my_label = Label(text="Label",font=("Arial", 24, "bold"))
# my_label.grid(row=0,column=0)
#
# # my_label["text"] = "New Text"
# # my_label.config(text="New Text")
# # 2 ways to change the text of the my_label (configuration)
# #
# # Button
#
# def button_clicked():
#     print()
#
#
# button = Button(text="Click Me", command=button_clicked)
# button.grid(row=1,column=1)
#
# #  Entry
#
#
#
#
#
#
#
#
# window.mainloop()
#
#
#
#
from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=str(km))


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=1)


kilometer_label = Label(text="Km")
kilometer_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(row=2, column=1)





window.mainloop()



