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

# Traitement une fois que le formulaire est soumis (en dehors du "with st.form")
if submit:
  # Validation basique
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

    # Message de succès affiché sur la page web
    st.success(
        f"✅ Merci {nom} ! Vos informations ont bien été transmises. Notre"
        " équipe vous contactera sous 2 heures ouvrées."
    )

    # Ajout de l'appel à l'action pour monétiser l'application
    st.markdown("---")
    st.subheader("🚀 Vous aimez ce système pour votre propre entreprise ?")
    st.write(
        "Commandez votre propre application personnalisée à vos couleurs en"
        " 24h."
    )

    st.link_button(
        "Commander votre appli (50 000 FCFA)",
        (
            "https://wa.me/237698278163?text=Bonjour,%20je%20veux%20commander"
            "%20cette%20application%20pour%20mon%20entreprise"
        ),
    )