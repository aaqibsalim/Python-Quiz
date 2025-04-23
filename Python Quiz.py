import ctypes
import tkinter as tk
from tkinter.font import Font

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root_home = tk.Tk()
root_home.title('Python Quiz')
root_home.geometry("1920x1080")
root_home.resizable(False, False)
root_home.iconphoto(True, tk.PhotoImage(file = "Images\\python_icon.png"))
screen_width = root_home.winfo_screenwidth()
screen_height = root_home.winfo_screenheight()
y_scale = screen_height / 1080

if screen_width == 1920 and screen_height == 1080:
    root_home.state('zoomed')

framelist = []
hoverbutton_list = []
visited_frames = []

def loadframes():
    for frame in framelist:
        frame.place(relwidth = 1, relheight = 1)
        frame.lower()

def back_home():
    for frame in framelist:
        frame.place_forget()    
    loadframes()

def show_frame(frame):
    visited_frames.append(frame)
    frame.tkraise()

def frame_back():
    visited_frames.pop()  
    visited_frames[-1].tkraise()

def on_enter(event):
    if event.widget['state'] == 'normal':
        event.widget.config(background = '#275b84', foreground = '#ffde57')

def on_leave(event):
    event.widget.config(background = '#ffde57', foreground = '#275b84')

def loadbutton():
    for button in hoverbutton_list:
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)

def font_scale(size, scaled_size):
    return int(size * scaled_size)

segoe_b = Font(family = 'Segoe UI Variable Text Semibold', size = font_scale(14, y_scale))
segoe_s = Font(family = 'Segoe UI Variable Text Semibold', size = font_scale(12, y_scale))
segoe_bo = Font(family = 'Segoe UI Variable Text', size = font_scale(15, y_scale), weight = 'bold')
rockwell_b = Font(family = 'Rockwell', size = font_scale(30, y_scale), weight = 'bold')

label_style = {'font': segoe_b, 'background': '#0277bc', 'foreground': '#ffffff'}
entry_style = {'font': segoe_b, 'background': '#275b84', 'disabledbackground': '#275b84', 'foreground': '#ffffff', 'borderwidth': 0}
feedback_style = {'font': segoe_bo, 'bg': '#0277bc', 'fg': '#ffde57'}
subbutton_style = {'font': segoe_bo, 'background': '#ffde57', 'foreground': '#275b84', 'borderwidth': 0, 'activebackground': '#275b84', 'activeforeground': '#ffde57'}
topbutton_style = {'font': segoe_s, 'background': '#ffde57', 'foreground': '#275b84', 'activebackground': '#275b84', 'activeforeground': '#ffde57', 'borderwidth': 0}
bigbutton_style = {'font': rockwell_b, 'background': '#ffde57', 'foreground': '#275b84', 'borderwidth': 0, 'activebackground': '#275b84', 'activeforeground': '#ffde57'}

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

def submitq6(event = None):
    q6feedback.config(text = 'Feedback:')

    q6a_v = q6a_entry.get()
    q6b_v = q6b_entry.get().replace(' ','')
    q6c_v = q6c_entry.get()
    q6d_v = q6d_entry.get()
    q6e_v = q6e_entry.get()
    q6f_v = q6f_entry.get()

    if q6a_v == '[' and q6b_v in ["'item1','item2','item3'", '"item1","item2","item3"'] and q6c_v == ']' and q6d_v == '[0]' and q6e_v == 'list' and q6f_v in ['-1', '2']:
        message = 'Correct! This program will successfully perform the required task.'
        q6submit_button.config(state = 'disabled')
        q6a_entry.config(state = 'disabled')
        q6b_entry.config(state = 'disabled')
        q6c_entry.config(state = 'disabled')
        q6d_entry.config(state = 'disabled')
        q6e_entry.config(state = 'disabled')
        q6f_entry.config(state = 'disabled')
    elif q6a_v != '[' or q6c_v != ']':
        message = 'Lists start and end with square brackets: [].'
    elif ',' not in q6b_v:
        message = 'Items in lists are separated by commas.'
    elif q6b_v not in ["'item1','item2','item3'", '"item1","item2","item3"']:
        message = 'Incorrect list (line 1).'
    elif '(' in q6d_v or ')' in q6d_v:
        message = 'Indexes are placed in square brackets: [], not ().'
    elif '1' in q6d_v:
        message = 'Indexes begin counting from 0, so an index of 1 is the second item.'
    elif q6d_v != '[0]':
        message = 'Incorrect index (line 2)'
    elif q6e_v != 'list':
        message = 'To access the index of a list, the list name must be used.'
    elif q6f_v not in ['-1', '2']:
        message = 'The last item can be accessed through an index of -1, or 2 since\nthere are 3 items.'
    else:
        message = 'Incorrect.'

    q6result.config(text = message)

def restartq6():
    q6submit_button.config(state = 'normal')
    q6a_entry.config(state = 'normal')
    q6b_entry.config(state = 'normal')
    q6c_entry.config(state = 'normal')
    q6d_entry.config(state = 'normal')
    q6e_entry.config(state = 'normal')
    q6f_entry.config(state = 'normal')
    q6a_entry.delete(0, 'end')
    q6b_entry.delete(0, 'end')
    q6c_entry.delete(0, 'end')
    q6d_entry.delete(0, 'end')
    q6e_entry.delete(0, 'end')
    q6f_entry.delete(0, 'end')
    q6b_entry.insert(0, "'item1' 'item2' 'item3'")
    q6d_entry.insert(0, '(1)')
    q6feedback.config(text = '')
    q6result.config(text = '')

def submitq7(event = None):
    q7feedback.config(text = 'Feedback:')

    q7a_v = q7a_entry.get()
    q7b_v = q7b_entry.get()
    q7c_v = q7c_entry.get().replace(' ', '')
    q7d_v = q7d_entry.get().replace(' ', '')
    q7e_v = q7e_entry.get()

    if q7a_v == 'True:' and q7b_v == '<' and q7c_v in ['x=x+1', 'x+=1'] and q7d_v in ["(f'{x}>=10')", '(f"{x}>=10")'] and q7e_v == 'break':
        message = "Correct! This program will keep adding to x until it's greater than\nor equal to ten."
        q7submit_button.config(state = 'disabled')
        q7a_entry.config(state = 'disabled')
        q7b_entry.config(state = 'disabled')
        q7c_entry.config(state = 'disabled')
        q7d_entry.config(state = 'disabled')
        q7e_entry.config(state = 'disabled')
    elif 'True' in q7a_v and ':' not in q7a_v:
        message = "You're using the correct keyword 'True', however a colon is needed\nat the end."
    elif q7a_v != 'True:':
        message = "To create an infinite loop the word 'True' must be used after 'while'."
    elif q7b_v != '<':
        message = "To check if x is less than 10, the '<' symbol is used."
    elif q7c_v not in ['x=x+1', 'x+=1']:
        message = "To add 1 to x, you can use 'x = x + 1' or 'x += 1' for short."
    elif 'f' not in q7d_v:
        message = 'To embed a variable within a string, an f-string must be used.'
    elif q7d_v not in ["(f'{x}>=10')", '(f"{x}>=10")']:
        message = 'Incorrect print statement.'
    elif q7e_v != 'break':
        message = "To end a loop, the keyword is an all lowercase 'break'."
    q7result.config(text = message)

def restartq7():
    q7submit_button.config(state = 'normal')
    q7a_entry.config(state = 'normal')
    q7b_entry.config(state = 'normal')
    q7c_entry.config(state = 'normal')
    q7d_entry.config(state = 'normal')
    q7e_entry.config(state = 'normal')
    q7a_entry.delete(0, 'end')
    q7b_entry.delete(0, 'end')
    q7c_entry.delete(0, 'end')
    q7d_entry.delete(0, 'end')
    q7e_entry.delete(0, 'end')
    q7d_entry.insert(0, "('{x} >= 10')")
    q7feedback.config(text = '')
    q7result.config(text = '')

def submitq8(event = None):
    q8feedback.config(text = 'Feedback:')

    q8a_v = q8a_entry.get()
    q8b_v = q8b_entry.get()
    q8c_v = q8c_entry.get()
    q8d_v = q8d_entry.get()
    
    if q8a_v in q8c_v and q8a_v in q8d_v and q8b_v == 'input' and 'for' in q8c_v and f'in {q8a_v}:' in q8c_v and q8d_v == f'{q8a_v}[0]':
        message = 'Perfect! This program functions as expected.'
        q8submit_button.config(state = 'disabled')
        q8a_entry.config(state = 'disabled')
        q8b_entry.config(state = 'disabled')
        q8c_entry.config(state = 'disabled')
        q8d_entry.config(state = 'disabled')
    elif q8a_v not in q8c_v or q8a_v not in q8d_v:
        message = 'Variables names do not match.'
    elif q8b_v != 'input':
        message = 'Use the input function to allow the user to pick a word.'
    elif 'for' in q8c_v and f'in {q8a_v}:' not in q8c_v:
        message = "Starting the for loop with 'for' is correct, however you need to use the 'for (loopvar) in (var):' format."
    elif 'for' not in q8c_v and f'in {q8a_v}:' not in q8c_v:
        message = "Your for loop should begin with ''for (loopvar) in (var):'."
    elif q8a_v in q8d_v and q8d_v != f'{q8a_v}[0]':
        message = 'You correctly call your variable but to get the first letter an index of 0 must be used.'
    elif q8d_v != f'{q8a_v}[0]':
        message = 'To check the first letter of your variable use the index 0.'
    else:
        message = 'Incorrect.'
    q8result.config(text = message)

def restartq8():
    q8submit_button.config(state = 'normal')
    q8a_entry.config(state = 'normal')
    q8b_entry.config(state = 'normal')
    q8c_entry.config(state = 'normal')
    q8d_entry.config(state = 'normal')
    q8a_entry.delete(0, 'end')
    q8b_entry.delete(0, 'end')
    q8c_entry.delete(0, 'end')
    q8d_entry.delete(0, 'end')
    q8feedback.config(text = '')
    q8result.config(text = '')

root_quizone = tk.Frame(root_home)
framelist.append(root_quizone)
q1_background = tk.PhotoImage(file = 'Images\\quiz_one.png')
q1_background_label = tk.Label(root_quizone, image = q1_background)
q1_background_label.place(x = 0, y = 0)

q1a1 = tk.Label(root_quizone, text = 'string =', **label_style)
q1a1.place(x = 1150, y = 630)
q1a1_entry = tk.Entry(root_quizone, width = 8, **entry_style)
q1a1_entry.place(x = 1275, y = 630)

q1a2 = tk.Label(root_quizone, text = 'integer =', **label_style)
q1a2.place(x = 1150, y = 680)
q1a2_entry = tk.Entry(root_quizone, width = 8, **entry_style)
q1a2_entry.place(x = 1275, y = 680)

q1a3 = tk.Label(root_quizone, text = 'float =', **label_style)
q1a3.place(x = 1500, y = 630)
q1a3_entry = tk.Entry(root_quizone, width = 8, **entry_style)
q1a3_entry.place(x = 1650, y = 630)

q1a4 = tk.Label(root_quizone, text = 'boolean =', **label_style)
q1a4.place(x = 1500, y = 680)
q1a4_entry = tk.Entry(root_quizone, width = 8, **entry_style)
q1a4_entry.place(x = 1650, y = 680)

q1b = tk.Label(root_quizone, text = 'print', **label_style)
q1b.place(x = 1150, y = 765)
q1b_entry = tk.Entry(root_quizone, width = 27, **entry_style)
q1b_entry.place(x = 1210, y = 765)
q1b_entry.insert(0, '()')

q1feedback = tk.Label(root_quizone, **feedback_style)
q1feedback.place(x = 1150, y = 850)
q1result = tk.Label(root_quizone, **label_style)
q1result.place(x = 1150, y = 890)

q1next = tk.Button(root_quizone, text = 'Next', command = lambda: show_frame(root_quiztwo), **topbutton_style).place(x = 1843, y = 429)
q1back = tk.Button(root_quizone, text = 'Back', command = frame_back, **topbutton_style).place(x = 1678, y = 429)
q1restart = tk.Button(root_quizone, text = 'Restart', command = restartq1, **topbutton_style).place(x = 1750, y = 429)
q1submit_button = tk.Button(root_quizone, text = 'Submit', command = submitq1, **subbutton_style)
q1submit_button.place(x = 1650, y = 765)
hoverbutton_list.append(q1submit_button)

for i in [q1a1_entry, q1a2_entry, q1a3_entry, q1a4_entry, q1b_entry]:
    i.bind('<Return>', submitq1)

root_quizone.bind('<Right>', lambda event: show_frame(root_quiztwo))

root_quiztwo = tk.Frame(root_home)
framelist.append(root_quiztwo)
q2_background = tk.PhotoImage(file = 'Images\\quiz_two.png')
q2_background_label = tk.Label(root_quiztwo, image = q2_background)
q2_background_label.place(x = 0, y = 0)

q2a_entry = tk.Entry(root_quiztwo, width = 5, **entry_style)
q2a_entry.place(x = 1150, y = 665)

q2b1 = tk.Label(root_quiztwo, text = '(x', **label_style)
q2b1.place(x = 1210, y = 665)
q2b_entry = tk.Entry(root_quiztwo, width = 1, **entry_style)
q2b_entry.place(x = 1237, y = 665)
q2b2 = tk.Label(root_quiztwo, text = 'y)', **label_style)
q2b2.place(x = 1258, y = 665)

q2submit_button = tk.Button(root_quiztwo, text = 'Submit', command = submitq2, **subbutton_style)
q2submit_button.place(x = 1340, y = 650)
hoverbutton_list.append(q2submit_button)
q2feedback = tk.Label(root_quiztwo, **feedback_style)
q2feedback.place(x = 1150, y = 745)
q2result = tk.Label(root_quiztwo, **label_style)
q2result.place(x = 1150, y = 775)
q2f_result = tk.Label(root_quiztwo, font = (segoe_b), bg = '#0277bc', fg = '#ffde57')
q2f_result.place(x = 1150, y = 825)
q2back = tk.Button(root_quiztwo, text = 'Back', command = frame_back, **topbutton_style).place(x = 1678, y = 429)
q2restart = tk.Button(root_quiztwo, text = 'Restart', command = restartq2, **topbutton_style).place(x = 1750, y = 429)
q2next = tk.Button(root_quiztwo, text = 'Next', command = lambda: show_frame(root_quizthree), **topbutton_style).place(x = 1843, y = 429)

for i in [q2a_entry, q2b_entry]:
    i.bind('<Return>', submitq2)

root_quizthree = tk.Frame(root_home)
framelist.append(root_quizthree)
q3_background = tk.PhotoImage(file = 'Images\\quiz_three.png')
q3_background_label = tk.Label(root_quizthree, image = q3_background)
q3_background_label.place(x = 0, y = 0)

q3a_entry = tk.Entry(root_quizthree, width = 1, **entry_style)
q3a_entry.place(x = 1150, y = 665)
q3a = tk.Label(root_quizthree, text = '(x * y)', **label_style)
q3a.place(x = 1185, y = 665)
q3b_entry = tk.Entry(root_quizthree, width = 1, **entry_style)
q3b_entry.place(x = 1255, y = 665)
q3b = tk.Label(root_quizthree, text = '30:', **label_style)
q3b.place(x = 1270, y = 665)
q3c = tk.Label(root_quizthree, text = 'print', **label_style)
q3c.place(x = 1200, y = 715)
q3c_entry = tk.Entry(root_quizthree, width = 5, **entry_style)
q3c_entry.place(x = 1260, y = 715)
q3c_entry.insert(0, '()')

q3d_entry = tk.Entry(root_quizthree, width = 4, **entry_style)
q3d_entry.place(x = 1150, y = 765)
q3d = tk.Label(root_quizthree, text = 'print', **label_style)
q3d.place(x = 1200, y = 815)
q3e_entry = tk.Entry(root_quizthree, width = 5, **entry_style)
q3e_entry.place(x = 1260, y = 815)
q3e_entry.insert(0, '()')

q3submit_button = tk.Button(root_quizthree, text = 'Submit', command = submitq3, **subbutton_style)
q3submit_button.place(x = 1375, y = 795)
hoverbutton_list.append(q3submit_button)
q3feedback = tk.Label(root_quizthree, **feedback_style)
q3feedback.place(x = 1375, y = 665)
q3result = tk.Label(root_quizthree, **label_style)
q3result.place(x = 1375, y = 695)

q3back = tk.Button(root_quizthree, text = 'Back', command = frame_back, **topbutton_style).place(x = 1678, y = 429)
q3restart = tk.Button(root_quizthree, text = 'Restart', command = restartq3, **topbutton_style).place(x = 1750, y = 429)
q3next = tk.Button(root_quizthree, text = 'Next', command = lambda: show_frame(root_quizfour), **topbutton_style).place(x = 1843, y = 429)

for i in [q3a_entry, q3b_entry, q3c_entry, q3d_entry, q3e_entry]:
    i.bind('<Return>', submitq3)

root_quizfour = tk.Frame(root_home)
framelist.append(root_quizfour)
q4_background = tk.PhotoImage(file = 'Images\\quiz_four.png')
q4_background_label = tk.Label(root_quizfour, image = q4_background)
q4_background_label.place(x = 0, y = 0)

q4a_entry = tk.Entry(root_quizfour, width = 6, **entry_style)
q4a_entry.place(x = 1150, y = 590)
q4a = tk.Label(root_quizfour, text = '=', **label_style)
q4a.place(x = 1250, y = 590)
q4b_entry = tk.Entry(root_quizfour, width = 31, **entry_style)
q4b_entry.place(x = 1290, y = 590)
q4b_entry.insert(0, 'inpt(Are you enjoying this course?)')
q4b = tk.Label(root_quizfour, text = 'if', **label_style)
q4b.place(x = 1150, y = 640)
q4c_entry = tk.Entry(root_quizfour, width = 6, **entry_style)
q4c_entry.place(x = 1190, y = 640)
q4c = tk.Label(root_quizfour, text = "==  'yes':", **label_style)
q4c.place(x = 1290, y = 640)
q4d = tk.Label(root_quizfour, text = "print('Great!')", **label_style)
q4d.place(x = 1200, y = 680)
q4d_entry = tk.Entry(root_quizfour, width = 4, **entry_style)
q4d_entry.place(x = 1150, y = 740)
q4d_entry.insert(0, 'Else')
q4e = tk.Label(root_quizfour, text = "print('Sorry to hear that.')", **label_style)
q4e.place(x = 1200, y = 780)

q4submit_button = tk.Button(root_quizfour, text = 'Submit', command = submitq4, **subbutton_style)
q4submit_button.place(x = 1530, y = 720)
hoverbutton_list.append(q4submit_button)
q4back = tk.Button(root_quizfour, text = 'Back', command = frame_back, **topbutton_style).place(x = 1678, y = 429)
q4restart = tk.Button(root_quizfour, text = 'Restart', command = restartq4, **topbutton_style).place(x = 1750, y = 429)
q4next = tk.Button(root_quizfour, text = 'Next', command = lambda: show_frame(root_quizfive), **topbutton_style).place(x = 1843, y = 429)

q4feedback = tk.Label(root_quizfour, **feedback_style)
q4feedback.place(x = 1150, y = 850)
q4result = tk.Label(root_quizfour, **label_style)
q4result.place(x = 1150, y = 885)

for i in [q4a_entry, q4b_entry, q4c_entry, q4d_entry]:
    i.bind('<Return>', submitq4)

root_quizfive = tk.Frame(root_home)
framelist.append(root_quizfive)
q5_background = tk.PhotoImage(file = 'Images\\quiz_five.png')
q5_background_label = tk.Label(root_quizfive, image = q5_background)
q5_background_label.place(x = 0, y = 0)

q5a = tk.Label(root_quizfive, text = 'print(', **label_style)
q5a.place(x = 1390, y = 620)
q5a_entry = tk.Entry(root_quizfive, width = 1, **entry_style)
q5a_entry.place(x = 1454, y = 620)
q5b_entry = tk.Entry(root_quizfive, width = 6, **entry_style)
q5b_entry.place(x = 1475, y = 620)
q5c = tk.Label(root_quizfive, text = 'works as a', **label_style)
q5c.place(x = 1560, y = 620)
q5c_entry = tk.Entry(root_quizfive, width = 4, **entry_style)
q5c_entry.place(x = 1680, y = 620)
q5d = tk.Label(root_quizfive, text = 'and is', **label_style)
q5d.place(x = 1740, y = 620)
q5d_entry = tk.Entry(root_quizfive, width = 4, **entry_style)
q5d_entry.place(x = 1810, y = 620)
q5e = tk.Label(root_quizfive, text = 'years old.', **label_style)
q5e.place(x = 1550, y = 660)
q5e_entry = tk.Entry(root_quizfive, width = 1, **entry_style)
q5e_entry.place(x = 1655, y = 660)
q5f = tk.Label(root_quizfive, text = ')', **label_style)
q5f.place(x = 1670, y = 660)

q5next = tk.Button(root_quizfive, text = 'Next', command = lambda: show_frame(root_quizsix), **topbutton_style).place(x = 1843, y = 429)
q5back = tk.Button(root_quizfive, text = 'Back', command = frame_back, **topbutton_style).place(x = 1678, y = 429)
q5restart = tk.Button(root_quizfive, text = 'Restart', command = restartq5, **topbutton_style).place(x = 1750, y = 429)

q5submit_button = tk.Button(root_quizfive, text = 'Submit', command = submitq5, **subbutton_style)
q5submit_button.place(x = 1565, y = 720)
hoverbutton_list.append(q5submit_button)
q5feedback = tk.Label(root_quizfive, **feedback_style)
q5feedback.place(x = 1150, y = 800)
q5result = tk.Label(root_quizfive, **label_style)
q5result.place(x = 1150, y = 835)

for i in [q5a_entry, q5b_entry, q5c_entry, q5d_entry, q5e_entry]:
    i.bind('<Return>', submitq5)

root_quizsix = tk.Frame(root_home)
framelist.append(root_quizsix)
q6_background = tk.PhotoImage(file = 'Images\\quiz_six.png')
q6_background_label = tk.Label(root_quizsix, image = q6_background)
q6_background_label.place(x = 0, y = 0)

q6a = tk.Label(root_quizsix, text = 'list =', **label_style)
q6a.place(x = 1150, y = 575)
q6a_entry = tk.Entry(root_quizsix, width = 1, **entry_style)
q6a_entry.place(x = 1215, y = 575)
q6b_entry = tk.Entry(root_quizsix, width = 20, **entry_style)
q6b_entry.place(x = 1232, y = 575)
q6b_entry.insert(0, "'item1' 'item2' 'item3'")
q6c_entry = tk.Entry(root_quizsix, width = 1, **entry_style)
q6c_entry.place(x = 1496, y = 575)
q6b = tk.Label(root_quizsix, text = 'list', **label_style)
q6b.place(x = 1150, y = 625)
q6d_entry = tk.Entry(root_quizsix, width = 2, **entry_style)
q6d_entry.place(x = 1186, y = 625)
q6d_entry.insert(0, '(1)')
q6c = tk.Label(root_quizsix, text = "=  'abc'", **label_style)
q6c.place(x = 1225, y = 625)
q6d = tk.Label(root_quizsix, text = 'print(', **label_style)
q6d.place(x = 1150, y = 675)
q6e_entry = tk.Entry(root_quizsix, width = 3, **entry_style)
q6e_entry.place(x = 1215, y = 677)
q6e = tk.Label(root_quizsix, text = '[0])', **label_style)
q6e.place(x = 1250, y = 675)
q6f = tk.Label(root_quizsix, text = 'print(list[', **label_style)
q6f.place(x = 1150, y = 725)
q6f_entry = tk.Entry(root_quizsix, width = 2, **entry_style)
q6f_entry.place(x = 1252, y = 727)
q6g = tk.Label(root_quizsix, text = '])', **label_style)
q6g.place(x = 1272, y = 725)

q6next = tk.Button(root_quizsix, text = 'Next', command = lambda: show_frame(root_quizseven), **topbutton_style).place(x = 1843, y = 429)
q6back = tk.Button(root_quizsix, text = 'Back', command = frame_back, **topbutton_style).place(x = 1678, y = 429)
q6restart = tk.Button(root_quizsix, text = 'Restart', command = restartq6, **topbutton_style).place(x = 1750, y = 429)

q6submit_button = tk.Button(root_quizsix, text = 'Submit', command = submitq6, **subbutton_style)
q6submit_button.place(x = 1350, y = 690)
hoverbutton_list.append(q6submit_button)
q6feedback = tk.Label(root_quizsix, **feedback_style)
q6feedback.place(x = 1150, y = 780)
q6result = tk.Label(root_quizsix, **label_style)
q6result.place(x = 1150, y = 815)

for i in [q6a_entry, q6b_entry, q6c_entry, q6d_entry, q6f_entry]:
    i.bind('<Return>', submitq6)

root_quizseven = tk.Frame(root_home)
framelist.append(root_quizseven)
q7_background = tk.PhotoImage(file = 'Images\\quiz_seven.png')
q7_background_label = tk.Label(root_quizseven, image = q7_background)
q7_background_label.place(x = 0, y = 0)

q7a = tk.Label(root_quizseven, text = 'while', **label_style)
q7a.place(x = 1150, y = 600)
q7a_entry = tk.Entry(root_quizseven, width =  4, **entry_style)
q7a_entry.place(x = 1220, y = 600)
q7b = tk.Label(root_quizseven, text = 'if x', **label_style)
q7b.place(x = 1200, y = 640)
q7b_entry = tk.Entry(root_quizseven, width = 1, **entry_style)
q7b_entry.place(x = 1245, y = 642)
q7c = tk.Label(root_quizseven, text = '10:', **label_style)
q7c.place(x = 1265, y = 640)
q7c_entry = tk.Entry(root_quizseven, width = 7, **entry_style)
q7c_entry.place(x = 1245, y = 680)
q7d = tk.Label(root_quizseven, text = 'else:', **label_style)
q7d.place(x = 1200, y = 720)
q7e = tk.Label(root_quizseven, text = 'print', **label_style)
q7e.place(x = 1245, y = 760)
q7d_entry = tk.Entry(root_quizseven, width = 10, **entry_style)
q7d_entry.place(x = 1305, y = 760)
q7d_entry.insert(0, "('{x} >= 10')")
q7e_entry = tk.Entry(root_quizseven, width = 5, **entry_style)
q7e_entry.place(x = 1245, y = 800)

q7next = tk.Button(root_quizseven, text = 'Next', command = lambda: show_frame(root_quizeight), **topbutton_style).place(x = 1843, y = 429)
q7back = tk.Button(root_quizseven, text = 'Back', command = frame_back, **topbutton_style).place(x = 1678, y = 429)
q7restart = tk.Button(root_quizseven, text = 'Restart', command = restartq7, **topbutton_style).place(x = 1750, y = 429)

q7submit_button = tk.Button(root_quizseven, text = 'Submit', command = submitq7, **subbutton_style)
q7submit_button.place(x = 1510, y = 690)
hoverbutton_list.append(q7submit_button)
q7feedback = tk.Label(root_quizseven, **feedback_style)
q7feedback.place(x = 1150, y = 880)
q7result = tk.Label(root_quizseven, **label_style)
q7result.place(x = 1150, y = 915)

for i in [q7a_entry, q7b_entry, q7c_entry, q7d_entry, q7e_entry]:
    i.bind('<Return>', submitq7)

root_quizeight = tk.Frame(root_home)
framelist.append(root_quizeight)
q8_background = tk.PhotoImage(file = 'Images\\quiz_eight.png')
q8_background_label = tk.Label(root_quizeight, image = q8_background)
q8_background_label.place(x = 0, y = 0)

q8a_entry = tk.Entry(root_quizeight, width = 6, **entry_style)
q8a_entry.place(x = 1150, y = 610)
q8a = tk.Label(root_quizeight, text = '=', **label_style)
q8a.place(x = 1250, y = 610)
q8b_entry = tk.Entry(root_quizeight, width = 5, **entry_style)
q8b_entry.place(x = 1293, y = 610)
q8b = tk.Label(root_quizeight, text = "('Pick a word: ')", **label_style)
q8b.place(x = 1355, y = 607)
q8c_entry = tk.Entry(root_quizeight, width = 11, **entry_style)
q8c_entry.place(x = 1150, y = 660)
q8c = tk.Label(root_quizeight, text = 'if', **label_style)
q8c.place(x = 1200, y = 710)
q8d_entry = tk.Entry(root_quizeight, width = 8, **entry_style)
q8d_entry.place(x = 1230, y = 710)
q8d = tk.Label(root_quizeight, text = "in ['a', 'e', 'i', 'o', 'u']:", **label_style)
q8d.place(x = 1340, y = 710)
q8e = tk.Label(root_quizeight, text = "print('This word starts with a vowel.')", **label_style)
q8e.place(x = 1250, y = 755)
q8f = tk.Label(root_quizeight, text = 'else:', **label_style)
q8f.place(x = 1200, y = 805)
q8g = tk.Label(root_quizeight, text = "print('This word does not start with a vowel.')", **label_style)
q8g.place(x = 1250, y = 850)

q8next = tk.Button(root_quizeight, text = 'Next', command = lambda: show_frame(root_quizzes), **topbutton_style).place(x = 1843, y = 429)
q8back = tk.Button(root_quizeight, text = 'Back', command = frame_back, **topbutton_style).place(x = 1678, y = 429)
q8restart = tk.Button(root_quizeight, text = 'Restart', command = restartq8, **topbutton_style).place(x = 1750, y = 429)

q8submit_button = tk.Button(root_quizeight, text = 'Submit', command = submitq8, **subbutton_style)
q8submit_button.place(x = 1600, y = 660)
hoverbutton_list.append(q8submit_button)
q8feedback = tk.Label(root_quizeight, **feedback_style)
q8feedback.place(x = 1150, y = 920)
q8result = tk.Label(root_quizeight, **label_style)
q8result.place(x = 1150, y = 955)

for i in [q8a_entry, q8b_entry, q8c_entry, q8d_entry]:
    i.bind('<Return>', submitq8)

root_guideone = tk.Frame(root_home)
framelist.append(root_guideone)
g1_background = tk.PhotoImage(file = 'Images\\guide_one.png')
g1_background_label = tk.Label(root_guideone, image = g1_background)
g1_background_label.place(x = 0, y = 0)

root_guidefive = tk.Frame(root_home)
framelist.append(root_guidefive)
g5_background = tk.PhotoImage(file = 'Images\\guide_five.png')
g5_background_label = tk.Label(root_guidefive, image = g5_background)
g5_background_label.place(x = 0, y = 0)

root_guides = tk.Frame(root_home)
framelist.append(root_guides)
guides_background = tk.PhotoImage(file = 'Images\\guides.png')
guides_background_label = tk.Label(root_guides, image = guides_background)
guides_background_label.place(x = 0, y = 0)

g1button = tk.Button(root_guides, text = 'G1', command = lambda: show_frame(root_guideone), **bigbutton_style)
g2button = tk.Button(root_guides, text = 'G2', command = lambda: show_frame(root_guides), **bigbutton_style)
g3button = tk.Button(root_guides, text = 'G3', command = lambda: show_frame(root_guides), **bigbutton_style)
g4button = tk.Button(root_guides, text = 'G4', command = lambda: show_frame(root_guides), **bigbutton_style)
g5button = tk.Button(root_guides, text = 'G5', command = lambda: show_frame(root_guidefive), **bigbutton_style)
g1button.place(x = 450, y = 415)
g2button.place(x = 678, y = 415)
g3button.place(x = 905, y = 415)
g4button.place(x = 1133, y = 415)
g5button.place(x = 1360, y = 415)
hoverbutton_list.extend([g1button, g2button, g3button, g4button, g5button])
guidesback = tk.Button(root_guides, text = 'Back', command = back_home).place(x = 50, y = 100)

root_quizzes = tk.Frame(root_home)
framelist.append(root_quizzes)
quizzes_background = tk.PhotoImage(file = 'Images\\quizzes.png')
quizzes_background_label = tk.Label(root_quizzes, image = quizzes_background)
quizzes_background_label.place(x = 0, y = 0)

q1button = tk.Button(root_quizzes, text = 'Q1', command = lambda: show_frame(root_quizone), **bigbutton_style)
q2button = tk.Button(root_quizzes, text = 'Q2', command = lambda: show_frame(root_quiztwo), **bigbutton_style)
q3button = tk.Button(root_quizzes, text = 'Q3', command = lambda: show_frame(root_quizthree), **bigbutton_style)
q4button = tk.Button(root_quizzes, text = 'Q4', command = lambda: show_frame(root_quizfour), **bigbutton_style)
q5button = tk.Button(root_quizzes, text = 'Q5', command = lambda: show_frame(root_quizfive), **bigbutton_style)
q6button = tk.Button(root_quizzes, text = 'Q6', command = lambda: show_frame(root_quizsix), **bigbutton_style)
q7button = tk.Button(root_quizzes, text = 'Q7', command = lambda: show_frame(root_quizseven), **bigbutton_style)
q8button = tk.Button(root_quizzes, text = 'Q8', command = lambda: show_frame(root_quizeight), **bigbutton_style)
q1button.place(x = 450, y = 415)
q2button.place(x = 678, y = 415)
q3button.place(x = 905, y = 415)
q4button.place(x = 1133, y = 415)
q5button.place(x = 1360, y = 415)
q6button.place(x = 450, y = 615)
q7button.place(x = 678, y = 615)
q8button.place(x = 905, y = 615)
hoverbutton_list.extend([q1button, q2button, q3button, q4button, q5button, q6button, q7button, q8button])
quizzesback = tk.Button(root_quizzes, text = 'Back', command = back_home).place(x = 50, y = 100)

background = tk.PhotoImage(file = 'Images\\home_page.png')
background_label = tk.Label(root_home, image = background)
background_label.place(x = 0, y = 0)

quiz_button_img = tk.PhotoImage(file = 'Images\\quizzes_button.png')
quiz_button_label = tk.Label(root_home, image = quiz_button_img)
quiz_button = tk.Button(root_home, image = quiz_button_img, command = lambda: show_frame(root_quizzes), bg = '#0277bc', bd = 0, activebackground = '#0277bc')
quiz_button_label, quiz_button.place(anchor = 'center', x = 960, y = 670)

guides_button_img = tk.PhotoImage(file = 'Images\\guides_button.png')
guides_button_label = tk.Label(root_home, image = guides_button_img)
guides_button = tk.Button(root_home, image = guides_button_img, command = lambda: show_frame(root_guides), bg = '#0277bc', bd = 0, activebackground = '#0277bc')
guides_button_label, guides_button.place(anchor = 'center', x = 960, y = 910)

loadframes()
loadbutton()

root_home.mainloop()