#1. Utwórz program do nauki obcych słówek. 
#Program powinien posiadać interfejs tektowy, w którym użytkownik wskazuje plik ze słówkami do nauki. 
#Następnie program importuje dane i wprowadza je do słownika. W kolejnym etapie program przepytuje uzytkownika z wiedzy zawartej w pliku ze słówkami. 
#Program powinien wyliczać za ile dni użytkownik powinien powtórzyć naukę - jeśli odpowiedział dobrze - za 7 dni, jeśli źle - za 0 dni
#Program tworzy nowy plik, który będzie zawierać informacje na temat daty ostatniej sesji nauki, id przerobionych słówek oraz za ile dni należy odbyć powtórkę. 
#Program dodatkowo ma importować log z poprzedniej sesji aby odpytywać użytkownika z zaplanowanej powtórki. 


from datetime import datetime
import glob
import random
import os.path
import json, time, sys

pl=[]
ang=[]


dec = input('czy zamierzasz wczytać poprzednia sesje T/N')
while (dec == 'T'):
    slownik = open('slownik.txt','r')
    words = []
        lines = f.readlines()
        for line in lines:
            line = line.split(';')
            line[3] = line[3].strip('\n')
            t = datetime.strptime(line[3], '%m/%d/%Y').date()
            words.append({'key': line[0], 'value': line[1], 'score': int(line[2]), 'time': t})
        return words
    
    break

dec2 = input('Czy zamierzasz dodać nowe słowa do słownika T/N')
while (dec2 == 'T'):
    polski = str(input('Znaczenie slowa po polsku'))
    pl.append(polski)
    angielski = str(input('Znaczenie slowa po angielsku'))
    en.append(angielski)
    dec3 = input('Czy zamierzasz dodać nowe słowa do słownika T/N')
    if (dec3 == 'N'):
        break

        
        
        
def askQuestion(self, key, value):
		print("przetlumacz slowo '" + value["pl"] + "' na jezyk angielski:")
		translated = input()

		if(translated == value["en"]):
			print("Poprawna odpowiedz!")

			self.dictionary.pop(key)
		else:
			print("Niestety, to nie jest poprawna odpowiedz.")
            
def checkLastSessionDone(self):
		session = self.getJSON(self.logPath)

		if("time" in session):
			if((float(session["time"]) + 604800) > self.currentTime):
				print("Ukończyles wszystkie zadania, kolejna sesja dostępna od: {0}".format(time.ctime(float(session["time"]) + 604800)))
				sys.exit()

		if(len(session) == 0 or (len(session) == 1 and "time" in session)):
			return True
		else:
			return False





slownik = close('slownik.txt','w')