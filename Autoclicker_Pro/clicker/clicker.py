import threading
from random import *
from pyautogui import *
import clicker.helpers as helpers
from pynput.keyboard import Controller, Key


class Clicker:
    def __init__(self, app):
        self.tfList = app.tfList
        self.combobox = app.myCombo
        self.delay = 0
        self.staticDelay = 0
        self.double_click_delay = 0
        self.clicking = False
        self.root = app.master
        self.controller = Controller()
        self.app = app
        self.threadList = []

    def start_clicking(self):
        print("Start button pressed")
        self.root.focus_set()
        self.staticDelay = (int(self.tfList[0].get() or 0) * 60000 +
                            (int(self.tfList[1].get() or 0) * 1000) +
                            (int(self.tfList[2].get() or 0)))

        if self.staticDelay == 0:
            return

        for tf in self.tfList:
            if tf.get() == '':
                print("test")
                self.tfList[4].insert(0, "123")
                tf.insert(0, "0")

        self.double_click_delay = randint(128, 315) / 1000
        print(self.combobox.get())
        if self.combobox.get() == "Left click":
            self.clicking = True
            self.update_delay()
            self.left_click_loop()
            self.start_timer(int(self.tfList[6].get()))

        elif self.combobox.get() == "Double click":
            print("testest")
            self.clicking = True
            self.update_delay()
            self.double_click_loop()
            self.start_timer(int(self.tfList[6].get()))

    # Stop clicking
    def stop_clicking(self):
        self.root.focus_set()
        self.clicking = False
        for thread in self.threadList:
            thread.cancel()
            thread.join()
        self.threadList.clear()

    # Start clicking with delay calculated by the calculate_new_delay function
    def left_click_loop(self):
        if self.clicking:
            timer = threading.Timer(self.delay, self.left_click_loop)
            timer.daemon = True
            timer.start()
            click()
            self.update_delay()

    # Start double clicking with delay calculated by the calculate_new_delay function
    def double_click_loop(self):
        if self.clicking:
            timer = threading.Timer(self.delay, self.double_click_loop)
            timer.daemon = True
            timer.start()
            self.double_click()
            self.update_delay()

    # Double click (delay between clicks from 128ms to 315ms)
    def double_click(self):
        if self.clicking:
            timer = threading.Timer(self.double_click_delay, click)
            timer.daemon = True
            timer.start()
            click()
            self.update_doubleclick_delay()

    # Start duration timer
    def start_timer(self, seconds):
        if not seconds == 0:
            timer = threading.Timer(seconds, self.app.stop_button_function)
            timer.daemon = True
            self.threadList.append(timer)
            timer.start()

    # Update delay using calculate_new_delay
    def update_delay(self):
        self.delay = helpers.calculate_new_delay(self.staticDelay, self.tfList)

    # Update doubleclick delay using calculate_new_doubleclick_delay
    def update_doubleclick_delay(self):
        self.double_click_delay = helpers.calculate_new_doubleclick_delay()
