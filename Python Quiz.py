import ctypes
import tkinter as tk
from tkinter.font import Font
import sys

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Creates the main window of the app and specifies the dimensions and icon image.
root_home = tk.Tk()
root_home.title('Python Quiz')
root_home.geometry("1920x1080")
root_home.resizable(False, False)
root_home.iconphoto(True, tk.PhotoImage(file = 'Images/python_icon.png'))
screen_width = root_home.winfo_screenwidth()
screen_height = root_home.winfo_screenheight()
# Finds screen dimensions and uses that to find a scale for the fonts.

# If the screen dimensions match the app, it goes into fullscreen.
if screen_width == 1920 and screen_height == 1080:
    root_home.state('zoomed')
    root_home.attributes('-fullscreen', True)

# Initialises a variety of lists used for different functions in the app.
framelist = []
help_framelist = []
hoverbutton_list = []
rhoverbutton_list = []
quit_hoverlist = []

# Dictionary which is used to make the help button toggle on and off.
open_close = {'q1help': False, 'q2help': False, 'q3help': False, 'q4help': False, 'q5help': False, 'q6help': False, 'q7help': False, 'q8help': False, 'q9help': False}
helpframe_codelist = ['q1help', 'q2help', 'q3help', 'q4help', 'q5help', 'q6help', 'q7help', 'q8help', 'q9help']
# Codelist which aligns with help_framelist to match each help frame to its code.

# Functions below do as stated in the function name.
def loadframes():
    for frame in framelist:
        frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        frame.lower()
    quit_button_frame.tkraise()

# Frames cleared to reveal the original window and then reloaded so they can be shown again if requested.
def back_home():
    for frame in framelist:
        frame.lower()
    for frame in help_framelist:
        frame.lower()  

def show_frame(frame):
    frame.tkraise()
    quit_button_frame.tkraise()

# Uses the open_close dictionary so the same button can both open and close the frame.
def show_help(help_frame):
    if open_close[helpframe_codelist[help_framelist.index(help_frame)]]:
        open_close[helpframe_codelist[help_framelist.index(help_frame)]] = False
        help_frame.lower()
    else:
        open_close[helpframe_codelist[help_framelist.index(help_frame)]] = True
        help_frame.tkraise()
        
def close_help(help_frame):
    open_close[helpframe_codelist[help_framelist.index(help_frame)]] = False
    help_frame.lower()

def quiz_to_guide(guide_root, help_frame):
    show_frame(guide_root)
    close_help(help_frame)

def load_helpframes():
    for frame in help_framelist:
        frame.place(x = 1015, y = 350)
        close_help(frame)

# Used for hover effects, 4 variations for opposite colours schemes and then the quit and home page buttons.
def on_enter(event):
    if event.widget['state'] == 'normal':
        event.widget.config(background = '#275b84', foreground = '#ffde57')

def ron_enter(event):
    event.widget.config(background = '#ffde57', foreground = '#275b84')

def on_leave(event):
    event.widget.config(background = '#ffde57', foreground = '#275b84')

def ron_leave(event):
    event.widget.config(background = '#275b84', foreground = '#ffde57')

def quit_enter(event):
    event.widget.config(background = '#ffffff', foreground = '#e81123')

def quit_leave(event):
    event.widget.config(background = '#e81123', foreground = '#ffffff')

def image_enter(event):
    if event.widget['font'] == str(segoe_s):
        event.widget.config(image = altquiz_button_img)
    else:
        event.widget.config(image = altguides_button_img)

def image_leave(event):
    if event.widget['font'] == str(segoe_b):
        event.widget.config(image = guides_button_img)
    else:
        event.widget.config(image = quiz_button_img)

# Binds each button I added to the hoverbutton_list to the hover effects.
def loadbutton():
    for button in hoverbutton_list:
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
    for button in rhoverbutton_list:
        button.bind('<Enter>', ron_enter)
        button.bind('<Leave>', ron_leave)
    for button in quit_hoverlist:
        button.bind('<Enter>', quit_enter)
        button.bind('<Leave>', quit_leave)

# Get actual system DPI (96 = 100%, 120 = 125%, etc.)
dc = ctypes.windll.user32.GetDC(0)
dpi = ctypes.windll.gdi32.GetDeviceCaps(dc, 88)
ctypes.windll.user32.ReleaseDC(0, dc)

# Calculate DPI scale factor
dpi_scale = dpi / 96

# Calculates the font scale.
def font_scale(size):
    return int(size / dpi_scale)

# Checks if the user has unlocked the final quiz or not based on the other quiz results.
def final_unlocked():
    if q1correct and q2correct and q3correct and q4correct and q5correct and q6correct and q7correct and q8correct and q9correct:
        q10button.config(state = 'normal', text = '🔓')
        g10quiz_button.config(state = 'normal')
        q9next.config(state = 'normal')

# Defines font variables used for consistent styling.
segoe_b = Font(family = 'Segoe UI Variable Text Semibold', size = font_scale(17.5))
segoe_s = Font(family = 'Segoe UI Variable Text Semibold', size = font_scale(15))
segoe_bo = Font(family = 'Segoe UI Variable Text', size = font_scale(18.75), weight = 'bold')
rockwell_b = Font(family = 'Rockwell', size = font_scale(37.5), weight = 'bold')

# Defines styles for the various widgets.
label_style = {'font': segoe_b, 'background': '#0277bc', 'foreground': '#ffffff', 'wraplength': '740'}
entry_style = {'font': segoe_b, 'background': '#275b84', 'disabledbackground': '#275b84', 'foreground': '#ffffff', 'borderwidth': 0}
feedback_style = {'font': segoe_bo, 'bg': '#0277bc', 'fg': '#ffde57'}
textbox_style = {'font': segoe_b, 'background': '#275b84', 'foreground': '#ffffff', 'borderwidth': 0}
subbutton_style = {'font': segoe_bo, 'background': '#ffde57', 'foreground': '#275b84', 'borderwidth': 0, 'activebackground': '#275b84', 'activeforeground': '#ffde57'}
topbutton_style = {'font': segoe_s, 'background': '#ffde57', 'foreground': '#275b84', 'activebackground': '#275b84', 'activeforeground': '#ffde57', 'borderwidth': 0}
bigbutton_style = {'font': rockwell_b, 'background': '#ffde57', 'foreground': '#275b84', 'borderwidth': 0, 'activebackground': '#275b84', 'activeforeground': '#ffde57'}

#Initialising the global variables used in each submit function to check if it's been completed (see below).
q1correct = False
q2correct = False
q3correct = False
q4correct = False
q5correct = False
q6correct = False
q7correct = False
q8correct = False
q9correct = False

# Other global variables, both so that they can be changed outside their main functions.
q2guessed_operations = set()
course_passed = "Congratulations, you've successfully completed this quiz and the entire Python course. Well done!"

# The following functions are submit and restart functions for every quiz (10 in total).
# Submit functions get the user inputs from entries, checks for mistakes, and gives feedback based on those mistakes.
# Restart functions clear entries / labels and reactivates the entries and buttons disabled when the question is answered correctly.
# The submit functions have the paramater 'x = None' because when binded to a key an argument is given which needs to be voided.

def submitq1(x = None):
    global q1correct
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
            q1correct = True
            q1result.config(text = 'All four data types were correctly matched and printed!')
            q1submit_button.config(state = 'disabled')
            q1a1_entry.config(state = 'disabled')
            q1a2_entry.config(state = 'disabled')
            q1a3_entry.config(state = 'disabled')
            q1a4_entry.config(state = 'disabled')
            q1b_entry.config(state = 'disabled')
        else:
            if 'hello' in q1b_v or "'hello'" in q1b_v or '"hello"' in q1b_v or '15' in q1b_v or '3.14' in q1b_v or 'False' in q1b_v:
                q1result.config(text = "Print the variable names, not the values. E.g string instead of 'hello'.")
            else:
                q1result.config(text = 'Your data types are correctly matched, but check your print statement and remember commas!')
    else:
        if correct_no == 1:
            q1result.config(text = '1/4 data type is correct.')
        else:
            q1result.config(text = f'{correct_no}/4 data types are correct.')
    final_unlocked()
    print(sys.getsizeof(q1a1_v))

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

def submitq2(x = None):
    global q2correct
    global q2guessed_operations

    q2feedback.config(text = 'Feedback & Output:')
    q2a_v = q2a_entry.get() 
    q2b_v = q2b_entry.get()

    q2guess = f"{q2a_v}(x {q2b_v} y)"
    q2correct_ans = ['print(x + y)', 'print(x - y)', 'print(x * y)', 'print(x / y)']
    if q2guess not in q2correct_ans:
        if 'print' != q2a_v.lower() and q2b_v not in ['+', '-', '*', '/']:
            incorrect_message = 'Use the print function to display and the operations (+, -, *, /) to calculate.'
        elif 'print' == q2a_v.lower() and q2b_v not in ['+', '-', '*', '/']:
            incorrect_message = 'The print function is correctly used, however use the operations (+, -, *, /) to calculate.'
        elif 'print' != q2a_v.lower() and q2b_v  in ['+', '-', '*', '/']:
            incorrect_message = 'You are correctly using an operation, however the print function is needed to display the result.'
        else:
            incorrect_message = "Make sure the 'print()' function is lowercase."
        q2result.config(text = incorrect_message)
    else:
        q2guessed_operations.add(q2b_v)
        q2result.config(text = f'10 {q2b_v} 5 = ' + str(round(eval(f'10 {q2b_v} 5'))))
        if {'+', '-', '*', '/'}.issubset(q2guessed_operations):
            q2correct = True
            q2f_result.config(text = 'That is all four operations correctly used. Congratulations!')
            q2submit_button.config(state = 'disabled') 
            q2a_entry.config(state = 'disabled')
            q2b_entry.config(state = 'disabled')
    final_unlocked()

def restartq2():

    q2submit_button.config(state = 'normal')
    q2a_entry.config(state = 'normal')
    q2b_entry.config(state = 'normal')
    q2a_entry.delete(0, 'end')
    q2b_entry.delete(0, 'end')  
    q2feedback.config(text = '')
    q2result.config(text = '')
    q2f_result.config(text = '')
    q2guessed_operations.clear()

def submitq3(x = None):
    global q3correct
    q3feedback.config(text = 'Feedback:')

    q3a_v = q3a_entry.get()
    q3b_v = q3b_entry.get()
    q3c_v = (q3c_entry.get()).replace(' ','').replace('(', '').replace(')', '')
    q3d_v = q3d_entry.get()
    q3e_v = (q3e_entry.get()).replace(' ','').replace('(', '').replace(')', '')
    
    if q3a_v == 'if' and q3b_v == '>' and q3c_v in ['x*y', 'y*x'] and q3d_v == 'else:' and q3e_v in ['x+y', 'y+x']:
        q3correct = True
        message = 'Perfect! This program will print 50 as 10 * 5 is greater than 30.'
        q3submit_button.config(state = 'disabled')
        q3a_entry.config(state = 'disabled')
        q3b_entry.config(state = 'disabled')
        q3c_entry.config(state = 'disabled')
        q3d_entry.config(state = 'disabled')
        q3e_entry.config(state = 'disabled')
    else:
        if q3a_v != 'if' or 'else' not in q3d_v:
            message = "If-Else statements require lowercase 'if' and 'else'."
        elif 'else' in q3d_v and q3d_v != 'else:':
            message = 'Colons (:) must be used after each if-else statement.'
        elif q3b_v != '>':
            message = "To check if a number is greater than another, the '>' symbol is used."
        elif q3c_v not in ['x*y', 'y*x']:
            message = 'To print the product (x * y) place it inside the print statement.'
        elif q3e_v not in ['x+y', 'y+x']:
            message = 'The sum is equal to (x + y), place it inside the print statement to display.'
        else:
            message = 'Incorrect.'
    q3result.config(text = message)
    final_unlocked()

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

def submitq4(x = None):
    global q4correct
    q4feedback.config(text = 'Feedback')

    q4a_v = q4a_entry.get()
    q4b_v = q4b_entry.get().replace('"', "'")
    q4c_v = q4c_entry.get()
    q4d_v = q4d_entry.get()
    
    if q4a_v == q4c_v != '' and q4b_v == "input('Are you enjoying this course?')" and q4d_v == 'else:':
        q4correct = True
        message = 'Correct! inpt -> input, the inside of your input function is a string, your else is lowercase with a colon, and your variable names match.'
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
    final_unlocked()
    
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

def submitq5(x = None):
    global q5correct
    q5feedback.config(text = 'Feedback:')

    q5a_v = q5a_entry.get()
    q5b_v = q5b_entry.get()
    q5c_v = q5c_entry.get()
    q5d_v = q5d_entry.get()
    q5e_v = q5e_entry.get()
    
    q5guess = f"{q5a_v}{q5b_v} works as a {q5c_v} and is {q5d_v} years old.{q5e_v}"
    q5expected = "f'{name} works as a {job} and is {age} years old.'"

    if q5guess == q5expected:
        q5correct = True
        message = 'Correct! f strings and curly brackets are used to display variables in a string.'
        q5submit_button.config(state = 'disabled')
        q5a_entry.config(state = 'disabled')
        q5b_entry.config(state = 'disabled')
        q5c_entry.config(state = 'disabled')
        q5d_entry.config(state = 'disabled')
        q5e_entry.config(state = 'disabled')
    else:
        if 'john' in q5guess.lower() or 'lawyer' in q5guess.lower() or '34' in q5guess:
            message = "Instead of putting the specific name/job/age we should put the variable names instead. E.g: {name} instead of John."
        elif "f'" in q5guess and '{' not in q5guess:
            message = "You are correct in using an f string but the variables should be inside curly brackets."
        elif '{' in q5guess and "f'" not in q5guess:
            message = "The variables are correctly placed in curly brackets. However, to have variables inside a string, an f string (f') must be used."
        elif "'" in q5guess and "f'" not in q5guess:
            message = "Remember to use an f string (f') when including variables within the string."
        elif "f'" in q5guess and '{' in q5guess:
            message = 'Check to make sure your sentence makes sense.'
        else:
            message = 'Use f-strings and curly brackets to embed variables within a string.'
    q5result.config(text = message)
    final_unlocked()

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

def submitq6(x = None):
    global q6correct
    q6feedback.config(text = 'Feedback:')

    q6a_v = q6a_entry.get()
    q6b_v = q6b_entry.get().replace(' ','')
    q6c_v = q6c_entry.get()
    q6d_v = q6d_entry.get()
    q6e_v = q6e_entry.get()
    q6f_v = q6f_entry.get()

    if q6a_v == '[' and q6b_v in ["'item1','item2','item3'", '"item1","item2","item3"'] and q6c_v == ']' and q6d_v == '[0]' and q6e_v == 'list' and q6f_v in ['-1', '2']:
        q6correct = True
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
        message = 'The last item can be accessed through an index of -1, or 2 since there are 3 items.'
    else:
        message = 'Incorrect.'

    q6result.config(text = message)
    final_unlocked()

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

def submitq7(x = None):
    global q7correct
    q7feedback.config(text = 'Feedback:')

    q7a_v = q7a_entry.get()
    q7b_v = q7b_entry.get()
    q7c_v = q7c_entry.get().replace(' ', '')
    q7d_v = q7d_entry.get().replace(' ', '')
    q7e_v = q7e_entry.get()

    if q7a_v == 'True:' and q7b_v == '<' and q7c_v in ['x=x+1', 'x+=1'] and q7d_v in ["(f'{x}>=10')", '(f"{x}>=10")'] and q7e_v == 'break':
        q7correct = True
        message = "Correct! This program will keep adding to x until it's greater than or equal to ten."
        q7submit_button.config(state = 'disabled')
        q7a_entry.config(state = 'disabled')
        q7b_entry.config(state = 'disabled')
        q7c_entry.config(state = 'disabled')
        q7d_entry.config(state = 'disabled')
        q7e_entry.config(state = 'disabled')
    elif 'True' in q7a_v and ':' not in q7a_v:
        message = "You're using the correct keyword 'True', however a colon is needed at the end."
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
    final_unlocked()

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

def submitq8(x = None):
    global q8correct
    q8feedback.config(text = 'Feedback:')

    q8a_v = q8a_entry.get()
    q8b_v = q8b_entry.get()
    q8c_v = q8c_entry.get()
    q8d_v = q8d_entry.get()
    
    if q8a_v in q8c_v and q8a_v in q8d_v and q8b_v == 'input' and 'for' in q8c_v and f'in {q8a_v}:' in q8c_v and q8d_v == f'{q8a_v}[0]':
        q8correct = True
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
    final_unlocked()

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

def submitq9(x = None):
    global q9correct
    q9feedback.config(text = 'Feedback:')

    q9a_v = q9a_entry.get()
    q9b_v = q9b_entry.get()
    q9c_v = q9c_entry.get()
    q9d_v = q9d_entry.get()
    q9e_v = q9e_entry.get()
    q9f_v = q9f_entry.get()
    try:
        if q9a_v == 'def' and q9b_v[0] == '(' and q9b_v[-1] == ')' and q9c_v in q9b_v and q9c_v != '' and q9d_v == 'return' and q9e_v == 'False' and 'print' in q9f_v and 'check_even' in q9f_v and q9f_v.count('(') == 2 and q9f_v.count(')') == 2 and q9f_v[q9f_v.index('))')-1] != '(':
            q9correct = True
            message = 'Correct. The check_even function is correctly defined and called.'
            q9submit_button.config(state = 'disabled')
            q9a_entry.config(state = 'disabled')
            q9b_entry.config(state = 'disabled')
            q9c_entry.config(state = 'disabled')
            q9d_entry.config(state = 'disabled')
            q9e_entry.config(state = 'disabled')
            q9f_entry.config(state = 'disabled')
    except: pass
    if q9a_v != 'def':
        message = "To begin defining a function use 'def'."
    elif q9c_v not in q9b_v or q9c_v == '':
        message = 'Variable / parameter names do not match or are empty.'
    elif q9b_v[0] != '(' or q9b_v[-1] != ')':
        message = 'Make sure your parameter is placed within brackets.'
    elif q9d_v != 'return':
        message = "To receive an output from a function, an all lowercase 'return' is used."
    elif q9e_v != 'False':
        message = "If the number isn't even, the function should return False."
    elif 'print' not in q9f_v:
        message = 'To display the output, the print function is still needed.'
    elif 'check_even' not in q9f_v:
        message = "To call the function use its name (check_even)."
    elif q9f_v.count('(') != 2 or q9f_v.count(')') != 2 or '))' not in q9f_v:
        message = 'Check your brackets when displaying / calling the function.'
    elif q9f_v[q9f_v.index('))')-1] == '(':
        message = 'Make sure you gave the function an input (also called arguments).'
    q9result.config(text = message)
    final_unlocked()

def restartq9():
    q9submit_button.config(state = 'normal')
    q9a_entry.config(state = 'normal')
    q9b_entry.config(state = 'normal')
    q9c_entry.config(state = 'normal')
    q9d_entry.config(state = 'normal')
    q9e_entry.config(state = 'normal')
    q9f_entry.config(state = 'normal')
    q9a_entry.delete(0, 'end')
    q9b_entry.delete(0, 'end')
    q9c_entry.delete(0, 'end')
    q9d_entry.delete(0, 'end')
    q9e_entry.delete(0, 'end')
    q9f_entry.delete(0, 'end')
    q9b_entry.insert(0, '()')
    q9feedback.config(text = '')
    q9result.config(text = '')

def submitq10():
    global course_passed
    q10feedback.config(text = 'Feedback:')
    passed_cases = 0
    submission = q10_entry.get("1.0", "end-1c")

    variable_store = {}

    try:
        exec(submission, variable_store)
        calculator = variable_store.get("calculator")

        if callable(calculator):
            test1 = calculator(6, 1, '+')
            test2 = calculator(5, 3, '-')
            test3 = calculator(4, 7, '*')
            test4 = calculator(8, 2, '/')

            if test1 == 7: passed_cases += 1
            if test2 == 2: passed_cases += 1
            if test3 == 28: passed_cases += 1
            if test4 == 4: passed_cases += 1

            if passed_cases == 4:
                message = course_passed
                course_passed = 'The function is successful and passes all cases.'
                q10submit_button.config(state = 'disabled')
                q10_entry.config(foreground = 'grey', state = 'disabled')
            else:
                message = f'{passed_cases}/4 cases passed.'
        else:
            message = "The calculator function was not found or not defined correctly."

    except Exception as e:
        message = f"Error: {e}"

    q10result.config(text = message)

def restartq10():
    q10submit_button.config(state = 'normal')
    q10_entry.config(state = 'normal')
    q10_entry.delete("1.0", "end")
    q10feedback.config(text = '')
    q10result.config(text = '')

# The quit button, made to be on top of any frame (which is made sure of by the functions at the start).
quit_button_frame = tk.Frame(root_home, width = 50, height = 50, bg = '#e81123')
quit_button_frame.place(relx = 0.99, rely = 0.01, anchor = 'ne')
quit_button = tk.Button(quit_button_frame, text = '❌', command = lambda: root_home.destroy(), width = 5, font  = segoe_bo, background = '#e81123', foreground = '#ffffff', borderwidth = 0)
quit_button.place(relx = 0.5, rely = 0.5, anchor = 'center')
quit_hoverlist.append(quit_button)

# Each quiz has the same main components. 
# The question widgets, which are the entries and labels making up the actual question.
# The submit, restart, back, and next buttons. Each activates their respective function above.
# There are also the feedback and result labels which are used to display messages based on user input and errors.
# Then every entry is binded to the Enter key so it can be used to submit.

# Each quiz has a help button (except the final one) which can take the user to the corresponding guide which teaches the skills needed for the quiz.

# Frame for quiz one which all entries, labels, and buttons are placed upon.
root_quizone = tk.Frame(root_home)
framelist.append(root_quizone)
q1_background = tk.PhotoImage(file = 'Images/quiz_one.png')
q1_background_label = tk.Label(root_quizone, image = q1_background)
q1_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

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

# These buttons are in every quiz, to submit, restart, and go to the next or previous quiz.
q1menu = tk.Button(root_quizone, text = 'Menu', command = lambda: show_frame(root_quizzes), **topbutton_style)
q1menu.place(x = 1160, y = 429)
q1next = tk.Button(root_quizone, text = 'Next', command = lambda: show_frame(root_quiztwo), **topbutton_style)
q1next.place(x = 1843, y = 429)
q1restart = tk.Button(root_quizone, text = 'Restart', command = restartq1, **topbutton_style)
q1restart.place(x = 1750, y = 429)
q1submit_button = tk.Button(root_quizone, text = 'Submit', command = submitq1, **subbutton_style)
q1submit_button.place(x = 1650, y = 765)
hoverbutton_list.extend([q1menu, q1next, q1restart, q1submit_button])

# Binds each entry to the submit function, meaning pressing Enter submits.
for i in [q1a1_entry, q1a2_entry, q1a3_entry, q1a4_entry, q1b_entry]:
    i.bind('<Return>', submitq1)

# Frame for quiz two.
root_quiztwo = tk.Frame(root_home)
framelist.append(root_quiztwo)
q2_background = tk.PhotoImage(file = 'Images/quiz_two.png')
q2_background_label = tk.Label(root_quiztwo, image = q2_background)
q2_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

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
q2feedback = tk.Label(root_quiztwo, **feedback_style)
q2feedback.place(x = 1150, y = 745)
q2result = tk.Label(root_quiztwo, **label_style)
q2result.place(x = 1150, y = 775)
q2f_result = tk.Label(root_quiztwo, **label_style)
q2f_result.place(x = 1150, y = 825)

q2menu = tk.Button(root_quiztwo, text = 'Menu', command = lambda: show_frame(root_quizzes), **topbutton_style)
q2menu.place(x = 1160, y = 429)
q2back = tk.Button(root_quiztwo, text = 'Back', command = lambda: show_frame(root_quizone), **topbutton_style)
q2back.place(x = 1678, y = 429)
q2restart = tk.Button(root_quiztwo, text = 'Restart', command = restartq2, **topbutton_style)
q2restart.place(x = 1750, y = 429)
q2next = tk.Button(root_quiztwo, text = 'Next', command = lambda: show_frame(root_quizthree), **topbutton_style)
q2next.place(x = 1843, y = 429)
hoverbutton_list.extend([q2menu, q2back, q2next, q2restart, q2submit_button])

for i in [q2a_entry, q2b_entry]:
    i.bind('<Return>', submitq2)

# Frame for quiz three.
root_quizthree = tk.Frame(root_home, borderwidth=0, highlightthickness=0)
framelist.append(root_quizthree)
q3_background = tk.PhotoImage(file = 'Images/quiz_three.png')
q3_background_label = tk.Label(root_quizthree, image = q3_background)
q3_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

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
q3feedback = tk.Label(root_quizthree, **feedback_style)
q3feedback.place(x = 1150, y = 890)
q3result = tk.Label(root_quizthree, **label_style)
q3result.place(x = 1150, y = 925)

q3menu = tk.Button(root_quizthree, text = 'Menu', command = lambda: show_frame(root_quizzes), **topbutton_style)
q3menu.place(x = 1160, y = 429)
q3back = tk.Button(root_quizthree, text = 'Back', command = lambda: show_frame(root_quiztwo), **topbutton_style)
q3back.place(x = 1678, y = 429)
q3restart = tk.Button(root_quizthree, text = 'Restart', command = restartq3, **topbutton_style)
q3restart.place(x = 1750, y = 429)
q3next = tk.Button(root_quizthree, text = 'Next', command = lambda: show_frame(root_quizfour), **topbutton_style)
q3next.place(x = 1843, y = 429)
hoverbutton_list.extend([q3menu, q3back, q3next, q3restart, q3submit_button])

for i in [q3a_entry, q3b_entry, q3c_entry, q3d_entry, q3e_entry]:
    i.bind('<Return>', submitq3)

# Frame for quiz four.
root_quizfour = tk.Frame(root_home)
framelist.append(root_quizfour)
q4_background = tk.PhotoImage(file = 'Images/quiz_four.png')
q4_background_label = tk.Label(root_quizfour, image = q4_background)
q4_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

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

q4menu = tk.Button(root_quizfour, text = 'Menu', command = lambda: show_frame(root_quizzes), **topbutton_style)
q4menu.place(x = 1160, y = 429)
q4back = tk.Button(root_quizfour, text = 'Back', command = lambda: show_frame(root_quizthree), **topbutton_style)
q4back.place(x = 1678, y = 429)
q4restart = tk.Button(root_quizfour, text = 'Restart', command = restartq4, **topbutton_style)
q4restart.place(x = 1750, y = 429)
q4next = tk.Button(root_quizfour, text = 'Next', command = lambda: show_frame(root_quizfive), **topbutton_style)
q4next.place(x = 1843, y = 429)
hoverbutton_list.extend([q4menu, q4back, q4next, q4restart, q4submit_button])

q4feedback = tk.Label(root_quizfour, **feedback_style)
q4feedback.place(x = 1150, y = 850)
q4result = tk.Label(root_quizfour, **label_style)
q4result.place(x = 1150, y = 885)

for i in [q4a_entry, q4b_entry, q4c_entry, q4d_entry]:
    i.bind('<Return>', submitq4)

# Frame for quiz five.
root_quizfive = tk.Frame(root_home)
framelist.append(root_quizfive)
q5_background = tk.PhotoImage(file = 'Images/quiz_five.png')
q5_background_label = tk.Label(root_quizfive, image = q5_background)
q5_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

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

q5menu = tk.Button(root_quizfive, text = 'Menu', command = lambda: show_frame(root_quizzes), **topbutton_style)
q5menu.place(x = 1160, y = 429)
q5next = tk.Button(root_quizfive, text = 'Next', command = lambda: show_frame(root_quizsix), **topbutton_style)
q5next.place(x = 1843, y = 429)
q5back = tk.Button(root_quizfive, text = 'Back', command = lambda: show_frame(root_quizfour), **topbutton_style)
q5back.place(x = 1678, y = 429)
q5restart = tk.Button(root_quizfive, text = 'Restart', command = restartq5, **topbutton_style)
q5restart.place(x = 1750, y = 429)

q5submit_button = tk.Button(root_quizfive, text = 'Submit', command = submitq5, **subbutton_style)
q5submit_button.place(x = 1565, y = 720)
q5feedback = tk.Label(root_quizfive, **feedback_style)
q5feedback.place(x = 1150, y = 800)
q5result = tk.Label(root_quizfive, **label_style)
q5result.place(x = 1150, y = 835)
hoverbutton_list.extend([q5menu, q5back, q5next, q5restart, q5submit_button])

for i in [q5a_entry, q5b_entry, q5c_entry, q5d_entry, q5e_entry]:
    i.bind('<Return>', submitq5)

# Frame for quiz six.
root_quizsix = tk.Frame(root_home)
framelist.append(root_quizsix)
q6_background = tk.PhotoImage(file = 'Images/quiz_six.png')
q6_background_label = tk.Label(root_quizsix, image = q6_background)
q6_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

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
q6d_entry = tk.Entry(root_quizsix, width = 3, **entry_style)
q6d_entry.place(x = 1186, y = 625)
q6d_entry.insert(0, '(1)')
q6c = tk.Label(root_quizsix, text = " =  'abc'", **label_style)
q6c.place(x = 1220, y = 625)
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

q6menu = tk.Button(root_quizsix, text = 'Menu', command = lambda: show_frame(root_quizzes), **topbutton_style)
q6menu.place(x = 1160, y = 429)
q6next = tk.Button(root_quizsix, text = 'Next', command = lambda: show_frame(root_quizseven), **topbutton_style)
q6next.place(x = 1843, y = 429)
q6back = tk.Button(root_quizsix, text = 'Back', command = lambda: show_frame(root_quizfive), **topbutton_style)
q6back.place(x = 1678, y = 429)
q6restart = tk.Button(root_quizsix, text = 'Restart', command = restartq6, **topbutton_style)
q6restart.place(x = 1750, y = 429)

q6submit_button = tk.Button(root_quizsix, text = 'Submit', command = submitq6, **subbutton_style)
q6submit_button.place(x = 1350, y = 690)
q6feedback = tk.Label(root_quizsix, **feedback_style)
q6feedback.place(x = 1150, y = 780)
q6result = tk.Label(root_quizsix, **label_style)
q6result.place(x = 1150, y = 815)
hoverbutton_list.extend([q6menu, q6back, q6next, q6restart, q6submit_button])

for i in [q6a_entry, q6b_entry, q6c_entry, q6d_entry, q6e_entry, q6f_entry]:
    i.bind('<Return>', submitq6)

# Frame for quiz seven.
root_quizseven = tk.Frame(root_home)
framelist.append(root_quizseven)
q7_background = tk.PhotoImage(file = 'Images/quiz_seven.png')
q7_background_label = tk.Label(root_quizseven, image = q7_background)
q7_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

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

q7menu = tk.Button(root_quizseven, text = 'Menu', command = lambda: show_frame(root_quizzes), **topbutton_style)
q7menu.place(x = 1160, y = 429)
q7next = tk.Button(root_quizseven, text = 'Next', command = lambda: show_frame(root_quizeight), **topbutton_style)
q7next.place(x = 1843, y = 429)
q7back = tk.Button(root_quizseven, text = 'Back', command = lambda: show_frame(root_quizsix), **topbutton_style)
q7back.place(x = 1678, y = 429)
q7restart = tk.Button(root_quizseven, text = 'Restart', command = restartq7, **topbutton_style)
q7restart.place(x = 1750, y = 429)

q7submit_button = tk.Button(root_quizseven, text = 'Submit', command = submitq7, **subbutton_style)
q7submit_button.place(x = 1510, y = 690)
q7feedback = tk.Label(root_quizseven, **feedback_style)
q7feedback.place(x = 1150, y = 880)
q7result = tk.Label(root_quizseven, **label_style)
q7result.place(x = 1150, y = 915)
hoverbutton_list.extend([q7menu, q7back, q7next, q7restart, q7submit_button])

for i in [q7a_entry, q7b_entry, q7c_entry, q7d_entry, q7e_entry]:
    i.bind('<Return>', submitq7)

# Frame for quiz eight.
root_quizeight = tk.Frame(root_home)
framelist.append(root_quizeight)
q8_background = tk.PhotoImage(file = 'Images/quiz_eight.png')
q8_background_label = tk.Label(root_quizeight, image = q8_background)
q8_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

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

q8menu = tk.Button(root_quizeight, text = 'Menu', command = lambda: show_frame(root_quizzes), **topbutton_style)
q8menu.place(x = 1160, y = 429)
q8next = tk.Button(root_quizeight, text = 'Next', command = lambda: show_frame(root_quiznine), **topbutton_style)
q8next.place(x = 1843, y = 429)
q8back = tk.Button(root_quizeight, text = 'Back', command = lambda: show_frame(root_quizseven), **topbutton_style)
q8back.place(x = 1678, y = 429)
q8restart = tk.Button(root_quizeight, text = 'Restart', command = restartq8, **topbutton_style)
q8restart.place(x = 1750, y = 429)

q8submit_button = tk.Button(root_quizeight, text = 'Submit', command = submitq8, **subbutton_style)
q8submit_button.place(x = 1600, y = 660)
q8feedback = tk.Label(root_quizeight, **feedback_style)
q8feedback.place(x = 1150, y = 920)
q8result = tk.Label(root_quizeight, **label_style)
q8result.place(x = 1150, y = 955)
hoverbutton_list.extend([q8menu, q8back, q8next, q8restart, q8submit_button])

for i in [q8a_entry, q8b_entry, q8c_entry, q8d_entry]:
    i.bind('<Return>', submitq8)

# Frame for quiz nine.
root_quiznine = tk.Frame(root_home)
framelist.append(root_quiznine)
q9_background = tk.PhotoImage(file = 'Images/quiz_nine.png')
q9_background_label = tk.Label(root_quiznine, image = q9_background)
q9_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

q9a_entry = tk.Entry(root_quiznine, width = 3, **entry_style)
q9a_entry.place(x = 1150, y = 600)
q9a = tk.Label(root_quiznine, text = 'check_even', **label_style)
q9a.place(x = 1210, y = 600)
q9b_entry = tk.Entry(root_quiznine, width = 7, **entry_style)
q9b_entry.place(x = 1335, y = 600)
q9b_entry.insert(0, '()')
q9b = tk.Label(root_quiznine, text = 'if', **label_style)
q9b.place(x = 1200, y = 650)
q9c_entry = tk.Entry(root_quiznine, width = 6, **entry_style)
q9c_entry.place(x = 1230, y = 650)
q9c = tk.Label(root_quiznine, text = '% 2 == 0:', **label_style)
q9c.place(x = 1315, y = 650)
q9d_entry = tk.Entry(root_quiznine, width = 5, **entry_style)
q9d_entry.place(x = 1250, y = 700)
q9d = tk.Label(root_quiznine, text = 'True', **label_style)
q9d.place(x = 1325, y = 700)
q9e = tk.Label(root_quiznine, text = 'else:', **label_style)
q9e.place(x = 1200, y = 750)
q9f = tk.Label(root_quiznine, text = 'return', **label_style)
q9f.place(x = 1250, y = 790)
q9e_entry = tk.Entry(root_quiznine, width = 4, **entry_style)
q9e_entry.place(x = 1325, y = 790)
q9f_entry = tk.Entry(root_quiznine, width = 18, **entry_style)
q9f_entry.place(x = 1150, y = 840)

q9menu = tk.Button(root_quiznine, text = 'Menu', command = lambda: show_frame(root_quizzes), **topbutton_style)
q9menu.place(x = 1160, y = 429)
q9next = tk.Button(root_quiznine, text = 'Next', command = lambda: show_frame(root_quizten), **topbutton_style, state = 'disabled')
q9next.place(x = 1843, y = 429)
q9back = tk.Button(root_quiznine, text = 'Back', command = lambda: show_frame(root_quizeight), **topbutton_style)
q9back.place(x = 1678, y = 429)
q9restart = tk.Button(root_quiznine, text = 'Restart', command = restartq9, **topbutton_style)
q9restart.place(x = 1750, y = 429)

q9submit_button = tk.Button(root_quiznine, text = 'Submit', command = submitq9, **subbutton_style)
q9submit_button.place(x = 1600, y = 660)
q9feedback = tk.Label(root_quiznine, **feedback_style)
q9feedback.place(x = 1150, y = 910)
q9result = tk.Label(root_quiznine, **label_style)
q9result.place(x = 1150, y = 945)
hoverbutton_list.extend([q9menu, q9back, q9next, q9restart, q9submit_button])

for i in [q9a_entry, q9b_entry, q9c_entry, q9d_entry, q9e_entry, q9f_entry]:
    i.bind('<Return>', submitq9)

# Quiz ten is the final test of the course and requires that every other quiz be successfully completed before it is unlocked.

# Frame for the final quiz, quiz ten.
root_quizten = tk.Frame(root_home)
framelist.append(root_quizten)  
q10_background = tk.PhotoImage(file = 'Images/quiz_ten.png')
q10_background_label = tk.Label(root_quizten, image = q10_background)
q10_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# This quiz is a single textbox for multiple lines, as the user has to code a program from scratch.
q10_entry = tk.Text(root_quizten, width = 57, height = 10, **textbox_style)
q10_entry.place(x = 1150, y = 600)

q10menu = tk.Button(root_quizten, text = 'Menu', command = lambda: show_frame(root_quizzes), **topbutton_style)
q10menu.place(x = 1160, y = 429)
hoverbutton_list.append(q10menu)
q10back = tk.Button(root_quizten, text = 'Back', command = lambda: show_frame(root_quiznine), **topbutton_style)
q10back.place(x = 1665, y = 429)
q10restart = tk.Button(root_quizten, text = 'Restart', command = restartq10, **topbutton_style)
q10restart.place(x = 1737, y = 429)

# Same functionality as the other quizzes.
q10submit_button = tk.Button(root_quizten, text = 'Submit', command = submitq10, **topbutton_style)
q10submit_button.place(x = 1830, y = 429)
hoverbutton_list.append(q10submit_button)
q10feedback = tk.Label(root_quizten, **feedback_style)
q10feedback.place(x = 1150, y = 920)
q10result = tk.Label(root_quizten, justify = 'left', **label_style)
q10result.place(x = 1150, y = 955)
hoverbutton_list.extend([q10menu, q10back, q10restart, q10submit_button])

# This time Enter is not binded as it is needed to create new lines in the textbox.

# The guides are made to cover the topics being tested in each quiz.
# They consist of the background image with information / examples, along with buttons.
# They have the menu button, which returns the user to the guides menu, a quiz button, and the back and next buttons.
# The quiz button directs the user to the corresponding quiz of that guide.

# Frame for guide one.
root_guideone = tk.Frame(root_home)
framelist.append(root_guideone)
g1_background = tk.PhotoImage(file = 'Images/guide_one.png')
g1_background_label = tk.Label(root_guideone, image = g1_background)
g1_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

g1menu = tk.Button(root_guideone, text = 'Menu', command = lambda: show_frame(root_guides), **topbutton_style)
g1menu.place(x = 20, y = 401)
g1quiz_button = tk.Button(root_guideone, text = 'Quiz', command = lambda: show_frame(root_quizone), **topbutton_style)
g1quiz_button.place(x = 101, y = 401)
g1next = tk.Button(root_guideone, text = 'Next', command = lambda: show_frame(root_guidetwo), **topbutton_style)
g1next.place(x = 170, y = 401)
hoverbutton_list.extend([g1menu, g1quiz_button, g1next])

# Frame for guide two.
root_guidetwo = tk.Frame(root_home)
framelist.append(root_guidetwo)
g2_background = tk.PhotoImage(file = 'Images/guide_two.png')
g2_background_label = tk.Label(root_guidetwo, image = g2_background)
g2_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

g2menu = tk.Button(root_guidetwo, text = 'Menu', command = lambda: show_frame(root_guides), **topbutton_style)
g2menu.place(x = 90, y = 401)
g2back = tk.Button(root_guidetwo, text = 'Back', command = lambda: show_frame(root_guideone), **topbutton_style)
g2back.place(x = 20, y = 401)
g2quiz_button = tk.Button(root_guidetwo, text = 'Quiz', command = lambda: show_frame(root_quiztwo), **topbutton_style)
g2quiz_button.place(x = 170, y = 401)
g2next = tk.Button(root_guidetwo, text = 'Next', command = lambda: show_frame(root_guidethree), **topbutton_style)
g2next.place(x = 240, y = 401)
hoverbutton_list.extend([g2menu, g2quiz_button, g2next, g2back])

# Frame for guide three.
root_guidethree = tk.Frame(root_home)
framelist.append(root_guidethree)
g3_background = tk.PhotoImage(file = 'Images/guide_three.png')
g3_background_label = tk.Label(root_guidethree, image = g3_background)
g3_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

g3menu = tk.Button(root_guidethree, text = 'Menu', command = lambda: show_frame(root_guides), **topbutton_style)
g3menu.place(x = 90, y = 401)
g3back = tk.Button(root_guidethree, text = 'Back', command = lambda: show_frame(root_guidetwo), **topbutton_style)
g3back.place(x = 20, y = 401)
g3quiz_button = tk.Button(root_guidethree, text = 'Quiz', command = lambda: show_frame(root_quizthree), **topbutton_style)
g3quiz_button.place(x = 170, y = 401)
hoverbutton_list.extend([g3menu, g3quiz_button])
g3next = tk.Button(root_guidethree, text = 'Next', command = lambda: show_frame(root_guidefour), **topbutton_style)
g3next.place(x = 240, y = 401)
hoverbutton_list.extend([g3menu, g3quiz_button, g3next, g3back])

# Frame for guide four.
root_guidefour = tk.Frame(root_home)
framelist.append(root_guidefour)
g4_background = tk.PhotoImage(file = 'Images/guide_four.png')
g4_background_label = tk.Label(root_guidefour, image = g4_background)
g4_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

g4menu = tk.Button(root_guidefour, text = 'Menu', command = lambda: show_frame(root_guides), **topbutton_style)
g4menu.place(x = 90, y = 401)
g4back = tk.Button(root_guidefour, text = 'Back', command = lambda: show_frame(root_guidethree), **topbutton_style)
g4back.place(x = 20, y = 401)
g4quiz_button = tk.Button(root_guidefour, text = 'Quiz', command = lambda: show_frame(root_quizfour), **topbutton_style)
g4quiz_button.place(x = 170, y = 401)
g4next = tk.Button(root_guidefour, text = 'Next', command = lambda: show_frame(root_guidefive), **topbutton_style)
g4next.place(x = 240, y = 401)
hoverbutton_list.extend([g4menu, g4quiz_button, g4next, g4back])

# Frame for guide five.
root_guidefive = tk.Frame(root_home)
framelist.append(root_guidefive)
g5_background = tk.PhotoImage(file = 'Images/guide_five.png')
g5_background_label = tk.Label(root_guidefive, image = g5_background)
g5_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

g5menu = tk.Button(root_guidefive, text = 'Menu', command = lambda: show_frame(root_guides), **topbutton_style)
g5menu.place(x = 90, y = 401)
g5back = tk.Button(root_guidefive, text = 'Back', command = lambda: show_frame(root_guidefour), **topbutton_style)
g5back.place(x = 20, y = 401)
g5quiz_button = tk.Button(root_guidefive, text = 'Quiz', command = lambda: show_frame(root_quizfive), **topbutton_style)
g5quiz_button.place(x = 170, y = 401)
g5next = tk.Button(root_guidefive, text = 'Next', command = lambda: show_frame(root_guidesix), **topbutton_style)
g5next.place(x = 240, y = 401)
hoverbutton_list.extend([g5menu, g5quiz_button, g5next, g5back])

# Frame for guide six.
root_guidesix = tk.Frame(root_home)
framelist.append(root_guidesix)
g6_background = tk.PhotoImage(file = 'Images/guide_six.png')
g6_background_label = tk.Label(root_guidesix, image = g6_background)
g6_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

g6menu = tk.Button(root_guidesix, text = 'Menu', command = lambda: show_frame(root_guides), **topbutton_style)
g6menu.place(x = 90, y = 401)
g6back = tk.Button(root_guidesix, text = 'Back', command = lambda: show_frame(root_guidefive), **topbutton_style)
g6back.place(x = 20, y = 401)
g6quiz_button = tk.Button(root_guidesix, text = 'Quiz', command = lambda: show_frame(root_quizsix), **topbutton_style)
g6quiz_button.place(x = 170, y = 401)
g6next = tk.Button(root_guidesix, text = 'Next', command = lambda: show_frame(root_guideseven), **topbutton_style)
g6next.place(x = 240, y = 401)
hoverbutton_list.extend([g6menu, g6quiz_button, g6next, g6back])

# Frame for guide seven.
root_guideseven = tk.Frame(root_home)
framelist.append(root_guideseven)
g7_background = tk.PhotoImage(file = 'Images/guide_seven.png')
g7_background_label = tk.Label(root_guideseven, image = g7_background)
g7_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

g7menu = tk.Button(root_guideseven, text = 'Menu', command = lambda: show_frame(root_guides), **topbutton_style)
g7menu.place(x = 90, y = 401)
g7back = tk.Button(root_guideseven, text = 'Back', command = lambda: show_frame(root_guidesix), **topbutton_style)
g7back.place(x = 20, y = 401)
g7quiz_button = tk.Button(root_guideseven, text = 'Quiz', command = lambda: show_frame(root_quizseven), **topbutton_style)
g7quiz_button.place(x = 170, y = 401)
g7next = tk.Button(root_guideseven, text = 'Next', command = lambda: show_frame(root_guideeight), **topbutton_style)
g7next.place(x = 240, y = 401)
hoverbutton_list.extend([g7menu, g7quiz_button, g7next, g7back])

# Frame for guide eight.
root_guideeight = tk.Frame(root_home)
framelist.append(root_guideeight)
g8_background = tk.PhotoImage(file = 'Images/guide_eight.png')
g8_background_label = tk.Label(root_guideeight, image = g8_background)
g8_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

g8menu = tk.Button(root_guideeight, text = 'Menu', command = lambda: show_frame(root_guides), **topbutton_style)
g8menu.place(x = 90, y = 401)
g8back = tk.Button(root_guideeight, text = 'Back', command = lambda: show_frame(root_guideseven), **topbutton_style)
g8back.place(x = 20, y = 401)
g8quiz_button = tk.Button(root_guideeight, text = 'Quiz', command = lambda: show_frame(root_quizeight), **topbutton_style)
g8quiz_button.place(x = 170, y = 401)
g8next = tk.Button(root_guideeight, text = 'Next', command = lambda: show_frame(root_guidenine), **topbutton_style)
g8next.place(x = 240, y = 401)
hoverbutton_list.extend([g8menu, g8quiz_button, g8next, g8back])

# Frame for guide nine.
root_guidenine = tk.Frame(root_home)
framelist.append(root_guidenine)
g9_background = tk.PhotoImage(file = 'Images/guide_nine.png')
g9_background_label = tk.Label(root_guidenine, image = g9_background)
g9_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

g9menu = tk.Button(root_guidenine, text = 'Menu', command = lambda: show_frame(root_guides), **topbutton_style)
g9menu.place(x = 90, y = 401)
g9back = tk.Button(root_guidenine, text = 'Back', command = lambda: show_frame(root_guideeight), **topbutton_style)
g9back.place(x = 20, y = 401)
g9quiz_button = tk.Button(root_guidenine, text = 'Quiz', command = lambda: show_frame(root_quiznine), **topbutton_style)
g9quiz_button.place(x = 170, y = 401)
g9next = tk.Button(root_guidenine, text = 'Next', command = lambda: show_frame(root_guideten), **topbutton_style)
g9next.place(x = 240, y = 401)
hoverbutton_list.extend([g9menu, g9quiz_button, g9next, g9back])

# Frame for final guide, guide ten.
root_guideten = tk.Frame(root_home)
framelist.append(root_guideten)
g10_background = tk.PhotoImage(file = 'Images/guide_ten.png')
g10_background_label = tk.Label(root_guideten, image = g10_background)
g10_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

g10menu = tk.Button(root_guideten, text = 'Menu', command = lambda: show_frame(root_guides), **topbutton_style)
g10menu.place(x = 90, y = 401)
g10back = tk.Button(root_guideten, text = 'Back', command = lambda: show_frame(root_guidenine), **topbutton_style)
g10back.place(x = 20, y = 401)
g10quiz_button = tk.Button(root_guideten, text = 'Quiz', command = lambda: show_frame(root_quizten), **topbutton_style, state = 'disabled')
g10quiz_button.place(x = 170, y = 401)
hoverbutton_list.extend([g10menu, g10quiz_button, g10back])

# Menu page for Guides
root_guides = tk.Frame(root_home)
framelist.append(root_guides)
guides_background = tk.PhotoImage(file = 'Images/guides.png')
guides_background_label = tk.Label(root_guides, image = guides_background)
guides_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Buttons for all the guides.
g1button = tk.Button(root_guides, text = 'G1', command = lambda: show_frame(root_guideone), **bigbutton_style)
g2button = tk.Button(root_guides, text = 'G2', command = lambda: show_frame(root_guidetwo), **bigbutton_style)
g3button = tk.Button(root_guides, text = 'G3', command = lambda: show_frame(root_guidethree), **bigbutton_style)
g4button = tk.Button(root_guides, text = 'G4', command = lambda: show_frame(root_guidefour), **bigbutton_style)
g5button = tk.Button(root_guides, text = 'G5', command = lambda: show_frame(root_guidefive), **bigbutton_style)
g6button = tk.Button(root_guides, text = 'G6', command = lambda: show_frame(root_guidesix), **bigbutton_style)
g7button = tk.Button(root_guides, text = 'G7', command = lambda: show_frame(root_guideseven), **bigbutton_style)
g8button = tk.Button(root_guides, text = 'G8', command = lambda: show_frame(root_guideeight), **bigbutton_style)
g9button = tk.Button(root_guides, text = 'G9', command = lambda: show_frame(root_guidenine), **bigbutton_style)
g10button = tk.Button(root_guides, text = '🎓', command = lambda: show_frame(root_guideten), **bigbutton_style)

g1button.place(x = 450, y = 415)
g2button.place(x = 678, y = 415)
g3button.place(x = 905, y = 415)
g4button.place(x = 1133, y = 415)
g5button.place(x = 1360, y = 415)
g6button.place(x = 450, y = 615)
g7button.place(x = 678, y = 615)
g8button.place(x = 905, y = 615)
g9button.place(x = 1133, y = 615)
g10button.place(x = 1360, y = 615)

# Binding them all to hover effects and back-to-home button.
hoverbutton_list.extend([g1button, g2button, g3button, g4button, g5button, g6button, g7button, g8button, g9button, g10button])
guidesback = tk.Button(root_guides, text = 'Back', command = back_home, font = segoe_bo, background = '#275b84', foreground = '#ffde57', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0)
guidesback.place(x = 450, y = 820)
rhoverbutton_list.append(guidesback)

# Menu page for Quizzes.
root_quizzes = tk.Frame(root_home)
framelist.append(root_quizzes)
quizzes_background = tk.PhotoImage(file = 'Images/quizzes.png')
quizzes_background_label = tk.Label(root_quizzes, image = quizzes_background)
quizzes_background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Buttons for all the quizzes.
q1button = tk.Button(root_quizzes, text = 'Q1', command = lambda: show_frame(root_quizone), **bigbutton_style)
q2button = tk.Button(root_quizzes, text = 'Q2', command = lambda: show_frame(root_quiztwo), **bigbutton_style)
q3button = tk.Button(root_quizzes, text = 'Q3', command = lambda: show_frame(root_quizthree), **bigbutton_style)
q4button = tk.Button(root_quizzes, text = 'Q4', command = lambda: show_frame(root_quizfour), **bigbutton_style)
q5button = tk.Button(root_quizzes, text = 'Q5', command = lambda: show_frame(root_quizfive), **bigbutton_style)
q6button = tk.Button(root_quizzes, text = 'Q6', command = lambda: show_frame(root_quizsix), **bigbutton_style)
q7button = tk.Button(root_quizzes, text = 'Q7', command = lambda: show_frame(root_quizseven), **bigbutton_style)
q8button = tk.Button(root_quizzes, text = 'Q8', command = lambda: show_frame(root_quizeight), **bigbutton_style)
q9button = tk.Button(root_quizzes, text = 'Q9', command = lambda: show_frame(root_quiznine), **bigbutton_style)
q10button = tk.Button(root_quizzes, text = '🔒', command = lambda: show_frame(root_quizten), **bigbutton_style, disabledforeground = '#a0a0a0', state = 'disabled')

q1button.place(x = 450, y = 415)
q2button.place(x = 678, y = 415)
q3button.place(x = 905, y = 415)
q4button.place(x = 1133, y = 415)
q5button.place(x = 1360, y = 415)
q6button.place(x = 450, y = 615)
q7button.place(x = 678, y = 615)
q8button.place(x = 905, y = 615)
q9button.place(x = 1133, y = 615)
q10button.place(x = 1360, y = 615)

# Binding them all to hover effects and back-to-home button.
hoverbutton_list.extend([q1button, q2button, q3button, q4button, q5button, q6button, q7button, q8button, q9button, q10button])
quizzesback = tk.Button(root_quizzes, text = 'Back', command = back_home, font = segoe_bo, background = '#275b84', foreground = '#ffde57', activebackground = '#275b84', activeforeground = '#ffde57', borderwidth = 0)
quizzesback.place(x = 450, y = 820)
rhoverbutton_list.append(quizzesback)

# The following are the help buttons on each quiz and the small frames each of them opens.
# The frames appear on top of the button and offer two buttons: one that takes you to the corresponding guide and an X to close.
# The help button itself can also be used to close as it toggles.

# Help frame for quiz one.

help_img = tk.PhotoImage(file = 'Images/help_button.png')

root_q1help = tk.Frame(root_home, width = 220, height = 55, background = '#0277bc')
help_framelist.append(root_q1help)
q1_guidebutton = tk.Button(root_q1help, text = 'Visit Guide One?', command = lambda: quiz_to_guide(root_guideone, root_q1help), font = segoe_s, background = '#275b84', foreground = '#ffde57', activebackground = '#ffde57', activeforeground = '#275b84', borderwidth = 0)
q1_guidebutton.place(relx = 0.02, rely = 0.5, anchor = 'w')
rhoverbutton_list.append(q1_guidebutton)
q1_guidecross = tk.Button(root_q1help, text = 'X', command = lambda: close_help(root_q1help), font  = segoe_s, background = '#e81123', foreground = '#ffffff', borderwidth = 0)
q1_guidecross.place(relx = 0.98, rely = 0.5, anchor = 'e')
quit_hoverlist.append(q1_guidecross)
q1help_button = tk.Button(root_quizone, command = lambda: show_help(root_q1help), image = help_img, bg = '#275b84', bd = 0, activebackground = '#275b84', borderwidth = 0)
q1help_button.place(x = 1083, y = 435)

# Help frame for quiz two.
root_q2help = tk.Frame(root_home, width = 220, height = 55, background = '#0277bc')
help_framelist.append(root_q2help)
q2_guidebutton = tk.Button(root_q2help, text = 'Visit Guide Two?', command = lambda: quiz_to_guide(root_guidetwo, root_q2help), font = segoe_s, background = '#275b84', foreground = '#ffde57', activebackground = '#ffde57', activeforeground = '#275b84', borderwidth = 0)
q2_guidebutton.place(relx = 0.02, rely = 0.5, anchor = 'w')
rhoverbutton_list.append(q2_guidebutton)
q2_guidecross = tk.Button(root_q2help, text = 'X', command = lambda: close_help(root_q2help), font  = segoe_s, background = '#e81123', foreground = '#ffffff', borderwidth = 0)
q2_guidecross.place(relx = 0.98, rely = 0.5, anchor = 'e')
quit_hoverlist.append(q2_guidecross)
q2help_button = tk.Button(root_quiztwo, command = lambda: show_help(root_q2help), image = help_img, bg = '#275b84', bd = 0, activebackground = '#275b84', borderwidth = 0)
q2help_button.place(x = 1083, y = 435)

# Help frame for quiz three.
root_q3help = tk.Frame(root_home, width = 220, height = 55, background = '#0277bc')
help_framelist.append(root_q3help)
q3_guidebutton = tk.Button(root_q3help, text = 'Visit Guide Three?', command = lambda: quiz_to_guide(root_guidethree, root_q3help), font = segoe_s, background = '#275b84', foreground = '#ffde57', activebackground = '#ffde57', activeforeground = '#275b84', borderwidth = 0)
q3_guidebutton.place(relx = 0.02, rely = 0.5, anchor = 'w')
rhoverbutton_list.append(q3_guidebutton)
q3_guidecross = tk.Button(root_q3help, text = 'X', command = lambda: close_help(root_q3help), font  = segoe_s, background = '#e81123', foreground = '#ffffff', borderwidth = 0)
q3_guidecross.place(relx = 0.98, rely = 0.5, anchor = 'e')
quit_hoverlist.append(q3_guidecross)
q3help_button = tk.Button(root_quizthree, command = lambda: show_help(root_q3help), image = help_img, bg = '#275b84', bd = 0, activebackground = '#275b84', borderwidth = 0)
q3help_button.place(x = 1083, y = 435)

# Help frame for quiz four.
root_q4help = tk.Frame(root_home, width = 220, height = 55, background = '#0277bc')
help_framelist.append(root_q4help)
q4_guidebutton = tk.Button(root_q4help, text = 'Visit Guide Four?', command = lambda: quiz_to_guide(root_guidefour, root_q4help), font = segoe_s, background = '#275b84', foreground = '#ffde57', activebackground = '#ffde57', activeforeground = '#275b84', borderwidth = 0)
q4_guidebutton.place(relx = 0.02, rely = 0.5, anchor = 'w')
rhoverbutton_list.append(q4_guidebutton)
q4_guidecross = tk.Button(root_q4help, text = 'X', command = lambda: close_help(root_q4help), font  = segoe_s, background = '#e81123', foreground = '#ffffff', borderwidth = 0)
q4_guidecross.place(relx = 0.98, rely = 0.5, anchor = 'e')
quit_hoverlist.append(q4_guidecross)
q4help_button = tk.Button(root_quizfour, command = lambda: show_help(root_q4help), image = help_img, bg = '#275b84', bd = 0, activebackground = '#275b84', borderwidth = 0)
q4help_button.place(x = 1083, y = 435)

# Help frame for quiz five.
root_q5help = tk.Frame(root_home, width = 220, height = 55, background = '#0277bc')
help_framelist.append(root_q5help)
q5_guidebutton = tk.Button(root_q5help, text = 'Visit Guide Five?', command = lambda: quiz_to_guide(root_guidefive, root_q5help), font = segoe_s, background = '#275b84', foreground = '#ffde57', activebackground = '#ffde57', activeforeground = '#275b84', borderwidth = 0)
q5_guidebutton.place(relx = 0.02, rely = 0.5, anchor = 'w')
rhoverbutton_list.append(q5_guidebutton)
q5_guidecross = tk.Button(root_q5help, text = 'X', command = lambda: close_help(root_q5help), font  = segoe_s, background = '#e81123', foreground = '#ffffff', borderwidth = 0)
q5_guidecross.place(relx = 0.98, rely = 0.5, anchor = 'e')
quit_hoverlist.append(q5_guidecross)
q5help_button = tk.Button(root_quizfive, command = lambda: show_help(root_q5help), image = help_img, bg = '#275b84', bd = 0, activebackground = '#275b84', borderwidth = 0)
q5help_button.place(x = 1083, y = 435)

# Help frame for quiz six.
root_q6help = tk.Frame(root_home, width = 220, height = 55, background = '#0277bc')
help_framelist.append(root_q6help)
q6_guidebutton = tk.Button(root_q6help, text = 'Visit Guide Six?', command = lambda: quiz_to_guide(root_guidesix, root_q6help), font = segoe_s, background = '#275b84', foreground = '#ffde57', activebackground = '#ffde57', activeforeground = '#275b84', borderwidth = 0)
q6_guidebutton.place(relx = 0.02, rely = 0.5, anchor = 'w')
rhoverbutton_list.append(q6_guidebutton)
q6_guidecross = tk.Button(root_q6help, text = 'X', command = lambda: close_help(root_q6help), font  = segoe_s, background = '#e81123', foreground = '#ffffff', borderwidth = 0)
q6_guidecross.place(relx = 0.98, rely = 0.5, anchor = 'e')
quit_hoverlist.append(q6_guidecross)
q6help_button = tk.Button(root_quizsix, command = lambda: show_help(root_q6help), image = help_img, bg = '#275b84', bd = 0, activebackground = '#275b84', borderwidth = 0)
q6help_button.place(x = 1083, y = 435)

# Help frame for quiz seven.
root_q7help = tk.Frame(root_home, width = 220, height = 55, background = '#0277bc')
help_framelist.append(root_q7help)
q7_guidebutton = tk.Button(root_q7help, text = 'Visit Guide Seven?', command = lambda: quiz_to_guide(root_guideseven, root_q7help), font = segoe_s, background = '#275b84', foreground = '#ffde57', activebackground = '#ffde57', activeforeground = '#275b84', borderwidth = 0)
q7_guidebutton.place(relx = 0.02, rely = 0.5, anchor = 'w')
rhoverbutton_list.append(q7_guidebutton)
q7_guidecross = tk.Button(root_q7help, text = 'X', command = lambda: close_help(root_q7help), font  = segoe_s, background = '#e81123', foreground = '#ffffff', borderwidth = 0)
q7_guidecross.place(relx = 0.98, rely = 0.5, anchor = 'e')
quit_hoverlist.append(q7_guidecross)
q7help_button = tk.Button(root_quizseven, command = lambda: show_help(root_q7help), image = help_img, bg = '#275b84', bd = 0, activebackground = '#275b84', borderwidth = 0)
q7help_button.place(x = 1083, y = 435)

# Help frame for quiz eight.
root_q8help = tk.Frame(root_home, width = 220, height = 55, background = '#0277bc')
help_framelist.append(root_q8help)
q8_guidebutton = tk.Button(root_q8help, text = 'Visit Guide Eight?', command = lambda: quiz_to_guide(root_guideeight, root_q8help), font = segoe_s, background = '#275b84', foreground = '#ffde57', activebackground = '#ffde57', activeforeground = '#275b84', borderwidth = 0)
q8_guidebutton.place(relx = 0.02, rely = 0.5, anchor = 'w')
rhoverbutton_list.append(q8_guidebutton)
q8_guidecross = tk.Button(root_q8help, text = 'X', command = lambda: close_help(root_q8help), font  = segoe_s, background = '#e81123', foreground = '#ffffff', borderwidth = 0)
q8_guidecross.place(relx = 0.98, rely = 0.5, anchor = 'e')
quit_hoverlist.append(q8_guidecross)
q8help_button = tk.Button(root_quizeight, command = lambda: show_help(root_q8help), image = help_img, bg = '#275b84', bd = 0, activebackground = '#275b84', borderwidth = 0)
q8help_button.place(x = 1083, y = 435)

# Help frame for quiz nine.
root_q9help = tk.Frame(root_home, width = 220, height = 55, background = '#0277bc')
help_framelist.append(root_q9help)
q9_guidebutton = tk.Button(root_q9help, text = 'Visit Guide Nine?', command = lambda: quiz_to_guide(root_guidenine, root_q9help), font = segoe_s, background = '#275b84', foreground = '#ffde57', activebackground = '#ffde57', activeforeground = '#275b84', borderwidth = 0)
q9_guidebutton.place(relx = 0.02, rely = 0.5, anchor = 'w')
rhoverbutton_list.append(q9_guidebutton)
q9_guidecross = tk.Button(root_q9help, text = 'X', command = lambda: close_help(root_q9help), font  = segoe_s, background = '#e81123', foreground = '#ffffff', borderwidth = 0)
q9_guidecross.place(relx = 0.98, rely = 0.5, anchor = 'e')
quit_hoverlist.append(q9_guidecross)
q9help_button = tk.Button(root_quiznine, command = lambda: show_help(root_q9help), image = help_img, bg = '#275b84', bd = 0, activebackground = '#275b84', borderwidth = 0)
q9help_button.place(x = 1083, y = 435)

# Finally there is all the widgets on the main root.
# The background is an image, as are the Quiz and Guide buttons.
# A hover effect was created by having two images for each button, and having the hover effect switch between them.

background = tk.PhotoImage(file = 'Images/home_page.png')
background_label = tk.Label(root_home, image = background)
background_label.place(x = 0, y = 0, relwidth=1, relheight=1)

quiz_button_img = tk.PhotoImage(file = 'Images/quizzes_button.png')
altquiz_button_img = tk.PhotoImage(file = 'Images/altquizzes_button.png')
quiz_button = tk.Button(root_home, image = quiz_button_img, command = lambda: show_frame(root_quizzes), bg = '#0277bc', bd = 0, activebackground = '#0277bc', font = segoe_s)
quiz_button.place(x = 960, y = 670, anchor = 'center')

quiz_button.bind('<Enter>', image_enter)
quiz_button.bind('<Leave>', image_leave)

guides_button_img = tk.PhotoImage(file = 'Images/guides_button.png')
altguides_button_img = tk.PhotoImage(file = 'Images/altguides_button.png')
guides_button = tk.Button(root_home, image = guides_button_img, command = lambda: show_frame(root_guides), bg = '#0277bc', bd = 0, activebackground = '#0277bc', font = segoe_b)
guides_button.place(x = 960, y = 910, anchor = 'center')

guides_button.bind('<Enter>', image_enter)
guides_button.bind('<Leave>', image_leave)

# Calling all the functions needed to load widgets.
loadframes()
load_helpframes()
loadbutton()
final_unlocked()
print(sys.getsizeof(q1a1_entry))
print(sys.getsizeof(q1a1))
root_home.mainloop()    