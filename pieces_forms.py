import customtkinter
import customtkinter as tk
import os
from tkinter import ttk,messagebox
from CTkTable import *
import actions
from PIL import Image
global  blue_color
blue_color = "#5cafe7"

def liste_fun(self):
    # print("sss",screen_height)
    self.liste_p_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.liste_p_frame.grid_columnconfigure(0, weight=1)

    # Label in the first row of self.liste_p_frame
    self.liste_p_frame_label = customtkinter.CTkLabel(self.liste_p_frame, font=("Arial", 20), text_color=blue_color, text="liste des pieces".upper())
    self.liste_p_frame_label.grid(row=0, column=0,padx=20, pady=40)

    # Create a new frame in the second row
    self.second_row_frame = customtkinter.CTkFrame(self.liste_p_frame, corner_radius=0, fg_color="transparent")
    self.second_row_frame.grid(row=1, column=0, pady=10, sticky="ew")
    self.second_row_frame.grid_columnconfigure(0, weight=1)
    self.second_row_frame.grid_columnconfigure(1, weight=1)
    self.second_row_frame.grid_columnconfigure(2, weight=1)
    self.second_row_frame.grid_rowconfigure(0, weight=1)
    self.second_row_frame.grid_rowconfigure(1, weight=1)

    value = actions.liste_p()

    self.table = CTkTable(self.second_row_frame, row=len(value), column=6, values=value, )
    self.table.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=3) 
    def _liste_p():
        x = actions.liste_p()
        self.table.destroy()
        self.table = CTkTable(self.second_row_frame, row=len(value), column=6, values=x, )
        self.table.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=3)
        liste_fun(self)
        self.liste_p_frame.grid_forget()
        self.liste_p_frame.grid(row=0, column=1, sticky="nsew")


    

    self.button = customtkinter.CTkButton(self.second_row_frame, font=("Arial", 18), text="actualiser", width=150, border_width=2, corner_radius=5,command=_liste_p)
    self.button.grid(row=0, column=2, padx=25, pady=25)


def ajouter_fun(self):
    self.ajouter_p_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.ajouter_p_frame.grid_columnconfigure(0, weight=1)
    self.ajouter_p_frame_label = customtkinter.CTkLabel(self.ajouter_p_frame,font=("Arial", 20),text_color=blue_color, text="ajouter des pieces".upper())
    self.ajouter_p_frame_label.grid(row=0, column=0, padx=20, pady=40)

    # Create a new frame in the second row
    self.second_row_frame = customtkinter.CTkFrame(self.ajouter_p_frame, corner_radius=0, fg_color="transparent")
    self.second_row_frame.grid(row=1, column=0, pady=125, sticky="ew")

    

# Configure columns and rows for the second_row_frame
    for i in range(2):  # Two columns
        self.second_row_frame.grid_columnconfigure(i, weight=1)
    for i in range(4):  # Three rows
        self.second_row_frame.grid_rowconfigure(i, weight=1)

    ref_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Référence",
                                width=220,
                                height=2,
                                font=("Arial", 18),
                                border_width=2,
                                corner_radius=5)
    ref_entry.grid(row=0, column=0, padx=25, pady=25)
    nom_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Nom",
                                width=220,
                                font=("Arial", 18),
                                height=2,
                                border_width=2,
                                corner_radius=5)
    nom_entry.grid(row=0, column=1, padx=25, pady=25)


    four_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Fournisseur",
                                width=220,
                                height=2,
                                font=("Arial", 18),
                                border_width=2,
                                corner_radius=5)
    four_entry.grid(row=1, column=0, padx=25, pady=25)
    qt_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Quantité",
                                width=220,
                                font=("Arial", 18),
                                height=2,
                                border_width=2,
                                corner_radius=5)
    qt_entry.grid(row=1, column=1, padx=25, pady=25)

    min_qt_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Quantité minimale",
                                width=220,
                                font=("Arial", 18),
                                height=2,
                                border_width=2,
                                corner_radius=5)
    min_qt_entry.grid(row=2, column=0, padx=25, pady=25)
    taille_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Taille",
                                width=220,
                                font=("Arial", 18),
                                height=5,              border_width=2,
                                corner_radius=5)
    taille_entry.grid(row=2, column=1, padx=25, pady=25)
    def _ajouter_p():
        values=[ref_entry.get(),nom_entry.get(),four_entry.get(),qt_entry.get(),min_qt_entry.get(),taille_entry.get()]
        for i,val in enumerate(values):
            if(val.strip()==''):
                messagebox.showerror("Erreur", "tous les champs doit être non vides")
                return
            if(i>=3 and not val.isdigit()):
                messagebox.showerror("Erreur", "la quantité, la quantité minimale et la taille doivent tous être des nombres")
                return
        actions.ajouter_p(values)

    # print("aaa",self.taille_entry.get() + "eee",type(self.taille_entry.get()),len(self.taille_entry.get()))


    # ...
    # self.taille_entry.insert(0,"mother fucker")
    self.button = customtkinter.CTkButton(self.second_row_frame, font=("Arial", 18), text="Ajouter", width=220, border_width=2, corner_radius=5, command=_ajouter_p)
    self.button.grid(row=3, column=1, padx=25, pady=25)


    




def modifier_fun(self):
    self.modifier_p_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.modifier_p_frame.grid_columnconfigure(0, weight=1)
    self.modifier_p_frame_label = customtkinter.CTkLabel(self.modifier_p_frame,font=("Arial", 20),text_color=blue_color,text="modifier des pieces".upper())
    self.modifier_p_frame_label.grid(row=0, column=0, padx=20, pady=40)


    self.second_row_frame = customtkinter.CTkFrame(self.modifier_p_frame, corner_radius=0, fg_color="transparent")
    self.second_row_frame.grid(row=1, column=0, pady=125, sticky="ew")

    

# Configure columns and rows for the second_row_frame
    for i in range(2):  # Two columns
        self.second_row_frame.grid_columnconfigure(i, weight=1)
    for i in range(4):  # Three rows
        self.second_row_frame.grid_rowconfigure(i, weight=1)

    ref_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Référence",
                                width=220,
                                height=2,
                                font=("Arial", 18),
                                border_width=2,
                                corner_radius=5)
    ref_entry.grid(row=0, column=0, padx=25, pady=25)
    nom_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Nom",
                                width=220,
                                font=("Arial", 18),
                                height=2,
                                border_width=2,
                                corner_radius=5)
    nom_entry.grid(row=0, column=1, padx=25, pady=25)


    four_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Fournisseur",
                                width=220,
                                height=2,
                                font=("Arial", 18),
                                border_width=2,
                                corner_radius=5)
    four_entry.grid(row=1, column=0, padx=25, pady=25)
    qt_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Quantité",
                                width=220,
                                font=("Arial", 18),
                                height=2,
                                border_width=2,
                                corner_radius=5)
    qt_entry.grid(row=1, column=1, padx=25, pady=25)

    min_qt_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Quantité minimale",
                                width=220,
                                font=("Arial", 18),
                                height=2,
                                border_width=2,
                                corner_radius=5)
    min_qt_entry.grid(row=2, column=0, padx=25, pady=25)
    taille_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Taille",
                                width=220,
                                font=("Arial", 18),
                                height=5,
                                border_width=2,
                                corner_radius=5)
    taille_entry.grid(row=2, column=1, padx=25, pady=25)

    def _modifier_p():
        values=[ref_entry.get(),nom_entry.get(),four_entry.get(),qt_entry.get(),min_qt_entry.get(),taille_entry.get()]
        for i,val in enumerate(values):
            if( i == 0 and val.strip()==''):
                messagebox.showerror("Erreur", "la Référence de doit pas être vide")
                return
            if(i>=3 and not val.isdigit() and val!=""):
                messagebox.showerror("Erreur", "la quantité, la quantité minimale et la taille doivent tous être des nombres")
                return
        actions.modifier_p(values)

    self.button = customtkinter.CTkButton(self.second_row_frame,font=("Arial", 18), text="Modifier",width=220,border_width=2, corner_radius=5, command=_modifier_p)
    self.button.grid(row=3, column=1, padx=25, pady=25)
    ###################################
    




def supprimer_fun(self):
    self.supprimer_p_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.supprimer_p_frame.grid_columnconfigure(0, weight=1)
    self.supprimer_p_frame_label = customtkinter.CTkLabel(self.supprimer_p_frame,font=("Arial", 20),text_color=blue_color, text="supprimer des pieces".upper())
    self.supprimer_p_frame_label.grid(row=0, column=0, padx=20, pady=40)

    self.second_row_frame = customtkinter.CTkFrame(self.supprimer_p_frame, corner_radius=0, fg_color="transparent")
    self.second_row_frame.grid(row=1, column=0, pady=250, sticky="ew")

    self.second_row_frame.grid_columnconfigure(0, weight=1)
    self.second_row_frame.grid_columnconfigure(1, weight=1)
    self.second_row_frame.grid_rowconfigure(0, weight=1)


    ref_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Référence",
                                width=220,
                                font=("Arial", 18),
                                height=5,
                                border_width=2,
                                corner_radius=5)
    ref_entry.grid(row=0, column=0, padx=25, pady=25)


    def _supprimer_p():
        if(ref_entry.get().strip()==''):
            messagebox.showerror("Erreur", "la Référence de doit pas être vide")
            return
        actions.supprimer_p(ref_entry.get())

    self.button = customtkinter.CTkButton(self.second_row_frame,font=("Arial", 18), text="Supprimer",width=220,border_width=2, corner_radius=5,command=_supprimer_p)
    self.button.grid(row=0, column=1, padx=25, pady=25)



def rechercher_fun(self):
    self.rechercher_p_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.rechercher_p_frame.grid_columnconfigure(0, weight=1)
    self.rechercher_p_frame_label = customtkinter.CTkLabel(self.rechercher_p_frame,font=("Arial", 20),text_color=blue_color, text="rechercher des pieces".upper())
    self.rechercher_p_frame_label.grid(row=0, column=0, padx=20, pady=40)


    self.second_row_frame = customtkinter.CTkFrame(self.rechercher_p_frame, corner_radius=0, fg_color="transparent")
    self.second_row_frame.grid(row=1, column=0, pady=180, sticky="ew")

    self.second_row_frame.grid_columnconfigure(0, weight=1)
    self.second_row_frame.grid_columnconfigure(1, weight=1)
    self.second_row_frame.grid_rowconfigure(0, weight=1)

    
    self.ref_entry = customtkinter.CTkEntry(self.second_row_frame,
                                placeholder_text="Référence",
                                width=220,
                                font=("Arial", 18),
                                height=5,
                                border_width=2,
                                corner_radius=5)
    self.ref_entry.grid(row=0, column=0, padx=25, pady=25)
    self.button = customtkinter.CTkButton(self.second_row_frame,font=("Arial", 18), text="Rechercher",width=220,border_width=2, corner_radius=5)
    self.button.grid(row=0, column=1, padx=25, pady=25)








def prevision_fun(self):
    self.prevision_p_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.prevision_p_frame.grid_columnconfigure(0, weight=1)
    self.prevision_p_frame_label = customtkinter.CTkLabel(self.prevision_p_frame,font=("Arial", 20),text_color=blue_color, text="Prevision".upper())
    self.prevision_p_frame_label.grid(row=0, column=0, padx=20, pady=40)