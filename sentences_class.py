import tkinter as tk
from tkinter import ttk
import random as rand
import threading
import cw_play as cp
import time

import word_2_sentences_2 as words_2
import word_3_sentences_3 as words_3
import word_4_sentences_4 as words_4
import word_5_sentences_5 as words_5
import word_6_sentences_6 as words_6
import word_7_sentences_7 as words_7
import word_8_sentences_8 as words_8

import top_100_words as words_top_100
import top_200_words as words_top_200
import top_600_words as words_top_600

class SentencesApp:
    def __init__(self, master):
        self.master = master
        self.sentences_list = ["2 words","3 words","4 words","5 words","6 words","7 words","8 words","Top 100 words","Top 200 words","Top 600 words"]
        self.sentences_checkbox_vars = {}
        self.checked_checkboxes = []
       
        self.create_widgets()

    def agreement_sentences_button(self):
        selected_value = self.wpm_sentences_combobox.get()
        wpm = int(''.join(filter(str.isdigit, selected_value)))
        self.result_sentences_text.delete(1.0, tk.END)  # Clear previous text
        self.stop_sentences = False
        threading.Thread(target=self.sentences, args=(wpm,)).start()  # Note the comma after (wpm)

    def agreement_sentences_button_stop(self):
        self.stop_sentences = True

    def create_widgets(self):
        for i, sentences in enumerate(self.sentences_list):
            self.sentences_checkbox_vars[sentences] = tk.StringVar()
            self.sentences_checkbox_vars[sentences].set('disagree')
            row_num = i // 5
            col_num = i % 5

            ttk.Checkbutton(self.master,
                        text=sentences,
                        command=lambda w=sentences: self.checkbox_sentences_changed(w),
                        variable=self.sentences_checkbox_vars[sentences],
                        onvalue='agree',
                        offvalue='disagree').grid(row=row_num + 3, column=col_num)
            wpm_sentences_combobox = ttk.Combobox(self.master, values=['15 wpm', '18 wpm', '20 wpm', '22 wpm','25 wpm', '28 wpm','30 wpm','32 wpm','35 wpm','38 wpm','40 wpm','42 wpm','45 wpm','48 wpm','50 wpm','52 wpm','55 wpm','58 wpm','60 wpm'], state="readonly", width=30)
            wpm_sentences_combobox.set('20 wpm')  # Set default value
            wpm_sentences_combobox.grid(row=9, column=0, columnspan=5, pady=10)
            self.wpm_sentences_combobox = wpm_sentences_combobox
            ttk.Button(self.master,
           text="Start Button",
           command=self.agreement_sentences_button).grid(row=13, columnspan=5, pady=20)
            ttk.Button(self.master,
          text="Stop Button",
          command=self.agreement_sentences_button_stop).grid(row=14, columnspan=5, pady=20)
            self.result_sentences_text = tk.Text(self.master, height=28, width=55)
            self.result_sentences_text.grid(row=11, column=0, columnspan=5)
            sentences_label = tk.Label(self.master, text="Auto choose the highest sentences.")
            sentences_label.grid(row=1, column=0)

    def checkbox_sentences_changed(self,option):
        result = self.sentences_checkbox_vars[option].get()
        
        if result == "agree":
            self.checked_checkboxes.append(option)
        else:
            if option in self.checked_checkboxes:
                self.checked_checkboxes.remove(option)

        checked_sentences = [sentences for sentences in self.checked_checkboxes ]
        checked_text = ", ".join(checked_sentences)

        self.result_sentences_text.delete(1.0, tk.END)  # Clear previous text

    def sentences(self,wpm):

        self.result_sentences_text.delete(1.0, tk.END)  # Clear previous text
        liste = []
        if self.sentences_checkbox_vars["Top 600 words"].get() == "agree":
            liste = words_top_600.top_600_words

        elif self.sentences_checkbox_vars["Top 200 words"].get() == "agree":
            liste = words_top_200.top_200_words

        elif self.sentences_checkbox_vars["Top 100 words"].get() == "agree":
            liste = words_top_100.top_100_words

        elif self.sentences_checkbox_vars["8 words"].get() == "agree":
            liste = words_8.sentences_8

        elif self.sentences_checkbox_vars["7 words"].get() == "agree":
            liste = words_7.sentences_7

        elif self.sentences_checkbox_vars["6 words"].get() == "agree":
            liste = words_6.sentences_6
        
        elif self.sentences_checkbox_vars["5 words"].get() == "agree":
            liste = words_5.sentences_5   

        elif self.sentences_checkbox_vars["4 words"].get() == "agree":
            liste = words_4.sentences_4
        
        elif self.sentences_checkbox_vars["3 words"].get() == "agree":
            liste = words_3.sentences_3

        elif self.sentences_checkbox_vars["2 words"].get() == "agree":
            liste = words_2.sentences_2
        
    
        for i in range(25):
            selected_sentences = [sentences for sentences in liste]
            
            if selected_sentences:
                bog = rand.choice(selected_sentences)
            
                for c in bog:
                    c = c.upper()
                    cp.play(c,wpm)
            if self.stop_sentences:
                break  
            self.result_sentences_text.insert(tk.END, bog + "\n")

            
            time.sleep(1)
            