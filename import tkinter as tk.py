import tkinter as tk
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Navigation Dropdown Example")

        # Define colors and images
        blue_color = "#5cafe7"
       

        # Create the navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # Create the main label
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="GAPR", text_color=blue_color,
                                                             compound="left", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Create buttons
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10,
                                                   text="Tableau de bord", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.gestion_des_stocks_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10,
                                                      text="gestion des stocks", fg_color="transparent",
                                                      text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.frame_2_button_event)
        self.gestion_des_stocks_button.grid(row=2, column=0, sticky="ew")
        self.gestion_des_stocks_button.bind("<Button-1>", self.toggle_submenu_1)

        # Create the gestion des commandes button
        self.gestion_des_commandes_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60,
                                                                    border_spacing=10, text="gestion des commandes",
                                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                                    hover_color=("gray70", "gray30"), anchor="w")
        self.gestion_des_commandes_button.grid(row=3, column=0, sticky="ew")
        self.gestion_des_commandes_button.bind("<Button-1>", self.toggle_submenu_2)

        # Create the sub-menu options (hidden by default)
        self.submenu_frame_1 = customtkinter.CTkFrame(self.navigation_frame, fg_color="gray50")
        self.submenu_frame_1.grid(row=3, column=0, sticky="ew")
        self.submenu_frame_1.grid_forget()

        self.sub1_option_1 = customtkinter.CTkButton(self.submenu_frame_1, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="listes des pieces", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.sub1_option_1.grid(row=0, column=0, sticky="ew")


        self.sub1_option_2 = customtkinter.CTkButton(self.submenu_frame_1, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="Ajouter", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.sub1_option_2.grid(row=1, column=0, sticky="ew")
        
        self.sub1_option_3 = customtkinter.CTkButton(self.submenu_frame_1, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="modifier", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.sub1_option_3.grid(row=2, column=0, sticky="ew")
        
        self.sub1_option_4 = customtkinter.CTkButton(self.submenu_frame_1, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="supprimer", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.sub1_option_4.grid(row=3, column=0, sticky="ew")
        
        self.sub1_option_5 = customtkinter.CTkButton(self.submenu_frame_1, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="rechercher", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.sub1_option_5.grid(row=4, column=0, sticky="ew")
        
        # Create the sub-menu options (hidden by default)
        self.submenu_frame_2 = tk.Frame(self.navigation_frame, bg="white")
        self.submenu_frame_2.grid(row=5, column=0, sticky="ew")
        self.submenu_frame_2.grid_forget()

        self.sub1_option_2 = tk.Label(self.submenu_frame_2, text="Option 1", bg="white")
        self.sub1_option_2.grid(row=0, column=0, sticky="w", padx=20, pady=5)

        self.sub2_option_2 = tk.Label(self.submenu_frame_2, text="Option 2", bg="white")
        self.sub2_option_2.grid(row=1, column=0, sticky="w", padx=20, pady=5)

        self.sub2_option_3 = tk.Label(self.submenu_frame_2, text="Option 3", bg="white")
        self.sub2_option_3.grid(row=2, column=0, sticky="w", padx=20, pady=5)

    def toggle_submenu_1(self, event):
        if self.submenu_frame_1.winfo_ismapped():
            self.submenu_frame_1.grid_forget()
        else:
            self.submenu_frame_1.grid(row=3, column=0, sticky="ew")
            self.gestion_des_commandes_button.grid(row=4, column=0, sticky="ew")
    def toggle_submenu_2(self, event):
        if self.submenu_frame_2.winfo_ismapped():
            self.submenu_frame_2.grid_forget()
        else:
            self.submenu_frame_2.grid(row=5, column=0, sticky="ew")
            self.gestion_des_commandes_button.grid(row=4, column=0, sticky="ew")


    def home_button_event(self):
        print("Home button clicked")

    def frame_2_button_event(self):
        print("Frame 2 button clicked")

    def frame_3_button_event(self):
        print("Frame 3 button clicked")

def main():
    app = App()
    app.mainloop()


main()
