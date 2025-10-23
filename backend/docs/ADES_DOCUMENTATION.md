# 📘 Documentation Complète de l'Application Lemadio

## 🎯 Objectif de l'Assistant Lemadio
### Qui suis-je ?
Je suis **Assistant Lemadio**, un assistant conversationnel conçu pour accompagner les vendeurs des points de vente ADES dans l’utilisation optimale de l’application mobile **Lemadio**.

### Quel est mon rôle ?
Ma mission principale est de **former, guider et assister** les vendeurs afin qu’ils puissent utiliser l’application Lemadio sans difficulté. Je suis disponible à tout moment pour répondre aux questions liées à l’utilisation de l’application.

### Que suis-je capable de faire ?
Fournir des **explications claires** sur les fonctionnalités de Lemadio.
- Aider à résoudre les **problèmes courants** rencontrés par les vendeurs.
- Proposer des **étapes détaillées** pour accomplir une action dans l’application.
- Répondre aux **questions fréquentes** sur l’authentification, la gestion des ventes, la synchronisation des données, etc.

Je suis conçu pour rendre l’expérience utilisateur plus fluide, autonome et efficace.

## 🔐 Page d’authentification

### Connexion à l’application Lemadio

Lorsqu’un vendeur ouvre l’application Lemadio, la première interface affichée est la page d’authentification. La toute première connexion nécessite une connexion Internet afin de valider les informations auprès du serveur. Une fois cette authentification initiale réussie, l’application enregistre localement le nom d’utilisateur associé.

Lors des connexions suivantes, le vendeur peut s’authentifier hors ligne en saisissant uniquement son mot de passe. Chaque instance de l’application est liée à un seul compte vendeur. Après une première authentification réussie en ligne, toute tentative de connexion avec un autre compte est bloquée, sur la base des données enregistrées localement.

---

## 🆔 Obtention des identifiants

### Où obtenir l’identifiant et le mot de passe vendeur

Les identifiants de connexion (nom d’utilisateur et mot de passe) sont fournis par l’administrateur, plus précisément par l’équipe IT.

---

## 🔄 Mot de passe oublié

### Réinitialisation du mot de passe

En cas d’oubli du mot de passe, le vendeur peut initier une procédure de réinitialisation directement depuis l’application.

#### Étapes à suivre :

1. Cliquez sur le lien « Mot de passe oublié ? » situé sous le bouton de connexion.
2. Une fenêtre contextuelle s’ouvre : sélectionnez votre centre de vente, saisissez le nouveau mot de passe souhaité, puis validez la demande.
3. Le système envoie automatiquement un code de confirmation à l’administrateur, accompagné de vos informations, par e-mail.
4. Il est recommandé de contacter l’administrateur au préalable afin qu’il puisse vous transmettre rapidement le code de confirmation.
5. L’application vous redirige vers une nouvelle fenêtre pour saisir ce code et finaliser la modification du mot de passe.
6. **NB** : ⚠️ Le code de confirmation est valide pendant **10 minutes** seulement.

---

## 🧩 Éléments de la page d’authentification

- **Logo ADES** : affiché en haut de la page pour identifier l’application.
- **Champ « Nom d’utilisateur »** : permet au vendeur de saisir son identifiant fourni par l’administrateur.
- **Champ « Mot de passe »** : champ sécurisé pour entrer le mot de passe associé au compte.
- **Bouton « Se connecter »** : déclenche la tentative d’authentification avec les informations saisies.
- **Lien « Mot de passe oublié ? »** : situé sous le bouton de connexion, il permet d’accéder au processus de réinitialisation du mot de passe.

---

## ✅ Actions pour se connecter

### 1. Saisir le nom d’utilisateur

Dans le champ prévu à cet effet, entrez le nom d’utilisateur fourni par l’administrateur. Ce nom correspond généralement au nom de votre point de vente.  
**Exemple** : pour le point de vente de Fianarantsoa, le nom d’utilisateur sera `Vente Fianarantsoa`.

### 2. Saisir le mot de passe

Dans le champ « Mot de passe », entrez votre mot de passe personnel. Une icône en forme d’œil, située à droite du champ, permet d’afficher ou masquer le mot de passe saisi pour plus de confort et de sécurité.

### 3. Cliquer sur le bouton « Se connecter »

Une fois les informations saisies, cliquez sur le bouton « Se connecter » pour accéder à l’application.

---

## 2. Vue d'ensemble de l'interface

### Description générale

Une fois connecté avec succès, le vendeur est redirigé vers la page principale dédiée à la gestion des ventes.

### Composants de l'interface

#### 🔝 Entête

- **Logo ADES** affiché à gauche.
- **Zone utilisateur** à droite :
  - Icône circulaire suivi du nom d'utilisateur du vendeur.
  - Icône à trois points verticaux ouvrant un menu contextuel avec les options suivantes :
    - **Mode** : Permet de basculer entre le mode clair et le mode sombre.
    - **Synchroniser** : Envoie les données locales non encore transmises au serveur ADES.
    - **Catalogue de prix** : Affiche les tarifs associés à chaque type de réchaud ou poêle.
    - **Changer le mot de passe** : Accès à la modification du mot de passe.
    - **Déconnexion** : Permet de quitter l'application.

#### 📄 Contenu principal (variable selon la barre de navigation inférieure)

##### 1. Page des ventes

Affiche les ventes réalisées par le vendeur. Si aucune vente n'a été enregistrée, un message indique : "Aucune vente trouvée."

**Éléments de la page :**

- **Barre de recherche** (en haut à gauche) : Recherche par type de réchaud, nom du client, numéro de facture ou contact.
- **Icône de filtrage** (à droite de la barre) : Permet d'afficher soit les ventes synchronisées avec le serveur ADES, soit celles encore stockées localement.
- **Liste des ventes** : Chaque vente est présentée sous forme de carte.

**Détails de chaque carte :**

- **Statut de synchronisation** :
  - "Synchronisé" (texte vert avec bordure arrondie) : Donnée envoyée au serveur ou à Salesforce.
  - "Non synchronisé" (texte orange) : Donnée encore locale.
- **Bouton "Annuler"** (en haut à droite, bordure rouge) : Permet d'annuler la vente localement et à distance.
- **Informations affichées** : Nom complet du client, numéro de facture, date de vente, numéro du réchaud.
- **Icône flèche vers le bas** : Déploie la carte pour afficher des détails supplémentaires (contact, adresse, région, fokontany).

##### 2. Page des stocks

La page "Stock" contient plusieurs fonctionnalités essentielles pour la gestion des réchauds :

- 🔍 Barre de recherche (en haut de la page)
  - Permet de rechercher un réchaud par type, numéro, ou type + numéro pour plus de précision.
  - Exemple de recherche efficace : OLI-c T123456, OLI-60b 258963.
- 🧭 Menu de navigation (sous la barre de recherche)
  Ce menu contient deux onglets principaux :
  1. Stocks actuels


      - C’est l’onglet affiché par défaut à l’ouverture de la page "Stock".
      - Il affiche tous les réchauds disponibles pour le vendeur ou le point de vente.
      - Les réchauds sont :
        - Encadrés en vert s’ils sont disponibles pour une nouvelle vente.
        - Encadrés en rouge avec un badge "vendu" s’ils sont déjà associés à une vente.
  2. Numéro facture
  - Situé à droite de l’onglet "Stocks actuels".
  - Permet de visualiser les numéros de facture liés au vendeur ou au point de vente.
  - Les numéros sont :
    - Encadrés en vert s’ils sont disponibles pour une nouvelle vente.
    - Encadrés en rouge avec un badge "vendu" s’ils sont déjà utilisés dans une vente.

##### 3. Page des remplacements sous garantie

Accès à la gestion des remplacements de réchauds sous garantie.

##### 4. Page des statistiques de vente

Visualisation graphique des performances commerciales du vendeur.

#### 📱 Barre de navigation inférieure

Permet de naviguer entre les différentes sections de l'application :

1. **Ventes** : Icône avec badge indiquant le nombre de ventes non synchronisées.
2. **Stocks** : Affiche les stocks disponibles.
3. **Remplacements sous garantie** : Gestion des remplacements.
4. **Statistiques de vente** : Visualisation des performances.

---

## 3. Créer une vente

### Processus complet

#### Étape 1 : Accéder à la création de vente

Sur la page de vente :

- Cliquez le bouton rond vert avec un icône plus (+) dedans, en haut à droite de la barre de navigation inférieure.
- Deux menus vont s'afficher :
  - **"Vente revendeur"** : Vente aux revendeurs de l'ADES
  - **"Vente directe"** : Vente directe aux clients

### Processus pour vente directe

#### Étape 2 : Page d'information client

Une formulaire permet de remplir l'information client :

**Champs du formulaire :**

- **Liste déroulante "Catégorie"** :

  - Hotel
  - Ecole
  - Restaurant
  - NGO
  - Hospital
  - Microbusiness
  - Prison
  - Private

- **Liste déroulante "Cluster"** :

  - Charcoal
  - Wood
  - Solar + OLI-b
  - Solar + OLI-c

- **Champ Mme/Mr** : nom du client
- **Champ Surnom** : prénom du client
- **Contact** : numéro de téléphone
- **Adresse** : adresse complète

- **Champ Localisation** :

  - Cliquez l'icône de localisation dans le formulaire côté droit, cela ouvrira une carte OpenStreetMap

  **Page carte :**

  - Cette carte permet de récupérer la longitude et latitude du client
  - Elle prend automatiquement la position actuelle de l'appareil pour aider le vendeur à tracer l'endroit du client et place un petit icône de localisation en rouge sur la carte
  - Une barre de recherche en haut permet de chercher l'endroit du client par fokontany, région, district, commune
  - Saisissez l'endroit et cliquez l'icône recherche côté droit
  - En faisant la recherche, l'app propose plusieurs endroits en montrant la province, région, district, commune, fokontany
  - Cliquez sur l'endroit exact du client, la carte redirigera vers l'endroit indiqué par le petit icône
  - Le vendeur peut zoomer la carte, scroller et cliquer partout sur la carte pour avoir l'endroit exact du client
  - Validez la sélection avec le bouton bleu en bas
  - Après validation, les champs (localisation, région, district, commune, fokontany) seront remplis automatiquement

  ⚠️ **Note importante** : Il faut bien vérifier les champs remplis automatiquement car parfois la carte ne trouve pas la commune, le district ou le fokontany et affiche "Non spécifié". Le vendeur peut remplir manuellement dans ce cas.

- **CIN recto** : facultatif, dédié pour capturer l'image du CIN recto du client
- **CIN verso** : facultatif, dédié pour capturer l'image du CIN verso du client

- Cliquez le bouton **"Valider"** pour passer à la page suivante.

#### Étape 3 : Sélectionner le numéro de facture

Cette page affiche la liste des numéros de facture liés au centre de vente. Il suffit de sélectionner un numéro puis cliquer le bouton valider.

#### Étape 4 : Page de vérification d'information client

Vérifiez toutes les informations saisies avant de continuer.

#### Étape 5 : Scanner les numéros de réchauds

- Cliquez le bouton arrondi dans le cadre jaune en bas à droite pour scanner le réchaud
- Le numéro de réchaud scanné s'affichera comme une liste dans le cadre
- Le vendeur peut scanner ou vendre seulement les réchauds dans sa liste de stock
- Chaque réchaud doit être associé à un prix et une zone (zone riche, zone moyen, zone LNOB) pour être validé
- Chaque zone doit avoir des régions différentes
- Chaque type de réchaud a un prix différent selon la zone
  - Exemple :
    - Zone riche : OLI-c = 21 000 Ar
    - Zone pauvre : OLI-c = 15 000 Ar
- Un client peut acheter plusieurs réchauds du même type ou de types différents
- En bas du cadre, un tableau montre :
  - Le type de réchaud
  - Le prix unitaire de chaque type
  - Le nombre de réchauds que le client a achetés
  - Le total (prix unitaire × nombre de réchauds)
- Cliquez le bouton **"Valider"** pour continuer

#### Étape 6 : Page de garantie

**Informations sur la garantie :**

- Chaque réchaud a une garantie d'un an à partir de la date d'achat.
- La garantie n'inclut pas les conséquences d'une utilisation non appropriée, ni les dommages dus à des actes volontaires.
- L'ADES ne garantit que l'argile.
- Lorsque les deux grilles fournies sont hors d'usage, des grilles supplémentaires peuvent être obtenues gratuitement auprès d'un point de vente ADES. Amenez votre reçu et votre carte garantie pour vérification du numéro de série de votre foyer amélioré.
- Tous les droits sur les certificats CO2 restent chez ADES.

**Actions :**

- Cochez la case **"J'accepte de céder le droit de ce dossier pour signer"**
- Faites signer le client sur l'application (signature tactile)
- Cliquez **"Enregistrer"** pour terminer la vente

#### Résultat de la vente

**Si la vente réussit :**

- Le vendeur peut voir le détail de la vente sur la page vente
- Sur la carte, la vente est marquée **"Synchronisé"**
- Le réchaud sera marqué **"vendu"** dans la liste de stock
- Le numéro de facture lié à la vente est marqué vendu

**Si la vente ne réussit pas (pas de connexion internet) :**

- La donnée de vente est sauvegardée en local
- Le statut sur le détail de vente dans la page vente est **"Non synchronisé"**
- Le réchaud sera marqué **"vendu"** dans la liste de stock
- Le numéro de facture lié à la vente est marqué vendu
- La barre de navigation inférieure affiche le badge du total nombre de ventes non synchronisées

---

## 4. Annuler une vente

**Processus d'annulation :**

- Cliquez le bouton **"Annuler"** sur la carte dans la page vente
- L'app récupère automatiquement le numéro de réchaud et de facture
- Entrez le motif pour lequel le vendeur annule la vente
- Cliquez le bouton **"Valider"**

⚠️ **Note importante** : Seule une journée depuis la création de la vente est valide pour annuler une vente depuis l'app mobile. Après une journée, il faut contacter le responsable pour l'annulation de la vente.

---

## 5. Types de réchauds chez ADES

L'ADES commercialise différents types de réchauds et poêles :

- **OLI-c** : charbon, petit format
- **OLI-b** : bois, petit format
- **OLI-45c** : charbon, moyen format
- **OLI-45b** : bois, moyen format
- **OLI-60c** : charbon, grand format
- **OLI-60b** : bois, grand format
- **Box** : multifonction
- **Parabole** : réflecteur solaire

---

## 6. Synchronisation des données

### Qu'est-ce que la synchronisation ?

La synchronisation est le processus d'envoi des données locales (ventes, stocks) vers le serveur ADES et Salesforce.

### Quand synchroniser ?

- **Automatique** : L'application tente de synchroniser automatiquement lorsqu'une connexion internet est disponible
- **Manuel** : Vous pouvez forcer la synchronisation via le menu (icône trois points → "Synchroniser")

### Comment savoir si une vente est synchronisée ?

- **Synchronisé** : Badge vert avec le texte "Synchronisé"
- **Non synchronisé** : Badge orange avec le texte "Non synchronisé"
- Le badge sur l'icône "Ventes" dans la barre de navigation indique le nombre de ventes non synchronisées

---

## 7. Déconnexion

**Étapes pour se déconnecter :**

1. Cliquez l'icône trois points verticaux en haut à droite près du nom d'utilisateur sur l'entête
2. Cliquez sur **"Déconnexion"**
3. Cliquez **"Oui"** pour confirmer
4. Vous serez redirigé vers l'écran de login

---

## 8. Messages d'erreur et solutions

| Message d'erreur              | Cause                         | Solution                                         |
| ----------------------------- | ----------------------------- | ------------------------------------------------ |
| "Connexion perdue"            | Pas d'internet                | Vérifiez votre connexion WiFi ou données mobiles |
| "Identifiants incorrects"     | Mauvais login ou mot de passe | Vérifiez votre nom d'utilisateur et mot de passe |
| "Stock insuffisant"           | Pas assez de réchauds         | Contactez le responsable du point de vente       |
| "Vente non enregistrée"       | Erreur serveur                | Vérifiez la connexion ou contactez le support    |
| "Réchaud déjà vendu"          | Réchaud scanné déjà vendu     | Vérifiez le numéro du réchaud                    |
| "Numéro de facture invalide"  | Facture déjà utilisée         | Sélectionnez un autre numéro de facture          |
| "Localisation introuvable"    | GPS désactivé                 | Activez le GPS de l'appareil                     |
| "Code de confirmation expiré" | 10 minutes dépassées          | Demandez un nouveau code à l'administrateur      |

---

## 9. Dépannage

### L'application ne démarre pas

**Solutions :**

- Vérifiez que vous avez une connexion internet (pour la première connexion)
- Redémarrez le téléphone
- Vérifiez l'espace de stockage disponible
- Réinstallez l'application si nécessaire

### La vente n'est pas enregistrée

**Solutions :**

- Vérifiez que vous avez cliqué sur "Enregistrer"
- Vérifiez que tous les champs obligatoires sont remplis
- Vérifiez la connexion internet
- Si la vente est "Non synchronisée", elle sera envoyée automatiquement quand la connexion reviendra

### Le scanner ne fonctionne pas

**Solutions :**

- Vérifiez que la caméra fonctionne
- Assurez-vous d'avoir autorisé l'accès à la caméra
- Nettoyez l'objectif de la caméra
- Assurez-vous que le code QR/numéro est lisible

### Le type de réchaud n'est pas disponible

**Solutions :**

- Vérifiez que la région du client est présente dans votre zone de catalogue de prix
- Vérifiez le prix du type de réchaud dans le catalogue
- Contactez l'administrateur si le prix n'est pas configuré

### La carte ne trouve pas la localisation

**Solutions :**

- Activez le GPS de l'appareil
- Autorisez l'accès à la localisation pour l'application
- Vérifiez la connexion internet
- Si "Non spécifié" apparaît, remplissez manuellement les champs

### Impossible de synchroniser

**Solutions :**

- Vérifiez votre connexion internet
- Attendez quelques minutes et réessayez
- Utilisez le menu "Synchroniser" manuellement
- Contactez le support si le problème persiste

---

## 10. FAQ (Foires Aux Questions)

**Q : Peut-on modifier une vente après l'avoir enregistrée ?**
R : Non, pas directement dans l'application. Contactez le responsable du point de vente pour toute modification.

**Q : Quel est le délai de confirmation d'une vente ?**
R : La vente est enregistrée instantanément sur Salesforce si vous avez une connexion internet. Sinon, elle sera synchronisée automatiquement plus tard.

**Q : Puis-je vendre un réchaud sans connexion internet ?**
R : Oui, la vente sera enregistrée localement et synchronisée automatiquement dès que la connexion internet sera disponible.

**Q : Comment voir mes ventes non synchronisées ?**
R : Le badge sur l'icône "Ventes" dans la barre de navigation indique le nombre. Vous pouvez aussi utiliser le filtre dans la page des ventes.

**Q : Combien de temps puis-je annuler une vente ?**
R : Vous avez 24 heures (une journée) après la création de la vente pour l'annuler depuis l'application. Au-delà, contactez le responsable.

**Q : Que faire si j'ai oublié mon mot de passe ?**
R : Utilisez le lien "Mot de passe oublié ?" sur la page de connexion. Vous aurez besoin de contacter l'administrateur pour obtenir le code de confirmation (valable 10 minutes).

**Q : Puis-je me connecter avec un autre compte sur le même téléphone ?**
R : Non, chaque application est liée à un seul compte vendeur. Après la première authentification, seul ce compte peut être utilisé sur cet appareil.

**Q : Que signifient les zones (riche, moyen, LNOB) ?**
R : Ce sont des zones de tarification différentes selon la région. Chaque zone a des prix différents pour les mêmes réchauds. Le prix est automatiquement appliqué selon la région du client.

**Q : Comment obtenir plus de numéros de facture ?**
R : Contactez le responsable de votre point de vente ou l'administrateur pour obtenir de nouveaux numéros de facture.

**Q : La garantie couvre-t-elle tout ?**
R : Non, la garantie ne couvre que l'argile du réchaud. Elle ne couvre pas les dommages dus à une mauvaise utilisation ou à des actes volontaires. La garantie est valable un an à partir de la date d'achat.

**Q : Que faire si le GPS ne trouve pas l'adresse exacte ?**
R : Si la carte affiche "Non spécifié" pour certains champs (commune, district, fokontany), vous pouvez les remplir manuellement dans le formulaire.
