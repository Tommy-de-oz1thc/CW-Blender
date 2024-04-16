import tkinter as tk
from tkinter import ttk
import random as rand
import threading
import cw_play as cp
import time
import us_states as us
import digit_2 as dig_2
import digit_3 as dig_3
import digit_4 as dig_4
import names_cwt as cwt
import names_sst as sst
import digit_challenger as challenger
import comment_qso as qso
import calls_cqww as cqww
import calls_cwops as cwops
import callsigns as calls

class RadioApp:
    def __init__(self, master):
        self.master = master
        self.radio_checkbox_vars = {}  
        self.checked_checkboxes = []
        self.radio_list = ["US-states","2 digit","3 digit","4 digit","cwt names","sst names","cwops Calls","cqww qso","digit challenger","comment qso","Callsigns"]
        self.create_widgets()

    def checkbox_radio_changed(self,option):
        result = self.radio_checkbox_vars[option].get()
        
        if result == "agree":
            self.checked_checkboxes.append(option)
        else:
            if option in self.checked_checkboxes:
                self.checked_checkboxes.remove(option)

        checked_radio = [radio for radio in self.checked_checkboxes ]
        checked_text = ", ".join(checked_radio)

        self.result_radio_text.delete(1.0, tk.END)  # Clear previous text

    def agreement_radio_button(self):
        selected_value = self.wpm_radio_combobox.get()
        wpm = int(''.join(filter(str.isdigit, selected_value)))
        self.result_radio_text.delete(1.0, tk.END)  # Clear previous text
        self.stop_radio = False
        threading.Thread(target=self.radio, args=(wpm,)).start()  # Note the comma after (wpm)

    def agreement_radio_button_stop(self):
        self.stop_radio = True

    def create_widgets(self):
        for i, radio in enumerate(self.radio_list):
            self.radio_checkbox_vars[radio] = tk.StringVar()
            self.radio_checkbox_vars[radio].set('disagree')
            row_num = i // 5
            col_num = i % 5
            ttk.Checkbutton(self.master,
                        text=radio,
                        command=lambda w=radio: self.checkbox_radio_changed(w),
                        variable=self.radio_checkbox_vars[radio],
                        onvalue='agree',
                        offvalue='disagree').grid(row=row_num + 3, column=col_num)
        wpm_radio_combobox = ttk.Combobox(self.master, values=['15 wpm', '18 wpm', '20 wpm', '22 wpm','25 wpm', '28 wpm','30 wpm','32 wpm','35 wpm','38 wpm','40 wpm','42 wpm','45 wpm','48 wpm','50 wpm','52 wpm','55 wpm','58 wpm','60 wpm'], state="readonly", width=30)
        wpm_radio_combobox.set('20 wpm')  # Set default value
        wpm_radio_combobox.grid(row=9, column=0, columnspan=5, pady=10)
        self.wpm_radio_combobox = wpm_radio_combobox
        ttk.Button(self.master,
           text="Start Button",
           command=self.agreement_radio_button).grid(row=12, columnspan=5, pady=20)
        ttk.Button(self.master,
          text="Stop Button",
          command=self.agreement_radio_button_stop).grid(row=13, columnspan=5, pady=20)
        self.result_radio_text = tk.Text(self.master, height=26, width=35)
        self.result_radio_text.grid(row=11, column=0, columnspan=5)
        radio_label = tk.Label(self.master, text="Auto choose the highest radio.")
        radio_label.grid(row=1, column=0)

    def radio(self,wpm):
        self.result_radio_text.delete(1.0, tk.END)  # Clear previous text
        liste = []
        if self.radio_checkbox_vars["US-states"].get() == "agree":
            liste = us.us_states

        elif self.radio_checkbox_vars["2 digit"].get() == "agree":
            liste = dig_2.digit_2

        elif self.radio_checkbox_vars["3 digit"].get() == "agree":
            liste = dig_3.digit_3

        elif self.radio_checkbox_vars["4 digit"].get() == "agree":
            liste = dig_4.digit_4

        elif self.radio_checkbox_vars["cwt names"].get() == "agree":
            liste = cwt.names_cwt

        elif self.radio_checkbox_vars["sst names"].get() == "agree":
            liste = sst.names_sst

        elif self.radio_checkbox_vars["cwops Calls"].get() == "agree":
            liste = cwops.calls_cwops

        elif self.radio_checkbox_vars["digit challenger"].get() == "agree":
            liste = challenger.digit_challenger

        elif self.radio_checkbox_vars["comment qso"].get() == "agree":
            liste = qso.comment_qso

        elif self.radio_checkbox_vars["cqww qso"].get() == "agree":
            liste = cqww.calls_cqww

        elif self.radio_checkbox_vars["Callsigns"].get() == "agree":
            liste = calls.callsigns

        for i in range(25):
            selected_radio = [radio for radio in liste]
            
            if selected_radio:
                bog = str(rand.choice(selected_radio))
                
                for c in bog:
                    
                    c = c.upper()
                    cp.play(c,wpm)
            if self.stop_radio:
                break  
            self.result_radio_text.insert(tk.END, bog + "\n")

            
            time.sleep(1)