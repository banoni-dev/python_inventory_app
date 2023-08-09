import customtkinter
import customtkinter as tk
import pieces_forms
import commandes_forms
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        blue_color= "#5cafe7"
        super().__init__()

        self.title("GAPR")
        self.resizable(1,1)
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set the desired window width and height
        window_width = 1000
        window_height = 650

        # Calculate the x and y position for the window to be centered
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Set the window geometry with the calculated position
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="GAPR",text_color=blue_color,
                                                             compound="left", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10, text="Tableau de bord",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10, text="gestion des stocks",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w")
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        self.frame_2_button.bind("<Button-1>", self.toggle_submenu_1)

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10, text="gestion des commandes",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w")
        self.frame_3_button.grid(row=4, column=0, sticky="ew")
        self.frame_3_button.bind("<Button-1>", self.toggle_submenu_2)


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame,font=("Arial", 20),text_color=blue_color, text="tableau de board".upper())
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=40)


        # create ajouter_p_frame 
        pieces_forms.ajouter_fun(self)

        # create liste_p_frame 
        pieces_forms.liste_fun(self)



        # create supprimer_p_frame 
        pieces_forms.supprimer_fun(self)


        # create modifier_p_frame 
        pieces_forms.modifier_fun(self)
       

        # create rechercher_p_frame 

        pieces_forms.rechercher_fun(self)

##################################################################################################################################
#=================================================================================================================================

             # create ajouter_c_frame 
        commandes_forms.ajouter_fun(self)

        # create liste_c_frame 
        commandes_forms.liste_fun(self)



        # create supprimer_c_frame 
        commandes_forms.supprimer_fun(self)


        # create modifier_c_frame 
        commandes_forms.modifier_fun(self)
       

        # create rechercher_c_frame 

        commandes_forms.rechercher_fun(self)



        # select default frame


# Create the sub-menu options (hidden by default)
        self.submenu_frame_1 = customtkinter.CTkFrame(self.navigation_frame, fg_color="gray50")

        self.submenu_frame_1.grid(row=0, column=0, sticky="ew")
        self.submenu_frame_1.grid_forget()

        self.sub1_option_1 = customtkinter.CTkButton(self.submenu_frame_1, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="listes des pieces", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.liste_p_event)
        self.sub1_option_1.grid(row=0, column=0, sticky="ew")


        self.sub1_option_2 = customtkinter.CTkButton(self.submenu_frame_1, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="Ajouter", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.ajouter_p_event)
        self.sub1_option_2.grid(row=1, column=0, sticky="ew")
        
        self.sub1_option_3 = customtkinter.CTkButton(self.submenu_frame_1, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="modifier", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.modifier_p_event)
        self.sub1_option_3.grid(row=2, column=0, sticky="ew")
        
        self.sub1_option_4 = customtkinter.CTkButton(self.submenu_frame_1, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="supprimer", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.supprimer_p_event)
        self.sub1_option_4.grid(row=3, column=0, sticky="ew")
        
        self.sub1_option_5 = customtkinter.CTkButton(self.submenu_frame_1, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="rechercher", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.rechercher_p_event)
        self.sub1_option_5.grid(row=4, column=0, sticky="ew")


        # Create the sub-menu options (hidden by default)
       
        self.submenu_frame_2 = customtkinter.CTkFrame(self.navigation_frame, fg_color="gray50")

        self.submenu_frame_2.grid(row=0, column=0, sticky="ew")
        self.submenu_frame_2.grid_forget()

        self.sub2_option_1 = customtkinter.CTkButton(self.submenu_frame_2, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="listes des commandes", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.liste_c_event)
        self.sub2_option_1.grid(row=0, column=0, sticky="ew")


        self.sub2_option_2 = customtkinter.CTkButton(self.submenu_frame_2, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="Ajouter", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.ajouter_c_event)
        self.sub2_option_2.grid(row=1, column=0, sticky="ew")
        
        self.sub2_option_3 = customtkinter.CTkButton(self.submenu_frame_2, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="modifier", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.modifier_c_event)
        self.sub1_option_3.grid(row=2, column=0, sticky="ew")
        
        self.sub2_option_4 = customtkinter.CTkButton(self.submenu_frame_2, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="supprimer", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.supprimer_c_event)
        self.sub2_option_4.grid(row=3, column=0, sticky="ew")
        
        self.sub2_option_5 = customtkinter.CTkButton(self.submenu_frame_2, corner_radius=0, width=200, height=60, border_spacing=15,
                                                   text="rechercher", fg_color="transparent",
                                                   text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.rechercher_c_event)
        self.sub2_option_5.grid(row=4, column=0, sticky="ew")

    def toggle_submenu_1(self, event):
        if self.submenu_frame_1.winfo_ismapped():
            self.submenu_frame_1.grid_forget()
        else:
            self.submenu_frame_1.grid(row=3, column=0, sticky="ew")
            self.frame_2_button.grid(row=2, column=0, sticky="ew")
    def toggle_submenu_2(self, event):
        if self.submenu_frame_2.winfo_ismapped():
            self.submenu_frame_2.grid_forget()
        else:
            self.submenu_frame_2.grid(row=5, column=0, sticky="ew")
            self.frame_3_button.grid(row=4, column=0, sticky="ew")






    def select_frame_by_name(self, name):
        # set button color for selected button
       # Assuming name holds the button's identifier ("home", "frame_2", "frame_3")
        # if name == "home":
        #     self.home_button.configure(fg_color=("gray75", "gray25"), text_color="#5cafe7")
        # else:
        #     self.home_button.configure(fg_color=("transparent"), text_color=("white"))

        # if name == "frame_2":
        #     self.frame_2_button.configure(fg_color=("gray75", "gray25"), text_color="#5cafe7")
        # else:
        #     self.frame_2_button.configure(fg_color=("transparent"), text_color=("white"))

        # if name == "frame_3":
        #     self.frame_3_button.configure(fg_color=("gray75", "gray25"), text_color="#5cafe7")
        # else:
        #     self.frame_3_button.configure(fg_color=("transparent"), text_color=("white"))



        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "liste_p_frame":
            self.liste_p_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.liste_p_frame.grid_forget()
        if name == "ajouter_p_frame":
            self.ajouter_p_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.ajouter_p_frame.grid_forget()
        if name == "supprimer_p_frame":
            self.supprimer_p_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.supprimer_p_frame.grid_forget()
        if name == "modifier_p_frame":
            self.modifier_p_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.modifier_p_frame.grid_forget()
        if name == "rechercher_p_frame":
            self.rechercher_p_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.rechercher_p_frame.grid_forget()
        if name == "liste_c_frame":
            self.liste_c_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.liste_c_frame.grid_forget()
        if name == "ajouter_c_frame":
            self.ajouter_c_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.ajouter_c_frame.grid_forget()
        if name == "supprimer_c_frame":
            self.supprimer_c_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.supprimer_c_frame.grid_forget()
        if name == "modifier_c_frame":
            self.modifier_c_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.modifier_c_frame.grid_forget()
        if name == "rechercher_c_frame":
            self.rechercher_c_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.rechercher_c_frame.grid_forget()


    def home_event(self):
        self.select_frame_by_name("home")

    def liste_p_event(self):
        self.select_frame_by_name("liste_p_frame")
    def ajouter_p_event(self):
        self.select_frame_by_name("ajouter_p_frame")
    def modifier_p_event(self):
        self.select_frame_by_name("modifier_p_frame")
    def supprimer_p_event(self):
        self.select_frame_by_name("supprimer_p_frame")
    def rechercher_p_event(self):
        self.select_frame_by_name("rechercher_p_frame")


    def liste_c_event(self):
        self.select_frame_by_name("liste_c_frame")
    def ajouter_c_event(self):
        self.select_frame_by_name("ajouter_c_frame")
    def modifier_c_event(self):
        self.select_frame_by_name("modifier_c_frame")
    def supprimer_c_event(self):
        self.select_frame_by_name("supprimer_c_frame")
    def rechercher_c_event(self):
        self.select_frame_by_name("rechercher_c_frame")



    


def main():
    app = App()
    app.mainloop()

main()