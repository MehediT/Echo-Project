# Application Flask de Reconnaissance de Couleur

Cette application Flask utilise une interface web simple avec un bouton Marche/Arrêt pour lancer la reconnaissance vocale. Elle peut reconnaître les couleurs : bleu, rouge, vert, et jaune.

## Prérequis

Assurez-vous d'avoir **Python 3.6+** installé sur votre machine.

## Installation

1. Clonez le dépôt ou téléchargez les fichiers du projet :

   ```bash
   git clone https://github.com/votre-repo/app-flask-couleur.git
   cd app-flask-couleur
   ```

2. Créez un environnement virtuel et activez-le :

   - Sur **Windows** :
     ```bash
     python -m venv env
     env\Scripts\activate
     ```
   - Sur **macOS/Linux** :
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

3. Installez les dépendances requises :

   ```bash
   pip install -r requirements.txt
   ```

4. Installez **PortAudio** (nécessaire pour la bibliothèque `SpeechRecognition`) :

   - **macOS** :
     ```bash
     brew install portaudio
     ```
   - **Linux** :
     ```bash
     sudo apt-get install portaudio19-dev
     ```
   - **Windows** :
     Téléchargez et installez [PortAudio](http://www.portaudio.com/download.html) pour votre système.

5. Assurez-vous que `SpeechRecognition` peut accéder au microphone.

## Exécution de l'application

1. Lancez l'application Flask :

   ```bash
   flask run
   ```

2. Ouvrez votre navigateur et accédez à `http://127.0.0.1:5000` pour utiliser l'application.

## Utilisation

- Cliquez sur le bouton **Marche** pour lancer la reconnaissance vocale.
- Dites une couleur parmi **bleu, rouge, vert, jaune**.
- Le résultat s'affichera sur la page.

## Dépendances

- Flask
- Flask-SocketIO
- SpeechRecognition
- PortAudio (pour l'accès au microphone)

```

```
