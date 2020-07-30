import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class Storin:

    def __init__(self, master):

        self.password = ''
        self.balance = 0
        self.address = None
        self.storage = ''
        self.date = 0
        self.pass_window = master
        self.pass_window.title('Storin')
        self.pass_window.geometry('500x300+300+150')
        self.pass_window['bg'] = 'grey'
        self.enter_pass = Entry(width=30)
        self.enter_pass.place(relx=0.20, rely=0.40, relwidth=0.40, relheight=0.07)
        entr_pass_button = Button(text='Enter', command=self.init_ui)
        entr_pass_button.place(relx=0.65, rely=0.40, relwidth=0.15, relheight=0.07)

    def init_ui(self):

        coords = self.pass_window.wm_geometry()

        if self.enter_pass.get() == self.password:
            self.pass_window.destroy()

            self.main_window = Tk()
            self.main_window.title('Operations')
            self.main_window.geometry(coords)
            self.main_window.update()

            notebook = ttk.Notebook(self.main_window)
            notebook.place(relx=0, rely=0, relwidth=1, relheight=0.93)

            get_file_tab = ttk.Frame(notebook)
            give_file_tab = ttk.Frame(notebook)
            give_mem_tab = ttk.Frame(notebook)
            exchange_tab = ttk.Frame(notebook)
            settings_tab = ttk.Frame(notebook)

            notebook.add(get_file_tab, text='       Get file        ')
            notebook.add(give_file_tab,text='       Give file       ')
            notebook.add(give_mem_tab, text='       Give memory    ')
            notebook.add(exchange_tab, text='       Exchange        ')
            notebook.add(settings_tab, text='       Settings        ')

            balance_window = Label(text=f'Balance : {self.balance}')
            balance_window.place(relx=0.05, rely=0.93)

            def update_date():
                self.date = time.ctime()
                date_window = Label(text=f'Date : {self.date}')
                date_window.place(relx=0.61, rely=0.93)
                self.main_window.after(1000, update_date)

            update_date()

            # 1 notebook
            self.get_file_pass = Entry(get_file_tab, width=25)
            self.get_file_pass.place(relx=0.25, rely=0.02, relwidth=0.50, relheight=0.08)

            get_file_find_button = Button(get_file_tab, text='Find file', command=self.choosing)
            get_file_find_button.place(relx=0.01, rely=0.02, relwidth=0.23, relheight=0.08)

            get_file_open_button = Button(get_file_tab, text='Open file', command=self.get_file_open)
            get_file_open_button.place(relx=0.76, rely=0.02, relwidth=0.23, relheight=0.08)

            result_frame = Frame(get_file_tab)
            result_frame.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.86)

            scroll_result = Scrollbar(result_frame)
            scroll_result.pack(side=RIGHT, fill=Y)

            self.get_file_result = Text(result_frame, wrap=None, yscrollcommand=scroll_result.set)
            self.get_file_result.pack(fill=BOTH)

            scroll_result.config(command=self.get_file_result.yview)

            # 2 notebook
            give_file_find_button = Button(give_file_tab, text='Find file', command=self.choosing)
            give_file_find_button.place(relx=0.05, rely=0.07, relwidth=0.20, relheight=0.08)

            num_copies_label = Label(give_file_tab, text='Number of copies')
            num_copies_label.place(relx=0.05, rely=0.24)

            num_days_label = Label(give_file_tab, text='Number of days')
            num_days_label.place(relx=0.05, rely=0.39)

            cost_per_copy_label = Label(give_file_tab, text='Cost per copy')
            cost_per_copy_label.place(relx=0.05, rely=0.54)

            give_file_name_label = Label(give_file_tab, text='Name')
            give_file_name_label.place(relx=0.05, rely=0.69)

            num_copies_entry = Entry(give_file_tab, width=20)
            num_copies_entry.place(relx=0.30, rely=0.24)

            num_days_entry = Entry(give_file_tab, width=20)
            num_days_entry.place(relx=0.30, rely=0.39)

            cost_per_copy_entry = Entry(give_file_tab, width=20)
            cost_per_copy_entry.place(relx=0.30, rely=0.54)

            give_file_name_entry = Entry(give_file_tab, width=20)
            give_file_name_entry.place(relx=0.30, rely=0.69)

            give_file_send_button = Button(give_file_tab, text='Send file', command=None)
            give_file_send_button.place(relx=0.30, rely=0.85, relwidth=0.25, relheight=0.08)

            give_file_list_frame = Frame(give_file_tab)
            give_file_list_frame.place(relx=0.60, rely=0.05, relwidth=0.40, relheight=0.95)

            scroll_give_file_list_x = Scrollbar(give_file_list_frame, orient=HORIZONTAL)
            scroll_give_file_list_x.pack(side=BOTTOM, fill=X)

            scroll_give_file_list_y = Scrollbar(give_file_list_frame)
            scroll_give_file_list_y.pack(side=RIGHT, fill=Y)

            self.give_file_list = Listbox(give_file_list_frame, selectmode=EXTENDED,
                                          xscrollcommand=scroll_give_file_list_x.set,
                                          yscrollcommand=scroll_give_file_list_y.set)
            self.give_file_list.pack(expand=True, fill=BOTH)

            scroll_give_file_list_x.config(command=self.give_file_list.xview)
            scroll_give_file_list_y.config(command=self.give_file_list.yview)

            # 5 notebook
            enter_pass_label = Label(settings_tab, text='Enter new password')
            enter_pass_label.place(relx=0.05, rely=0.10)

            repeat_pass_label = Label(settings_tab, text='Repeat new password')
            repeat_pass_label.place(relx=0.05, rely=0.25)

            self.enter_pass_entry = Entry(settings_tab, width=25)
            self.enter_pass_entry.place(relx=0.35, rely=0.10)

            self.repeat_pass_entry = Entry(settings_tab, width=25)
            self.repeat_pass_entry.place(relx=0.35, rely=0.25)

            confirm_pass_button = Button(settings_tab, text='Confirm password', command=self.enter_pass_confirming)
            confirm_pass_button.place(relx=0.71, rely=0.25, relwidth=0.25, relheight=0.08)

            address_label = Label(settings_tab, text='Enter address')
            address_label.place(relx=0.05, rely=0.40)

            self.address_entry = Entry(settings_tab, width=25)
            self.address_entry.place(relx=0.35, rely=0.40)

            confirm_address_button = Button(settings_tab, text='Confirm address', command=self.address_confirming)
            confirm_address_button.place(relx=0.71, rely=0.40, relwidth=0.25, relheight=0.08)


            self.menu = Menu(tearoff=0)

            self.menu.add_command(label='Cut', command=lambda: self.menu.focus_get().event_generate('<<Cut>>'))
            self.menu.add_command(label='Copy', command=lambda: self.menu.focus_get().event_generate('<<Copy>>'))
            self.menu.add_command(label='Paste', command=lambda: self.menu.focus_get().event_generate('<<Paste>>'))

            self.get_file_pass.bind('<Button-3>', self.text_selection)
            self.get_file_result.bind('<Button-3>', self.text_selection)
            self.address_entry.bind('<Button-3>', self.text_selection)
            self.enter_pass_entry.bind('<Button-3>', self.text_selection)
            self.repeat_pass_entry.bind('<Button-3>', self.text_selection)


    def choosing(self):

        try:
            path = filedialog.askopenfilename()
            with open(path, 'r') as file:
                self.storage = file.read().encode()
        except Exception:
            pass

    def get_file_open(self):

        try:
            if len(self.storage) > 0 and len(self.get_file_pass.get()) > 1:
                key = self.get_file_pass.get()
                frn = Fernet(key)
                file = self.storage.encode()
                data = frn.decrypt(file)
                data = data.decode()
                self.get_file_result.insert(1.0, data)
        except Exception:
            self.get_file_pass.delete(0, END)
            self.storage = ''
            self.get_file_pass.insert(0, 'Data is wrong!')

    def text_selection(self, e):

        self.menu.post(e.x_root, e.y_root)

    def address_confirming(self):

        if len(self.address_entry.get()) > 0:
            self.address = self.address_entry.get()
            self.address_entry.delete(0, END)

    def enter_pass_confirming(self):

        if self.enter_pass_entry.get() == self.repeat_pass_entry.get():
            self.password = self.repeat_pass_entry.get()
            self.enter_pass_entry.delete(0, END)
            self.repeat_pass_entry.delete(0, END)



if __name__ == '__main__':
    root = Tk()
    run = Storin(root)
    root.mainloop()
