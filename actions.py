import mysql.connector
from tkinter import messagebox

cnx= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
global cursor
cursor = cnx.cursor()

# # cursor.excute(f"SELECT * FROM people",(nom,prenom))

# cursor.execute(f"SELECT * FROM users")

# print(cursor.fetchall())

    # cursor.execute(f"SELECT * FROM pieces where ref = ?",())
    # ref,nom,four,qt,min_qt,taille = values
def ajouter_p(values):
    ref,nom,four,qt,min_qt,taille = values
    cursor.execute("SELECT * FROM pieces WHERE ref = %s", (ref,))
    rows = cursor.fetchall()
    if(len(rows) != 0):
        messagebox.showerror("Erreur", "le numero de référence est deja utilisé")
    else:
        cursor.execute("INSERT INTO pieces (ref, nom, fournisseur, quantite, quantite_min, taille) VALUES (%s,%s,%s,%s,%s,%s)", (ref,nom,four,qt,min_qt,taille))
        cnx.commit()
        messagebox.showinfo("Succès", "L'ajout a été effectué avec succès!")



def liste_p():
    cursor.execute("SELECT * FROM pieces")
    rows = cursor.fetchall()
    res=[["Référence","Nom","Fournisseur", "Quantité", "Quantité minimale", "Taille"]]
    for row in rows:
        res.append(list(row))

    return res


def modifier_p(values):
    ref,nom,four,qt,min_qt,taille = values
    cursor.execute("SELECT * FROM pieces WHERE ref = %s", (ref,))
    rows = cursor.fetchall()
    if(len(rows) == 0):
        messagebox.showerror("Erreur", "le numero de référence n'existe pas")
    else:
        if(nom != ""):
            cursor.execute("UPDATE pieces SET nom = %s WHERE pieces.ref = %s", (nom,ref))
        if(four != ""):
            cursor.execute("UPDATE pieces SET fournisseur = %s WHERE pieces.ref = %s", (four,ref))
        if(qt != ""):
            cursor.execute("UPDATE pieces SET quantite = %s WHERE pieces.ref = %s", (qt,ref))
        if(min_qt != ""):
            cursor.execute("UPDATE pieces SET quantite_min = %s WHERE pieces.ref = %s", (min_qt,ref))
        if(taille != ""):
            cursor.execute("UPDATE pieces SET taille = %s WHERE pieces.ref = %s", (taille,ref))
        


        cnx.commit()
        messagebox.showinfo("Succès", "La modification a été effectué avec succès!")


def supprimer_p(ref):
    cursor.execute("SELECT * FROM pieces WHERE ref = %s", (ref,))
    rows = cursor.fetchall()
    
    if len(rows) == 0:
        messagebox.showerror("Erreur", "Le numéro de référence n'existe pas.")
    else:
        confirm = messagebox.askquestion("Confirmation", "Êtes-vous sûr de vouloir supprimer cette entrée ?")
        if confirm == "yes":
            cursor.execute("DELETE FROM pieces WHERE ref = %s", (ref,))
            cnx.commit()
            messagebox.showinfo("Succès", "La suppression a été effectuée avec succès!")
