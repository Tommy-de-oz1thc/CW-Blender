import tkinter as tk
from tkinter import ttk
import random as rand
import threading
import cw_play as cp
import time
import letter_3_word as let_3
import letter_3_4_word as let_3_4
import letter_4_word as let_4
import letter_4_5_word as let_4_5
import letter_5_word as let_5
import letter_4_6_word as let_4_6
import letter_5_6_word as let_5_6
import letter_6_word as let_6
import top_100 as top_100
import top_200 as top_200
import top_500 as top_500

class WordsApp:
    def __init__(self, master):
        self.master = master
        self.words_list = ["3 letters", "3-4 letters","4 letters", "4-5 letters","5 letters","4-6 letters","5-6 letters","6 letters","Top 100","Top 200","Top 500"]     
        self.word_checkbox_vars = {}
        self.checked_checkboxes = []
       
        self.create_widgets()

    def agreement_word_button(self):
        selected_value = self.wpm_word_combobox.get()
        wpm = int(''.join(filter(str.isdigit, selected_value)))
        self.result_word_text.delete(1.0, tk.END)  # Clear previous text
        self.stop_word = False
        threading.Thread(target=self.word, args=(wpm,)).start()  # Note the comma after (wpm)

    def agreement_word_button_stop(self):
        self.stop_word = True

    def word(self,wpm):
       
        liste = []
        # Check if the checkbox associated with "3 letters" is checked
        if self.word_checkbox_vars["Top 500"].get() == "agree":
            liste = top_500.top_500 
        elif self.word_checkbox_vars["Top 200"].get() == "agree":
            liste = top_200.top_200 
        elif self.word_checkbox_vars["Top 100"].get() == "agree":
            liste = top_100.top_100 
        elif self.word_checkbox_vars["6 letters"].get() == "agree":
            liste = let_6.letter_6 

        elif self.word_checkbox_vars["5-6 letters"].get() == "agree":
            liste = let_5_6.letter_5_6 

        elif self.word_checkbox_vars["4-6 letters"].get() == "agree":
            liste = let_4_6.letter_4_6 
        
        elif self.word_checkbox_vars["5 letters"].get() == "agree":
            liste = let_5.letter_5   

        elif self.word_checkbox_vars["4-5 letters"].get() == "agree":
            liste = let_4_5.letter_4_5
        
        elif self.word_checkbox_vars["4 letters"].get() == "agree":
            liste = let_4.letter_4

        elif self.word_checkbox_vars["3-4 letters"].get() == "agree":
            liste = let_3_4.letter_3_4
            
        elif self.word_checkbox_vars["3 letters"].get() == "agree":
            liste = let_3.letter_3
        
        for i in range(25):
            selected_words = [word for word in liste]
            
            if selected_words:
                bog = rand.choice(selected_words)
                #print(bog)
                for c in bog:
                    c = c.upper()
                    cp.play(c,wpm)
            if self.stop_word:
                break

            self.result_word_text.insert(tk.END, bog + "\n")

            
            time.sleep(1)       
        
    def checkbox_word_changed(self,option):
        result = self.word_checkbox_vars[option].get()
        
        if result == "agree":
            self.checked_checkboxes.append(option)
        else:
            if option in self.checked_checkboxes:
                self.checked_checkboxes.remove(option)

        checked_letters = [letter for letter in self.checked_checkboxes if letter.isalpha()]
        checked_text = ", ".join(checked_letters)

        self.result_word_text.delete(1.0, tk.END)  # Clear previous text


    def create_widgets(self):
        for i, word in enumerate(self.words_list):
            self.word_checkbox_vars[word] = tk.StringVar()
            self.word_checkbox_vars[word].set('disagree')
            row_num = i // 5
            col_num = i % 5

            ttk.Checkbutton(self.master,
                text=word,
                command=lambda w=word: self.checkbox_word_changed(w),
                variable=self.word_checkbox_vars[word],
                onvalue='agree',
                offvalue='disagree').grid(row=row_num + 3, column=col_num)
          
        wpm_word_combobox = ttk.Combobox(self.master, values=['15 wpm', '18 wpm', '20 wpm', '22 wpm','25 wpm', '28 wpm','30 wpm','32 wpm','35 wpm','38 wpm','40 wpm','42 wpm','45 wpm','48 wpm','50 wpm','52 wpm','55 wpm','58 wpm','60 wpm'], state="readonly", width=30)
        wpm_word_combobox.set('20 wpm')  # Set default value
        wpm_word_combobox.grid(row=9, column=0, columnspan=5, pady=10)
        self.wpm_word_combobox = wpm_word_combobox

        ttk.Button(self.master,
           text="Start Button",
           command=self.agreement_word_button).grid(row=13, columnspan=5, pady=20)
        ttk.Button(self.master,
          text="Stop Button",
          command=self.agreement_word_button_stop).grid(row=14, columnspan=5, pady=20)
        self.result_word_text = tk.Text(self.master, height=26, width=20)
        self.result_word_text.grid(row=11, column=0, columnspan=5)
        word_label = tk.Label(self.master, text="Auto choose the highest letters.")
        word_label.grid(row=1, column=0)
    def select_all(self):
        for word in self.words_list:
            self.word_checkbox_vars[word].set('agree')

    def unselect_all(self):
        for word in self.words_list:
            self.word_checkbox_vars[word].set('disagree')

