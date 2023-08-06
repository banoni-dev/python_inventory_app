import customtkinter
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
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="GAPR",text_color=blue_color,
                                                             compound="left", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10, text="Tableau de bord",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10, text="gestion des stocks",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=60, border_spacing=10, text="gestion des commandes",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame,font=("Arial", 20),text_color=blue_color, text="tableau de board".upper())
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=40)


        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_frame_label = customtkinter.CTkLabel(self.second_frame,font=("Arial", 20),text_color=blue_color, text="gestion des stocks".upper())
        self.second_frame_label.grid(row=0, column=0, padx=20, pady=40)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)
        self.third_frame_label = customtkinter.CTkLabel(self.third_frame,font=("Arial", 20),text_color=blue_color, text="gestion des commandes".upper())
        self.third_frame_label.grid(row=0, column=0, padx=20, pady=40)
        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
       # Assuming name holds the button's identifier ("home", "frame_2", "frame_3")
        if name == "home":
            self.home_button.configure(fg_color=("gray75", "gray25"), text_color="#5cafe7")
        else:
            self.home_button.configure(fg_color=("transparent"), text_color=("white"))

        if name == "frame_2":
            self.frame_2_button.configure(fg_color=("gray75", "gray25"), text_color="#5cafe7")
        else:
            self.frame_2_button.configure(fg_color=("transparent"), text_color=("white"))

        if name == "frame_3":
            self.frame_3_button.configure(fg_color=("gray75", "gray25"), text_color="#5cafe7")
        else:
            self.frame_3_button.configure(fg_color=("transparent"), text_color=("white"))



        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    


def main():
    app = App()
    app.mainloop()

main()