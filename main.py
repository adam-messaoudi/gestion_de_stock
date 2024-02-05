import tkinter as tk
from tkinter import ttk
from gui_functions import display_products, add_product, delete_product, edit_product, export_csv, plot_graph
from database_functions import connect_to_database

# Interface graphique avec tkinter
root = tk.Tk()
root.title("Gestion de Stock")

# Créer le tableau de bord
tree = ttk.Treeview(root, columns=("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie"))
tree.heading("#0", text="ID")
tree.heading("#1", text="Nom")
tree.heading("#2", text="Description")
tree.heading("#3", text="Prix")
tree.heading("#4", text="Quantité")
tree.heading("#5", text="Catégorie")

# Affichage des produits au lancement de l'application
display_products(tree)

# Ajouter des boutons
btn_add = tk.Button(root, text="Ajouter Produit", command=add_product)
btn_delete = tk.Button(root, text="Supprimer Produit", command=lambda: delete_product(tree))
btn_edit = tk.Button(root, text="Modifier Produit", command=edit_product)
btn_export_csv = tk.Button(root, text="Exporter CSV", command=export_csv)
btn_plot_graph = tk.Button(root, text="Afficher Graphique", command=plot_graph)

# Placement des éléments
tree.pack(padx=10, pady=10)
btn_add.pack(side=tk.LEFT, padx=10)
btn_delete.pack(side=tk.LEFT, padx=10)
btn_edit.pack(side=tk.LEFT, padx=10)
btn_export_csv.pack(side=tk.LEFT, padx=10)
btn_plot_graph.pack(side=tk.LEFT, padx=10)

# Boucle principale de l'interface graphique
root.mainloop()
