import datetime
import os

def lancer_chatbot():
    print("=" * 60)
    print("🤖 Bienvenue sur l'assistant virtuel de qualification de prospects")
    print("=" * 60)
    print("Objectif : Capturer les besoins du client et enregistrer ses coordonnées.\n")

    # 1. Collecte du besoin
    print("Services disponibles :")
    print("1. Installation / Travaux neufs")
    print("2. Dépannage / Réparation urgente")
    print("3. Autre demande")
    
    choix = input("\nVeuillez entrer le numéro correspondant à votre demande (1, 2 ou 3) : ")
    
    activites = {
        "1": "Installation / Travaux neufs",
        "2": "Dépannage / Réparation urgente",
        "3": "Autre demande"
    }
    
    type_demande = activites.get(choix, "Demande générale")

    # 2. Description du projet
    description = input("\nDécrivez brièvement votre projet ou votre besoin : ")

    # 3. Localisation
    ville = input("\nDans quelle ville se situe le chantier / le besoin ? : ")

    # 4. Coordonnées
    nom = input("\nQuel est votre nom complet ? : ")
    telephone = input("Quel est votre numéro de téléphone pour vous joindre ? : ")

    # Structuration des données du prospect
    date_du_jour = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    nouveau_lead = f"""
--------------------------------------------------
Date : {date_du_jour}
Nom : {nom}
Téléphone : {telephone}
Type de demande : {type_demande}
Description : {description}
Ville : {ville}
--------------------------------------------------
"""

    # Sauvegarde automatique dans un fichier texte (simule l'envoi au client final)
    nom_fichier = "leads_clients.txt"
    with open(nom_fichier, "a", encoding="utf-8") as f:
        f.write(nouveau_lead)

    # Message de fin pour l'utilisateur
    print("\n" + "=" * 60)
    print(f"✅ Merci {nom} ! Vos informations ont bien été transmises.")
    print("Notre équipe vous contactera sous 2 heures ouvrées.")
    print("=" * 60)
    print(f"\n[Info développeur] Le prospect a été sauvegardé dans '{nom_fichier}'.")

if __name__ == "__main__":
    lancer_chatbot()