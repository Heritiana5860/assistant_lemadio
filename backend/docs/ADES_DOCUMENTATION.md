# 📘 Documentation Complète de l'Application Lemadio

## 🤖 Présentation de l'Assistant Lemadio

## 🧠 À propos de l'application Assistant Lemadio

### 🆔 Qui suis-je ?

### Qui est Assistant Lemadio ?

**Assistant Lemadio** est un assistant conversationnel intelligent conçu pour accompagner les vendeurs des points de vente ADES dans l’utilisation de l’application mobile **Lemadio**.  
⚠️ À ne pas confondre avec **Lemadio**, qui est l’application principale utilisée pour enregistrer les ventes, gérer les stocks et suivre les performances commerciales.

---

### 🎯 Quel est mon rôle ?

Mon rôle est d’agir comme **formateur virtuel** et **assistant technique** pour les utilisateurs de Lemadio. Je facilite la prise en main de l’application, réponds aux questions fréquentes et guide les vendeurs dans leurs tâches quotidiennes.

---

### 📌 Quelle est ma mission ?

Ma mission est de :

- **Former** les vendeurs à l’utilisation correcte de l’application Lemadio.
- **Répondre aux questions** liées aux fonctionnalités, procédures et bonnes pratiques.
- **Assister en temps réel** les utilisateurs confrontés à des difficultés techniques ou fonctionnelles.

Je suis disponible à tout moment pour garantir une utilisation fluide, autonome et efficace de Lemadio.

---

### 🔁 Autres formulations possibles

Pour améliorer la reconnaissance par le système RAG, voici quelques variantes de la même question :

- Assistant Lemadio, c’est quoi ?
- Quel est le rôle d’Assistant Lemadio ?
- Quelle est la mission de l’assistant virtuel ?
- Assistant Lemadio est-il un chatbot ?
- Est-ce que Assistant Lemadio est lié à Lemadio ?

---

### ⚙️ Que suis-je capable de faire ?

Voici ce que je peux faire :

- Fournir des **explications claires et contextualisées** sur les fonctionnalités de Lemadio.
- Proposer des **étapes détaillées** pour accomplir une action dans l’application.
- Aider à résoudre les **problèmes courants** rencontrés par les vendeurs.
- Répondre aux **questions fréquentes** sur :
  - L’authentification
  - La gestion des ventes
  - La synchronisation des données
  - Les remplacements sous garantie
  - Les statistiques de performance

Je suis conçu pour rendre l’expérience utilisateur plus simple, plus rapide et plus autonome.

## 📱 À propos de l'application Lemadio

**Lemadio** est l’application mobile officielle utilisée par les vendeurs des points de vente **ADES**.  
Elle permet d’enregistrer les ventes, gérer les stocks, effectuer des remplacements sous garantie et consulter les statistiques de performance.

⚠️ À ne pas confondre avec **Assistant Lemadio**, qui est un chatbot conçu pour aider les vendeurs à bien utiliser l’application Lemadio.

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

## 🧭 Vue d’ensemble de l’interface après une connexion réussie

Après une authentification réussie, l’interface de l’application Lemadio se compose généralement de trois zones principales :

1. **L’en-tête** (en haut de l’écran)
2. **Le contenu principal** (au centre, selon la section active)
3. **La barre de navigation inférieure** (en bas de l’écran)

Par défaut, le vendeur est redirigé vers la page principale dédiée à la gestion des ventes. Cette interface regroupe les fonctionnalités essentielles pour :

- Suivre les ventes réalisées
- Gérer les stocks de réchauds
- Effectuer des remplacements sous garantie
- Visualiser les statistiques de performance

---

### 🧩 Composants de l’interface

#### 🔝 En-tête

L’en-tête est affiché en haut de l’écran et contient :

- **Logo ADES** : situé à gauche, il permet d’identifier visuellement l’application.
- **Zone utilisateur** : située à droite, elle comprend :
  - Une icône circulaire suivie du nom d’utilisateur du vendeur.
  - Une icône à trois points verticaux ouvrant un menu contextuel avec les options suivantes :
    - **Mode** : bascule entre le mode clair et le mode sombre.
    - **Synchroniser** : envoie les données locales non encore transmises au serveur ADES.
    - **Catalogue de prix** : affiche les tarifs des différents types de réchauds et poêles.
    - **Changer le mot de passe** : permet de modifier le mot de passe utilisateur.
    - **Déconnexion** : permet de quitter l’application.

---

#### 📄 Contenu principal

Le contenu affiché varie selon la section sélectionnée via la barre de navigation inférieure.

##### 🛒 1. Page des ventes

Cette page affiche l’historique des ventes enregistrées par le vendeur.  
Si aucune vente n’a encore été effectuée, le message suivant s’affiche :  
**« Aucune vente trouvée. »**

**Éléments de la page :**

- **Barre de recherche** : située en haut à gauche, elle permet de rechercher une vente par type de réchaud, nom du client, numéro de facture ou contact.
- **Icône de filtrage** : située à droite de la barre, elle permet de filtrer les ventes synchronisées ou non avec le serveur ADES.
- **Liste des ventes** : chaque vente est présentée sous forme de carte.

**Détails d’une carte de vente :**

- **Statut de synchronisation** :
  - _Synchronisé_ (texte vert, bordure arrondie) : la vente a été envoyée au serveur ou à Salesforce.
  - _Non synchronisé_ (texte orange) : la vente est encore stockée localement.
- **Bouton "Annuler"** : situé en haut à droite de la carte, avec une bordure rouge, il permet d’annuler la vente localement et à distance.
- **Informations affichées** : nom complet du client, numéro de facture, date de vente, numéro du réchaud.
- **Icône flèche vers le bas** : permet de déployer la carte pour afficher des détails supplémentaires (contact, adresse, région, fokontany).

---

##### 📦 2. Page des stocks

Cette page permet de consulter et gérer les réchauds disponibles au point de vente.

**Fonctionnalités principales :**

- **Barre de recherche** : située en haut, elle permet de rechercher un réchaud par type, numéro ou combinaison des deux.  
  _Exemples_ : `OLI-c T123456`, `OLI-60b 258963`.

- **Menu de navigation** : situé sous la barre de recherche, il contient deux onglets :

  1. **Stocks actuels**

     - Onglet affiché par défaut.
     - Affiche tous les réchauds disponibles pour le vendeur.
     - Réchauds encadrés en :
       - **Vert** : disponibles pour une nouvelle vente.
       - **Rouge** avec badge _vendu_ : déjà associés à une vente.

  2. **Numéros de facture**
     - Permet de visualiser les numéros de facture liés au vendeur.
     - Numéros encadrés en :
       - **Vert** : disponibles pour une nouvelle vente.
       - **Rouge** avec badge _vendu_ : déjà utilisés.

---

##### 🔄 3. Page des remplacements sous garantie

Cette section permet de gérer les remplacements de réchauds couverts par la garantie, en lien avec les ventes précédemment enregistrées.

---

##### 📊 4. Page des statistiques de vente

Affiche des graphiques et indicateurs de performance commerciale, permettant au vendeur de suivre ses résultats.

---

#### 📱 Barre de navigation inférieure

Cette barre permet de naviguer entre les différentes sections de l’application :

1. **Ventes** : icône avec badge indiquant le nombre de ventes non synchronisées.
2. **Stocks** : accès à la gestion des réchauds disponibles.
3. **Remplacements sous garantie** : suivi des réchauds remplacés.
4. **Statistiques de vente** : visualisation des performances commerciales.

---

## 🛒 Création d’une vente

### 📍 Accès à la page de vente

Pour créer une vente, le vendeur doit se trouver sur la **page des ventes**, qui s’ouvre automatiquement après une connexion réussie.

---

### 🧭 Étapes pour initier une vente

1. Cliquez sur le **bouton rond vert** avec une icône « + », situé en haut à droite de la barre de navigation inférieure.
2. Deux options s’affichent :
   - **Vente revendeur** : vente destinée aux revendeurs ADES.
   - **Vente directe** : vente directe aux clients finaux.

---

## 🔄 Processus de vente directe

En sélectionnant **Vente directe**, le vendeur est redirigé vers la **page d’information client**, où il doit renseigner les données du client.

---

### 🧑‍💼 Page d’information client

#### Champs à compléter :

1. **Sélectionner une catégorie** : liste déroulante pour choisir le type de client.  
   Options disponibles :

   - Private (client individuel)
   - Hotel
   - Ecole
   - NGO
   - Restaurant
   - Hopital
   - Microbusiness
   - Prison

2. **Sélectionner un cluster** : liste déroulante pour définir le type de réchaud.  
   Options :

   - Charcoal
   - Wood
   - Solar + OLI-b
   - Solar + OLI-c

3. **Mme/Mr** : nom du client
4. **Surnom** : prénom du client
5. **Contact** : numéro de téléphone
6. **Adresse** : adresse complète

7. **Localisation** :
   - Cliquez sur l’icône de localisation à droite du formulaire.
   - Une carte OpenStreetMap s’ouvre pour définir la position du client.

#### 🗺️ Fonctionnement de la carte :

- La carte récupère automatiquement la position actuelle de l’appareil.
- Une barre de recherche permet de trouver un lieu par fokontany, région, district ou commune.
- Cliquez sur l’endroit exact pour placer un marqueur rouge.
- Validez avec le bouton bleu en bas.
- Les champs de localisation sont remplis automatiquement.

⚠️ **Note** : Vérifiez les champs auto-remplis. Si certains sont marqués « Non spécifié », remplissez-les manuellement.

8. **CIN recto** : facultatif, capture de la face avant du CIN
9. **CIN verso** : facultatif, capture de la face arrière du CIN

10. Cliquez sur **Valider** pour passer à la page suivante.

⚠️ **Note** : Les champs obligatoires doivent être correctement remplis pour poursuivre.

---

### 🧾 Page de sélection du numéro de facture

- Barre de recherche en haut pour filtrer les numéros disponibles.
- Liste des numéros de facture affichée en dessous.
- Le nombre total est indiqué en haut : `Résultats (XX)`.
- Le vendeur peut sélectionner **un seul numéro** par vente.
- Une fois sélectionné, le bouton **Valider** apparaît pour passer à la vérification.

---

### ✅ Page de vérification des informations client

Cette page permet de confirmer les données saisies avec le client.

#### En-tête :

- **Numéro de facture** : en haut à gauche
- **Date de vente** : en haut à droite

#### Informations à vérifier :

- Mme/Mr : nom
- Surnom : prénom
- Numéro : téléphone
- Adresse : adresse complète
- Région, District, Commune, Fokontany

⚠️ **Note** : Si tout est correct, cliquez sur **Valider** pour passer au scan du réchaud.  
En cas d’erreur, utilisez le bouton retour ou l’icône « ← » pour corriger les données.

---

### 🔍 Page de scan du réchaud

- Cliquez sur le **bouton rond vert** dans le cadre jaune pour lancer le scanner.
- Scannez le **code-barres** du réchaud.
- Le système vérifie si le numéro scanné existe dans le stock du vendeur.
  - Si oui : le type + numéro s’affiche.
  - Si non : un message d’erreur clair est affiché.

#### Tableau récapitulatif :

- Type de réchaud
- Prix unitaire
- Quantité
- Total

Le vendeur peut scanner plusieurs réchauds, même de types différents.

⚠️ **Note** : Le prix dépend de la zone géographique du client.  
Zones disponibles :

- Zone forte
- Zone moyenne
- Zone LNOB

---

### 🛡️ Page des conditions de garantie

Conditions affichées :

- Garantie d’un an sur le bon fonctionnement.
- Exclusion des dommages dus à une mauvaise utilisation.
- Garantie limitée à l’argile.
- Grilles supplémentaires disponibles gratuitement sur présentation du reçu.
- Les certificats CO₂ restent la propriété d’ADES.

#### Signature du client :

- Cochez la case « J’accepte de céder le droit de ce dossier ».
- Un cadre de signature s’affiche en bas.
- Le client signe dans le **signature pad**.
- Une icône poubelle permet d’effacer et recommencer.

Cliquez sur **Enregistrer** pour finaliser la vente.

---

### 🌐 Synchronisation des données

⚠️ **Important** : Une connexion Internet est requise pour envoyer la vente vers Salesforce.

- En cas d’absence de connexion, les données sont enregistrées localement.
- Synchronisez dès que possible pour éviter toute perte.

#### Pour synchroniser :

1. Accédez à la page des ventes.
2. Vérifiez le statut des cartes :
   - **Non synchronisé** (orange) = données locales.
3. Cliquez sur les **trois points verticaux** dans l’en-tête.
4. Sélectionnez **Synchroniser** pour envoyer les données.

### Comment savoir si une vente est synchronisée ?

- **Synchronisé** : Badge vert avec le texte "Synchronisé"
- **Non synchronisé** : Badge orange avec le texte "Non synchronisé"
- Le badge sur l'icône "Ventes" dans la barre de navigation indique le nombre de ventes non synchronisées





## Processus pour vente revendeur

C'est la vente dedié au revendeur d'ADES. C'est à dire, des boutiques ou autre qui revende les réchauds avec des prix différente. Ils font un approvisionnement chez le point de vente ADES puis revendre les réchauds. L'application Lemadio peut gerer aussi la vente revendeur en chosisant l'option "vente revendeur".

### Étape 3 : Sélectionner le numéro de facture

Cette page affiche la liste des numéros de facture liés au centre de vente. Il suffit de sélectionner un numéro puis cliquer le bouton valider.

### Étape 4 : Page de vérification d'information client

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
| "Vente non enregistrée"       | Erreur serveur                | Vérifiez la connexion ou contactez le support    |
| "Réchaud déjà vendu"          | Réchaud scanné déjà vendu     | Vérifiez le numéro du réchaud                    |
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
- Contactez le support si le problème persiste

---

## 10. FAQ (Foires Aux Questions)

**Q : Peut-on modifier une vente après l'avoir enregistrée ?**
R : Non, pas directement dans l'application. Contactez le responsable du point de vente pour toute modification.

**Q : Quel est le délai de confirmation d'une vente ?**
R : La vente est enregistrée instantanément sur Salesforce si vous avez une connexion internet. Sinon, le vendeur le synchronisé manuelement plus tard.

**Q : Puis-je vendre un réchaud sans connexion internet ?**
R : Oui, la vente sera enregistrée localement et synchronisée manuelement par le venteur dès que la connexion internet sera disponible.

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
