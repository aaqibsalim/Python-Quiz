import tkinter as tk
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)
root_home = tk.Tk()
root_home.title('Python Quiz')
root_home.geometry("1920x1080")
root_home.state('zoomed')
root_home.iconphoto(True, tk.PhotoImage(file = "Python Quiz\Images\Python Icon.png"))

root_home.grid_rowconfigure(0, weight=1)
root_home.grid_columnconfigure(0, weight=1)

framelist = []

def back_home():
    for frame in framelist:
        frame.grid_forget()

def show_frame(frame):
    frame.grid(row=0, column=0, sticky="nsew")
    frame.tkraise()

q1guess_no = 0

def submitq1():
    
    global q1guess_no

    q1a_v = q1a_entry.get()
    q1b_v = q1b_entry.get()
    q1c_v = q1c_entry.get()
    q1d_v = q1d_entry.get()
    q1e_v = q1e_entry.get()
    
    q1guess = f"{q1a_v}{q1b_v} works as a {q1c_v} and is {q1d_v} years old.{q1e_v}"
    q1correct = "f'{name} works as a {job} and is {age} years old.'"

    q1_is_correct = False
    incorrect_message = ''

    if q1guess == q1correct:
        correct_message = 'Correct! f strings and curly brackets are used to display variables in a string.'
        q1_is_correct = True
    elif 'john' in q1guess.lower() or 'lawyer' in q1guess.lower() or '34' in q1guess:
        incorrect_message = "Instead of putting the specific name/job/age we should put the variable names instead. E.g: {name} instead of John."
    elif "f'" in q1guess and '{' not in q1guess:
        incorrect_message = "You are correct in using an f string but the variables should be inside curly brackets."
    elif '{' in q1guess and "f'" not in q1guess:
        incorrect_message = "The variables are correctly placed in curly brackets. However, to have variables inside a string, an f string (f') must be used."
    elif "'" in q1guess and "f'" not in q1guess:
        incorrect_message = "Remember to use an f string (f') when including variables within the string."
    elif "f'" in q1guess and '{' in q1guess:
        incorrect_message = 'Check to make sure your sentence makes sense.'
    else:
        incorrect_message = 'Incorrect.'
    q1guess_no += 1
    if q1_is_correct:
        q1submit_button.config(state = 'disabled')
        if q1guess_no > 1:
            q1result.config(text = f'''{correct_message}
You took ({q1guess_no}) guesses to find the answer.''')
        else:
            q1result.config(text = f'''{correct_message}
You took ({q1guess_no}) guess to find the answer.''')
    else: 
        q1result.config(text = incorrect_message)

q2guessed_operations = set()

def submitq2():

    global q2guessed_operations
    q2feedback.config(text = 'Feedback & Output:')
    q2a_v = q2a_entry.get()
    q2b_v = q2b_entry.get()

    q2guess = f"{q2a_v}(x {q2b_v} y)"
    q2correct = ['print(x + y)', 'print(x - y)', 'print(x * y)', 'print(x / y)']
    if q2guess not in q2correct:
        if 'print' != q2a_v.lower() and q2b_v.lower() not in ['+', '-', '*', '/']:
            incorrect_message = 'Use the print function to display and the operations (+, -, *, /) to calculate.'
        elif 'print' == q2a_v.lower() and q2b_v.lower() not in ['+', '-', '*', '/']:
            incorrect_message = 'The print function is correctly used, however use the operations (+, -, *, /) to calculate.'
        elif 'print' != q2a_v.lower() and q2b_v.lower()  in ['+', '-', '*', '/']:
            incorrect_message = 'You are correctly using an operation, however the print function is needed to display the result.'
        else:
            incorrect_message = 'Incorrect.'
        q2result.config(text = incorrect_message)
    else:
        q2_is_correct = True
        q2guessed_operations.add(q2b_v)
        q2result.config(text = f'10 {q2b_v} 5 = ' + str(eval(f'10 {q2b_v} 5')))
        if {'+', '-', '*', '/'}.issubset(q2guessed_operations):
            q2f_result.config(text = 'That is all four operations correctly used. Congratulations!')
            q2submit_button.config(state = 'disabled')
        
root_quizone = tk.Frame(root_home)
framelist.append(root_quizone)
q1question = tk.Label(root_quizone, text = '''
name = 'John'
job = 'lawyer'
age = 34
a)__ b)____ works as a c)___ and is d)___ years old. e)_''')
q1question.grid(columnspan = 10)

q1a = tk.Label(root_quizone, text = 'a)')
q1a.grid(row = 1, column = 0)
q1a_entry = tk.Entry(root_quizone, width = 1)
q1a_entry.grid(row = 1, column = 1)

q1b = tk.Label(root_quizone, text = 'b)')
q1b.grid(row = 1, column = 2)
q1b_entry = tk.Entry(root_quizone, width = 6)
q1b_entry.grid(row = 1, column = 3)

q1c = tk.Label(root_quizone, text = 'c)')
q1c.grid(row = 1, column = 4)
q1c_entry = tk.Entry(root_quizone, width = 4)
q1c_entry.grid(row = 1, column = 5)

q1d = tk.Label(root_quizone, text = 'd)')
q1d.grid(row = 1, column = 6)
q1d_entry = tk.Entry(root_quizone, width = 5)
q1d_entry.grid(row = 1, column = 7)

q1e = tk.Label(root_quizone, text = 'e)')
q1e.grid(row = 1, column = 8)
q1e_entry = tk.Entry(root_quizone, width = 1)
q1e_entry.grid(row = 1, column = 9)

q1submit_button = tk.Button(root_quizone, text = 'Submit', command = submitq1)
q1submit_button.grid(row = 2, column = 4)
q1result = tk.Label(root_quizone)
q1result.grid(row = 3, columnspan = 10)
q1back = tk.Button(root_quizone, text = 'Back', command = lambda: show_frame(root_quiz)).grid(row = 2, column = 5)

root_quiztwo = tk.Frame(root_home)
framelist.append(root_quiztwo)
q2_background = tk.PhotoImage(file = 'Python Quiz\Images\Quiz Two.png')
q2_background_label = tk.Label(root_quiztwo, image = q2_background)
q2_background_label.place(x = 0, y = 0)

q2question = tk.Label(root_quiztwo, text = '''x = 10
y = 5''', font = ('Bricolage Grotesque 14pt', 20), bg = '#0277bc')
q2question.place(x = 1470, y = 525)

q2a_entry = tk.Entry(root_quiztwo, width = 4, font = ('Bricolage Grotesque 14pt', 12))
q2a_entry.place(x = 1445, y = 665)

q2b1 = tk.Label(root_quiztwo, text = '(x', font = ('Bricolage Grotesque 14pt', 12))
q2b1.place(x = 1505, y = 665)
q2b_entry = tk.Entry(root_quiztwo, width = 1, font = ('Bricolage Grotesque 14pt', 12))
q2b_entry.place(x = 1530, y = 665)
q2b2 = tk.Label(root_quiztwo, text = 'y)', font = ('Bricolage Grotesque 14pt', 12))
q2b2.place(x = 1551, y = 665)

q2submit_button = tk.Button(root_quiztwo, text = 'Submit', font = ('Bricolage Grotesque 14pt', 12), command = submitq2)
q2submit_button.place(x = 1475, y = 750)
q2feedback = tk.Label(root_quiztwo, font = ('Bricolage Grotesque 14pt', 12), bg = '#0277bc')
q2feedback.place(x = 1150, y = 820)
q2result = tk.Label(root_quiztwo, font = ('Bricolage Grotesque 14pt', 11), bg = '#0277bc')
q2result.place(x = 1150, y = 850)
q2f_result = tk.Label(root_quiztwo, font = ('Bricolage Grotesque 14pt', 11), bg = '#0277bc')
q2f_result.place(x = 1150, y = 900)
q2back = tk.Button(root_quiztwo, text = 'Back', command = lambda: show_frame(root_quiz)).place(x = 1000, y = 1050)

root_tutorials = tk.Frame(root_home)
framelist.append(root_tutorials)

root_quiz = tk.Frame(root_home)
framelist.append(root_quiz)
q1button = tk.Button(root_quiz, text = 'Quiz 1', command = lambda: show_frame(root_quizone)).grid(row = 0, column = 0)
q2button = tk.Button(root_quiz, text = 'Quiz 2', font = ('Bricolage Grotesque 14pt', 12), command = lambda: show_frame(root_quiztwo)).grid(row = 0, column = 1)
quizback = tk.Button(root_quiz, text = 'Back', command = lambda: back_home()).grid(row = 0, column = 2)

for frame in (framelist):
    frame.grid(row=0, column=0, sticky="nsew")

background = tk.PhotoImage(file = 'Python Quiz\Images\Home Page.png')
background_label = tk.Label(root_home, image = background)
background_label.place(x = 0, y = 0)

quiz_button_img = tk.PhotoImage(file = 'Python Quiz\Images\Quiz Button.png')
quiz_button_label = tk.Label(root_home, image = quiz_button_img)
quiz_button = tk.Button(root_home, image = quiz_button_img, command = lambda: show_frame(root_quiz), bg = '#0277bc', bd = 0, activebackground = '#0277bc')
quiz_button_label, quiz_button.place(anchor = 'center', x = 960, y = 670)

tutorials_button_img = tk.PhotoImage(file = 'Python Quiz\Images\Tutorials Button.png')
tutorials_button_label = tk.Label(root_home, image = tutorials_button_img)
tutorials_button = tk.Button(root_home, image = tutorials_button_img, command = lambda: show_frame(root_tutorials), bg = '#0277bc', bd = 0, activebackground = '#0277bc')
tutorials_button_label, tutorials_button.place(anchor = 'center', x = 960, y = 910)

root_home.mainloop()