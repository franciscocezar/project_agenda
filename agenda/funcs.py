from modulos import *


class Funcs:

    def center(self):
        APP_WIDTH = 620
        APP_HEIGHT = 400

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        app_center_coordinate_x = (screen_width / 2) - (APP_WIDTH / 2)
        app_center_coordinate_y = (screen_height / 2) - (APP_HEIGHT / 2)

        # Position App to the Centre of the Screen
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{int(app_center_coordinate_x)}+{int(app_center_coordinate_y)}")

    def cleans_entries(self):
        self.name_entry.delete(0, tkinter.END)
        self.vehicle_license_plate_entry.delete(0, tkinter.END)
        self.house_name_entry.delete(0, tkinter.END)

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

        self.disconnect_db()
        self.search_entry.delete(0, tkinter.END)
