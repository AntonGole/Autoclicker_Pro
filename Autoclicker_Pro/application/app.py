from tkinter.ttk import Entry
from tkinter import *
from tkinter import ttk, font
import application.helpers as helpers
import pickle


class App:
    def __init__(self, master, is_valid_command, is_valid_command2):
        self.master = master
        self.is_valid_command = is_valid_command
        self.is_valid_command2 = is_valid_command2

        # Declare frame for buttons
        self.cFrame = Frame(master)
        self.cFrame.grid(row=0, column=0, columnspan=3)
        self.cFrame.configure(bg='#1D2025')

        # Declare frame for textfields, labels and comboboxes
        self.tFrame = Frame(master)
        self.tFrame.grid(row=1, column=0, columnspan=5)
        self.tFrame.configure(bg='#1D2025')

        # Create frames behind entries working as borders
        helpers.create_background_frames(self.tFrame, self.cFrame)

        # Declare combobox
        self.options = [
            "Left click",
            "Double click"
        ]

        self.combostyle_enabled = ttk.Style()
        self.combostyle_enabled.theme_create('combostyle_enabled', parent='alt', settings={'TCombobox': {'configure':
            {
                'selectbackground': '#2E2E2E',
                'selectforeground': '#D3CEC4',
                'fieldbackground': '#2E2E2E',
                'background': '#2E2E2E',
                'foreground': '#D3CEC4'}}})

        self.combostyle_disabled = ttk.Style()
        self.combostyle_disabled.theme_create('combostyle_disabled', parent='alt', settings={'TCombobox': {'configure':
            {
                'fieldbackground': 'grey',
                'background': 'grey',
                'foreground': '#404040'}}})
        self.combostyle_enabled.theme_use('combostyle_enabled')
        self.myCombo = ttk.Combobox(self.tFrame, width=15, value=self.options, state="readonly")
        self.myCombo.current(0)
        self.myCombo.grid(row=4, column=3, padx=(48, 0), pady=20, columnspan=2, sticky=W)

        # Declare text fields
        self.tfList = self.create_textfields()
        helpers.setup_time_entries(self.tfList)

        self.keyEntry = Entry(self.cFrame, validatecommand=(self.is_valid_command2, '%P', '%s'), validate='key',
                              disabledbackground="#5e5e5e", disabledforeground="#404040")
        self.keyEntry.configure(width=30, insertbackground="white", relief="flat")
        self.keyEntry.grid(row=1, column=2, padx=(3, 0), pady=(0, 0), sticky=W)
        self.keyEntry.insert(0, "None")

        self.isPicking = False
        self.unsaved_keys = set()
        self.saved_keys = set()
        self.current = set()
        self.isDone = False

        self.coordinateString = []
        self.paused = False

        # Declare functions for keyEntry
        def remove_all(event, self1=self.keyEntry):
            self.unsaved_keys.clear()
            self.saved_keys.clear()
            self.current.clear()
            self.isPicking = True
            self.isDone = False
            self1.delete(0, END)
            self.disable_buttons(self.save)

        def put_none(event, self1=self.keyEntry):
            if not self.isDone:
                self1.delete(0, END)
                self.disable_buttons(self.save)
                self.unsaved_keys.clear()
            self.isPicking = False
            if self1.get() == "":
                self1.insert(0, "None")

        def handle_keypress(event, self1=self.keyEntry):
            print("Key pressed: " + event.keysym)
            if (event.keysym == "Shift_L") or (event.keysym == "Shift_R"):
                if "Shift" not in self1.get():
                    temp = self1.get()
                    self1.delete(0, END)
                    self1.insert(0, f"{temp}Shift + ")
                else:
                    return
            elif (event.keysym == "Alt_L") or (event.keysym == "Alt_R"):
                if "Alt" not in self1.get():
                    temp = self1.get()
                    self1.delete(0, END)
                    self1.insert(0, f"{temp}Alt + ")
                else:
                    return
            elif (event.keysym == "Control_L") or (event.keysym == "Control_R"):
                if "CTRL" not in self1.get():
                    temp = self1.get()
                    self1.delete(0, END)
                    self1.insert(0, f"{temp}CTRL + ")
                else:
                    return
            else:
                temp = self1.get()
                self1.delete(0, END)
                key_name = self.convert_key_name(event.keycode, event.keysym)
                self1.insert(0, f"{temp}{key_name}")
                self.isDone = True
                self.enable_buttons(self.save)
                self1.master.focus_set()

        def handle_keyrelease(event, self1=self.keyEntry):
            print("Key released: " + event.keysym)
            if (event.keysym == "Shift_L") or (event.keysym == "Shift_R"):
                if "Shift" in self1.get():
                    temp = str(self1.get()).replace("Shift + ", "")
                    self1.delete(0, END)
                    self1.insert(0, temp)
            elif (event.keysym == "Alt_L") or (event.keysym == "Alt_R"):
                if "Alt" in self1.get():
                    temp2 = self1.get().replace("Alt + ", "")
                    self1.delete(0, END)
                    self1.insert(0, temp2)
            elif (event.keysym == "Control_L") or (event.keysym == "Control_R"):
                if "CTRL" in self1.get():
                    temp2 = self1.get().replace("CTRL + ", "")
                    self1.delete(0, END)
                    self1.insert(0, temp2)

        self.keyEntry.bind('<FocusOut>', put_none)
        self.keyEntry.bind('<KeyPress>', handle_keypress)
        self.keyEntry.bind('<KeyRelease>', handle_keyrelease)
        self.keyEntry.bind('<FocusIn>', remove_all)
        self.keyEntry.bind('<Enter>', lambda event, high=True: self.toggle_highlight(event, high))
        self.keyEntry.bind('<Leave>', lambda event, high=False: self.toggle_highlight(event, high))

        # Declare labels
        helpers.create_labels(self.tFrame, self.cFrame)

        # Declare buttons
        self.start = Button(self.cFrame, text="Start (SHIFT+F1)", disabledforeground="#404040",
                            command=self.start_button_function, bg="#BB86FC")
        self.start.configure(height=2, width=18, activebackground="#cea6ff", cursor="hand2")
        self.start.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), columnspan=1, rowspan=2, sticky=W)
        self.start.bind('<Enter>', lambda event, high=True: self.toggle_button_highlight(event, high))
        self.start.bind('<Leave>', lambda event, high=False: self.toggle_button_highlight(event, high))

        self.stop = Button(self.cFrame, text="Stop (SHIFT+F2)", disabledforeground="#404040",
                           command=self.stop_button_function, bg="#5e5e5e")
        self.stop.configure(height=2, width=18, activebackground="#cea6ff", cursor="arrow")
        self.stop.bind('<Enter>', lambda event, high=True: self.toggle_button_highlight(event, high))
        self.stop.bind('<Leave>', lambda event, high=False: self.toggle_button_highlight(event, high))
        self.stop.grid(row=0, column=1, padx=(0, 55), pady=(10, 0), columnspan=1, rowspan=2, sticky=W)
        self.stop["state"] = DISABLED

        # Crate frame for save and remove buttons
        self.srFrame = Frame(self.tFrame)
        self.srFrame.grid(row=1, column=3, columnspan=3, sticky=W)
        self.srFrame.configure(bg='#1D2025')

        self.save = Button(self.srFrame, text="SAVE", bg="#5e5e5e", disabledforeground="#404040",
                           command=self.save_button_function)
        self.save.configure(height=1, width=8, activebackground="#cea6ff", cursor="arrow")
        self.save.bind('<Enter>', lambda event, high=True: self.toggle_button_highlight(event, high))
        self.save.bind('<Leave>', lambda event, high=False: self.toggle_button_highlight(event, high))
        self.save.grid(row=0, column=0, padx=(10, 0), sticky=W)
        self.save["state"] = DISABLED

        self.delete = Button(self.srFrame, text="REMOVE", bg="#BB86FC", disabledforeground="#404040",
                             command=self.delete_button_function)
        self.delete.configure(height=1, width=8, activebackground="#cea6ff", cursor="hand2")
        self.delete.bind('<Enter>', lambda event, high=True: self.toggle_button_highlight(event, high))
        self.delete.bind('<Leave>', lambda event, high=False: self.toggle_button_highlight(event, high))
        self.delete.grid(row=0, column=1, padx=(10, 0), sticky=W)

    # Create necessary text fields and bind them to functions remove_all, add_zero and remove_zero
    def create_textfields(self):
        tfList = []
        for i in range(7):
            tf = Entry(self.tFrame, validatecommand=(self.is_valid_command, '%P', '%s'), validate='key',
                       disabledbackground="#5e5e5e", disabledforeground="#404040", relief="flat",
                       insertbackground="white")
            tf.configure(width=12)
            tfList.append(tf)

            def remove_all(event, self=tf):
                self.delete(0, END)

            def add_zero(event, self=tf):
                if self.get() == "":
                    self.insert(0, "0")

            def remove_zero(event, self=tf):
                if self.get() == "0":
                    self.delete(0, END)

            def enter_press(event, self=tf):
                self.master.focus_set()

            tf.insert(0, "0")
            tf.bind('<FocusIn>', remove_all)
            tf.bind('<FocusOut>', add_zero)
            tf.bind('<KeyPress>', remove_zero)
            tf.bind('<Return>', enter_press)
            tf.bind('<Enter>', lambda event, high=True: self.toggle_highlight(event, high))
            tf.bind('<Leave>', lambda event, high=False: self.toggle_highlight(event, high))
        return tfList

    # Function to be called when exit button is pressed (save data)
    def exit_function(self):
        self.save_data()
        self.clicker.clicking = False
        self.master.destroy()

    # Save all values from entries to binary file
    def save_data(self):
        numbers = []
        for number in self.tfList:
            if str(number.get()).isdigit():
                numbers.append(int(number.get()))
            else:
                numbers.append(0)
        numbers.append(self.myCombo.get())
        numbers.append(self.keyEntry.get())
        numbers.append(self.saved_keys)
        pickle.dump(numbers, open("data.dat", "wb"))

    # Load all values from binary file to entries
    def load_data(self):
        numbers = pickle.load(open("data.dat", "rb"))
        try:
            for x in range(7):
                self.tfList[x].delete(0, END)
                self.tfList[x].insert(0, numbers[x])
            self.myCombo.current(self.options.index(numbers[7]))
            self.keyEntry.delete(0, END)
            self.keyEntry.insert(0, numbers[8])
            self.saved_keys = numbers[9]
        except:
            print("All values not found")

    # Toggle states of widgets to be NORMAL or DISABLED
    def toggle_widgets(self):
        # If start is disabled, enable all widgets but stop
        if self.start["state"] == DISABLED:
            self.enable_buttons(self.start)
            self.disable_buttons(self.stop)
            self.start["text"] = "Start (SHIFT+F1)"
            self.myCombo["state"] = "readonly"
            self.combostyle_enabled.theme_use('combostyle_enabled')
            for x in self.tfList:
                x["state"] = NORMAL
                x["cursor"] = "xterm"
        # If start is enabled, disable all widgets but stop
        else:
            self.enable_buttons(self.stop)
            self.disable_buttons(self.start)
            self.start["text"] = "Clicking"
            self.myCombo["state"] = "disabled"
            self.combostyle_disabled.theme_use('combostyle_disabled')
            for x in self.tfList:
                x["state"] = DISABLED
                x["cursor"] = "arrow"

    # Enable specified buttons
    def enable_buttons(self, *buttons):
        for button in buttons:
            button.configure(bg="#BB86FC", state=NORMAL, cursor="hand2")

    # Disable specified buttons
    def disable_buttons(self, *buttons):
        for button in buttons:
            button.configure(bg="#5e5e5e", state=DISABLED, cursor="arrow")

    # Toggle highlight of widgets on or off
    def toggle_highlight(self, event, high):
        if high and event.widget["state"] == NORMAL:
            event.widget["bg"] = "#454545"
        if not high and event.widget["state"] == NORMAL:
            event.widget["bg"] = "#2E2E2E"

    # Toggle highlight of widgets on or off
    def toggle_button_highlight(self, event, high):
        if high and event.widget["state"] == NORMAL:
            event.widget["bg"] = "#cea6ff"
        if not high and event.widget["state"] == NORMAL:
            event.widget["bg"] = "#BB86FC"

    # Remove focus from entries etc. when clicking outside the widget
    def click_event(self, event):
        x, y = self.master.winfo_pointerxy()
        widget = self.master.winfo_containing(x, y)
        if widget == self.master or widget == self.tFrame or widget != self.master.focus_get():
            self.master.focus()

    def start_button_function(self):
        if int(self.tfList[0].get() or 0) * 60000 + \
                (int(self.tfList[1].get() or 0) * 1000) + \
                (int(self.tfList[2].get() or 0)) == 0:
            return
        self.toggle_widgets()
        self.clicker.start_clicking()

    def stop_button_function(self):
        self.clicker.stop_clicking()
        self.toggle_widgets()

    def save_button_function(self):
        self.saved_keys = self.unsaved_keys
        self.disable_buttons(self.save)
        print("Saved keys: " + str(self.saved_keys))

    def delete_button_function(self):
        self.keyEntry.delete(0, END)
        self.keyEntry.insert(0, "None")
        self.saved_keys.clear()
        self.unsaved_keys.clear()
        self.disable_buttons(self.save)

    def convert_key_name(self, keycode, keysym):
        print(chr(keycode))
        print("Converting keycode: " + str(keycode))
        print("Converting keysym: " + keysym)
        if (keycode in range(48, 58)) or (keycode in range(65, 91)):
            return chr(keycode)
        elif keycode == 187:
            return "PLUS"
        elif keycode == 219:
            return "MULTI_KEY"
        elif keycode == 226:
            return "<"
        elif keycode == 33:
            return "PGUP"
        elif keycode == 34:
            return "PGDN"
        elif keycode == 45:
            return "INS"
        elif keycode == 46:
            return "DEL"
        elif keycode == 220:
            return "§"
        elif keycode == 188:
            return ","
        elif keycode == 190:
            return "."
        elif keycode == 189:
            return "-"
        elif keycode in range(96, 106):
            return f"NUM {keysym}"
        elif keycode == 106:
            return f"NUM *"
        elif keycode == 111:
            return f"NUM /"
        elif keycode == 107:
            return f"NUM PLUS"
        elif keycode == 27:
            return "ESC"
        elif keycode == 191:
            return "'"
        elif keycode == 221:
            return "Å"
        elif keycode == 222:
            return "Ä"
        elif keycode == 192:
            return "Ö"
        elif keysym == "Win_L":
            return ""

        return keysym.upper().replace("_", " ")

    def update_window(self, event):
        return "break"
