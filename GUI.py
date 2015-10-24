#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Will Skywalker
# Email: cxbats@gmail.com

# License: Apache

import os
from sys import argv
from threading import Thread

import Tkinter as Tk
import tkFont
from tkFileDialog import askopenfilename, askdirectory
from PIL import Image, ImageTk

from facepp_python_sdk.facepp import API, File


API_KEY = 'd493d00d51c972ff9dbcc7cf7c038c2c' 
API_SECRET = 'HjmsDT4WZqOU0xzFfmO_0uCQXyLdR8Tw'
api = API(API_KEY, API_SECRET)


def uploadPhoto(photo):
    pass


class FaceWizard(object):


    def __init__(self, gui=True, cwd=None, directory=None):
        self._root = Tk.Tk()
        self._root.title('Face Wizard v0.1')
        
        self._photo = None
        self._cwd = cwd
        self._directory = directory

        if gui:
            self._banner = Tk.Label(self._root, fg='blue',
                font=tkFont.Font(family='Helvetica', size=24, 
                    weight='bold'), text='Face Wizard').grid()

            self._dir_input = Tk.Entry(self._root, width=40,
                textvariable=self._cwd)
            self._dir_input.grid(row=2, column=0, columnspan=6)
            self._choose_button = Tk.Button(text="Choose...",
                command=self.open_file, width=8).grid(row=2, column=6)

            Tk.Label(self._root,
                font=tkFont.Font(family='Helvetica', size=12, 
                    ), text='Or choose directory to monitor:').grid(row=3)

            self._pwd_input = Tk.Entry(self._root, width=40,
                textvariable=self._cwd)
            self._pwd_input.grid(row=4, column=0, columnspan=6)
            self._choose_button = Tk.Button(text="Choose...",
                command=self.choose_directory, width=8).grid(row=4, column=6)


            self._upload_button = Tk.Button(text='Upload', 
                command=self.upload_photo).grid(row=5, column=3)
            self._monitor_button = Tk.Button(text='Monitor', 
                command=self.monitor_directory).grid(row=5, column=4)


    def open_file(self):
        self._cwd = askopenfilename()
        self._dir_input.delete(0, 'end')
        self._dir_input.insert(index=0, 
            string=self._cwd)
        self._photo = ImageTk.PhotoImage(Image.open(self._cwd))
        self._imageshow = Tk.Label(image=self._photo).grid(row=1, column=0,
            columnspan=6)


    def choose_directory(self):
        self._directory = askdirectory()
        self._pwd_input.delete(0, 'end')
        self._pwd_input.insert(index=0, 
            string=self._directory)



    def upload_photo(self):
        self.w = popupWindow(self._root)
        self._root.wait_window(self.w.top)
        name = self.w.value
        details = api.detection.detect(img=File(self._cwd))
        print details
        api.person.create(person_name = name, 
            face_id = details['face'][0]['face_id'])


    def monitor_directory(self):
        self._monitor_button. = Tk.Button(text='Monitor', 
            command=self.monitor_directory).grid(row=5, column=4)
        ls = os.listdir(self._directory)
        ntd = Thread(uploadPhoto())





    def run(self):
        self._root.mainloop()



class popupWindow(object):

    def __init__(self, father):
        top = self.top = Tk.Toplevel(father)
        self.input_row = Tk.Label(top, text="Input the Name:")
        self.e = Tk.Entry(top)
        self.e.pack()
        self.b = Tk.Button(top, text='OK', command=self.cleanup)
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        self.top.destroy()




if __name__ == '__main__':
    np = FaceWizard()
    np.run()
