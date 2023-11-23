from tkinter import *

# window initialization
window = Tk()
window.geometry("550x500")
window.title("Complex Number Calculator")

icon = PhotoImage(file="mathicon.png")
window.iconphoto(True, icon)
window.config(background="#1f2833")

# header shit
header = Label(window, text="COMPLEX NUMBER CACULATOR",
               font=('Arial', 18, 'bold'), background="#1f2833",
               fg="#66fcf1")
header.place(x=75, y=20)

description = Label(window, text="Enter the given complex numbers to calculate.",
                    font=('Arial', 11), background="#1f2833", fg="#c5c6c7")
description.place(x=115, y=53)


# FIRST NUMBER KEME

lbl_first_num = Label(window, text="First Number:", font=('Arial', 11),
                       background="#1f2833", fg="#c5c6c7")
lbl_first_num.place(x=145, y=110)

tb_first_real = Entry(window, width=4, font=('Arial', 30), fg="#1f2833",
                background="#c5c6c7",justify='center')
tb_first_real.place(x=145, y=140)

plus_sign_first = Label(window, text="+", font=('Arial', 30, 'bold'),
                  background="#1f2833", fg="#66fcf1",)
plus_sign_first.place(x=248, y=138)

tb_first_imaginary = Entry(window, width=4, font=('Arial', 30), fg="#1f2833",
                background="#c5c6c7", justify='center')
tb_first_imaginary.place(x=290, y=140)

i_first = Label(window, text="i", font=('Arial', 30, 'bold'),
                  background="#1f2833", fg="#66fcf1",)
i_first.place(x=390, y=140)



# SECOND NUMBER AMPUCHA

lbl_second_num = Label(window, text="Second Number:", font=('Arial', 11),
                       background="#1f2833", fg="#c5c6c7")
lbl_second_num.place(x=145, y=220)

tb_second_real = Entry(window, width=4, font=('Arial', 30), fg="#1f2833",
                background="#c5c6c7",justify='center')
tb_second_real.place(x=145, y=250)

plus_sign_second = Label(window, text="+", font=('Arial', 30, 'bold'),
                  background="#1f2833", fg="#66fcf1",)
plus_sign_second.place(x=248, y=248)

textbox_imaginary = Entry(window, width=4, font=('Arial', 30), fg="#1f2833",
                background="#c5c6c7", justify='center')
textbox_imaginary.place(x=290, y=250)

i_second = Label(window, text="i", font=('Arial', 30, 'bold'),
                  background="#1f2833", fg="#66fcf1",)
i_second.place(x=390, y=248)


# OPERATIONS

btn_add = Button(text="Add", font=('Arial', 11), background="#66fcf1",
                 fg="#1f2833")
btn_add.place(x=70, y=340)

btn_subtract = Button(text="Subtract", font=('Arial', 11), background="#66fcf1",
                      fg="#1f2833")
btn_subtract.place(x=120, y=340)

btn_multipy = Button(text="Multiply", font=('Arial', 11), background="#66fcf1",
                     fg="#1f2833")
btn_multipy.place(x=70, y=380)

btn_divide = Button(text="Divide", font=('Arial', 11), background="#66fcf1",
                    fg="#1f2833")
btn_divide.place(x=130, y=380)

btn_conj_first = Button(text="Conjugate the First Number", font=('Arial', 11),
                        background="#66fcf1", fg="#1f2833")
btn_conj_first.place(x=200, y=340)

btn_conj_second = Button(text="Conjugate the Second Number", font=('Arial', 11),
                         background="#66fcf1", fg="#1f2833")
btn_conj_second.place(x=200, y=380)

window.mainloop()

