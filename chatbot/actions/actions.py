import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import logging
import pyautogui
import os

logger = logging.getLogger(__name__)

class ActionTellThemedJoke(Action):

    def name(self) -> str:
        return "action_tell_themed_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        theme = tracker.get_slot("joke_theme")
        if not theme:
            theme = "blagues"

        url = f"https://api.blablagues.net/?rub=blagues&cat={theme}"
        response = requests.get(url)
        logger.info(f"Request to {url} returned {response.json() if response.status_code == 200 else response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            joke_head = data.get('data', {}).get('content', {}).get('text_head', "")
            joke_text = data.get('data', {}).get('content', {}).get('text', "")
            joke_hidden = data.get('data', {}).get('content', {}).get('text_hidden', "")
            if joke_text:
                joke = joke_text
            else:
                joke = f"{joke_head} {joke_hidden}"
        else:
            joke = "Je n'ai pas réussi à récupérer une blague pour le moment, réessaie plus tard."

        dispatcher.utter_message(text=joke)
        return []
    
class ActionTellJoke(Action):

    def name(self) -> str:
        return "action_tell_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        jokes = [
            "Quel poisson n'a pas de certificat de naissance ? Le poisson pané.",
            "Quel est le médecin qui nous fait tous craquer ? L’ostéo.",
            "Quel est le super héros qui a tout le temps peur ? Le super-sticieux.",
            "Pourquoi est-ce que les chercheurs ont-ils des trous de mémoire ? Parce qu’ils se creusent la tête.",
            "Comment les musiciens choisissent-ils leur parquet ? Ils choisissent un parquet facile à cirer. (Fa Si La Si Ré)",
            "Quel est le musicien préféré des maladies ? Bach-terie.",
            "Quel est le réseau préféré des pêcheurs ? Truiteur.",
            "Que fait un geek quand il a peur ? Il URL.",
            "Quel est le carburant le plus détendu ? Le kérozen.",
            "Quel est le fast food préféré de Flash ? Quick.",
            "Qu'est-ce qui est vert et qui se déplace sous l'eau ? Un chou marin.",
            "Quel est le pays le plus cool du monde ? Le Yééémen.",
            "Que fait une vache quand elle ferme les yeux ? Du lait concentré.",
            "Quel est le super héros qui donne l'heure le plus vite ? Spiderman. (Speed heure man)",
            "Pourquoi est-ce que les anges sont sourds ? Parce que Jésus crie. (Jésus Christ)",
            "Quel est le fruit préféré des profs d'histoire ? Les dattes.",
            "Quelle est la déesse de l'internet ? L’ADSL. (La déesse L)",
            "Qu'est-ce qui est pire que le vent ? Un vampire.",
            "Quelle est l'arme préférée des vegan ? Le lance roquette.",
            "Quelle est la femme du hamster ? L’Amsterdam.",
            "Dans quel pays ne bronze-t-on pas du nez ? Au Népal.",
            "Que fait une théière devant un ascenseur ? Elle veut mon thé.",
            "Pourquoi est-ce que Winnie l'Ourson veut absolument se marier ? Pour partir en lune de miel.",
            "Que dit une mère à son fils geek quand le dîner est servi ? Alt Tab !",
            "Quelle est la meilleure heure pour écouter de la musique ? Deezer !",
            "Que fait un geek quand il descend du métro ? Il libère la RAM.",
            "Quel est l'animal le plus connecté ? Le porc USB.",
            "Où vont les biscottes pour danser ? En biscothèque.",
            "Quel est le style musical préféré des médecins ? Le blouse.",
            "Comment appelle-t-on un chat qui va dans l'espace ? Un chatellite.",
            "Que fait un jardinier quand il ment ? Il raconte des salades.",
            "Où est-ce que l'homme invisible part en vacances ? Chez ses transparents.",
            "Pourquoi est-ce que Napoléon n'a pas voulu acheter de maison ? Parce qu’il avait déjà un Bonaparte.",
            "Que dit Frodon devant sa maison ? C’est là que j’hobbit.",
            "Quels sont les fruits qu'on trouve dans toutes les maisons ? Des coings et des mûres.",
            "Pourquoi un chasseur emmène-t-il son fusil aux toilettes ? Pour tirer la chasse.",
            "Quel est le crustacé le plus léger de la mer ? La palourde.",
            "Que dit un informaticien quand il s'ennuie ? Je me fichier.",
            "Avec quelle monnaie les marins payent-ils ? Avec des sous marins.",
            "Que dit un italien pour dire au revoir ? Pasta la vista.",
            "Où va Messi quand il se blesse ? À la pharmessi.",
            "Que demande un footballeur à son coiffeur ? La coupe du monde s’il vous plaît.",
            "Que dit un rappeur lorsqu'il rentre dans une fromagerie ? Faites du briiiie !",
            "Que dit une lampe lorsqu'elle a un problème ? Elle crie « à LED ! »",
            "Quelle est la viande préférée des Russes ? Le steak tsar tsar.",
            "Quel est le poisson le moins cher ? Le requin marteau : il ne vaut pas un clou.",
            "Qu'est-ce qu'un hamster dans l'espace ? Un hamstéroïde.",
            "Comment appelle-t-on deux canards qui se disputent ? Un conflit de canards.",
            "Pourquoi est-ce que les moutons aiment le chewing-gum ? Parce que c’est bon pour l’haleine. (la laine)",
            "Pourquoi les cordonniers sont-ils curieux ? Parce qu’ils se mêlent de tout. (semelle)",
            "Que dit le citron quand il braque une banque ? « Pas un zeste, ze suis pressé ! »",
            "Comment appelle-t-on une manifestation d'aveugles ? Un festival de cannes.",
            "Que risque-t-on à lancer de l'ail sur un mur ? Le retour du jet d’ail.",
            "Quelle est la fée la plus paresseuse ? La fée Néante.",
            "Que dit une noisette qui tombe à l'eau ? « Au secours, je me noix ! »",
            "Tu connais l'histoire de l'armoire ? Elle est pas commode.",
            "Tu connais l'histoire de la feuille de papier ? Elle déchire !",
            "Comment appelle-t-on un chat tout-terrain ? Un cat cat.",
            "Quelle est l'info la plus tirée par les cheveux ? Il n’y a pas de chauve à Bastia, mais à Calvi si.",
            "Que disaient les apôtres à Jésus quand il racontait une blague de ce top ? « C’est naze, arrête. »",
            "Quel genre de melon donne du lait ? Le mamelon.",
            "Comment savoir quand un sapin est en colère ? Il a les boules.",
            "Que dit un sommelier quand il est en retard ? Désolé, y’avait des bouchons.",
            "Qu'est-ce qui fait « poin-poin » ? Un panard.",
            "Que fait un hippie quand il veut uriner ? Il peace.",
            "Quel crustacé est le plus léger de la mer ? La palourde.",
            "C'est un aveugle qui rentre dans un bar. Le poisson, cette fois-ci.",
            "De quelle couleur est la voiture de John Travolta ? Grease.",
            "Que font les brosses à dents le 14 juillet ? Un feu dentifrice.",
            "Qu'est-ce qui vole et qui brille ? Une mouche avec une dent en or.",
            "Pourquoi les Bretons sont-ils tous frères et soeurs ? Parce qu’ils n’ont Quimper.",
            "Comment appelle-t-on un ascenseur en Argentine ? En appuyant sur le bouton.",
            "Comment appelle-t-on les testicules des dauphins ? Les boules de Flipper.",
            "Comment reconnait-on un politicien qui ment ? Ses lèvres bougent.",
            "Un homme et son chien sont sur un bateau. Le chien lâche une caisse, l'homme tombe à l'eau et se noie. Quelle est la race de son chien ? Un pékinois.",
            "À la maternité un nouveau père tout content demande à l'infirmière : « Vous trouvez que mon fils me ressemble ? » « Oui, mais c’est pas grave, l’essentiel c’est qu’il soit en bonne santé ! »",
            "Un homme inquiet s'adresse à un autre : « Docteur, je pense que j’ai besoin de porter des lunettes. » « Oui probablement vu que vous êtes dans une banque. »",
            "Comment appelle-t-on un nain qui est facteur ? Un nain posteur.",
            "Comment appelle-t-on Peter Dinklage ? Un nain connu.",
            "Un homme qui est en train de se noyer dans un lac appelle un autre qui passe : « HELP HELP !! » « T’aurais mieux fait d’apprendre à nager au lieu d’apprendre l’anglais ducon ! »",
            "Qu'est-ce qu'un lavab ? Un lavabo sans o.",
            "Un patient s'adresse à son médecin : « J’ai très mal à l’œil gauche quand je bois mon café le matin. » « Vous avez essayé d’enlever la cuillère de la tasse ? »",
            "Pourquoi peint-on un chat à Noël ? Pour faire un chapeint de Noël.",
            "Une mère discute avec un voisin : « Alors, ça fait combien de temps qu’il marche votre enfant ? » « Ça va bientôt faire un an. » « Eh ben il doit être loin du coup. »",
            "Quelle est la meilleure chose de la Suisse ? Aucune idée, mais le drapeau est un gros plus.",
            "De quoi a besoin un astronaute claustrophobe ? D’un peu d’espace.",
            "Un grand-père discute avec son petit-fils : « Papy, c’est quoi une déclaration d’impôts ? » « C’est le contraire du bulletin scolaire, quand t’as bien travaillé, t’es puni ! »",
            "Que dit-on à l'enterrement d'un comptable ? Qu’il comptait beaucoup pour les gens."
        ]
        
        joke = random.choice(jokes)
        dispatcher.utter_message(text=joke)
        
        return []

class ActionBackflip(Action):
    def name(self) -> str:
        return "action_backflip"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        os_name = os.name
        
        if os_name == 'nt':
            self.rotate_screen_windows()
        elif os_name == 'posix':  # macOS (and Linux in general)
            self.rotate_screen_mac()
        else:
            dispatcher.utter_message(text="Cette action n'est pas supportée sur votre système d'exploitation.")
            return []

        dispatcher.utter_message(text="Et hop !")
        return []

    def rotate_screen_windows(self):
        # Simuler les touches pour Windows
        pyautogui.hotkey('ctrl', 'alt', 'down')
        pyautogui.hotkey('ctrl', 'alt', 'right')
        pyautogui.hotkey('ctrl', 'alt', 'up')
        pyautogui.hotkey('ctrl', 'alt', 'left')

    def rotate_screen_mac(self):
        # Simuler les touches pour macOS
        # Attention : les autorisations d'accessibilité doivent être activées pour pyautogui, enfin je ne sais pas : je ne suis pas assez riche pour tester
        pyautogui.hotkey('command', 'option')
        pyautogui.click(50, 10)  # Clique sur l'icône Apple dans le coin supérieur gauche
        pyautogui.typewrite('Displays')
        pyautogui.press('enter')
        pyautogui.press('tab', presses=6, interval=0.1)  # Navigue dans les menus
        pyautogui.press('down')  # Sélectionne la rotation
        pyautogui.press('enter')
        pyautogui.press('down')  # Sélectionner 90˚
        pyautogui.press('enter')