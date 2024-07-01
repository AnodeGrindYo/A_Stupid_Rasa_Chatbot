# JokeBot README.md 🤖

## Bienvenue dans l'univers de JokeBot !

Si vous avez toujours rêvé de parler à un chatbot qui raconte des blagues (pas toujours drôles), donne des informations sur l'année scolaire à EPSI et peut même tenter de faire des backflips numériques, alors vous êtes au bon endroit. JokeBot est là pour vous faire rire... ou du moins essayer. 🙃

### Installation et configuration

1. **Cloner le repo**
    ```bash
    git clone https://github.com/votre-username/jokebot.git
    cd jokebot
    ```

2. **Installer les dépendances**
    ```bash
    pip install rasa
    pip install rasa-sdk
    pip install requests
    pip install pyautogui
    ```

3. **Configurer les fichiers**
    - **endpoints.yml** : Assurez-vous que l'URL pointe vers votre serveur d'actions.
    - **domain.yml** et **stories.yml** : Ces fichiers sont déjà configurés pour répondre à vos besoins les plus farfelus.

### Démarrage du bot

1. **Entraîner le modèle**
    ```bash
    rasa train
    ```

2. **Lancer le serveur d'actions**
    ```bash
    rasa run actions
    ```

3. **Lancer le bot**
    ```bash
    rasa shell
    ```

### Fonctionnalités de JokeBot

- **Salutations et adieux** : Parce que commencer et terminer une conversation en beauté, c'est important.
    - "Salut", "Bonjour", "Au revoir", "À plus tard"

- **Blagues diverses** : Une collection de blagues pour tous les goûts, ou presque.
    - "Raconte-moi une blague"
    - "Dis-moi une blague sur les belges"

- **Informations scolaires** : Tout ce que vous devez savoir sur l'année scolaire à EPSI.
    - "Quelles sont les dates importantes pour l'année scolaire à EPSI ?"

- **Backflips numériques** : Vous voulez voir un bot faire des backflips ? Nous aussi, mais tout ce qu'on a c'est cette tentative ridicule.
    - "Fais un backflip"

### Notes de fin

- **Humour non garanti** : Les blagues de JokeBot sont certifiées pour ne pas faire rire tout le monde.
- **Compatibilité** : Le bot essaie de faire des backflips sur Windows et macOS, mais sans promesse de succès.
- **Support limité** : Si quelque chose ne fonctionne pas, c'est probablement parce que ce bot est supposé être une récréation.

Profitez bien de ce chef-d'œuvre de comédie et amusez-vous avec JokeBot ! 🤡

---

Fait avec ❤️ et beaucou de 😜
