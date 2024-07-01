$env:VIRTUAL_ENV = ".\env" 
$env:PATH = "$env:VIRTUAL_ENV\Scripts;$env:PATH"

# Se déplace dans le dossier .\chatbot
cd .\chatbot

# Démarrer le serveur d'actions personnalisées dans une nouvelle fenêtre PowerShell
Start-Process powershell -ArgumentList "rasa run actions"

# Pause pour s'assurer que le serveur d'actions est démarré
Start-Sleep -Seconds 30

# Démarre le Rasa shell dans une nouvelle fenêtre PowerShell
Start-Process powershell -ArgumentList "rasa shell --endpoints endpoints.yml"

## si ça ne fonctionne pas, ouvir deux fenêtres PowerShell et exécuter les commandes suivantes (attendre que la première commande soit terminée avant d'exécuter la deuxième):
# rasa run actions
# rasa shell --endpoints endpoints.yml
