class Buch():
    def __init__(self, seiten, seite_aktuell, titel):
        self.seiten = seiten
        self.seite_aktuell = seite_aktuell
        self.titel = titel
        self.im_regal = True

    def __str__(self, arg):
        print(arg)

    def blaettern(self, arg):
        if self.im_regal == True:
            self.__str__('Buch aus dem Regal nehmen!')
        else:
            if self.seite_aktuell + arg < 0:
                self.seiten = 0 
            elif self.seite_aktuell + arg > self.seiten:
                self.seite_aktuell = self.seiten
            else:
                self.seite_aktuell += arg
            self.__str__(f'jetzt auf Seite: {self.seite_aktuell}')

    def entnehmen(self, arg):
        self.im_regal = arg

    def titel_aendern(self, arg):
        self.titel = arg
        self.__str__(f'Titel ist jetzt: {self.titel}')

    def seiten_aendern(self, arg):
        self.seiten = arg
        if arg < self.seite_aktuell:
            self.seite_aktuell = 0
        self.__str__(f'Seitenzahl beträgt jetzt: {self.seiten}')
            
    def ausgabe(self):
        self.__str__(f'\n--aktuelle Eigenschaften des Buches--\n \nSeitenzahl: {self.seiten} \
                     \naktuelle Seite: {self.seite_aktuell}\nTitel: {self.titel}')

buch = Buch(500, 0, '')

buch.blaettern(37) 
buch.titel_aendern('Ein Roman')
buch.seiten_aendern(490)
buch.entnehmen(False)
buch.ausgabe()
buch.blaettern(230)
buch.entnehmen(True)
buch.blaettern(20)
buch.entnehmen(False)
buch.blaettern(20)