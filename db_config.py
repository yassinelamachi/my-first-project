import mysql.connector

# Configuration de la connexion
config = {
    'host': 'localhost',    # Serveur MySQL
    'user': 'root',         # Ton utilisateur MySQL
    'password': 'Pochita17$',  # Mets ton vrai mot de passe MySQL
    'database': 'my_project_db'  # Nom de la base de données
}

# Connexion à MySQL
try:
    conn = mysql.connector.connect(**config)
    if conn.is_connected():
        print("✅ Connexion réussie à la base de données !")
except mysql.connector.Error as err:
    print(f"❌ Erreur : {err}")
