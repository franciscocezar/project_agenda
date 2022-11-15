from modulos import *
from funcs import Funcs

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "dark-blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk, Funcs):
    WIDTH = 620
    HEIGHT = 400

    def __init__(self):
        super().__init__()

        self.title("")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.center()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.frames()
        self.widgets()
        self.create_tables()

    def center(self):
        APP_WIDTH = 620
        APP_HEIGHT = 400

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        app_center_coordinate_x = (screen_width / 2) - (APP_WIDTH / 2)
        app_center_coordinate_y = (screen_height / 2) - (APP_HEIGHT / 2)

        # Position App to the Centre of the Screen
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{int(app_center_coordinate_x)}+{int(app_center_coordinate_y)}")

    def frames(self):
        self.frame_1 = customtkinter.CTkFrame(master=self,
                                              width=180,
                                              corner_radius=10)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def widgets(self):
        # Entries
        self.name_entry = customtkinter.CTkEntry(master=self.frame_1,
                                                 width=120,
                                                 placeholder_text="Proprietário(a)",
                                                 border_width=1)
        self.name_entry.place(relx=0.25, rely=0.32, relwidth=0.5)

        self.vehicle_license_plate_entry = customtkinter.CTkEntry(master=self.frame_1,
                                                                  width=120,
                                                                  placeholder_text="Placa do Veículo",
                                                                  border_width=1
                                                                  )
        self.vehicle_license_plate_entry.place(relx=0.25, rely=0.43, relwidth=0.2)

        self.house_name_entry = customtkinter.CTkEntry(master=self.frame_1,
                                                       width=120,
                                                       placeholder_text="Casa",
                                                       border_width=1
                                                       )
        self.house_name_entry.place(relx=0.47, rely=0.43, relwidth=0.28)

        # Buttons
        self.save_button = customtkinter.CTkButton(master=self.frame_1,
                                                   text="Salvar",
                                                   border_width=1,
                                                   fg_color=None,
                                                   command=self.save_button_func
                                                   )
        self.save_button.place(relx=0.25, rely=0.55, relwidth=0.24)

        self.list_button = customtkinter.CTkButton(master=self.frame_1,
                                                   text="Ver Lista",
                                                   border_width=1,  # <- custom border_width
                                                   fg_color=None,  # <- no fg_color
                                                   command=self.new_window
                                                   )
        self.list_button.place(relx=0.51, rely=0.55, relwidth=0.24)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_1, text="Appearance Mode:")
        self.label_mode.place(relx=0.01, rely=0.82)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_1,
                                                        values=["System", "Light", "Dark"],
                                                        command=self.change_appearance_mode,
                                                        button_color=("#edfffa", "#000214"),
                                                        fg_color=("#9befd7", "#03030d"))
        self.optionmenu_1.place(relx=0.02, rely=0.9, relwidth=0.22, relheight=0.064)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
