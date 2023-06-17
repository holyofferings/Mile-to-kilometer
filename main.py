from tkinter import *
window = Tk()
window.title("Mile to kilometer program ")
window.minsize(width=400, height=200)

def cal_Mile_to_KM():
    miles = float(input.get())
    km = miles*1.609
    my_label2.config(text=f"{km}")


#entry

input = Entry()
input.grid(column=1,row=0)




#label

my_label = Label(text=" Miles", font=("Arial", 20, "italic"),highlightcolor="blue")
my_label.grid(column=2,row=0)

#label2

my_label1 = Label(text=" is Equal to ", font=("Arial", 20, "italic"))
my_label1.grid(column=0, row=1)


#label3

my_label2 = Label(text="0")
my_label2.grid(column=1,row=1)

#label4

my_label3 = Label(text="Km")
my_label3.grid(column=2, row=1)


#button

button = Button(text="Calculate",command=cal_Mile_to_KM)
button.grid(column=1,row=2)
























































window.mainloop()