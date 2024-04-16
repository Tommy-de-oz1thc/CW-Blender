import tkinter as tk
from tkinter import ttk
import random
import cw_play as cp
import time

class GuessLettersApp:
    def __init__(self, master):
        self.master = master
        self.large_font = ('Helvetica', 14)
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.counters = {letter: {'correct': 0, 'incorrect': 0} for letter in self.letters}
        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        self.start_button = tk.Button(self.master, text="Start", command=self.new_selected_letter, font=self.large_font)
        self.start_button.grid(row=0, column=0, columnspan=4, pady=10)

        self.label = tk.Label(self.master, text="", font=self.large_font)
        self.label.grid(row=3, column=0, columnspan=4, pady=10)

        self.create_counters_labels()

        self.color_box = tk.Canvas(self.master, width=350, height=50, bg='black')
        self.color_box.grid(row=1, column=1, pady=10)

        self.wpm_guess_combobox = ttk.Combobox(self.master, values=['15 wpm', '18 wpm', '20 wpm', '22 wpm','25 wpm', '28 wpm','30 wpm','32 wpm','35 wpm','38 wpm','40 wpm','42 wpm','45 wpm','48 wpm','50 wpm','52 wpm','55 wpm','58 wpm','60 wpm'], state="readonly", width=30)
        self.wpm_guess_combobox.set('20 wpm')  # Set default value
        self.wpm_guess_combobox.grid(row=1, column=0, columnspan=1, pady=10)

    def create_counters_labels(self):
        for i, letter in enumerate(self.letters):
            label = tk.Label(self.master, text=f"{letter}: Correct guesses - 0, Incorrect guesses - 0", font=self.large_font)
            label.grid(row=i // 3 + 4, column=i % 3, padx=5, pady=5)  # Adjust the number of columns here
            setattr(self, f"{letter}_label", label)

    def update_counters_labels(self):
        for letter in self.letters:
            correct = self.counters[letter]['correct']
            incorrect = self.counters[letter]['incorrect']
            label = getattr(self, f"{letter}_label")
            label.config(text=f"{letter}: Correct guesses - {correct}, Incorrect guesses - {incorrect}")

    def bind_events(self):
        self.master.bind('<Key>', self.on_key)  # Bind Key event to on_key

    def on_key(self, event):
        key_pressed = event.char.upper()

        if key_pressed and hasattr(self, 'color_box'):
            if key_pressed == self.selected_letter:
                self.counters[self.selected_letter]['correct'] += 1
                self.color_box.config(bg='green')  # Change box color to green for correct key
            else:
                self.counters[self.selected_letter]['incorrect'] += 1
                self.color_box.config(bg='red')  # Change box color to red for incorrect key

            self.update_counters_labels()
            self.master.after(200, self.reset_color_and_new_letter)  # Schedule reset and new letter after 1000 milliseconds (1 second)

    def reset_color_and_new_letter(self):
        self.color_box.config(bg='black')  # Reset box color to black
        self.new_selected_letter()


    def new_selected_letter(self):
        self.color_box.config(bg='black')  # Reset box color to black
        self.selected_letter = random.choice(self.letters)
        selected_value = self.wpm_guess_combobox.get()
        wpm = int(''.join(filter(str.isdigit, selected_value)))
        cp.play(self.selected_letter, wpm)

