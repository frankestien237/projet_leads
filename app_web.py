import datetime
import requests
import streamlit as st

# Configuration de la page web
st.set_page_config(
    page_title="Assistant Virtuel - Devis & Prospects", page_icon="🤖", layout="centered"
)

st.title("🤖 Assistant Virtuel de Qualification")
st.write(
    "Répondez à ces quelques questions pour que notre équipe vous recontacte"
    " rapidement."
)

# 1. Formulaire prospect
with st.form("form_lead"):
    type_demande = st.selectbox(
        "Services disponibles :",
        [
            "1. Installation / Travaux neufs",
            "2. Dépannage / Réparation urgente",
            "3. Autre demande",
        ],
    )
    description = st.text_area(
        "Décrivez clairement votre projet ou votre besoin :"
    )
    ville = st.text_input("Dans quelle ville se situe le chantier / le besoin ?")
    nom = st.text_input("Quel est votre nom complet ?")
    telephone = st.text_input("Quel est votre numéro de téléphone ?")
    submit = st.form_submit_button("Envoyer ma demande")

if submit:
    if not nom or not telephone or not ville:
        st.error(
            "⚠️ Veuillez remplir au moins votre nom, votre téléphone et la ville."
        )
    else:
        # Enregistrement des données du lead
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
        with open("leads_clients.txt", "a", encoding="utf-8") as f:
            f.write(nouveau_lead)

        st.success(
            f"✅ Merci {nom} ! Vos informations ont bien été transmises. Notre"
            " équipe vous contactera sous 2 heures ouvrées."
        )

        # 2. Section de Paiement Automatisé Notch Pay
        st.markdown("---")
        st.subheader(
            "🚀 Commandez votre propre application personnalisée en 24h"
        )

        formule_choisie = st.selectbox(
            "Choisissez votre formule :",
            [
                "Formule Standard (50 000 FCFA)",
                "Formule Pro (150 000 FCFA)",
                "Formule Entreprise (250 000 FCFA)",
            ],
        )

        montant = 50000
        if "Pro" in formule_choisie:
            montant = 150000
        elif "Entreprise" in formule_choisie:
            montant = 250000

        num_paiement = st.text_input(
            "Entrez votre numéro Mobile Money (Orange ou MTN) :"
        )

        if st.button("Lancer le paiement sécurisé"):
            if not num_paiement:
                st.error("⚠️ Veuillez entrer un numéro de téléphone.")
            else:
                # Configuration de la requête vers l'API Notch Pay
                url_notch = "https://api.notchpay.co/payments"

                headers = {
                    "Authorization": "sk_test.c1kgb3QK8qlvRncPIm62lgqCILZC5zTqlEBTSMWDHGGYfKqYHEHzhh7BxfRhMIbjfXYgU6eKrTfR9aJzBtWzIM6TB1LWM4JRm1H7XZUN88ONYGkqKbLD2PDZyswsE",
                    "Content-Type": "application/json",
                }

                payload = {
                    "amount": montant,
                    "currency": "XAF",
                    "phone": num_paiement,
                    "description": f"Paiement {formule_choisie}",
                    "email": "client@example.com",
                    "name": nom,
                }

                try:
                    response = requests.post(url_notch, json=payload, headers=headers)
                    data = response.json()

                    if response.status_code == 200 or response.status_code == 201:
                        st.success(
                            "🎉 Demande de paiement initialisée avec succès ! Vérifiez votre"
                            " téléphone pour entrer votre code secret."
                        )
                    else:
                        st.error(
                            f"❌ Erreur lors de l'initialisation : {data.get('message', 'Vérifiez les informations')}"
                        )
                except Exception as e:
                    st.error(
                        "⚠️ Impossible de contacter la passerelle de paiement pour le"
                        " moment."
                    )

        # Option Internationale
        st.markdown("---")
        st.link_button(
            "🌐 Payer par Carte Bancaire / PayPal (International)",
            "https://wa.me/237698278163?text=Bonjour,%20je%20veux%20payer%20par%20Carte%20depuis%20l'etranger",
        )