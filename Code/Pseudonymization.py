import json

# Fonction pour générer un identifiant unique
def generate_unique_id():
    return str(hash(str(id)))  # Cela génère un identifiant unique basé sur l'identifiant de l'objet Python

# Charger le fichier JSON
with open('oral_modified.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
with open('written_modified.json', 'r', encoding='utf-8') as file:
    data2 = json.load(file)

# Parcourir les données et pseudonymiser les noms d'auteurs
for item in data:
    author = item.get("author", {})
    author_name = author.get("name", "")
    if author_name:
        author["name"] = generate_unique_id()
for item in data2:
    author = item.get("author", {})
    author_name = author.get("name", "")
    if author_name:
        author["name"] = generate_unique_id()

# Enregistrer les données pseudonymisées dans un nouveau fichier JSON
with open('oral_pseudonymise.json', 'w', encoding='utf-8') as output_file:
    json.dump(data, output_file, ensure_ascii=False, indent=4)
with open('written_pseudonymise.json', 'w', encoding='utf-8') as output_file:
    json.dump(data2, output_file, ensure_ascii=False, indent=4)

print("Pseudonymisation terminée. Les données pseudonymisées sont enregistrées dans 'votre_fichier_pseudonymise.json'.")
