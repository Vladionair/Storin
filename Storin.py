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
        self.entr_pass_frame = Frame(self.master)
        self.entr_pass_frame.place(relx=0.2, rely=0.4, relwidth=0.4, relheight=0.05)

        # задаем поле ввода пароля
        self.entr_pass_field = Entry(self.entr_pass_frame, width=30)
        self.entr_pass_field.pack(side=BOTTOM)

        # задаем кнопку ввода пароля
        pass_button = Button(text='Enter', command=self.main_window_call)
        pass_button.place(relx=0.65, rely=0.4, relwidth=0.15, relheight=0.05)

    # задаем функцию вызова главного окна
    def main_window_call(self):

        # задаем проверку пароля
        if self.entr_pass_field.get() == '1':
            self.master.destroy()

            # задаем главное окно
            func_window = Tk()
            func_window.title('Functions')
            func_window.geometry('500x300+50+50')

            # задаем кнопки переключения вкладок
            give_file_button = Button(text='Get file', command=None)
            give_file_button.place(relx=0, rely=0, relwidth=0.25, relheight=0.23)

            get_file_button = Button(text='Give file', command=None)
            get_file_button.place(relx=0, rely=0.23, relwidth=0.25, relheight=0.23)

            give_memory_button = Button(text='Give memory', command=None)
            give_memory_button.place(relx=0, rely=0.46, relwidth=0.25, relheight=0.23)

            exchange_button = Button(text='Exchange', command=None)
            exchange_button.place(relx=0, rely=0.69, relwidth=0.25, relheight=0.23)

            # задаем функцию обновления даты
            def update_date():

                self.date = time.ctime()
                date_window_name = Label(text=f'Date: {self.date}')
                date_window_name.place(relx=0.42, rely=0.92)
                func_window.after(1000, update_date)

            update_date()

            # задаем фрейм окна операций
            operation_frame = Frame()
            operation_frame.place(relx=0.25, rely=0, relwidth=0.75, relheight=0.92)

            # задаем функцию вызова окна получения файла
            def get_file_func():
                pass


root = Tk()
test = Storin(root)
root.mainloop()