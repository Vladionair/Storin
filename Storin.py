import time
from tkinter import *
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Storin:

    # инициализируем класс
    def __init__(self, master):

        self.balance = 0
        self.address = None
        self.contracts = []
        self.date = 0

        # задаем окно ввода пароля
        self.master = master
        self.master.title('Storin')
        self.master.geometry('500x300+50+50')
        self.master['bg'] = 'grey'

        # задаем фрейм ввода пароля входа в программу
        entr_pass_frame = Frame(self.master)
        entr_pass_frame.place(relx=0.2, rely=0.4, relwidth=0.4, relheight=0.05)

        # задаем поле ввода пароля
        self.entr_pass_field = Entry(entr_pass_frame, width=30)
        self.entr_pass_field.place(relx=0, rely=0, relwidth=1, relheight=1)

        # задаем кнопку ввода пароля
        pass_button = Button(text='Enter', command=self.main_window_call)
        pass_button.place(relx=0.65, rely=0.4, relwidth=0.15, relheight=0.05)

    # задаем функцию вызова главного окна
    def main_window_call(self):

        # задаем проверку пароля
        if self.entr_pass_field.get() == '':
            self.master.destroy()

            # задаем главное окно
            main_window = Tk()
            main_window.title('Operations')
            main_window.geometry('500x300+50+50')

            # задаем кнопки переключения вкладок
            get_file_button = Button(text='Get file', command=self.get_file_func)
            get_file_button.place(relx=0, rely=0, relwidth=0.25, relheight=0.07)

            give_file_button = Button(text='Give file', command=None)
            give_file_button.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.07)

            give_memory_button = Button(text='Give memory', command=None)
            give_memory_button.place(relx=0.50, rely=0, relwidth=0.25, relheight=0.07)

            exchange_button = Button(text='Exchange', command=None)
            exchange_button.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.07)

            # задаем метку баланса
            balance_window = Label(text=f'Balance : {self.balance}')
            balance_window.place(relx=0.10, rely=0.93)

            # задаем функцию обновления даты
            def update_date():

                self.date = time.ctime()
                date_window = Label(text=f'Date : {self.date}')
                date_window.place(relx=0.61, rely=0.93)
                main_window.after(1000, update_date)

            update_date()

            # задаем поле операций
            self.operating_field = Frame()
            self.operating_field.place(relx=0, rely=0.10, relwidth=1, relheight=0.83)

    # задаем функцию вызова окна получения файла
    def get_file_func(self):

        # задаем имена окон ввода
        get_file_name = Label(self.operating_field, text='File name :')
        get_file_name.place(relx=0.10, rely=0.05)
        get_file_pass = Label(self.operating_field, text='Password :')
        get_file_pass.place(relx=0.10, rely=0.15)

        # задаем окно ввода имени файла
        self.get_file_name_field = Entry(self.operating_field, width=25)
        self.get_file_name_field.place(relx=0.25, rely=0.05, relwidth=0.50, relheight=0.05)

        # задаем окно ввода пароля
        self.get_file_pass_field = Entry(self.operating_field, width=25)
        self.get_file_pass_field.place(relx=0.25, rely=0.15, relwidth=0.50, relheight=0.05)

        # задаем кнопку поиска файла в хранилище
        get_file_button = Button(self.operating_field, text='Look', command=self.get_file_addresses)
        get_file_button.place(relx=0.83, rely=0.15, relwidth=0.09, relheight=0.05)

    # задаем функцию поиска файла в хранилище
    def get_file_addresses(self):
        contract = self.get_file_name_field.get()
        if contract in self.contracts:
            if type(self.contracts) is list:
                pass
