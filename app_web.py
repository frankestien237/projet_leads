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

# Formulaire de prospect initial
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

    # --- SECTION BOUTIQUE & PAIEMENT AUTOMATISÉ ---
    st.markdown("---")
    st.subheader(
        "🚀 Commandez votre propre application personnalisée en 24h"
    )

    # Choix du pack par le client
    pack_choisi = st.selectbox(
        "Sélectionnez votre formule :",
        [
            "Formule Standard - 50 000 FCFA",
            "Formule Pro - 150 000 FCFA",
            "Formule Entreprise - 250 000 FCFA",
        ],
    )

    # Saisie du numéro pour le prélèvement Mobile Money
    numero_paiement = st.text_input(
        "Entrez votre numéro Mobile Money (ex: 698278163 ou 670000000) :"
    )
    operateur = st.selectbox(
        "Choisissez votre opérateur :", ["Orange Money", "MTN MoMo"]
    )

    # Bouton de validation du paiement
    if st.button("Valider et payer maintenant"):
      if not numero_paiement:
        st.error("⚠️ Veuillez entrer un numéro de téléphone pour le paiement.")
      else:
        # Ici, si vous connectez une API comme Notch Pay ou Fapshi,
        # une requête est envoyée pour afficher la demande de code PIN sur le téléphone du client.
        # En attendant, on redirige vers WhatsApp avec les détails pré-remplis pour validation manuelle sécurisée.

        url_whatsapp = (
            f"https://wa.me/237698278163?text=Bonjour,%20je%20veux%20payer%20"
            f"{pack_choisi}%20via%20{operateur}%20au%20numero%20{numero_paiement}."
        )

        st.success(
            "🔄 Demande de paiement transmise ! Vérifiez votre téléphone pour"
            " valider la transaction ou cliquez ci-dessous si la pop-up ne s'affiche"
            " pas :"
        )
        st.link_button("📲 Confirmer sur WhatsApp", url_whatsapp)

    # Option Carte Bancaire Internationale
    st.markdown("---")
    st.link_button(
        "🌐 Payer par Carte Bancaire / PayPal (International)",
        "https://wa.me/237698278163?text=Bonjour,%20je%20veux%20payer%20par%20Carte%20depuis%20l'etranger",
    )