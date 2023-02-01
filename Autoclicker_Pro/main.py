from tkinter.font import Font

import application.appearance as appearance
from application.app import App
from tkinter import *
from clicker.clicker import *
from pynput.keyboard import Listener, Controller, Key


# Function for listening to key presses, will be running on a different thread
def input_thread(app):
    # Handling on keypress and on keyrelease event
    def on_press(key):
        if app.isPicking:
            app.unsaved_keys.add(key)
            print("Adding key: " + str(key))
            print("Saved keys: ")
            print(app.unsaved_keys)
        else:
            print("Key pressing: " + str(key))

            if key in app.saved_keys:
                app.current.add(key)
                print("Current after press: " + str(app.current))
                if app.current == app.saved_keys:
                    if app.start["state"] == NORMAL:
                        app.start_button_function()
                        app.current.clear()
                    else:
                        app.stop_button_function()

    def on_release(key):
        if app.isPicking:
            try:
                app.unsaved_keys.remove(key)
                app.current.remove(key)
                print("Removing key: " + str(key))
                print("Saved keys: ")
                print(app.unsaved_keys)
            except KeyError:
                pass

        else:
            try:
                if key in app.current:
                    app.current.clear()

            except KeyError:
                pass

    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()


# Check if character typed is an integer and that only one "0" is typed in the beginning of the number
def is_valid_input(new, old):
    try:
        int(new)
        if new[-1] == "0" and old == "0":
            return False
        elif len(new) > 6:
            return False
        else:
            return True
    except ValueError:
        if new == '':
            return True
        else:
            return False


# Check if character typed is an integer and that only one "0" is typed in the beginning of the number
def is_valid_key(new, old):
    if (old in new) and old != "":
        return False
    if len(new) == len(old) - 1 and new != "":
        return False
    return True


def main():
    # Create new root
    root = Tk()

    # Register is_valid_input to root as is_valid_command(for time entries)
    # and is_valid_key to root as is_valid_command2
    is_valid_command = root.register(is_valid_input)
    is_valid_command2 = root.register(is_valid_key)

    # Add default options for different widgets inside root
    appearance.add_options(root)

    # set window title
    root.title('Autoclicker Pro')

    # set window width and height
    root.geometry("850x290")
    root.resizable(False, False)
    # set window background color
    root.configure(bg='#1D2025')

    # move window center
    winWidth = root.winfo_reqwidth()
    winwHeight = root.winfo_reqheight()
    posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
    posDown = int(root.winfo_screenheight() / 2 - winwHeight / 2)
    root.geometry("+{}+{}".format(posRight, posDown))

    # Change icon of application
    root.iconbitmap("images/click.ico")

    # Create new instance of class App and pass root, is_valid_command
    app = App(root, is_valid_command, is_valid_command2)
    app.clicker = Clicker(app)

    # Start thread for listening to key inputs
    thread = threading.Thread(target=lambda: input_thread(app), args=(), daemon=True)
    thread.start()

    # Adding functions to root
    root.protocol('WM_DELETE_WINDOW', app.exit_function)
    root.bind("<Button-1>", app.click_event)
    root.bind("<KeyRelease>", app.update_window)

    # Load data from file
    if os.path.isfile("data.dat"):
        app.load_data()

    root.mainloop()


if __name__ == '__main__':
    main()
