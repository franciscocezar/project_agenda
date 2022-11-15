from modulos import *


class SearchData:
    def new_window(self):
        # New window with database data
        self.window = customtkinter.CTkToplevel(self)
        self.window.title("")
        self.window.geometry("700x600")

        self.frame_new_window = customtkinter.CTkFrame(master=self.window,
                                                       width=180,
                                                       corner_radius=10, )
        self.frame_new_window.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.78)

        self.frame_search_button = customtkinter.CTkFrame(master=self.window)

        self.frame_search_button.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.15)

        # ttk.Treeview style and it shows database data in the new window
        style = ttk.Style()
        style.theme_use("aqua")
        style.configure(
            'Treeview',
            background='#292929',
            foreground='white',
            fielbackground='#292929',
        )

        style.map(
            'Treeview',
            background=[('selected', 'white')],
            foreground=[('selected', 'black')],
        )

        self.database_data_list = ttk.Treeview(
            self.frame_new_window,
            height=3,
            columns=('col1', 'col2', 'col3'),
        )
        self.database_data_list.heading('#0', text='', )
        self.database_data_list.heading('#1', text='Proprietário(a)')
        self.database_data_list.heading('#2', text='Placa do Veículo')
        self.database_data_list.heading('#3', text='Casa')

        self.database_data_list.column('#0', width=0, stretch=tkinter.NO)
        self.database_data_list.column('#1', width=1, anchor='center')
        self.database_data_list.column('#2', width=90, anchor='center')
        self.database_data_list.column('#3', width=110, anchor='center')

        self.database_data_list.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.97)

        # lines color without selecting them
        self.database_data_list.tag_configure('oddrow', background='gray20')
        self.database_data_list.tag_configure('evenrow', background='gray10')

        self.select_list()  # selects data list

        # search_in_db method's Button and Entry
        self.button_search = customtkinter.CTkButton(master=self.frame_search_button,
                                                     text="Buscar",
                                                     border_width=1,
                                                     fg_color=None,
                                                     command=self.search_in_db
                                                     )
        self.button_search.place(relx=0.32, rely=0.5, relwidth=0.2, anchor=tkinter.CENTER)

        self.search_entry = customtkinter.CTkEntry(master=self.frame_search_button,
                                                   width=120,
                                                   border_width=1)
        self.search_entry.place(relx=0.62, rely=0.5, relwidth=0.33, anchor=tkinter.CENTER)

        # create CTk scrollbar
        frame_new_window_scrollbar = customtkinter.CTkScrollbar(self.frame_new_window,
                                                                command=self.database_data_list.yview,
                                                                corner_radius=10,
                                                                border_spacing=1)
        frame_new_window_scrollbar.place(relx=0.98, rely=0.01, relwidth=0.017, relheight=0.98)

        self.database_data_list.configure(yscrollcommand=frame_new_window_scrollbar.set)
