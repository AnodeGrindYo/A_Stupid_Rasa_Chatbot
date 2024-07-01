# Définir le nom de l'environnement virtuel
$envName = "env"

# nom d'utilisateur windows
$userName = "Administrateur"

# Chemin vers l'exécutable Python 3.9
$python39Path = "C:\Users\$userName\AppData\Local\Programs\Python\Python39\python.exe"

# Créer l'environnement virtuel avec Python 3.9
& $python39Path -m venv $envName

# Activer l'environnement virtuel
$activateScript = ".\" + $envName + "\Scripts\Activate.ps1"
. $activateScript

# Mettre à jour pip
python -m pip install --upgrade pip

# Installer les packages nécessaires pour Jupyter et la data science
pip install numpy pandas scikit-learn spacy nltk rasa

# création d'un fichier requirements.txt
pip freeze > requirements.txt

# Afficher un message de confirmation
Write-Host "L'environnement virtuel a été créé et les paquets nécessaires ont été installés."

