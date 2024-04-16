import tkinter as tk
from tkinter import ttk
import random as rand
import threading
import cw_play as cp
import time

class LettersApp:
    def __init__(self, master):
        self.master = master
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.checkbox_vars = {}
        self.stop_letter = False
        self.checked_checkboxes = []
        self.create_widgets()
        

    
    def agreement_letter_button(self):
        selected_value = self.wpm_combobox.get()
        wpm = int(''.join(filter(str.isdigit, selected_value)))
        self.result_letter_text.delete(1.0, tk.END)  # Clear previous text
        self.stop_letter = False
        threading.Thread(target=self.letter, args=(wpm,)).start()

    def agreement_letter_button_stop(self):
        self.stop_letter = True

    def letter(self, wpm):
        
        for j in range(20):
            output_text = ""
            for i in range(5):
                selected_letters = [letter for letter, value in self.checkbox_vars.items() if value.get() == 'agree']
                if selected_letters:
                    bog = rand.choice(selected_letters)
                    cp.play(bog, wpm)
                    output_text += bog + " "
                
            self.result_letter_text.insert(tk.END, output_text + "\n")
            self.master.update_idletasks()
            time.sleep(1)
            if self.stop_letter:
                break

    def create_widgets(self):
        # Initialize letter checkboxes
        for idx, letter in enumerate(self.alphabet):
            self.checkbox_vars[letter] = tk.StringVar()
            self.checkbox_vars[letter].set('disagree')
            row_num = idx // 5
            col_num = idx % 5

            ttk.Checkbutton(self.master,
                            text=letter,
                            command=lambda l=letter: self.checkbox_changed(l),
                            variable=self.checkbox_vars[letter],
                            onvalue='agree',
                            offvalue='disagree').grid(row=row_num + 3, column=col_num)

        wpm_combobox = ttk.Combobox(self.master, values=['15 wpm', '18 wpm', '20 wpm', '22 wpm','25 wpm', '28 wpm','30 wpm','32 wpm','35 wpm','38 wpm','40 wpm','42 wpm','45 wpm','48 wpm','50 wpm','52 wpm','55 wpm','58 wpm','60 wpm'], state="readonly", width=30)
        wpm_combobox.set('20 wpm')  # Set default value
        wpm_combobox.grid(row=9, column=0, columnspan=5, pady=10)
        self.wpm_combobox = wpm_combobox

        ttk.Button(self.master,
                   text="Start Button",
                   command=self.agreement_letter_button).grid(row=12, column=0, columnspan=5, pady=20)
        ttk.Button(self.master,
                   text="Stop Button",
                   command=self.agreement_letter_button_stop).grid(row=13, column=0, columnspan=5, pady=20)
        self.result_letter_text = tk.Text(self.master, height=20, width=20)
        self.result_letter_text.grid(row=11, column=0, columnspan=5)
        self.result_letter_text.delete(1.0, tk.END)  # Clear previous text

    # Function to handle the "Select All" checkbox
    def select_all(self):
        for letter in self.alphabet:
            self.checkbox_vars[letter].set('agree')

    # Function to handle the "Unselect All" checkbox
    def unselect_all(self):
        for letter in self.alphabet:
            self.checkbox_vars[letter].set('disagree')

    def checkbox_changed(self, letter):
        pass

