import tkinter as tk
import ctypes
from tkinter.font import Font

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root_home = tk.Tk()
root_home.title('Python Quiz')
root_home.geometry("1920x1080")
root_home.state('zoomed')
root_home.iconphoto(True, tk.PhotoImage(file = "D:\Aaqib - 11SENG1\Python Quiz\Images\Python Icon.png"))

root_home.grid_rowconfigure(0, weight=1)
root_home.grid_columnconfigure(0, weight=1)

framelist = []
bricolage_b = Font(family = 'Bricolage Grotesque 14pt', size = 13)
bricolage_s = Font(family = 'Bricolage Grotesque 14pt', size = 11)

def back_home():
    for frame in framelist:
        frame.grid_forget()

def show_frame(frame):
    frame.grid(row=0, column=0, sticky="nsew")
    frame.tkraise()

def on_enter(event):
    event.widget.config(background = '#275b84', foreground = '#ffde57')
def on_leave(event):
    event.widget.config(background = '#ffde57', foreground = '#275b84')

q2guessed_operations = set()

def submitq1():
    q1feedback.config(text = 'Feedback:')

    q1a1_v = q1a1_entry.get()
    q1a2_v = q1a2_entry.get()
    q1a3_v = q1a3_entry.get()
    q1a4_v = q1a4_entry.get()
    q1b_v = ((q1b_entry.get().replace('(', '')).replace(')', '')).split(',')
    for i in range(len(q1b_v)):
        q1b_v[i] = q1b_v[i].strip()
    q1b_v.sort()
    correct_no = 0
    if q1a1_v == "'hello'":
        correct_no += 1
    if q1a2_v == '15':
        correct_no += 1
    if q1a3_v == '3.14':
        correct_no += 1
    if q1a4_v == 'False':
        correct_no += 1
    if correct_no == 4:
        if q1b_v == ['boolean', 'float', 'integer', 'string']:
            q1result.config(text = 'All four data types were correctly matched and printed!')
            q1submit_button.config(state = 'disabled')
            q1a1_entry.config(state = 'disabled')
            q1a2_entry.config(state = 'disabled')
            q1a3_entry.config(state = 'disabled')
            q1a4_entry.config(state = 'disabled')
            q1b_entry.config(state = 'disabled')
        else:
            q1result.config(text = 'Your data types are correctly matcheed, but check your print\n statement and remember commas!')
    else:
        if correct_no == 1:
            q1result.config(text = '1/4 data type correct.')
        else:
            q1result.config(text = f'{correct_no}/4 data types are correct.')


def restartq1():

    q1submit_button.config(state = 'normal')
    q1a1_entry.config(state = 'normal')
    q1a2_entry.config(state = 'normal')
    q1a3_entry.config(state = 'normal')
    q1a4_entry.config(state = 'normal')
    q1b_entry.config(state = 'normal')
    q1a1_entry.delete(0, 'end')
    q1a2_entry.delete(0, 'end')
    q1a3_entry.delete(0, 'end')
    q1a4_entry.delete(0, 'end')
    q1b_entry.delete(0, 'end')
    q1b_entry.insert('end', '()')
    q1feedback.config(text = '')
    q1result.config(text = '')

def submitq2():

    global q2guessed_operations

    q2feedback.config(text = 'Feedback & Output:')
    q2a_v = q2a_entry.get()
    q2b_v = q2b_entry.get()

    q2guess = f"{q2a_v}(x {q2b_v} y)"
    q2correct = ['print(x + y)', 'print(x - y)', 'print(x * y)', 'print(x / y)']
    if q2guess not in q2correct:
        if 'print' != q2a_v.lower() and q2b_v not in ['+', '-', '*', '/']:
            incorrect_message = 'Use the print function to display and the operations (+, -, *, /) to calculate.'
        elif 'print' == q2a_v.lower() and q2b_v not in ['+', '-', '*', '/']:
            incorrect_message = 'The print function is correctly used, however use the operations (+, -, *, /) to calculate.'
        elif 'print' != q2a_v.lower() and q2b_v  in ['+', '-', '*', '/']:
            incorrect_message = 'You are correctly using an operation, however the print function is needed to display \nthe result.'
        else:
            incorrect_message = "Make sure the 'print()' function is lowercase."
        q2result.config(text = incorrect_message)
    else:
        q2guessed_operations.add(q2b_v)
        q2result.config(text = f'10 {q2b_v} 5 = ' + str(round(eval(f'10 {q2b_v} 5'))))
        if {'+', '-', '*', '/'}.issubset(q2guessed_operations):
            q2f_result.config(text = 'That is all four operations correctly used. Congratulations!')
            q2submit_button.config(state = 'disabled') 
            q2a_entry.config(state = 'disabled')
            q2b_entry.config(state = 'disabled')

def restartq2():

    global q2guessed_operations
    q2submit_button.config(state = 'normal')
    q2a_entry.config(state = 'normal')
    q2b_entry.config(state = 'normal')
    q2a_entry.delete(0, 'end')
    q2b_entry.delete(0, 'end')  
    q2feedback.config(text = '')
    q2result.config(text = '')
    q2f_result.config(text = '')
    q2guessed_operations.clear()

root_quizone = tk.Frame(root_home)
framelist.append(root_quizone)
q1_background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\Quiz One.png')
q1_background_label = tk.Label(root_quizone, image = q1_background)
q1_background_label.place(x = 0, y = 0)

q1a1 = tk.Label(root_quizone, text = 'string =', font = (bricolage_b), bg = '#0277bc', fg = '#ffffff')
q1a1.place(x = 1150, y = 630)
q1a1_entry = tk.Entry(root_quizone, width = 8, font = (bricolage_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q1a1_entry.place(x = 1275, y = 630)

q1a2 = tk.Label(root_quizone, text = 'integer =', font = (bricolage_b), bg = '#0277bc', fg = '#ffffff')
q1a2.place(x = 1150, y = 680)
q1a2_entry = tk.Entry(root_quizone, width = 8, font = (bricolage_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q1a2_entry.place(x = 1275, y = 680)

q1a3 = tk.Label(root_quizone, text = 'float =', font = (bricolage_b), bg = '#0277bc', fg = '#ffffff')
q1a3.place(x = 1500, y = 630)
q1a3_entry = tk.Entry(root_quizone, width = 8, font = (bricolage_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q1a3_entry.place(x = 1650, y = 630)

q1a4 = tk.Label(root_quizone, text = 'boolean =', font = (bricolage_b), bg = '#0277bc', fg = '#ffffff')
q1a4.place(x = 1500, y = 680)
q1a4_entry = tk.Entry(root_quizone, width = 8, font = (bricolage_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q1a4_entry.place(x = 1650, y = 680)

q1b = tk.Label(root_quizone, text = 'print', font = (bricolage_b), bg = '#0277bc', fg = '#ffffff')
q1b.place(x = 1150, y = 765)
q1b_entry = tk.Entry(root_quizone, width = 25, font = (bricolage_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q1b_entry.place(x = 1210, y = 765)
q1b_entry.insert('end', '()')

q1feedback = tk.Label(root_quizone, font = ('Bricolage Grotesque 14pt', 13, 'bold'), bg = '#0277bc', fg = '#ffde57')
q1feedback.place(x = 1150, y = 850)
q1result = tk.Label(root_quizone, font = (bricolage_b), bg = '#0277bc', fg = '#ffffff')
q1result.place(x = 1150, y = 890)

q1back = tk.Button(root_quizone, text = 'Back', font = (bricolage_s), command = lambda: show_frame(root_quiz), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1750, y = 427)
q1restart = tk.Button(root_quizone, text = 'Restart', font = (bricolage_s), command = restartq1, background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1825, y = 427)
q1submit_button = tk.Button(root_quizone, text = 'Submit', font = ('NT Brick Sans', 13), command = submitq1, background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q1submit_button.place(x = 1650, y = 765)
q1submit_button.bind('<Enter>', on_enter)
q1submit_button.bind('<Leave>', on_leave)

root_quiztwo = tk.Frame(root_home)
framelist.append(root_quiztwo)
q2_background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\Quiz Two.png')
q2_background_label = tk.Label(root_quiztwo, image = q2_background)
q2_background_label.place(x = 0, y = 0)

q2question = tk.Label(root_quiztwo, text = '''x = 10
y = 5''', font = ('Bricolage Grotesque 14pt', 20), bg = '#0277bc', fg = '#ffffff')
q2question.place(x = 1470, y = 525)

q2a_entry = tk.Entry(root_quiztwo, width = 4, font = (bricolage_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q2a_entry.place(x = 1445, y = 665)

q2b1 = tk.Label(root_quiztwo, text = '(x', font = (bricolage_b), background = '#0277bc', foreground = '#ffffff')
q2b1.place(x = 1505, y = 665)
q2b_entry = tk.Entry(root_quiztwo, width = 1, font = (bricolage_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q2b_entry.place(x = 1532, y = 665)
q2b2 = tk.Label(root_quiztwo, text = 'y)', font = (bricolage_b), background = '#0277bc', foreground = '#ffffff')
q2b2.place(x = 1551, y = 665)

q2submit_button = tk.Button(root_quiztwo, text = 'Submit', font = ('NT Brick Sans', 13), command = submitq2, background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q2submit_button.place(x = 1455, y = 750)
q2submit_button.bind('<Enter>', on_enter)
q2submit_button.bind('<Leave>', on_leave)
q2feedback = tk.Label(root_quiztwo, font = ('Bricolage Grotesque 14pt', 13, 'bold'), bg = '#0277bc', fg = '#ffde57')
q2feedback.place(x = 1150, y = 820)
q2result = tk.Label(root_quiztwo, font = (bricolage_b), bg = '#0277bc', fg = '#ffffff')
q2result.place(x = 1150, y = 850)
q2f_result = tk.Label(root_quiztwo, font = (bricolage_b), bg = '#0277bc', fg = '#ffde57')
q2f_result.place(x = 1150, y = 900)
q2back = tk.Button(root_quiztwo, text = 'Back', font = (bricolage_s), command = lambda: show_frame(root_quiz), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1750, y = 427)
q2restart = tk.Button(root_quiztwo, text = 'Restart', font = (bricolage_s), command = restartq2, background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1825, y = 427)

root_tutorials = tk.Frame(root_home)
framelist.append(root_tutorials)

root_quiz = tk.Frame(root_home)
framelist.append(root_quiz)
q1button = tk.Button(root_quiz, text = 'Quiz 1', command = lambda: show_frame(root_quizone)).grid(row = 0, column = 0)
q2button = tk.Button(root_quiz, text = 'Quiz 2', font = (bricolage_b), command = lambda: show_frame(root_quiztwo)).grid(row = 0, column = 1)
quizback = tk.Button(root_quiz, text = 'Back', command = lambda: back_home()).grid(row = 0, column = 2)

for frame in (framelist):
    frame.grid(row=0, column=0, sticky="nsew")

background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\Home Page.png')
background_label = tk.Label(root_home, image = background)
background_label.place(x = 0, y = 0)

quiz_button_img = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\Quiz Button.png')
quiz_button_label = tk.Label(root_home, image = quiz_button_img)
quiz_button = tk.Button(root_home, image = quiz_button_img, command = lambda: show_frame(root_quiz), bg = '#0277bc', bd = 0, activebackground = '#0277bc')
quiz_button_label, quiz_button.place(anchor = 'center', x = 960, y = 670)

tutorials_button_img = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\Tutorials Button.png')
tutorials_button_label = tk.Label(root_home, image = tutorials_button_img)
tutorials_button = tk.Button(root_home, image = tutorials_button_img, command = lambda: show_frame(root_tutorials), bg = '#0277bc', bd = 0, activebackground = '#0277bc')
tutorials_button_label, tutorials_button.place(anchor = 'center', x = 960, y = 910)

root_home.mainloop()