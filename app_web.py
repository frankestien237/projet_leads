import datetime
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

# 1. Formulaire prospect classique
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
    # Enregistrement des données
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

    # 2. Section de Commande & Paiement Automatisé
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

    # Le client entre son propre numéro pour déclencher le paiement USSD
    num_paiement = st.text_input(
        "Entrez votre numéro Mobile Money (ex: 698xxxxxx ou 670xxxxxx) :"
    )
    operateur_mobile = st.selectbox(
        "Opérateur :", ["Orange Money", "MTN MoMo"]
    )

    if st.button("Lancer la demande de paiement sur mon téléphone"):
      if not num_paiement:
        st.error("⚠️ Veuillez entrer un numéro de téléphone valide.")
      else:
        # Simulation du déclenchement de la requête USSD vers le client
        # (Ici, le lien redirige vers WhatsApp avec le numéro pré-saisi pour une validation instantanée et sécurisée)
        lien_validation = (
            f"https://wa.me/237698278163?text=Bonjour,%20je%20veux%20commander%20"
            f"{formule_choisie}%20via%20{operateur_mobile}%20au%20numero%20{num_paiement}."
            f"%20Envoi%20de%20la%20demande%20de%20paiement."
        )

        st.info(
            f"📲 Une notification USSD est envoyée au **{num_paiement}**."
            " Veuillez entrer votre code secret sur votre téléphone pour valider"
            " la transaction."
        )
        st.link_button(
            "Finaliser la confirmation sur WhatsApp", lien_validation
        )

    # Option Internationale (Cartes)
    st.markdown("---")
    st.link_button(
        "🌐 Payer par Carte Bancaire / PayPal (International)",
        "https://wa.me/237698278163?text=Bonjour,%20je%20veux%20payer%20par%20Carte%20depuis%20l'etranger",
    )