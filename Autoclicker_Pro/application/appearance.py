from tkinter.font import Font


def add_options(root):
    default_font = Font(family="Helvetica", size=15)
    root.option_add("*Font", default_font)
    root.option_add("*Label.background", '#2E2E2E')
    root.option_add("*Label.foreground", '#D3CEC4')
    root.option_add("*Entry.background", '#2E2E2E')
    root.option_add("*Entry.foreground", '#D3CEC4')
    root.option_add('*TCombobox*Listbox.background', '#2E2E2E')
    root.option_add('*TCombobox*Listbox.foreground', '#D3CEC4')
    root.option_add('*TCombobox*Listbox.selectBackground', '#454545')
    root.option_add('*TCombobox*Listbox.selectForeground', '#D3CEC4')
