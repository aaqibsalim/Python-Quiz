import ctypes
import tkinter as tk
from tkinter.font import Font

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root_home = tk.Tk()
root_home.title('Python Quiz')
root_home.geometry("1920x1080")
root_home.resizable(False, False)
root_home.iconphoto(True, tk.PhotoImage(file = "D:\Aaqib - 11SENG1\Python Quiz\Images\python_icon.png"))
screen_width = root_home.winfo_screenwidth()
screen_height = root_home.winfo_screenheight()
y_scale = screen_height / 1080

if screen_width == 1920 and screen_height == 1080:
    root_home.state('zoomed')

framelist = []
hoverbutton_list = []

def font_scale(size, scaled_size):
    return int(size * scaled_size)

segoe_b = Font(family = 'Segoe UI Variable Text Semibold', size = font_scale(14, y_scale))
segoe_s = Font(family = 'Segoe UI Variable Text Semibold', size = font_scale(12, y_scale))
segoe_bo = Font(family = 'Segoe UI Variable Text', size = font_scale(15, y_scale), weight = 'bold')
rockwell_b = Font(family = 'Rockwell', size = font_scale(30, y_scale), weight = 'bold')

def loadframes():
    for frame in framelist:
        frame.place(relwidth = 1, relheight = 1)
        frame.lower()

def back_home():
    for frame in framelist:
        frame.place_forget()
    loadframes()

def show_frame(frame):
    frame.tkraise()

def on_enter(event):
    if event.widget['state'] == 'normal':
        event.widget.config(background = '#275b84', foreground = '#ffde57')

def on_leave(event):
    event.widget.config(background = '#ffde57', foreground = '#275b84')

def loadbutton():
    for button in hoverbutton_list:
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)

q2guessed_operations = set()

def submitq1(event = None):
    q1feedback.config(text = 'Feedback:')

    q1a1_v = q1a1_entry.get()
    q1a2_v = q1a2_entry.get()
    q1a3_v = q1a3_entry.get()
    q1a4_v = q1a4_entry.get()
    q1b_v = q1b_entry.get()
    if q1b_v[0] == '(' and q1b_v[-1] == ')':
        q1b_v = q1b_v.replace('(', '').replace(')', '').split(',')
        for i in range(len(q1b_v)):
            q1b_v[i] = q1b_v[i].strip()
        q1b_v.sort()
    correct_no = 0
    if q1a1_v == "'hello'" or q1a1_v == '"hello"':
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
            if 'hello' in q1b_v or "'hello'" in q1b_v or '"hello"' in q1b_v or '15' in q1b_v or '3.14' in q1b_v or 'False' in q1b_v:
                q1result.config(text = "Print the variable names, not the values. E.g string instead\nof 'hello'.")
            else:
                q1result.config(text = 'Your data types are correctly matched, but check your print\n statement and remember commas!')
    else:
        if correct_no == 1:
            q1result.config(text = '1/4 data type is correct.')
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
    q1b_entry.insert(0, '()')
    q1feedback.config(text = '')
    q1result.config(text = '')

def submitq2(event = None):

    global q2guessed_operations

    q2feedback.config(text = 'Feedback & Output:')
    q2a_v = q2a_entry.get()
    q2b_v = q2b_entry.get()

    q2guess = f"{q2a_v}(x {q2b_v} y)"
    q2correct = ['print(x + y)', 'print(x - y)', 'print(x * y)', 'print(x / y)']
    if q2guess not in q2correct:
        if 'print' != q2a_v.lower() and q2b_v not in ['+', '-', '*', '/']:
            incorrect_message = 'Use the print function to display and the operations (+, -, *, /)\nto calculate.'
        elif 'print' == q2a_v.lower() and q2b_v not in ['+', '-', '*', '/']:
            incorrect_message = 'The print function is correctly used, however use the operations\n(+, -, *, /) to calculate.'
        elif 'print' != q2a_v.lower() and q2b_v  in ['+', '-', '*', '/']:
            incorrect_message = 'You are correctly using an operation, however the print function is\nneeded to display the result.'
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

def submitq3(event = None):
    q3feedback.config(text = 'Feedback:')

    q3a_v = q3a_entry.get()
    q3b_v = q3b_entry.get()
    q3c_v = (q3c_entry.get()).replace(' ','').replace('(', '').replace(')', '')
    q3d_v = q3d_entry.get()
    q3e_v = (q3e_entry.get()).replace(' ','').replace('(', '').replace(')', '')
    
    if q3a_v == 'if' and q3b_v == '>' and q3c_v in ['x*y', 'y*x'] and q3d_v == 'else:' and q3e_v in ['x+y', 'y+x']:
        message = 'Perfect! This program will print 50 as 10 * 5 is\ngreater than 30.'
        q3submit_button.config(state = 'disabled')
        q3a_entry.config(state = 'disabled')
        q3b_entry.config(state = 'disabled')
        q3c_entry.config(state = 'disabled')
        q3d_entry.config(state = 'disabled')
        q3e_entry.config(state = 'disabled')
    else:
        if q3a_v != 'if' or 'else' not in q3d_v:
            message = "If-Else statements require lowercase 'if' and\n'else'."
        elif 'else' in q3d_v and q3d_v != 'else:':
            message = 'Colons (:) must be used after each if-else\nstatement.'
        elif q3b_v != '>':
            message = "To check if a number is greater than another,\nthe '>' symbol is used."
        elif q3c_v not in ['x*y', 'y*x']:
            message = 'To print the product (x * y) place it inside the\nprint statement.'
        elif q3e_v not in ['x+y', 'y+x']:
            message = 'The sum is equal to (x + y), place it inside the\nprint statement to display.'
        else:
            message = 'Incorrect.'
    q3result.config(text = message)

def restartq3():
    q3submit_button.config(state = 'normal')
    q3a_entry.config(state = 'normal')
    q3b_entry.config(state = 'normal')
    q3c_entry.config(state = 'normal')
    q3d_entry.config(state = 'normal')
    q3e_entry.config(state = 'normal')
    q3a_entry.delete(0, 'end')
    q3b_entry.delete(0, 'end')
    q3c_entry.delete(0, 'end')
    q3d_entry.delete(0, 'end')
    q3e_entry.delete(0, 'end')
    q3c_entry.insert(0, '()')
    q3e_entry.insert(0, '()')
    q3feedback.config(text = '')
    q3result.config(text = '')

def submitq4(event = None):
    q4feedback.config(text = 'Feedback')

    q4a_v = q4a_entry.get()
    q4b_v = q4b_entry.get().replace('"', "'")
    q4c_v = q4c_entry.get()
    q4d_v = q4d_entry.get()
    
    if q4a_v == q4c_v != '' and q4b_v == "input('Are you enjoying this course?')" and q4d_v == 'else:':
        message = 'Correct! inpt -> input, the inside of your input function is a string,\nyour else is lowercase with a colon, and your variable names match.'
        q4submit_button.config(state = 'disabled')
        q4a_entry.config(state = 'disabled')
        q4b_entry.config(state = 'disabled')
        q4c_entry.config(state = 'disabled')
        q4d_entry.config(state = 'disabled')
    else:
        if q4a_v == '' or q4c_v == '':
            message = 'You are missing variable names.'
        elif q4a_v != q4c_v:
            message = 'Your variable names do not match.'
        elif q4b_v != "input('Are you enjoying this course?')":
            message = "There's something wrong with your input function."
        elif q4d_v != 'else:':
            message = 'Can you find the error with your else: statement?'
        else:
            message = 'Incorrect.'
    q4result.config(text = message)
    
def restartq4():
    q4submit_button.config(state = 'normal')
    q4a_entry.config(state = 'normal')
    q4b_entry.config(state = 'normal')
    q4c_entry.config(state = 'normal')
    q4d_entry.config(state = 'normal')
    q4a_entry.delete(0, 'end')
    q4b_entry.delete(0, 'end')
    q4c_entry.delete(0, 'end')
    q4d_entry.delete(0, 'end')
    q4feedback.config(text = '')
    q4result.config(text = '')
    q4b_entry.insert(0, 'inpt(Are you enjoying this course?)')
    q4d_entry.insert(0, 'Else')

def submitq5(event = None):
    q5feedback.config(text = 'Feedback:')

    q5a_v = q5a_entry.get()
    q5b_v = q5b_entry.get()
    q5c_v = q5c_entry.get()
    q5d_v = q5d_entry.get()
    q5e_v = q5e_entry.get()
    
    q1guess = f"{q5a_v}{q5b_v} works as a {q5c_v} and is {q5d_v} years old.{q5e_v}"
    q1correct = "f'{name} works as a {job} and is {age} years old.'"

    if q1guess == q1correct:
        message = 'Correct! f strings and curly brackets are used to display variables in a\nstring.'
        q5submit_button.config(state = 'disabled')
        q5a_entry.config(state = 'disabled')
        q5b_entry.config(state = 'disabled')
        q5c_entry.config(state = 'disabled')
        q5d_entry.config(state = 'disabled')
        q5e_entry.config(state = 'disabled')
    else:
        if 'john' in q1guess.lower() or 'lawyer' in q1guess.lower() or '34' in q1guess:
            message = "Instead of putting the specific name/job/age we should put the variable\nnames instead. E.g: {name} instead of John."
        elif "f'" in q1guess and '{' not in q1guess:
            message = "You are correct in using an f string but the variables should be inside\ncurly brackets."
        elif '{' in q1guess and "f'" not in q1guess:
            message = "The variables are correctly placed in curly brackets. However, to have\nvariables inside a string, an f string (f') must be used."
        elif "'" in q1guess and "f'" not in q1guess:
            message = "Remember to use an f string (f') when including variables within the\nstring."
        elif "f'" in q1guess and '{' in q1guess:
            message = 'Check to make sure your sentence makes sense.'
        else:
            message = 'Use f-strings and curly brackets to embed variables within a string.'
    q5result.config(text = message)

def restartq5():
    q5submit_button.config(state = 'normal')
    q5a_entry.config(state = 'normal')
    q5b_entry.config(state = 'normal')
    q5c_entry.config(state = 'normal')
    q5d_entry.config(state = 'normal')
    q5e_entry.config(state = 'normal')
    q5a_entry.delete(0, 'end')
    q5b_entry.delete(0, 'end')
    q5c_entry.delete(0, 'end')
    q5d_entry.delete(0, 'end')
    q5e_entry.delete(0, 'end')
    q5feedback.config(text = '')
    q5result.config(text = '')

root_quizone = tk.Frame(root_home)
framelist.append(root_quizone)
q1_background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\quiz_one.png')
q1_background_label = tk.Label(root_quizone, image = q1_background)
q1_background_label.place(x = 0, y = 0)

q1a1 = tk.Label(root_quizone, text = 'string =', font = (segoe_b), bg = '#0277bc', fg = '#ffffff')
q1a1.place(x = 1150, y = 630)
q1a1_entry = tk.Entry(root_quizone, width = 8, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q1a1_entry.place(x = 1275, y = 630)

q1a2 = tk.Label(root_quizone, text = 'integer =', font = (segoe_b), bg = '#0277bc', fg = '#ffffff')
q1a2.place(x = 1150, y = 680)
q1a2_entry = tk.Entry(root_quizone, width = 8, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q1a2_entry.place(x = 1275, y = 680)

q1a3 = tk.Label(root_quizone, text = 'float =', font = (segoe_b), bg = '#0277bc', fg = '#ffffff')
q1a3.place(x = 1500, y = 630)
q1a3_entry = tk.Entry(root_quizone, width = 8, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q1a3_entry.place(x = 1650, y = 630)

q1a4 = tk.Label(root_quizone, text = 'boolean =', font = (segoe_b), bg = '#0277bc', fg = '#ffffff')
q1a4.place(x = 1500, y = 680)
q1a4_entry = tk.Entry(root_quizone, width = 8, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q1a4_entry.place(x = 1650, y = 680)

q1b = tk.Label(root_quizone, text = 'print', font = (segoe_b), bg = '#0277bc', fg = '#ffffff')
q1b.place(x = 1150, y = 765)
q1b_entry = tk.Entry(root_quizone, width = 27, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q1b_entry.place(x = 1210, y = 765)
q1b_entry.insert(0, '()')

q1feedback = tk.Label(root_quizone, font = (segoe_bo), bg = '#0277bc', fg = '#ffde57')
q1feedback.place(x = 1150, y = 850)
q1result = tk.Label(root_quizone, font = (segoe_b), bg = '#0277bc', fg = '#ffffff')
q1result.place(x = 1150, y = 890)

q1next = tk.Button(root_quizone, text = 'Next', font = (segoe_s), command = lambda: show_frame(root_quiztwo), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1843, y = 429)
q1back = tk.Button(root_quizone, text = 'Back', font = (segoe_s), command = lambda: show_frame(root_quizzes), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1678, y = 429)
q1restart = tk.Button(root_quizone, text = 'Restart', font = (segoe_s), command = restartq1, background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1750, y = 429)
q1submit_button = tk.Button(root_quizone, text = 'Submit', font = (segoe_bo), command = submitq1, background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q1submit_button.place(x = 1650, y = 765)
hoverbutton_list.append(q1submit_button)

for i in [q1a1_entry, q1a2_entry, q1a3_entry, q1a4_entry, q1b_entry]:
    i.bind('<Return>', submitq1)

root_quiztwo = tk.Frame(root_home)
framelist.append(root_quiztwo)
q2_background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\quiz_two.png')
q2_background_label = tk.Label(root_quiztwo, image = q2_background)
q2_background_label.place(x = 0, y = 0)

q2a_entry = tk.Entry(root_quiztwo, width = 5, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q2a_entry.place(x = 1150, y = 665)

q2b1 = tk.Label(root_quiztwo, text = '(x', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q2b1.place(x = 1210, y = 665)
q2b_entry = tk.Entry(root_quiztwo, width = 1, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q2b_entry.place(x = 1237, y = 665)
q2b2 = tk.Label(root_quiztwo, text = 'y)', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q2b2.place(x = 1258, y = 665)

q2submit_button = tk.Button(root_quiztwo, text = 'Submit', font = (segoe_bo), command = submitq2, background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q2submit_button.place(x = 1340, y = 650)
hoverbutton_list.append(q2submit_button)
q2feedback = tk.Label(root_quiztwo, font = (segoe_bo), bg = '#0277bc', fg = '#ffde57')
q2feedback.place(x = 1150, y = 745)
q2result = tk.Label(root_quiztwo, font = (segoe_b), bg = '#0277bc', fg = '#ffffff')
q2result.place(x = 1150, y = 775)
q2f_result = tk.Label(root_quiztwo, font = (segoe_b), bg = '#0277bc', fg = '#ffde57')
q2f_result.place(x = 1150, y = 825)
q2back = tk.Button(root_quiztwo, text = 'Back', font = (segoe_s), command = lambda: show_frame(root_quizzes), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1678, y = 429)
q2restart = tk.Button(root_quiztwo, text = 'Restart', font = (segoe_s), command = restartq2, background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1750, y = 429)
q2next = tk.Button(root_quiztwo, text = 'Next', font = (segoe_s), command = lambda: show_frame(root_quizthree), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1843, y = 429)

for i in [q2a_entry, q2b_entry]:
    i.bind('<Return>', submitq2)

root_quizthree = tk.Frame(root_home)
framelist.append(root_quizthree)
q3_background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\quiz_three.png')
q3_background_label = tk.Label(root_quizthree, image = q3_background)
q3_background_label.place(x = 0, y = 0)

q3a_entry = tk.Entry(root_quizthree, width = 1, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q3a_entry.place(x = 1150, y = 665)
q3a = tk.Label(root_quizthree, text = '(x * y)', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q3a.place(x = 1185, y = 665)
q3b_entry = tk.Entry(root_quizthree, width = 1, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q3b_entry.place(x = 1255, y = 665)
q3b = tk.Label(root_quizthree, text = '30:', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q3b.place(x = 1270, y = 665)
q3c = tk.Label(root_quizthree, text = 'print', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q3c.place(x = 1200, y = 715)
q3c_entry = tk.Entry(root_quizthree, width = 5, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q3c_entry.place(x = 1260, y = 715)
q3c_entry.insert(0, '()')

q3d_entry = tk.Entry(root_quizthree, width = 4, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q3d_entry.place(x = 1150, y = 765)
q3d = tk.Label(root_quizthree, text = 'print', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q3d.place(x = 1200, y = 815)
q3e_entry = tk.Entry(root_quizthree, width = 5, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q3e_entry.place(x = 1260, y = 815)
q3e_entry.insert(0, '()')

q3submit_button = tk.Button(root_quizthree, text = 'Submit', font = (segoe_bo), command = submitq3, background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q3submit_button.place(x = 1375, y = 795)
hoverbutton_list.append(q3submit_button)
q3feedback = tk.Label(root_quizthree, font = (segoe_bo), bg = '#0277bc', fg = '#ffde57')
q3feedback.place(x = 1375, y = 665)
q3result = tk.Label(root_quizthree, font = (segoe_b), bg = '#0277bc', fg = '#ffffff')
q3result.place(x = 1375, y = 695)

q3back = tk.Button(root_quizthree, text = 'Back', font = (segoe_s), command = lambda: show_frame(root_quizzes), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1678, y = 429)
q3restart = tk.Button(root_quizthree, text = 'Restart', font = (segoe_s), command = restartq3, background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1750, y = 429)
q3next = tk.Button(root_quizthree, text = 'Next', font = (segoe_s), command = lambda: show_frame(root_quizfour), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1843, y = 429)

for i in [q3a_entry, q3b_entry, q3c_entry, q3d_entry, q3e_entry]:
    i.bind('<Return>', submitq3)

root_quizfour = tk.Frame(root_home)
framelist.append(root_quizfour)
q4_background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\quiz_four.png')
q4_background_label = tk.Label(root_quizfour, image = q4_background)
q4_background_label.place(x = 0, y = 0)

q4a_entry = tk.Entry(root_quizfour, width = 6, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q4a_entry.place(x = 1150, y = 590)
q4a = tk.Label(root_quizfour, text = '=', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q4a.place(x = 1250, y = 590)
q4b_entry = tk.Entry(root_quizfour, width = 31, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q4b_entry.place(x = 1290, y = 590)
q4b_entry.insert(0, 'inpt(Are you enjoying this course?)')
q4b = tk.Label(root_quizfour, text = 'if', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q4b.place(x = 1150, y = 640)
q4c_entry = tk.Entry(root_quizfour, width = 6, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q4c_entry.place(x = 1190, y = 640)
q4c = tk.Label(root_quizfour, text = "==  'yes':", font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q4c.place(x = 1290, y = 640)
q4d = tk.Label(root_quizfour, text = "print('Great!')", font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q4d.place(x = 1200, y = 680)
q4d_entry = tk.Entry(root_quizfour, width = 4, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q4d_entry.place(x = 1150, y = 740)
q4d_entry.insert(0, 'Else')
q4e = tk.Label(root_quizfour, text = "print('Sorry to hear that.')", font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q4e.place(x = 1200, y = 780)

q4submit_button = tk.Button(root_quizfour, text = 'Submit', font = (segoe_bo), command = submitq4, background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q4submit_button.place(x = 1530, y = 720)
hoverbutton_list.append(q4submit_button)
q4back = tk.Button(root_quizfour, text = 'Back', font = (segoe_s), command = lambda: show_frame(root_quizzes), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1678, y = 429)
q4restart = tk.Button(root_quizfour, text = 'Restart', font = (segoe_s), command = restartq4, background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1750, y = 429)
q4next = tk.Button(root_quizfour, text = 'Next', font = (segoe_s), command = lambda: show_frame(root_quizfive), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1843, y = 429)

q4feedback = tk.Label(root_quizfour, font = (segoe_bo), bg = '#0277bc', fg = '#ffde57')
q4feedback.place(x = 1150, y = 850)
q4result = tk.Label(root_quizfour, font = (segoe_b), bg = '#0277bc', fg = '#ffffff')
q4result.place(x = 1150, y = 885)

for i in [q4a_entry, q4b_entry, q4c_entry, q4d_entry]:
    i.bind('<Return>', submitq4)

root_quizfive = tk.Frame(root_home)
framelist.append(root_quizfive)
q5_background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\quiz_five.png')
q5_background_label = tk.Label(root_quizfive, image = q5_background)
q5_background_label.place(x = 0, y = 0)

q5a = tk.Label(root_quizfive, text = 'print(', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q5a.place(x = 1390, y = 620)
q5a_entry = tk.Entry(root_quizfive, width = 1, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q5a_entry.place(x = 1454, y = 620)
q5b_entry = tk.Entry(root_quizfive, width = 6, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q5b_entry.place(x = 1475, y = 620)
q5c = tk.Label(root_quizfive, text = 'works as a', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q5c.place(x = 1560, y = 620)
q5c_entry = tk.Entry(root_quizfive, width = 4, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q5c_entry.place(x = 1680, y = 620)
q5d = tk.Label(root_quizfive, text = 'and is', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q5d.place(x = 1740, y = 620)
q5d_entry = tk.Entry(root_quizfive, width = 4, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q5d_entry.place(x = 1810, y = 620)
q5e = tk.Label(root_quizfive, text = 'years old.', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q5e.place(x = 1550, y = 660)
q5e_entry = tk.Entry(root_quizfive, width = 1, font = (segoe_b), background = '#275b84', disabledbackground = '#275b84', foreground = '#ffffff', borderwidth = 0)
q5e_entry.place(x = 1655, y = 660)
q5f = tk.Label(root_quizfive, text = ')', font = (segoe_b), background = '#0277bc', foreground = '#ffffff')
q5f.place(x = 1670, y = 660)

q5next = tk.Button(root_quizfive, text = 'Next', font = (segoe_s), command = lambda: show_frame(root_quizzes), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1843, y = 429)
q5back = tk.Button(root_quizfive, text = 'Back', font = (segoe_s), command = lambda: show_frame(root_quizzes), background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1678, y = 429)
q5restart = tk.Button(root_quizfive, text = 'Restart', font = (segoe_s), command = restartq5, background = '#ffde57', foreground = '#275b84', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0).place(x = 1750, y = 429)

q5submit_button = tk.Button(root_quizfive, text = 'Submit', font = (segoe_bo), command = submitq5, background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q5submit_button.place(x = 1565, y = 720)
hoverbutton_list.append(q5submit_button)
q5feedback = tk.Label(root_quizfive, font = (segoe_bo), bg = '#0277bc', fg = '#ffde57')
q5feedback.place(x = 1150, y = 800)
q5result = tk.Label(root_quizfive, font = (segoe_b), bg = '#0277bc', fg = '#ffffff')
q5result.place(x = 1150, y = 835)

for i in [q5a_entry, q5b_entry, q5c_entry, q5d_entry, q5e_entry]:
    i.bind('<Return>', submitq5)

root_guideone = tk.Frame(root_home)
framelist.append(root_guideone)
g1_background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\guide_one.png')
g1_background_label = tk.Label(root_guideone, image = g1_background)
g1_background_label.place(x = 0, y = 0)

root_guidefive = tk.Frame(root_home)
framelist.append(root_guidefive)
g5_background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\guide_five.png')
g5_background_label = tk.Label(root_guidefive, image = g5_background)
g5_background_label.place(x = 0, y = 0)

root_guides = tk.Frame(root_home)
framelist.append(root_guides)
guides_background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\\guides.png')
guides_background_label = tk.Label(root_guides, image = guides_background)
guides_background_label.place(x = 0, y = 0)

g1button = tk.Button(root_guides, text = 'G1', font = (rockwell_b), command = lambda: show_frame(root_guideone), background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
g2button = tk.Button(root_guides, text = 'G2', font = (rockwell_b), command = lambda: show_frame(root_guides), background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
g3button = tk.Button(root_guides, text = 'G3', font = (rockwell_b), command = lambda: show_frame(root_guides), background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
g4button = tk.Button(root_guides, text = 'G4', font = (rockwell_b), command = lambda: show_frame(root_guides), background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
g5button = tk.Button(root_guides, text = 'G5', font = (rockwell_b), command = lambda: show_frame(root_guidefive), background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
g1button.place(x = 450, y = 415)
g2button.place(x = 678, y = 415)
g3button.place(x = 905, y = 415)
g4button.place(x = 1133, y = 415)
g5button.place(x = 1360, y = 415)
hoverbutton_list.extend([g1button, g2button, g3button, g4button, g5button])
guidesback = tk.Button(root_guides, text = 'Back', command = lambda: back_home()).place(x = 50, y = 100)

root_quizzes = tk.Frame(root_home)
framelist.append(root_quizzes)
quizzes_background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\quizzes.png')
quizzes_background_label = tk.Label(root_quizzes, image = quizzes_background)
quizzes_background_label.place(x = 0, y = 0)

q1button = tk.Button(root_quizzes, text = 'Q1', font = (rockwell_b), command = lambda: show_frame(root_quizone), background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q2button = tk.Button(root_quizzes, text = 'Q2', font = (rockwell_b), command = lambda: show_frame(root_quiztwo), background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q3button = tk.Button(root_quizzes, text = 'Q3', font = (rockwell_b), command = lambda: show_frame(root_quizthree), background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q4button = tk.Button(root_quizzes, text = 'Q4', font = (rockwell_b), command = lambda: show_frame(root_quizfour), background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q5button = tk.Button(root_quizzes, text = 'Q5', font = (rockwell_b), command = lambda: show_frame(root_quizfive), background = '#ffde57', foreground = '#275b84', borderwidth = 0, activebackground = '#275b84', activeforeground = '#ffde57')
q1button.place(x = 450, y = 415)
q2button.place(x = 678, y = 415)
q3button.place(x = 905, y = 415)
q4button.place(x = 1133, y = 415)
q5button.place(x = 1360, y = 415)
hoverbutton_list.extend([q1button, q2button, q3button, q4button, q5button])
quizzesback = tk.Button(root_quizzes, text = 'Back', command = lambda: back_home()).place(x = 50, y = 100)

background = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\home_page.png')
background_label = tk.Label(root_home, image = background)
background_label.place(x = 0, y = 0)

quiz_button_img = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\quizzes_button.png')
quiz_button_label = tk.Label(root_home, image = quiz_button_img)
quiz_button = tk.Button(root_home, image = quiz_button_img, command = lambda: show_frame(root_quizzes), bg = '#0277bc', bd = 0, activebackground = '#0277bc')
quiz_button_label, quiz_button.place(anchor = 'center', x = 960, y = 670)

guides_button_img = tk.PhotoImage(file = 'D:\Aaqib - 11SENG1\Python Quiz\Images\\guides_button.png')
guides_button_label = tk.Label(root_home, image = guides_button_img)
guides_button = tk.Button(root_home, image = guides_button_img, command = lambda: show_frame(root_guides), bg = '#0277bc', bd = 0, activebackground = '#0277bc')
guides_button_label, guides_button.place(anchor = 'center', x = 960, y = 910)

loadframes()
loadbutton()

root_home.mainloop()