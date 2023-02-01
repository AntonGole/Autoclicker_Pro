from tkinter import *


def create_background_frames(tFrame, cFrame):
    tempFrame = Frame(tFrame)
    tempFrame.grid(row=2, column=1)
    tempFrame.configure(bg='#ECC299', width=142, height=33)
    tempFrame2 = Frame(tFrame)
    tempFrame2.grid(row=3, column=1)
    tempFrame2.configure(bg='#ECC299', width=142, height=33)
    tempFrame3 = Frame(tFrame)
    tempFrame3.grid(row=4, column=1)
    tempFrame3.configure(bg='#ECC299', width=142, height=33)
    tempFrame4 = Frame(tFrame)
    tempFrame4.grid(row=2, column=2)
    tempFrame4.configure(bg='#ECC299', width=142, height=33)
    tempFrame5 = Frame(tFrame)
    tempFrame5.grid(row=3, column=2)
    tempFrame5.configure(bg='#ECC299', width=142, height=33)
    tempFrame6 = Frame(tFrame)
    tempFrame6.grid(row=4, column=2)
    tempFrame6.configure(bg='#ECC299', width=142, height=33)
    tempFrame6 = Frame(tFrame)
    tempFrame6.grid(row=3, column=3, padx=(47, 0), sticky=W)
    tempFrame6.configure(bg='#ECC299', width=142, height=33)
    tempFrame7 = Frame(cFrame)
    tempFrame7.grid(row=1, column=2, pady=(0, 0), sticky=W)
    tempFrame7.configure(bg='#ECC299', width=340, height=33)


def setup_time_entries(tfList):
    tfList[0].grid(row=2, column=1, pady=10)
    tfList[1].grid(row=3, column=1, pady=10)
    tfList[2].grid(row=4, column=1, pady=10)
    tfList[3].grid(row=2, column=2, pady=10)
    tfList[4].grid(row=3, column=2, pady=10)
    tfList[5].grid(row=4, column=2, pady=10)
    tfList[6].grid(row=3, column=3, pady=10, padx=(50, 0), sticky=W)


def create_labels(tFrame, cFrame):
    static_label = Label(tFrame, text="Time delay", width=12)
    static_label.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), columnspan=1)
    random_label = Label(tFrame, text="Random delay", width=12)
    random_label.grid(row=1, column=2, padx=(10, 10), pady=(10, 10), columnspan=1)
    duration_label = Label(tFrame, text="Clicking duration (seconds)", width=23)
    duration_label.grid(row=2, column=3, padx=(50, 0), pady=(10, 10), columnspan=2, sticky=W)
    info_label_one = Label(tFrame, text="0 = infinite", width=9)
    info_label_one.grid(row=3, column=4, padx=(17, 0), pady=(10, 10), columnspan=1, sticky=W)
    info_label_two = Label(cFrame, text="Configure start/stop key", width=20)
    info_label_two.grid(row=0, column=2, padx=(0, 0), pady=(10, 0), columnspan=1, sticky=W)

    min_label = Label(tFrame, text="Minutes", width=9)
    min_label.grid(row=2, column=0, padx=(10, 10), pady=10, sticky=W)
    sec_label = Label(tFrame, text="Seconds", width=9)
    sec_label.grid(row=3, column=0, padx=(10, 10), pady=10, sticky=W)
    ms_label = Label(tFrame, text="Milliseconds", width=9)
    ms_label.grid(row=4, column=0, padx=(10, 10), pady=10, sticky=W)

