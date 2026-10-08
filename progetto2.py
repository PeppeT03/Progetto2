import numpy as np
from abc import ABC, abstractmethod
#Parte 1
 
Nome_Paziente_1 ="Mario"
Cognome_Paziente_1 = "Rossi"
Codice_Fiscale_Paziente_1="MRBRDFGESFE07"
Eta_Paziente_1= 40
Peso_Paziente_1= 72.5
Analisi_Effettuate_Paziente_1= ["Emocroma","Glicemia","Colesterolo"]

Nome_Paziente_2 = "Luca"
Cognome_Paziente_2 = "Bianchi"
Codice_Fiscale_Paziente_2 = "BNCLCU85M12F205Z"
Eta_Paziente_2 = 35
Peso_Paziente_2 = 68.2
Analisi_Effettuate_Paziente_2 = ["Glicemia", "Trigliceridi", "Creatinina"]

Nome_Paziente_3 = "Giulia"
Cognome_Paziente_3 = "Verdi"
Codice_Fiscale_Paziente_3 = "VRDGLI92T41H501W"
Eta_Paziente_3 = 28
Peso_Paziente_3 = 57.0
Analisi_Effettuate_Paziente_3 = ["Emocromo", "Ferritina", "Vitamina D"]

#Parte 2

class Paziente:
    def __init__(self,nome,cognome,codice_fiscale,eta,peso,analisi_effettuate):
        self.nome=nome
        self.cognome=cognome
        self.codice_fiscale=codice_fiscale
        self.eta=eta
        self.peso=peso
        self.analisi_effettuate=analisi_effettuate
        self.risultati_analisi = np.array([])
    def scheda_personale(self):
        print(f"Nome: {self.nome},\n Cognome: {self.cognome},\n  Eta: {self.eta},\n Peso: {self.peso},\n Analisi Effettuate: {self.analisi_effettuate}")
    def aggiungi_risultato(self,valore):
        self.risultati_analisi=np.append(self.risultati_analisi,valore)

    def statistiche_analisi(self):
        if len(self.risultati_analisi)==0:
            print("Non e stato aggiunto nessun risultato")
            return
        media= np.mean(self.risultati_analisi)
        minimo= np.min(self.risultati_analisi)
        massimo=np.max(self.risultati_analisi)
        deviazione_standard=np.std(self.risultati_analisi)
    
class Medico:
    def __init__(self,nome,cognome,specializzazione):
        self.nome=nome
        self.cognome=cognome
        self.specializzazione=specializzazione
    def visita_paziente(self,paziente):
        print(f"IL medico {self.nome} sta visitando {paziente.nome}")

class Analisi(ABC):
    def __init__(self,tipo,risultato):
        self.tipo=tipo
        self.risultato=risultato
    
    @abstractmethod
    def valuta(self):
        pass
        
class AnalisiGlicemia(Analisi):
    def valuta(self):
        if 70 <= self.risultato <= 99:
            return f"{self.tipo}: {self.risultato} mg/dL -> Nella norma"
        else:
            return f"{self.tipo}: {self.risultato} mg/dL -> Fuori norma"

class AnalisiEmocromo(Analisi):
    def valuta(self):
        if 12.0 <= self.risultato <= 17.5:
            return f"{self.tipo}: {self.risultato} g/dL -> Nella norma"
        return f"{self.tipo}: {self.risultato} g/dL -> Fuori norma"

class AnalisiColesterolo(Analisi):
    def valuta(self):
        if self.risultato < 200:
            return f"{self.tipo}: {self.risultato} mg/dL -> Nella norma"
        return f"{self.tipo}: {self.risultato} mg/dL -> Fuori norma"

class AnalisiCreatinina(Analisi):
    def valuta(self):
        if 0.6 <= self.risultato <= 1.2:
            return f"{self.tipo}: {self.risultato} mg/dL -> Nella norma"
        return f"{self.tipo}: {self.risultato} mg/dL -> Fuori norma"

class AnalisiTrigliceridi(Analisi):
    def valuta(self):
        if self.risultato < 150:
            return f"{self.tipo}: {self.risultato} mg/dL -> Nella norma"
        return f"{self.tipo}: {self.risultato} mg/dL -> Fuori norma"

class AnalisiFerritina(Analisi):
    def valuta(self):
        if 30 <= self.risultato <= 200:
            return f"{self.tipo}: {self.risultato} ng/mL -> Nella norma"
        return f"{self.tipo}: {self.risultato} ng/mL -> Fuori norma"

class AnalisiVitaminaD(Analisi):
    def valuta(self):
        if self.risultato >= 30:
            return f"{self.tipo}: {self.risultato} ng/mL -> Sufficiente / Nella norma"
        return f"{self.tipo}: {self.risultato} ng/mL -> Carenza / Fuori norma"

#Parte 3

risultati_glicemia = np.random.randint (70,140, size= (10))

media_risultati_glicemia = np.mean(risultati_glicemia)

valore_massimo_glicemia = np.max(risultati_glicemia)

valore_minimo_glicemia = np.min(risultati_glicemia)

deviazione_standard = np.std(risultati_glicemia)

Medico1= Medico("Paolo","Bruno","Cardiologia")
Medico2= Medico("Vittoria","Romano","Endocrinologia")
Medico3= Medico("Marco","Russo","Medicina Generale")

paziente_1 = Paziente("Mario", "Rossi", "MRBRDFGESFE07", 40, 72.5, ["Emocromo", "Glicemia", "Colesterolo"])
paziente_2 = Paziente("Luca", "Bianchi", "BNCLCU85M12F205Z", 35, 68.2, ["Glicemia", "Trigliceridi", "Creatinina"])
paziente_3 = Paziente("Giulia", "Verdi", "VRDGLI92T41H501W", 28, 57.0, ["Emocromo", "Ferritina", "Vitamina D"])
paziente_4 = Paziente("Anna", "Neri", "NRNNNA95A41F205K", 30, 55.0, ["Glicemia", "Colesterolo", "Trigliceridi"])
paziente_5 = Paziente("Francesco", "Gialli", "GLLFNC88B15H501U", 45, 80.2, ["Emocromo", "Creatinina", "Vitamina D"])

lista_medici= [Medico1,Medico2,Medico3]
lista_pazienti= [paziente_1,paziente_2,paziente_3,paziente_4,paziente_5]

paziente_1.aggiungi_risultato(14.2) 
paziente_1.aggiungi_risultato(95.0)
paziente_1.aggiungi_risultato(180.0)


paziente_2.aggiungi_risultato(88.0) 
paziente_2.aggiungi_risultato(130.0)
paziente_2.aggiungi_risultato(0.9)   

paziente_3.aggiungi_risultato(13.5)
paziente_3.aggiungi_risultato(45.0)
paziente_3.aggiungi_risultato(32.0)

paziente_4.aggiungi_risultato(92.0)
paziente_4.aggiungi_risultato(190.0)
paziente_4.aggiungi_risultato(145.0)

paziente_5.aggiungi_risultato(15.0)
paziente_5.aggiungi_risultato(1.1)
paziente_5.aggiungi_risultato(28.0)

for paziente in lista_pazienti:
    paziente.scheda_personale()
    paziente.statistiche_analisi()
    print("-"*30)

for medico,paziente in zip(lista_medici,lista_pazienti):
    medico.visita_paziente(paziente)
    