#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Will Skywalker
# Email: cxbats@gmail.com

# License: Apache

import os
from sys import argv, exit
from threading import Thread
from time import sleep

# import Tkinter as Tk
# import tkFont
# from tkFileDialog import askopenfilename, askdirectory
from PIL import Image, ImageTk

from facepp_python_sdk.facepp import API, File
from myMail import send_a_mail


API_KEY = 'd493d00d51c972ff9dbcc7cf7c038c2c' 
API_SECRET = 'HjmsDT4WZqOU0xzFfmO_0uCQXyLdR8Tw'
GROUP_NAME = 'hackathon'
api = API(API_KEY, API_SECRET)





class FaceWizard(object):


    def __init__(self, gui=True, cwd=None, directory=None):
        # self._root = Tk.Tk()
        # self._root.title('Face Wizard v0.1')
        
        self._photo = None
        self._cwd = cwd
        self._directory = directory

        # if gui:
        #     self._banner = Tk.Label(self._root, fg='blue',
        #         font=tkFont.Font(family='Helvetica', size=24, 
        #             weight='bold'), text='Face Wizard').grid(row=0)

        #     # Tk.Label(self._root,
        #     #     font=tkFont.Font(family='Helvetica', size=12,), 
        #     #     text='Choose a photo to train:').grid(row=0, column=3)


        #     self._dir_input = Tk.Entry(self._root, width=40,
        #         textvariable=self._cwd)
        #     self._dir_input.grid(row=2, column=0, columnspan=6)
        #     self._choose_button = Tk.Button(text="Choose...",
        #         command=self.open_file, width=8).grid(row=2, column=6)

        #     Tk.Label(self._root,
        #         font=tkFont.Font(family='Helvetica', size=12, 
        #             ), text='Or choose directory to monitor:').grid(row=3)

        #     self._pwd_input = Tk.Entry(self._root, width=40,
        #         textvariable=self._cwd)
        #     self._pwd_input.grid(row=4, column=0, columnspan=6)
        #     self._choose_button = Tk.Button(text="Choose...",
        #         command=self.choose_directory, width=8).grid(row=4, column=6)


        #     self._upload_button = Tk.Button(text='Upload', 
        #         command=self.upload_photo, width=6).grid(row=2, column=7)
        #     self._monitor_button = Tk.Button(text='Monitor', 
        #         command=self.monitor_directory, width=6)
        #     self._monitor_button.grid(row=4, column=7)


    def open_file(self):
        self._cwd = askopenfilename()
        self._dir_input.delete(0, 'end')
        self._dir_input.insert(index=0, 
            string=self._cwd)
        self._photo = ImageTk.PhotoImage(Image.open(self._cwd))
        self._imageshow = Tk.Label(image=self._photo, height=400, 
            width=400).grid(row=1, column=0, columnspan=6)


    def choose_directory(self):
        self._directory = askdirectory()
        self._pwd_input.delete(0, 'end')
        self._pwd_input.insert(index=0, 
            string=self._directory)


    def upload_photo(self):
        detalla = api.detection.detect(img=File(self._cwd))
        if detalla['face']:
            send_a_mail('asen_sdu@yeah.net', 'A new face detacted', detalla)
            rst = api.recognition.identify(group_name=GROUP_NAME, 
                img=File(self._cwd))
            print 'recognition result', rst
            print '=' * 60
            print 'The person with highest confidence:', \
            rst['face'][0]['candidate'][0]['person_name']
        else:
            print 'No face.'

    def monitor_directory(self):
        # self._monitor_button.configure(text='Stop', 
        #     command=self.reset)
        waits = []
        if self._directory:
            nlp = Thread(target=self.uploadPhotod)
            nlp.start()
            print 'Monitoring...'
            # nlp.join()

        # self._monitor_button.configure(text='Monitor', 
        #     command=self.monitor_directory)


    def uploadPhotod(self):
        ls = set(os.listdir(self._directory))
        while self._directory:
            newfile = set(os.listdir(self._directory)) - ls
            if newfile:
                print 'New file: ', newfile
                ls = set(os.listdir(self._directory))
                for f in newfile:
                    if f.endswith(('.jpg', '.jpeg')):
                        detalla = api.detection.detect(File(self._directory+f))
                        rst = api.recognition.identify(group_name=GROUP_NAME, 
                            img=File(self._directory+f))
                        print 'recognition result', rst
                        print '=' * 60
                        print 'The person with highest confidence:', \
                        rst['face'][0]['candidate'][0]['person_name']

            sleep(5)
        # self._monitor_button.configure(text='Monitor', 
        #     command=self.monitor_directory)


    def reset(self):
        self._directory = None

    # def run(self):
    #     self._root.mainloop()



# class popupWindow(object):

#     def __init__(self, father):
#         top = self.top = Tk.Toplevel(father)
#         self.input_row = Tk.Label(top, text="Input the Name:")
#         self.e = Tk.Entry(top)
#         self.e.pack()
#         self.b = Tk.Button(top, text='OK', command=self.cleanup)
#         self.b.pack()

#     def cleanup(self):
#         self.value = self.e.get()
#         self.top.destroy()





def main():
    args = argv[1:]

    if not args:
        print 'usage: dir'
        exit(1)


    todir = args[0]


    ft = FaceWizard(cwd=todir)
    ft.upload_photo()

if __name__ == '__main__':
    main()


