import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.tix import Tree
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connexion à la base de données
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A.m.13015",
    database="store"
)
cursor = db_connection.cursor()

# Fonction pour afficher les produits dans le tableau
# gui_functions.py
def display_products(tree):
    tree.delete(*tree.get_children())
    cursor.execute("""
        SELECT p.id, p.name, p.description, p.price, p.quantity, c.name
        FROM product p
        JOIN category c ON p.id_category = c.id
    """)
    products = cursor.fetchall()
    for product in products:
        tree.insert("", "end", values=product)

# Fonction pour ajouter un produit
def add_product():
    # Implémenter la logique pour ajouter un produit à la base de données
    pass

# Fonction pour supprimer un produit
def delete_product():
    selected_item = ttk.Treeview.selection()
    if not selected_item:
        messagebox.showerror("Erreur", "Veuillez sélectionner un produit à supprimer.")
    else:
        # Implémenter la logique pour supprimer le produit de la base de données
        pass

# Fonction pour modifier un produit
def edit_product():
    selected_item = ttk.Treeview.selection()
    if not selected_item:
        messagebox.showerror("Erreur", "Veuillez sélectionner un produit à modifier.")
    else:
        # Implémenter la logique pour modifier le produit dans la base de données
        pass

# Fonction pour exporter les produits en CSV
def export_csv():
    cursor.execute("""
        SELECT p.id, p.name, p.description, p.price, p.quantity, c.name
        FROM product p
        JOIN category c ON p.id_category = c.id
    """)
    products = cursor.fetchall()
    df = pd.DataFrame(products, columns=["ID", "Nom", "Description", "Prix", "Quantité", "Catégorie"])
    df.to_csv("stock_export.csv", index=False)
    messagebox.showinfo("Export CSV", "Les données ont été exportées avec succès.")

# Fonction pour afficher un graphique
def plot_graph():
    cursor.execute("""
        SELECT c.name, SUM(p.quantity) as total_quantity
        FROM product p
        JOIN category c ON p.id_category = c.id
        GROUP BY c.name
    """)
    category_data = cursor.fetchall()

    categories = [data[0] for data in category_data]
    quantities = [data[1] for data in category_data]

    # Créer le graphique
    fig, ax = plt.subplots()
    ax.bar(categories, quantities)
    ax.set_xlabel("Catégorie")
    ax.set_ylabel("Quantité totale")
    ax.set_title("Quantités de produits par catégorie")

    # Afficher le graphique dans une fenêtre séparée
    plt.show()
