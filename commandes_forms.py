import customtkinter
import customtkinter as tk
import os
from PIL import Image
global  blue_color
blue_color = "#5cafe7"


def ajouter_fun(self):
    self.ajouter_c_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.ajouter_c_frame.grid_columnconfigure(0, weight=1)
    self.ajouter_c_frame_label = customtkinter.CTkLabel(self.ajouter_c_frame,font=("Arial", 20),text_color=blue_color, text="ajouter des commandes".upper())
    self.ajouter_c_frame_label.grid(row=0, column=0, padx=20, pady=40)

def liste_fun(self):
    self.liste_c_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.liste_c_frame.grid_columnconfigure(0, weight=1)
    self.liste_c_frame_label = customtkinter.CTkLabel(self.liste_c_frame,font=("Arial", 20),text_color=blue_color, text="liste des commandes".upper())
    self.liste_c_frame_label.grid(row=0, column=0, padx=20, pady=40)



def supprimer_fun(self): 
    self.supprimer_c_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.supprimer_c_frame.grid_columnconfigure(0, weight=1)
    self.supprimer_c_frame_label = customtkinter.CTkLabel(self.supprimer_c_frame,font=("Arial", 20),text_color=blue_color, text="supprimer des commandes".upper())
    self.supprimer_c_frame_label.grid(row=0, column=0, padx=20, pady=40)

def modifier_fun(self):
    self.modifier_c_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.modifier_c_frame.grid_columnconfigure(0, weight=1)
    self.modifier_c_frame_label = customtkinter.CTkLabel(self.modifier_c_frame,font=("Arial", 20),text_color=blue_color, text="modifier des commandes".upper())
    self.modifier_c_frame_label.grid(row=0, column=0, padx=20, pady=40)

def rechercher_fun(self):
    self.rechercher_c_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
    self.rechercher_c_frame.grid_columnconfigure(0, weight=1)
    self.rechercher_c_frame_label = customtkinter.CTkLabel(self.rechercher_c_frame,font=("Arial", 20),text_color=blue_color, text="rechercher des commandes".upper())
    self.rechercher_c_frame_label.grid(row=0, column=0, padx=20, pady=40)
