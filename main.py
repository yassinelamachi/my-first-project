import mysql.connector
from db_config import config

def add_user(name, email):
    # Connexion à la base de données
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    try:
        # Requête pour insérer un utilisateur
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (name, email)
        cursor.execute(query, values)
        conn.commit()
        print(f"✅ Utilisateur {name} ajouté avec succès !")
    except mysql.connector.Error as err:
        print(f"❌ Erreur : {err}")
    finally:
        cursor.close()
        conn.close()

# Exemple d'ajout d'un utilisateur
add_user("John Doe", "john@example.com")
