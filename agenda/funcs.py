from modulos import *


class Funcs:

    def cleans_entries(self):
        self.name_entry.delete(0, tkinter.END)
        self.vehicle_license_plate_entry.delete(0, tkinter.END)
        self.house_name_entry.delete(0, tkinter.END)
        self.search_entry.delete(0, tkinter.END)

    def connect_db(self):
        # Creates and connects to the database.
        self.conn = sqlite3.connect(
            'lista_proprietarios.db'
        )
        self.cursor = self.conn.cursor()
        print('Connecting to the database.')

    def disconnect_db(self):
        # Disconnects to the database.
        self.conn.close()
        print('Disconnecting to the database.')

    def create_tables(self):
        self.connect_db()

        # Criar Tabela
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS proprietarios(
                            id INTEGER PRIMARY KEY,
                            nome_proprietario CHAR(40),
                            placa_veiculo CHAR(20),
                            casa CHAR(40)
                            );""")
        self.conn.commit()

        print('Database table created.')
        self.disconnect_db()

    def save_button_func(self):
        # Saves the data entered in the Entries to the database.

        self.name = self.name_entry.get().title()
        plate = self.vehicle_license_plate_entry.get().upper()
        self.plate = f'{plate[:3]} {plate[3:]}'
        house = self.house_name_entry.get().title()
        self.house = f'{house[:-2]} ({house[-2:]})'

        self.connect_db()

        self.cursor.execute(
            """ INSERT INTO proprietarios (nome_proprietario, placa_veiculo, casa) 
                VALUES (?, ?, ?)""", (self.name, self.plate, self.house),
        )
        self.conn.commit()
        self.disconnect_db()
        self.cleans_entries()

    def change_appearance_mode(self, new_appearance_mode):
        # Muda o tema do programa --> Sistema / Claro / Escuro
        customtkinter.set_appearance_mode(new_appearance_mode)

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
                                                     text="buscar",
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

    def select_list(self):
        # Shows database data on the screen.

        # Deletes all the data shown on the screen to update the list.
        self.database_data_list.delete(*self.database_data_list.get_children())

        # Connect to database and gets data
        self.connect_db()
        data_list = self.cursor.execute(
            """ SELECT nome_proprietario, placa_veiculo, casa 
                FROM proprietarios
                ORDER BY nome_proprietario ASC; """
        )

        # Gets selected data and shows it on the screen
        count = 0
        for i in data_list:
            if count % 2 == 0:
                self.database_data_list.insert(
                    '', tkinter.END, values=i, iid=count, tag=('evenrow',)
                )
            else:
                self.database_data_list.insert(
                    '', tkinter.END, values=i, iid=count, tag=('oddrow',)
                )
            count += 1

        self.disconnect_db()

    def search_in_db(self):
        self.connect_db()
        self.database_data_list.delete(*self.database_data_list.get_children())

        self.search = self.search_entry.get()

        self.cursor.execute(
            f"""
                            SELECT nome_proprietario, placa_veiculo, casa 
                            FROM proprietarios
                            WHERE nome_proprietario LIKE '%{self.search}%' OR 
                            placa_veiculo LIKE '%{self.search}%' OR 
                            casa LIKE '%{self.search}%'
                            ORDER BY nome_proprietario ASC"""
        )

        searched_data = self.cursor.fetchall()

        for i in searched_data:
            self.database_data_list.insert('', tkinter.END, values=i)

        self.cleans_entries()
        self.disconnect_db()
