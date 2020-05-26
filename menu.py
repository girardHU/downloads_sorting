import inquirer
ye = ['Y', 'y', 'YES', 'yes', 'O', 'o', 'OUI', 'oui', 'oue stp']
class Menu:
    """
    Menu class that holds everything related to the configuration

    Attributes
    ----------
    audioFormats : list
        list of audio extensions to support, empty if none, 'all' if all should be supported
    videoFormats : list
        list of video extensions to support, empty if none, 'all' if all should be supported
    lessons : bool
        determine wether the program should enable the lessons section

    Methods
    -------
    display_menu()
        Main function that displays the menu and call each functions according to user's input

    select_audio_format()
        Displays audio formats selection list

    select_video_format()
        Displays video formats selection list
    """
    monitoredFolder: str
    audioFormats :list
    videoFormats :list
    lessons :bool
    lessonsConfig :dict

    def __init__(self):
        self.monitoredFolder = ''
        self.audioFormats = []
        self.videoFormats = []
        self.lessons = False
        self.lessonsConfig = {}

    def display_menu(self):
        """
        Main function that displays the menu and call each functions according to user's input
        """
        try:
            print('J\'ai besoin du chemin absolu du dossier a surveiller !')
            print('Ne te trompe pas, je ne fais pas de verification :o')
            self.monitoredFolder = input()
            
            print('Souhaites-tu que je range automatiquement tes nouvelles chansons ?')
            song = input('Y/n : ') in ye
            if song:
                self.select_audio_format()

            print('Souhaites-tu que je range automatiquement tes nouveaux films ?')
            movie = input('Y/n : ') in ye
            if movie:
                self.select_video_format()
            
            print('Souhaites-tu que je range automatiquement tes nouveaux fichiers de cours ?')
            lesson = input('Y/n : ') in ye
            
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
            self.audioFormats.extend(formats.get('formats'))
        else:
            self.audioFormats = ['all']

        print(self.audioFormats)

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
            self.videoFormats.extend(formats.get('formats'))
        else:
            self.videoFormats = ['all']
        print(self.videoFormats)

    def select_lessons_related(self):
        user_input = ''
        print('combien de matieres differentes as-tu ?')
        nb_discipline = int(input())
        for i in range(1, nb_discipline + 1):
            print(f'J\'ai besoin du chemin absolu vers le dossier de la matiere {i} :')
            path = input()
            print('quelle norme de nommage dois-je utiliser pour cette matiere ?')
            pattern = input()
            self.lessonsConfig.update({path: pattern})
        print(self.lessonsConfig)

menu = Menu()
menu.select_lessons_related()