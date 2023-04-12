import json
import tkinter as tk
from tkinter import messagebox

class JSONCreator:
    def __init__(self, master):
        self.master = master
        self.master.title("JSON Creator")

        # Créer un widget Frame pour contenir les entrées et boutons
        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(padx=10, pady=10)

        # Entrée pour l'ID
        self.id_label = tk.Label(self.input_frame, text="ID:")
        self.id_label.grid(row=0, column=0, sticky="w")
        self.id_entry = tk.Entry(self.input_frame)
        self.id_entry.grid(row=0, column=1)

        # Entrée pour le pattern
        self.pattern_label = tk.Label(self.input_frame, text="Pattern:")
        self.pattern_label.grid(row=1, column=0, sticky="w")
        self.pattern_entry = tk.Entry(self.input_frame)
        self.pattern_entry.grid(row=1, column=1)

        # Bouton pour ajouter une nouvelle demande
        self.add_button = tk.Button(self.input_frame, text="Ajouter", command=self.add_request)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=(10,0))

        # Bouton pour créer le fichier JSON
        self.create_button = tk.Button(self.input_frame, text="Créer JSON", command=self.create_json)
        self.create_button.grid(row=3, column=0, columnspan=2, pady=(10,0))

        # Liste pour afficher les demandes ajoutées
        self.requests_list = tk.Listbox(self.master)
        self.requests_list.pack(padx=10, pady=10)

        self.requests = []

    def add_request(self):
        # Récupérer l'ID et le pattern entrés
        id = self.id_entry.get()
        pattern = self.pattern_entry.get()

        # Vérifier que les deux champs sont remplis
        if id and pattern:
            # Ajouter la nouvelle demande à la liste des demandes
            self.requests.append({"id": id, "request": [{"pattern": [pattern]}]})
            self.requests_list.insert(tk.END, f"{id}: {pattern}")
            # Réinitialiser les champs d'entrée
            self.id_entry.delete(0, tk.END)
            self.pattern_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    def create_json(self):
        # Vérifier qu'il y a au moins une demande
        if len(self.requests) > 0:
            # Enregistrer les demandes dans un fichier JSON
            with open("requests.json", "w") as f:
                json.dump(self.requests, f, indent=2)
            messagebox.showinfo("Succès", "Le fichier JSON a été créé.")
        else:
            messagebox.showerror("Erreur", "Ajoutez au moins une demande.")

if __name__ == "__main__":
    root = tk.Tk()
    app = JSONCreator(root)
    root.mainloop()
