from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("350x100")
root.title("BMI-calculator")

height = StringVar()
weight = StringVar()
output = StringVar()

#height screen
h1 = Entry(root)
h1.grid(row = 0,column = 0)

#weight screen
w1 = Entry(root)
w1.grid(row = 1,column = 0)

#output screen
o1 = Entry(root,textvariable = output)
o1.grid(row = 2,column =0,ipadx = 40)

#height dropbox
height_unit = ttk.Combobox(root, width = 15, textvariable = height)


height_unit["value"] = ("Centimeter",
                        "Meter",
                        "Foot"
                        )
height_unit.current(0)
height_unit.grid(row = 0,column = 1)

#weight dropbox
weight_unit = ttk.Combobox(root, width = 15, textvariable = weight)


weight_unit["value"] = ("Kg",
                        "lbs"
                        )
weight_unit.current(0)
weight_unit.grid(row = 1,column =1)

def height_converter():
    h = float(h1.get())
    hu = height_unit.get()

    if hu == "Centimeter":
        h = h*0.01
        return h

    elif hu == "Foot":
        h = h*0.3048
        return h

    elif hu == "Meter":
        return h

    else:
        output.set("invalid unit")
        o1.update()

def weight_converter():
    w = float(w1.get())
    wu = weight_unit.get()

    if wu == "Kg":
        return w

    elif wu == "lbs":
        w = w*0.453592

    else:
        output.set("invalid unit")
        o1.update()

def bmi():
    bmi_op = weight_converter()/(height_converter()*height_converter())
    bmi_op = round(bmi_op,2)

    if bmi_op < 16:
        output.set(f"{bmi_op} - Sever Thinness")
        o1.update()

    elif bmi_op > 16 and bmi_op < 17:
        output.set(f"{bmi_op} - Moderate Thinness")
        o1.update()

    elif bmi_op > 17 and bmi_op < 18.5:
        output.set(f"{bmi_op} - Mild Thinness")
        o1.update()

    elif bmi_op > 18.5 and bmi_op < 25:
        output.set(f"{bmi_op} - Normal")
        o1.update()

    elif bmi_op > 25 and bmi_op < 30:
        output.set(f"{bmi_op} - Over Weight")
        o1.update()

    elif bmi_op > 30 and bmi_op < 35:
        output.set(f"{bmi_op} - Obese Class-1")
        o1.update()

    elif bmi_op > 35 and bmi_op < 40:
        output.set(f"{bmi_op} - Obese Class-2")
        o1.update()

    elif bmi_op > 40:
        output.set(f"{bmi_op} - Obese Class-3")
        o1.update()

    else:
        output.set("Invalid Choice")
        o1.update()
#button
b1 = Button(root ,text = "Calculate BMI",command = bmi)
b1.grid(row = 2,column =1,)


root.mainloop()