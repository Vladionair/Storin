from tkinter import *

import time

class Storin:

    # инициализируем класс
    def __init__(self, master):

        self.balance = 0
        self.address = None
        self.contracts = {}
        self.date = 0

        # задаем окно ввода пароля
        self.master = master
        self.master.title('Storin')
        self.master.geometry('500x300+50+50')

        # задаем фрейм ввода пароля входа в программу
        entr_pass_frame = Frame(self.master)
        entr_pass_frame.place(relx=0.2, rely=0.4, relwidth=0.4, relheight=0.05)

        # задаем поле ввода пароля
        self.entr_pass_field = Entry(entr_pass_frame, width=30)
        self.entr_pass_field.pack()

        # задаем кнопку ввода пароля
        pass_button = Button(text='Enter', command=self.main_window_call)
        pass_button.place(relx=0.65, rely=0.4, relwidth=0.15, relheight=0.05)

    # задаем функцию вызова главного окна
    def main_window_call(self):

        # задаем проверку пароля
        if self.entr_pass_field.get() == '1':
            self.master.destroy()

            # задаем главное окно
            main_window = Tk()
            main_window.title('Operations')
            main_window.geometry('500x300+50+50')

            # задаем кнопки переключения вкладок
            get_file_button = Button(text='Get file', command=self.get_file_func)
            get_file_button.place(relx=0, rely=0, relwidth=0.20, relheight=0.23)

            give_file_button = Button(text='Give file', command=None)
            give_file_button.place(relx=0, rely=0.23, relwidth=0.20, relheight=0.23)

            give_memory_button = Button(text='Give memory', command=None)
            give_memory_button.place(relx=0, rely=0.46, relwidth=0.20, relheight=0.23)

            exchange_button = Button(text='Exchange', command=None)
            exchange_button.place(relx=0, rely=0.69, relwidth=0.20, relheight=0.23)

            # задаем функцию обновления даты
            def update_date():

                self.date = time.ctime()
                date_window_name = Label(text=f'Date {self.date}')
                date_window_name.place(relx=0.42, rely=0.92)
                main_window.after(1000, update_date)

            update_date()

            # задаем поле операций
            self.operating_field = Frame()
            self.operating_field.place(relx=0.20, rely=0, relwidth=0.80, relheight=0.92)

    # задаем функцию вызова окна получения файла
    def get_file_func(self):

        # задаем имена окон ввода
        get_file_name = Label(self.operating_field, text='File name')
        get_file_name.place(relx=0.05, rely=0.03)
        get_file_pass = Label(self.operating_field, text='Password')
        get_file_pass.place(relx=0.05, rely=0.13)

        # задаем окно ввода имени файла
        get_file_name_field = Entry(self.operating_field, width=25)
        get_file_name_field.place(relx=0.25, rely=0.04, relwidth=0.50, relheight=0.05)

        # задаем окно ввода пароля
        get_file_pass_field = Entry(self.operating_field, width=25)
        get_file_pass_field.place(relx=0.25, rely=0.14, relwidth=0.50, relheight=0.05)

        # задаем кнопку получения файла
        get_file_button = Button(self.operating_field, text='Get', command=None)
        get_file_button.place(relx=0.83, rely=0.14, relwidth=0.10, relheight=0.05)


root = Tk()
test = Storin(root)
root.mainloop()
