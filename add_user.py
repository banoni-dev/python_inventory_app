import customtkinter
import customtkinter as tk
import os
from tkinter import ttk
from CTkTable import *
from PIL import Image
global  blue_color
blue_color = "#5cafe7"





def add_user_frame(self):
    self.add_user_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.add_user_frame.grid_columnconfigure(0, weight=1)
    self.add_user_frame_label = customtkinter.CTkLabel(self.add_user_frame,font=("Arial", 20),text_color=blue_color, text="Ajouter un utilisateur".upper())
    self.add_user_frame_label.grid(row=0, column=0, padx=20, pady=40)