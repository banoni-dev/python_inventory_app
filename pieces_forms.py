import customtkinter
import customtkinter as tk
import os
from tkinter import ttk
from CTkTable import *
from PIL import Image
global  blue_color
blue_color = "#5cafe7"

def liste_fun(self):
    self.liste_p_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.liste_p_frame.grid_columnconfigure(0, weight=1)

    # Label in the first row of self.liste_p_frame
    self.liste_p_frame_label = customtkinter.CTkLabel(self.liste_p_frame, font=("Arial", 20), text_color=blue_color, text="liste des pieces".upper())
    self.liste_p_frame_label.grid(row=0, column=0,padx=20, pady=40)

    # Create a new frame in the second row
    self.second_row_frame = customtkinter.CTkFrame(self.liste_p_frame, corner_radius=0, fg_color="transparent")
    self.second_row_frame.grid(row=1, column=0, pady=10, sticky="ew")
    self.second_row_frame.grid_columnconfigure(0, weight=1)

    value = [[1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5]]

    self.table = CTkTable(self.second_row_frame, row=5, column=5, values=value, )
    self.table.grid(row=0, column=0, padx=20, pady=20, sticky="ew") 
    


def ajouter_fun(self):
    self.ajouter_p_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.ajouter_p_frame.grid_columnconfigure(0, weight=1)
    self.ajouter_p_frame_label = customtkinter.CTkLabel(self.ajouter_p_frame,font=("Arial", 20),text_color=blue_color, text="ajouter des pieces".upper())
    self.ajouter_p_frame_label.grid(row=0, column=0, padx=20, pady=40)

    # Create a new frame in the second row
    second_row_frame = customtkinter.CTkFrame(self.ajouter_p_frame, corner_radius=0, fg_color="transparent")
    second_row_frame.grid(row=1, column=0, pady=10, sticky="ew")

    

# Configure columns and rows for the second_row_frame
    for i in range(2):  # Two columns
        second_row_frame.grid_columnconfigure(i, weight=1)
    for i in range(3):  # Three rows
        second_row_frame.grid_rowconfigure(i, weight=1)

    entry = customtkinter.CTkEntry(second_row_frame,
                                placeholder_text="Référence",
                                width=220,
                                height=2,
                                font=("Arial", 18),
                                border_width=2,
                                corner_radius=5)
    entry.grid(row=0, column=0, padx=25, pady=25)
    entry = customtkinter.CTkEntry(second_row_frame,
                                placeholder_text="Nom",
                                width=220,
                                font=("Arial", 18),
                                height=2,
                                border_width=2,
                                corner_radius=5)
    entry.grid(row=0, column=1, padx=25, pady=25)


    entry = customtkinter.CTkEntry(second_row_frame,
                                placeholder_text="Fournisseur",
                                width=220,
                                height=2,
                                font=("Arial", 18),
                                border_width=2,
                                corner_radius=5)
    entry.grid(row=1, column=0, padx=25, pady=25)
    entry = customtkinter.CTkEntry(second_row_frame,
                                placeholder_text="Quantité",
                                width=220,
                                font=("Arial", 18),
                                height=2,
                                border_width=2,
                                corner_radius=5)
    entry.grid(row=1, column=1, padx=25, pady=25)

    entry = customtkinter.CTkEntry(second_row_frame,
                                placeholder_text="Taille",
                                width=220,
                                font=("Arial", 18),
                                height=2,
                                border_width=2,
                                corner_radius=5)
    entry.grid(row=2, column=0, padx=25, pady=25)




def modifier_fun(self):
    self.modifier_p_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.modifier_p_frame.grid_columnconfigure(0, weight=1)
    self.modifier_p_frame_label = customtkinter.CTkLabel(self.modifier_p_frame,font=("Arial", 20),text_color=blue_color,text="modifier des pieces".upper())
    self.modifier_p_frame_label.grid(row=0, column=0, padx=20, pady=40)







def supprimer_fun(self):
    self.supprimer_p_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.supprimer_p_frame.grid_columnconfigure(0, weight=1)
    self.supprimer_p_frame_label = customtkinter.CTkLabel(self.supprimer_p_frame,font=("Arial", 20),text_color=blue_color, text="supprimer des pieces".upper())
    self.supprimer_p_frame_label.grid(row=0, column=0, padx=20, pady=40)






def rechercher_fun(self):
    self.rechercher_p_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.rechercher_p_frame.grid_columnconfigure(0, weight=1)
    self.rechercher_p_frame_label = customtkinter.CTkLabel(self.rechercher_p_frame,font=("Arial", 20),text_color=blue_color, text="rechercher des pieces".upper())
    self.rechercher_p_frame_label.grid(row=0, column=0, padx=20, pady=40)


