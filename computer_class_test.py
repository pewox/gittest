class Computer:

    def __init__(self, cpu_core, ram, hdd, bs, sw):
        self.cpu_core = cpu_core
        self.ram = ram
        self.hdd = hdd
        self.bs = bs
        self.sw = sw
        self.computer_ein = True

    def __str__(self, arg):
        print(arg)

    def computer_starten(self):
        if self.computer_ein == False:
            if self.cpu_core == 0:
                self.__str__("Keine CPU vorhanden, kein Start möglich!")
            elif self.ram == 0:
                self.__str__("Kein RAM vorhanden, kein Start möglich!")
            elif self.hdd == 0:
                self.__str__("Keine HDD vorhanden, kein Start möglich!")
            else:
                self.computer_ein = True
                self.__str__("Computer ist gestartet")
    
    def computer_herunterfahren(self):
        if self.computer_ein == True:
            self.computer_ein = False
        self.__str__("Computer wurde heruntergefahren")
    
    def cpu_kerne_aendern(self, kerne):
        if self.computer_ein == True:
            self.__str__("Computer läuft noch!")
        elif self.cpu_core + kerne < 0:
                self.cpu_core = 0
                self.__str__("CPU entfernt")
        else: 
            self.cpu_core += kerne
            self.__str__(f"CPU hat jetzt {self.cpu_core} Kerne")
        
    def ram_aendern(self, ram_zusatz):
        if self.computer_ein == True:
            self.__str__("Computer läuft noch!")
        elif self.ram + ram_zusatz < 0:
            self.ram = 0
            self.__str__("RAM entfernt")
        else:
            self.ram += ram_zusatz
            self.__str__(f"Ram hat jetzt {self.ram} GB RAM")
    
    def hdd_aendern(self,hdd_zusatz):
        if self.computer_ein == True:
            self.__str__("Computer läuft noch!")
        elif self.hdd + hdd_zusatz < 0:
            self.hdd = 0
            self.__str__("HDD entfernt")
        else:
            self.hdd += hdd_zusatz
            self.__str__(f"Ram hat jetzt {self.hdd} GB HDD")
    
    def bs_aendern(self, bs_wechsel):
        if self.computer_ein == False:
            self.__str__("Computer einschalten!")
        else:
            self.bs = bs_wechsel
            self.__str__(f"Betriebssystem ist jetzt {self.bs}")

    def sw_aendern(self, sw_wechsel):
        if self.computer_ein == False:
            self.__str__("Computer einschalten!")
        else:
            self.sw = sw_wechsel
            self.__str__(f"Software ist jetzt {self.sw}")

    def ausgabe(self):
        self.__str__(f"--Computerzustand aktuell--\nCPU-Kerne: {self.cpu_core} \
                     \nRAM: {self.ram} GB\nHDD: {self.hdd} \
                     \nBetriebssystem: {self.bs}\nSoftware: {self.sw} \
                     \nComputer läuft: {self.computer_ein}"
                     )

class Server(Computer):
    pass
computer_neu = Computer(2, 64, 500, "Windows", "Win-Office")
computer_neu.computer_herunterfahren()
computer_neu.hdd_aendern(600)
computer_neu.ram_aendern(23)
computer_neu.cpu_kerne_aendern(2)
computer_neu.computer_starten()
computer_neu.sw_aendern("Libre-Office")
computer_neu.bs_aendern("Debian")
computer_neu.computer_herunterfahren()
computer_neu.ram_aendern(-90)
computer_neu.ausgabe()
computer_neu.computer_starten()
