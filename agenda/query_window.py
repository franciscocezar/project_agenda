from modulos import *


class QueryData:
    def new_window(self):
        # New window with database data
        self.window = customtkinter.CTkToplevel(self)
        self.window.title("")
        self.window.geometry("700x600")
        self.frames_querywin()
        self.widgets2()
        self.treeview()
        self.select_list()

    def frames_querywin(self):
        self.frame_query_button = customtkinter.CTkFrame(master=self.window)

        self.frame_query_button.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.15)

        self.frame_new_window = customtkinter.CTkFrame(master=self.window,
                                                       width=180,
                                                       corner_radius=10, )
        self.frame_new_window.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.78)

    def treeview(self):
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
            columns=('col0', 'col1', 'col2', 'col3'),
        )
        self.database_data_list.heading('#0', text='', )
        self.database_data_list.heading('#4', text='ID', )
        self.database_data_list.heading('#1', text='Proprietário(a)')
        self.database_data_list.heading('#2', text='Placa do Veículo')
        self.database_data_list.heading('#3', text='Casa')

        self.database_data_list.column('#0', width=0, stretch=tkinter.NO)
        self.database_data_list.column('#4', width=1, stretch=tkinter.NO)
        self.database_data_list.column('#1', width=1, anchor='center')
        self.database_data_list.column('#2', width=90, anchor='center')
        self.database_data_list.column('#3', width=110, anchor='center')

        self.database_data_list.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.97)

        # lines color without selecting them
        self.database_data_list.tag_configure('oddrow', background='gray20')
        self.database_data_list.tag_configure('evenrow', background='gray10')

        self.database_data_list.bind("<Double-1>", self.OnDoubleClick)

        # create CTk scrollbar
        frame_new_window_scrollbar = customtkinter.CTkScrollbar(self.frame_new_window,
                                                                command=self.database_data_list.yview,
                                                                corner_radius=10,
                                                                border_spacing=1)
        frame_new_window_scrollbar.place(relx=0.98, rely=0.01, relwidth=0.017, relheight=0.98)

        self.database_data_list.configure(yscrollcommand=frame_new_window_scrollbar.set)

    def widgets2(self):
        # search_in_db method's Button and Entry
        self.button_query = customtkinter.CTkButton(master=self.frame_query_button,
                                                    text="Buscar",
                                                    border_width=1,
                                                    fg_color=None,
                                                    command=self.read_data
                                                    )
        self.button_query.place(relx=0.32, rely=0.5, relwidth=0.2, anchor=tkinter.CENTER)

        self.query_entry = customtkinter.CTkEntry(master=self.frame_query_button,
                                                  width=120,
                                                  border_width=1)
        self.query_entry.place(relx=0.62, rely=0.5, relwidth=0.33, anchor=tkinter.CENTER)

    def reconfigure_frame(self):
        for widgets in self.frame_query_button.winfo_children():
            widgets.destroy()

        self.qrname_entry = customtkinter.CTkEntry(master=self.frame_query_button,
                                                   width=120,
                                                   placeholder_text="Proprietário(a)",
                                                   border_width=1)
        self.qrname_entry.place(relx=0.03, rely=0.15, relwidth=0.33)

        self.qrvehicle_license_plate_entry = customtkinter.CTkEntry(master=self.frame_query_button,
                                                                    width=120,
                                                                    placeholder_text="Placa do Veículo",
                                                                    border_width=1
                                                                    )
        self.qrvehicle_license_plate_entry.place(relx=0.4, rely=0.15, relwidth=0.22)

        self.qrhouse_name_entry = customtkinter.CTkEntry(master=self.frame_query_button,
                                                         width=120,
                                                         placeholder_text="Casa",
                                                         border_width=1
                                                         )
        self.qrhouse_name_entry.place(relx=0.67, rely=0.15, relwidth=0.3)

        self.id_entry = customtkinter.CTkEntry(master=self.frame_query_button)

        self.button_update = customtkinter.CTkButton(master=self.frame_query_button,
                                                     text="Alterar",
                                                     border_width=1,
                                                     fg_color=None,
                                                     command=self.update_data
                                                     )
        self.button_update.place(relx=0.38, rely=0.73, relwidth=0.2, anchor=tkinter.CENTER)

        self.button_delete = customtkinter.CTkButton(master=self.frame_query_button,
                                                     text="Apagar",
                                                     border_width=1,
                                                     fg_color=None,
                                                     command=self.delete_data
                                                     )
        self.button_delete.place(relx=0.63, rely=0.73, relwidth=0.2, anchor=tkinter.CENTER)

