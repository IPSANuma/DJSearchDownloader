import tkinter
import tkinter.messagebox
import customtkinter
from func import *
import threading

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("theme.json")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("DJSearch")
        self.geometry(f"{490}x{290}")
        self.resizable(True, False)

        self.grid_rowconfigure(2, weight=0)  # Redimensionne la ligne 2
        self.grid_columnconfigure(0, weight=1)  # Redimensionne la colonne 0
        self.grid_columnconfigure(1, weight=1)  # Redimensionne la colonne 1
        self.grid_columnconfigure(3, weight=1)  # Redimensionne la colonne 3

        self.genre_list = ["Tech House", "Latin Tech House", "Bass House", "Commercial FR", "Commercial", "Latino",
                           "Accapella", "Techno", "Rap FR", "Rap US", "Pop"]

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Titre de la chanson")
        self.accapella_checkbox = customtkinter.CTkCheckBox(self, text="Accapella")
        self.remix_checkbox = customtkinter.CTkCheckBox(self, text="Remix")

        self.file_combo = customtkinter.CTkComboBox(self, values=self.genre_list)
        self.soundcloud_radiobutton_frame = customtkinter.CTkFrame(self)
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group_sc = customtkinter.CTkLabel(master=self.soundcloud_radiobutton_frame)
        self.youtube_radiobutton_frame = customtkinter.CTkFrame(self)
        self.radio_var = tkinter.IntVar(value=6)
        self.label_radio_group_yt = customtkinter.CTkLabel(master=self.youtube_radiobutton_frame)

        def handle_resize(self):
            pass

        self.bind("<Configure>", handle_resize)
        self.ListeURL_sc = []
        self.ListeURL_yt = []
        self.ListeTitre_sc = []
        self.ListeTitre_yt = []
        self.ListeDuration_yt = []

        def button_recherche():
            query = self.entry.get()
            if query == "":
                return

            self.ListeURL_sc = []
            self.ListeURL_yt = []
            self.ListeTitre_sc = []
            self.ListeTitre_yt = []
            self.ListeDuration_yt = []

            print(query)
            self.ListeURL_sc, self.ListeTitre_sc = recherche_soundcloud(query)
            self.ListeTitre_yt, self.ListeURL_yt, self.ListeDuration_yt = recherche_youtube(query)

            self.geometry(f"{1200}x{360}")

            self.title_sc = customtkinter.CTkLabel(self.label_radio_group_sc, text="Recherche Soundcloud",
                                                   fg_color="gray30", corner_radius=6)
            self.title_sc.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

            self.label_radio_group_sc.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="nsew")
            for i in range(5):
                self.radio_button = customtkinter.CTkRadioButton(master=self.soundcloud_radiobutton_frame,
                                                                 text=str(self.ListeURL_sc[i].split('/')[1]) + " |  " +
                                                                      self.ListeTitre_sc[i],
                                                                 variable=self.radio_var, value=i)
                self.radio_button.grid(row=i + 1, column=2, pady=10, padx=20, sticky="W")

            self.label_radio_group_yt.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="nsew")
            self.title_yt = customtkinter.CTkLabel(self.label_radio_group_yt, text="Recherche Youtube",
                                                   fg_color="gray30", corner_radius=6)
            self.title_yt.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

            for i in range(5):
                self.radio_button = customtkinter.CTkRadioButton(master=self.youtube_radiobutton_frame,
                                                                 text=self.ListeTitre_yt[i] + '(' +
                                                                      self.ListeDuration_yt[i] + ')',
                                                                 variable=self.radio_var, value=i + 5)
                self.radio_button.grid(row=i + 1, column=2, pady=10, padx=20, sticky="W")

        def button_telecharger():
            print("ListeURL_sc :", self.ListeURL_sc)
            print("ListeURL_yt :", self.ListeURL_yt)
            print("ListeTitre_sc :", self.ListeTitre_sc)
            print("ListeTitre_yt :", self.ListeTitre_yt)
            print("ListeDuration_yt :", self.ListeDuration_yt)
            genre = self.file_combo.get()
            butnum = self.radio_var.get()
            print(butnum)
            if self.remix_checkbox.get() == True:
                genre = genre + "/remix"
            try:
                if butnum in [0, 1, 2, 3, 4]:
                    print("SC")
                    download_soundcloud(self.ListeURL_sc[butnum], self.ListeTitre_sc[butnum], genre)
                if butnum in [5, 6, 7, 8, 9]:
                    print("YT")
                    download_youtube_audio(self.ListeURL_yt[butnum - 5], self.ListeTitre_yt[butnum - 5], genre)
            except IndexError:
                pass

        self.search_button_1 = customtkinter.CTkButton(master=self, text="Recherche",
                                                       fg_color="transparent", border_width=2,
                                                       text_color=("gray10", "#DCE4EE"),
                                                       command=button_recherche)
        self.dl_button_1 = customtkinter.CTkButton(master=self, text="Telecharger",
                                                   fg_color="transparent", border_width=2,
                                                   text_color=("gray10", "#DCE4EE"),
                                                   command=button_telecharger)

        self.search_button_1.grid(row=3, column=3, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.dl_button_1.grid(row=2, column=0, columnspan=3, padx=(10, 5), pady=(5, 5), sticky="ew")
        self.soundcloud_radiobutton_frame.grid(row=0, column=0, columnspan=2, padx=(10, 5), pady=(10, 5), sticky="nswe")
        self.youtube_radiobutton_frame.grid(row=0, column=3, columnspan=2, padx=(5, 10), pady=(10, 5), sticky="nswe")
        self.entry.grid(row=3, column=0, columnspan=2, padx=(10, 5), pady=(5, 5), sticky="nsew")
        self.accapella_checkbox.grid(row=3, column=4, sticky="nsew")
        self.file_combo.grid(row=2, column=3, padx=(5, 5), pady=(5, 5), sticky="ew")
        self.remix_checkbox.grid(row=2, column=4, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
