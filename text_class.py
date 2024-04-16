import tkinter as tk
from tkinter import ttk
import random as rand
import threading
import cw_play as cp
import time

class TextApp:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def agreement_text_button(self):
        selected_value = self.wpm_text_combobox.get()
        wpm = int(''.join(filter(str.isdigit, selected_value)))
        
        self.stop_text = False
        threading.Thread(target=self.text, args=(wpm,)).start()  # Note the comma after (wpm)

    def agreement_text_button_stop(self):
        self.stop_text = True

    def reset(self):
        self.result_text_text.delete(1.0, tk.END)  # Clear previous text


    def create_widgets(self):
        wpm_text_combobox = ttk.Combobox(self.master, values=['15 wpm', '18 wpm', '20 wpm', '22 wpm','25 wpm', '28 wpm','30 wpm','32 wpm','35 wpm','38 wpm','40 wpm','42 wpm','45 wpm','48 wpm','50 wpm','52 wpm','55 wpm','58 wpm','60 wpm'], state="readonly", width=30)
        wpm_text_combobox.set('20 wpm')  # Set default value
        wpm_text_combobox.grid(row=2, column=0, columnspan=5, pady=10)
        self.wpm_text_combobox = wpm_text_combobox
        self.result_text_text = tk.Text(self.master, height=25, width=60)
        self.result_text_text.grid(row=3, column=0, columnspan=5)
        text_label = tk.Label(self.master, text="Pass your text into the TextArea.")
        text_label.grid(row=1, column=0)
        
        ttk.Button(self.master,
           text="Start Button",
           command=self.agreement_text_button).grid(row=5, columnspan=5, pady=20)
        ttk.Button(self.master,
          text="Stop Button",
          command=self.agreement_text_button_stop).grid(row=6, columnspan=5, pady=20)
        ttk.Button(self.master,
          text="Reset Text",
          command=self.reset).grid(row=4, columnspan=5, pady=20)
        
    def text(self,wpm):
        loaded_text = self.result_text_text.get(1.0, tk.END)
       
        print(loaded_text)
        for t in loaded_text:
            t = t.upper()
            cp.play(t,wpm)
        
            if self.stop_text:
                break
