import tkinter


def button_click(num):
    global operator
    operator = operator + str(num)
    input_val.set(operator)


def buttonclear():
    global operator
    operator = ""
    input_val.set(operator)


def buttonequal():
    global operator
    try:
        result = str(eval(operator))
    except Exception:
        result = "ERROR"

    input_val.set(result)
    operator = ""

window = tkinter.Tk()
window.title("Calculator")
operator = ""


input_val = tkinter.StringVar()


result = tkinter.Entry(window, textvariable = input_val, bg = "grey", font = ("Aerial", 20, "bold"), bd = 20)
result.grid(row = 0, columnspan = 4)

_1 = tkinter.Button(window, text = "1", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click(1))
_1.grid(row = 1, column = 0)

_2 = tkinter.Button(window, text = "2", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click(2))
_2.grid(row = 1, column = 1)

_3 = tkinter.Button(window, text = "3", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click(3))
_3.grid(row = 1, column = 2)

_div = tkinter.Button(window, text = "/", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click("/"))
_div.grid(row = 1, column = 3)


_4 = tkinter.Button(window, text = "4", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click(4))
_4.grid(row = 2, column = 0)

_5 = tkinter.Button(window, text = "5", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click(5))
_5.grid(row = 2, column = 1)

_6 = tkinter.Button(window, text = "6", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click(6))
_6.grid(row = 2, column = 2)

_multi = tkinter.Button(window, text = "*", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click("*"))
_multi.grid(row = 2, column = 3)



_7 = tkinter.Button(window, text = "7", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click(7))
_7.grid(row = 3, column = 0)

_8 = tkinter.Button(window, text = "8", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click(8))
_8.grid(row = 3, column = 1)

_9 = tkinter.Button(window, text = "9", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click(9))
_9.grid(row = 3, column = 2)

_add = tkinter.Button(window, text = "+", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click("+"))
_add.grid(row = 3, column = 3)



_c = tkinter.Button(window, text = "C", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = buttonclear)
_c.grid(row = 4, column = 0)

_0 = tkinter.Button(window, text = "0", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click(0))
_0.grid(row = 4, column = 1)

_equal = tkinter.Button(window, text = "=", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = buttonequal)
_equal.grid(row = 4, column = 2)

_min = tkinter.Button(window, text = "-", bg = "grey", fg = "#ffffff", font = ("cursive", 20), padx = 16, bd = 8, command = lambda: button_click("-"))
_min.grid(row = 4, column = 3)

window.mainloop()