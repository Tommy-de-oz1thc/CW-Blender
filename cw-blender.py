import time
import tkinter as tk
from tkinter import ttk
import random as rand
import cw_play as cp
import threading
import guess_class as gc
import letter_class as lc
import word_class as wc
import sentences_class as sc
import radio_class as rc
import text_class as tc

def create_tab(tab_name):
    # Function to create the content of the tab
    tab_content = ttk.Frame(notebook)
    notebook.add(tab_content, text=tab_name)
    return tab_content



def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')
   
# Create the main Tkinter window
root = tk.Tk()
# Create a Notebook-widget
notebook = ttk.Notebook(root)
letters_tab = create_tab("Letters")
words_tab = create_tab("Words")
sentences_tab = create_tab("Sentences")
radio_tab = create_tab("Radio")
text_tab = create_tab("Text")
guess_tab = create_tab("Guess")
letter_L_App = lc.LettersApp(letters_tab)
word_L_App = wc.WordsApp(words_tab)
sentences_L_App = sc.SentencesApp(sentences_tab)
radio_L_App = rc.RadioApp(radio_tab)
text_L_App = tc.TextApp(text_tab)
gueess_L_App = gc.GuessLettersApp(guess_tab)

window_height = 700
window_width = 600
def on_tab_change(event):
    global window_width
    selected_tab_index = notebook.index(notebook.select()) 
    print(selected_tab_index)  # Corrected variable name
    if selected_tab_index == 5:
        window_width = 1300
    elif selected_tab_index == 0:  # Use "elif" for proper condition checking
        window_width = 350
    else:
        window_width = 600
    center_window(root, window_width, window_height)
    
notebook.bind("<<NotebookTabChanged>>", on_tab_change)
root.resizable(False, False)
root.title('CW Blender v.7.0 by OZ1THC')

center_window(root, window_width, window_height)



text = "cw blender".upper()
def start():
    for c in text:
        cp.play(c,20)
threading.Thread(target=start).start()  # Note the comma after (wpm)


notebook.grid(row=1, column=1)
root.mainloop()

