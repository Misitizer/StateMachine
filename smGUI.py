from tkinter import *
from smLogical import StateMachine, State

root = Tk()
root.title('Симуляция работы конечного автомата')
root.geometry('640x400+200+100')

s = StateMachine()


def z1b_insert():
    for var in variables:
        var.set(0)

    current_state.delete(1.0, END)
    next_state.delete(1.0, END)
    state = s.activeState.name
    _, var = s.active(1)
    variables[var].set(1)
    current_state.insert(1.0, s.activeState.name)
    line = str(state) + '->' + str(s.activeState.name) + '\n'
    next_state.insert(1.0, line)


def z2b_insert():
    for var in variables:
        var.set(0)

    current_state.delete(1.0, END)
    next_state.delete(1.0, END)
    state = s.activeState.name
    _, var = s.active(2)
    variables[var].set(1)
    current_state.insert(1.0, s.activeState.name)
    line = str(state) + '->' + str(s.activeState.name) + '\n'
    next_state.insert(1.0, line)


def z3b_insert():
    for var in variables:
        var.set(0)

    current_state.delete(1.0, END)
    next_state.delete(1.0, END)
    state = s.activeState.name
    _, var = s.active(3)
    variables[var].set(1)
    current_state.insert(1.0, s.activeState.name)
    line = str(state) + '->' + str(s.activeState.name) + '\n'
    next_state.insert(1.0, line)


def z4b_insert():
    for var in variables:
        var.set(0)

    current_state.delete(1.0, END)
    next_state.delete(1.0, END)
    state = s.activeState.name
    _, var = s.active(4)
    variables[var].set(1)
    current_state.insert(1.0, s.activeState.name)
    line = str(state) + '->' + str(s.activeState.name) + '\n'
    next_state.insert(1.0, line)


def reset_sm():
    for var in variables:
        var.set(0)
    current_state.delete(1.0, END)
    next_state.delete(1.0, END)
    s.activeState = State.b1
    current_state.insert(1.0, s.activeState.name)


label_z = Label(text='Входные значения:')
label_a_curr = Label(text='Текущее состояние:')
label_a_next = Label(text='Переходы:')

z1 = Button(text='Z1', padx=20, pady=5, command=z1b_insert)
z2 = Button(text='Z2', padx=20, pady=5, command=z2b_insert)
z3 = Button(text='Z3', padx=20, pady=5, command=z3b_insert)
z4 = Button(text='Z4', padx=20, pady=5, command=z4b_insert)
reset = Button(text='Сброс', padx=25, pady=5, command=reset_sm)

variables = [IntVar(), IntVar(), IntVar(), IntVar()]

w1 = Checkbutton(root, text='W1', variable=variables[0])
w2 = Checkbutton(root, text='W2', variable=variables[1])
w3 = Checkbutton(root, text='W3', variable=variables[2])
w4 = Checkbutton(root, text='W4', variable=variables[3])

current_state = Text(width=2, height=1)
current_state.place(x=280, y=40)

next_state = Text(width=25, height=5)
next_state.place(x=160, y=105)

label_z.place(x=10, y=40)
label_a_curr.place(x=160, y=40)
label_a_next.place(x=160, y=80)

z1.place(x=40, y=80)
z2.place(x=40, y=120)
z3.place(x=40, y=160)
z4.place(x=40, y=200)
reset.place(x=450, y=300)

w1.place(x=500, y=80)
w2.place(x=500, y=120)
w3.place(x=500, y=160)
w4.place(x=500, y=200)

current_state.insert(1.0, s.activeState.name)

root = mainloop()
