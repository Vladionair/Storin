from tkinter import *
from tkinter import filedialog
import time


class Storin:

    def __init__(self, master):

        self.balance = 0
        self.address = None
        self.storage = ''
        self.date = 0
        self.master = master
        self.master.title('Storin')
        self.master.geometry('500x300+300+200')
        self.master['bg'] = 'grey'
        self.entr_pass = Entry(width=30)
        self.entr_pass.place(relx=0.20, rely=0.40, relwidth=0.40, relheight=0.07)
        entr_pass_button = Button(text='Enter', command=self.init_ui)
        entr_pass_button.place(relx=0.65, rely=0.40, relwidth=0.15, relheight=0.07)

    def init_ui(self):

        coords = self.master.wm_geometry()[self.master.wm_geometry().find('+'):]

        if self.entr_pass.get() == '':
            self.master.destroy()
            self.main_window = Tk()
            self.main_window.title('Operations')
            self.main_window.geometry(f'500x300{coords}')
            self.main_window['bg'] = 'grey'

            get_file_button = Button(text='Get file', command=self.get_file)
            get_file_button.place(relx=0.01, rely=0.02, relwidth=0.19, relheight=0.07)
            give_file_button = Button(text='Give file', command=self.give_file)
            give_file_button.place(relx=0.21, rely=0.02, relwidth=0.19, relheight=0.07)
            give_memory_button = Button(text='Give memory', command=self.give_mem)
            give_memory_button.place(relx=0.41, rely=0.02, relwidth=0.19, relheight=0.07)
            exchange_button = Button(text='Exchange', command=self.exchange)
            exchange_button.place(relx=0.61, rely=0.02, relwidth=0.19, relheight=0.07)
            set_button = Button(text='Settings', command=self.settings)
            set_button.place(relx=0.81, rely=0.02, relwidth=0.18, relheight=0.07)
            balance_window = Label(text=f'Balance : {self.balance}', bg='grey')
            balance_window.place(relx=0.06, rely=0.93)

            def update_date():

                self.date = time.ctime()
                date_window = Label(text=f'Date : {self.date}', bg='grey')
                date_window.place(relx=0.61, rely=0.93)
                self.main_window.after(1000, update_date)

            update_date()

            self.get_file_window = Toplevel()
            self.get_file_window.geometry(f'500x255{coords}')
            self.get_file_window.overrideredirect(True)
            self.get_file_window['bg'] = 'grey'
            self.get_file_pass = Entry(self.get_file_window, width=25)
            self.get_file_pass.place(relx=0.255, rely=0.02, relwidth=0.495, relheight=0.08)
            get_file_find_button = Button(self.get_file_window, text='Find', command=self.get_file_find)
            get_file_find_button.place(relx=0.01, rely=0.025, relwidth=0.24, relheight=0.08)
            get_file_open_button = Button(self.get_file_window, text='Open', command=None)
            get_file_open_button.place(relx=0.76, rely=0.025, relwidth=0.23, relheight=0.08)
            result_frame = Frame(self.get_file_window)
            result_frame.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.87)
            scroll_result = Scrollbar(result_frame)
            scroll_result.pack(side=RIGHT, fill=Y)
            self.get_file_result = Text(result_frame, wrap=None, yscrollcommand=scroll_result.set)
            self.get_file_result.pack(fill=BOTH)
            scroll_result.config(command=self.get_file_result.yview)
            self.get_file_window.withdraw()

            self.give_file_window = Toplevel()
            self.give_file_window.geometry(f'500x255{coords}')
            self.give_file_window.overrideredirect(True)
            self.give_file_window['bg'] = 'black'
            self.give_file_window.withdraw()

            self.give_mem_window = Toplevel()
            self.give_mem_window.geometry(f'500x255{coords}')
            self.give_mem_window.overrideredirect(True)
            self.give_mem_window['bg'] = 'green'
            self.give_mem_window.withdraw()

            self.exchange_window = Toplevel()
            self.exchange_window.geometry(f'500x255{coords}')
            self.exchange_window.overrideredirect(True)
            self.exchange_window['bg'] = 'blue'
            self.exchange_window.withdraw()

            self.set_window = Toplevel()
            self.set_window.geometry(f'500x255{coords}')
            self.set_window.overrideredirect(True)
            self.set_window['bg'] = 'yellow'
            self.set_window.withdraw()

    def get_file(self):

        coords = f'+{self.main_window.winfo_rootx()}+{(self.main_window.winfo_rooty()) + 26}'

        self.get_file_window.withdraw()
        self.give_file_window.withdraw()
        self.give_mem_window.withdraw()
        self.set_window.withdraw()
        self.exchange_window.withdraw()
        self.get_file_window.geometry(coords)
        self.get_file_window.deiconify()
        self.get_file_window.update()

    def get_file_find(self):

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
            self.get_file_pass.insert(0, 'Data is wrong!')

    def give_file(self):

        coords = f'+{self.main_window.winfo_rootx()}+{int(self.main_window.winfo_rooty()) + 26}'

        self.get_file_window.withdraw()
        self.give_mem_window.withdraw()
        self.set_window.withdraw()
        self.exchange_window.withdraw()
        self.give_file_window.geometry(coords)
        self.give_file_window.deiconify()
        self.give_file_window.update()

    def give_mem(self):

        coords = f'+{self.main_window.winfo_rootx()}+{int(self.main_window.winfo_rooty()) + 26}'

        self.get_file_window.withdraw()
        self.give_file_window.withdraw()
        self.set_window.withdraw()
        self.exchange_window.withdraw()
        self.give_mem_window.geometry(coords)
        self.give_mem_window.deiconify()
        self.give_mem_window.update()

    def exchange(self):

        coords = f'+{self.main_window.winfo_rootx()}+{int(self.main_window.winfo_rooty()) + 26}'

        self.get_file_window.withdraw()
        self.give_file_window.withdraw()
        self.give_mem_window.withdraw()
        self.set_window.withdraw()
        self.exchange_window.geometry(coords)
        self.exchange_window.deiconify()
        self.exchange_window.update()

    def settings(self):

        coords = f'+{self.main_window.winfo_rootx()}+{int(self.main_window.winfo_rooty()) + 26}'

        self.get_file_window.withdraw()
        self.give_file_window.withdraw()
        self.give_mem_window.withdraw()
        self.exchange_window.withdraw()
        self.set_window.geometry(coords)
        self.set_window.deiconify()
        self.set_window.update()

if __name__ == '__main__':
    root = Tk()
    run = Storin(root)
    root.mainloop()

