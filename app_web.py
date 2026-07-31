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

# Création du formulaire web
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

  # Bouton de validation du formulaire
  submit = st.form_submit_button("Envoyer ma demande")

# Traitement après soumission
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

    # Message de succès
    st.success(
        f"✅ Merci {nom} ! Vos informations ont bien été transmises. Notre"
        " équipe vous contactera sous 2 heures ouvrées."
    )

    # Section de monétisation avec les différentes gammes de prix (50k à 250k FCFA)
    st.markdown("---")
    st.subheader(
        "🚀 Vous souhaitez ce même système pour votre propre entreprise ?"
    )
    st.write("Choisissez votre formule pour commander :")

    # Formule Standard
    st.markdown("**1. Formule Standard (50 000 FCFA)** : Appli prête à l'emploi")
    st.link_button(
        "📱 Commander la Formule Standard (Mobile Money)",
        (
            "https://wa.me/237698278163?text=Bonjour,%20je%20veux%20commander%20la%20Formule%20Standard%20à%2050%20000%20FCFA"
        ),
    )

    # Formule Pro / Avancée
    st.markdown(
        "**2. Formule Pro (150 000 FCFA)** : Intégration sur mesure +"
        " Automatisation WhatsApp"
    )
    st.link_button(
        "📱 Commander la Formule Pro (Mobile Money)",
        (
            "https://wa.me/237698278163?text=Bonjour,%20je%20veux%20commander%20la%20Formule%20Pro%20à%20150%20000%20FCFA"
        ),
    )

    # Formule Entreprise / Sur-mesure
    st.markdown(
        "**3. Formule Entreprise (250 000 FCFA)** : Solution complète avec"
        " nom de domaine personnalisé et support prioritaire"
    )
    st.link_button(
        "📱 Commander la Formule Entreprise (Mobile Money)",
        (
            "https://wa.me/237698278163?text=Bonjour,%20je%20veux%20commander%20la%20Formule%20Entreprise%20à%20250%20000%20FCFA"
        ),
    )

    # Option Carte Bancaire Internationale (pour les clients étrangers)
    st.markdown("---")
    st.link_button(
        "🌍 Payer par Carte Bancaire (International / Étranger)",
        "https://wa.me/237698278163?text=Bonjour,%20je%20veux%20payer%20par%20Carte%20Bancaire%20depuis%20l'etranger",
    )