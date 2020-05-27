import inquirer
import json
ye = ['Y', 'y', 'YES', 'yes', 'O', 'o', 'OUI', 'oui', 'oue stp']
class Menu:
    """
    Menu class that holds everything related to the configuration

    Attributes
    ----------
    monitored_folder : str
        absolute path to the monitored folder
    audio_formats : list
        list of audio extensions to support, empty if none, 'all' if all should be supported
    audio_path : str
        path where the audio files will go
    video_path : str
        path where the video files will go
    video_formats : list
        list of video extensions to support, empty if none, 'all' if all should be supported
    lessons : bool
        determine wether the program should enable the lessons section
    lessons_config : dict
        dictionary containing all the conf for the lessons management part

    Methods
    -------
    display_menu()
        Main function that displays the menu and call each functions according to user's input

    select_audio_format()
        Displays audio formats selection list

    select_video_format()
        Displays video formats selection list

    select_lessons_related()
        Sub-menu to configure the lessons part of the program
    """
    monitored_folder :str
    audio_formats :list
    audio_path: str
    video_formats :list
    video_path: str
    lessons :bool
    lessons_config :dict


    def __init__(self):
        self.monitored_folder = ''
        self.audio_formats = []
        self.audio_path = ''
        self.video_formats = []
        self.video_path = ''
        self.lessons = False
        self.lessons_config = {}


    def display_menu(self):
        """
        Main function that displays the menu and call each functions according to user's input
        """
        try:
            print('J\'ai besoin du chemin absolu du dossier a surveiller !')
            print('Ne te trompe pas, je ne fais pas de verification :o')
            # TODO : verification du/des path(s)
            self.monitored_folder = input()
            
            print('Souhaites-tu que je range automatiquement tes nouvelles chansons ?')
            if input('Y/n : ') in ye:
                self.select_audio_format()

            print('Souhaites-tu que je range automatiquement tes nouveaux films ?')
            if input('Y/n : ') in ye:
                self.select_video_format()
            
            print('Souhaites-tu que je range automatiquement tes nouveaux fichiers de cours ?')
            if input('Y/n : ') in ye:
                self.select_lessons_related()

            print('Dois-je enregistrer ces parametres ?')
            if input('Y/n : ') in ye:
                self.write_config()
            
        except KeyboardInterrupt:
            pass


    def select_audio_format(self):
        """
        Displays audio formats selection list
        """
        question1 = [
            inquirer.List(
                'auto',
                message='Dois-je m\'occuper de tous les formats audios ou veux-tu choisir toi-meme ?',
                choices=['Tous', 'Choisir']
            )
        ]
        question2 = [
            inquirer.Checkbox(
                'formats',
                message='De quels formats dois-je m\'occuper ?',
                choices=['mp3', 'wav', 'flac', '.m4a', 'wma', 'aac']
            )
        ]

        auto = inquirer.prompt(question1)

        if 'Choisir' in auto.get('auto'):
            formats = inquirer.prompt(question2)
            self.audio_formats.extend(formats.get('formats'))

        else:
            self.audio_formats = ['all']

        print('Ou dois-je ranger les fichiers audios ?')
        self.audio_path = input()


    def select_video_format(self):
        """
        Displays video formats selection list
        """

        question1 = [
            inquirer.List(
                'auto',
                message='Dois-je m\'occuper de tous les formats videos ou veux-tu choisir toi-meme ?',
                choices=['Tous', 'Choisir']
            )
        ]
        question2 = [
            inquirer.Checkbox(
                'formats',
                message='De quels formats dois-je m\'occuper ?',
                choices=['mp4', 'avi', 'mkv', 'mov', 'wmv', 'mpg', 'm4v', 'flv', 'webm', 'gif', 'ogg']
            )
        ]

        auto = inquirer.prompt(question1)

        if 'Choisir' in auto.get('auto'):
            formats = inquirer.prompt(question2)
            self.video_formats.extend(formats.get('formats'))

        else:
            self.video_formats = ['all']
        
        print('Ou dois-je ranger les fichiers videos ?')
        self.video_path = input()


    def select_lessons_related(self):
        """
        Sub-menu to configure the lessons part of the program
        """

        print('combien de matieres differentes as-tu ?')
        nb_discipline = int(input())

        for i in range(1, nb_discipline + 1):
            
            print('quelle norme de nommage dois-je utiliser pour cette matiere ?')
            pattern = input()

            print(f'J\'ai besoin du chemin absolu vers le dossier de la matiere {i} :')
            path = input()

            self.lessons_config.update({pattern: path})


    def write_config(self):

        with open('formats.json') as format_json_file:
            formats = json.load(format_json_file)

        if not self.audio_formats:
            definitive_audio_format = []
        elif 'all' in self.audio_formats and len(self.audio_formats) == 1:
            definitive_audio_format = formats.get("audio_formats")
        else:
            definitive_audio_format = self.audio_formats

        if not self.video_formats:
            definitive_video_format = []
        elif 'all' in self.video_formats and len(self.video_formats) == 1:
            definitive_video_format = formats.get("video_formats")
        else:
            definitive_video_format = self.video_formats

        data = {
            "monitored_folder": self.monitored_folder,
            "audio_formats": definitive_audio_format,
            "audio_path": self.audio_path,
            "video_formats": definitive_video_format,
            "video_path": self.video_path,
            "lessons_pattern": self.lessons_config
        }

        print(data)
        with open('config.json', 'w') as configFile:
            json.dump(data, configFile, indent=2)



menu = Menu()
# menu.monitored_folder = '/input'
# menu.audio_formats = ['all']
# menu.audio_path = '/audios'
# menu.video_formats = ['.mp4', '.m4p']
# menu.video_path = '/videos'
# menu.lessons_config = {
#     'cours1': '/cours/1',
#     'cours2': '/cours/2',
#     'cours3': '/cours/3'
# }
menu.display_menu()