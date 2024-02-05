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
