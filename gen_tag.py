#!/usr/bin/python3

import os
import sys
import tkinter as tk
from tkinter import filedialog
import time
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askinteger

class GenTag:

    def __init__(self):
        self.main_window = tk.Tk()
        self.work_dir = tk.StringVar()
        
        self.select_path_frame = tk.Frame(self.main_window, width=50)
        self.work_dir_label = tk.Label(self.select_path_frame, textvariable=self.work_dir, width=40)
        self.select_button = tk.Button(self.select_path_frame, text="workdir", command=self.SelectWorkDir, width=8)
        #self.select_button['state'] = tk.DISABLED
        self.select_button.grid(row=0, column=0)
        self.work_dir_label.grid(row=0, column=1)
        self.select_path_frame.pack(expand=1, fill='x')

        self.work_mode = tk.StringVar()
        self.work_mode_frame = tk.Frame(self.main_window, width=50)
        self.work_mode_label = tk.Label(self.work_mode_frame, text="workmode", width=8)
        self.work_mode_label.grid(row=0, column=0)
        self.work_mode_button = []
        dit = {"GenXmlTag":0, "GenCodeTag":1, "Increace":2}
        for name in dit.keys():
            radiobutton = tk.Radiobutton(self.work_mode_frame, text=name, variable=self.work_mode, value=dit[name], width=10, command=self.ModeSelect)
            self.work_mode_button.append(radiobutton)
        for ii in range(len(self.work_mode_button)):
            self.work_mode_button[ii].grid(row=0, column=ii+1)
        self.blank = tk.Label(self.work_mode_frame, width=1)
        self.blank.grid(row=0, column=4)
        self.work_mode_frame.pack(expand=1, fill='x')

        self.all_button = []
        self.xml_frame = tk.Frame(self.main_window, width=50)
        self.xml_tag_button = tk.Button(self.xml_frame, text="GenXmlTag", command=self.GenXmlTag, width=8)
        self.xml_tag_button.grid(row=0, column=0)
        self.xml_ver_label = tk.Label(self.xml_frame, text="XmlVersion", width=11)
        self.xml_ver_label.grid(row=0, column=1)
        self.xml_ver_entry = tk.Entry(self.xml_frame, width=28)
        self.xml_ver_entry.grid(row=0, column=2, sticky=tk.NSEW)
        self.xml_tag_button['state'] = tk.DISABLED
        self.all_button.append(self.xml_tag_button)

        self.code_ver = tk.StringVar()
        self.code_frame = tk.Frame(self.main_window, width=50)
        self.code_tag_button = tk.Button(self.code_frame, text="GenCodeTag", command=self.GenCodeTag, width=8)
        self.code_tag_button.grid(row=0, column=0)
        self.code_ver_label = tk.Label(self.code_frame, text="CodeVersion", width=11)
        self.code_ver_label.grid(row=0, column=1)
        self.code_ver_entry = tk.Entry(self.code_frame, textvariable=self.code_ver, width=28)
        self.code_ver_entry.grid(row=0, column=2)
        self.code_ver.set(time.strftime("%Y_%m_%d", time.localtime()))
        self.code_tag_button['state'] = tk.DISABLED
        self.all_button.append(self.code_tag_button)

        self.inc_target_tag = tk.StringVar()
        self.increace_frame = tk.Frame(self.main_window, width=50)
        self.increace_button = tk.Button(self.increace_frame, text="Increace",  command=self.Increace, width=8)
        self.increace_button.grid(row=0, column=0)
        self.inc_target_tag_label = tk.Label(self.increace_frame, text="TargetTag", width=11)
        self.inc_target_tag_label.grid(row=0, column=1)
        self.inc_target_tag_combo = ttk.Combobox(self.increace_frame, textvariable=self.inc_target_tag, width=27)
        self.inc_target_tag_combo.grid(row=0, column=2)
        self.inc_target_tag_combo['value'] = os.popen("ls ~").read()
        self.increace_button['state'] = tk.DISABLED
        self.all_button.append(self.increace_button)
        
        self.file_add_frame = tk.Frame(self.main_window, width=50)
        self.file_add_button = tk.Button(self.file_add_frame, text="AddFile", width=8, command=self.AddFile)
        self.file_list = tk.Text(self.file_add_frame, width=40, height=10)
        self.file_add_button.grid(row=0, column=0)
        self.file_list.grid(row=0, column=1)
        self.file_add_button['state'] = tk.DISABLED

        self.xml_frame.pack()
        self.code_frame.pack()
        self.increace_frame.pack()
        self.file_add_frame.pack()
        self.main_window.mainloop()

    def SelectWorkDir(self):
        self.work_dir.set(filedialog.askdirectory())

    def ModeSelect(self):
        for i in range(len(self.work_mode_button)):
            if (self.work_mode.get() == str(i)) :
                self.all_button[i]['state'] = tk.NORMAL
            else:
                self.all_button[i]['state'] = tk.DISABLED
        if (self.work_mode.get() != '2'):
            self.file_add_button['state'] = tk.DISABLED
        else:
            self.file_add_button['state'] = tk.NORMAL

    def GenXmlTag(self):
        self.test_val = 9
        return

    def GenCodeTag(self):
        print(self.test_val)
        return

    def Increace(self):
        return

    def AddFile(self):
        file_path = filedialog.askopenfilename(initialdir=self.work_dir.get())
        file_path = os.path.relpath(file_path, self.work_dir.get())
        if self.file_list.search(file_path, 1.0, stopindex="end"):
            messagebox.showerror(title="Error!", message="file already exist!")
            return
        version = askinteger(title="", prompt="up to version:")
        description = file_path + " " + str(version) + "\n"
        self.file_list.insert("end", description)

if __name__ == "__main__":
    GenTag()
