



from turtle import*
colormode(255)

setup(width=750, height=625, startx=400, starty=300)
speed("fastest")

def zamianaNazespolone(liczba):
	if (liczba[1] > 0):
		return eval(str(liczba[0])+"+"+str(liczba[1])+"j")
	else:
		return eval(str(liczba[0])+"-"+str(liczba[1])+"j")
	

# liczba - zespolona ktorej modul chce porownac zCzym - z czym chce porownac. Zwraca |liczba| >= zCzym
def porownywanieModulu(liczba,zCzym):
	liczba = abs(liczba)
	return True if (liczba >= (zCzym*zCzym)) else False

def sprawdzenieCzyNalezyDoZbioru(punkt,przyblizenie):
	z = punkt
	iteracja = 0
	while (iteracja<100):
		iteracja += 1
		z = pow(z,2)+przyblizenie
		if (porownywanieModulu(z,2)):
			return iteracja
	return 0	



def tworzenieTablicy(przyblizenie,wysokosc,szerokosc,dokladnosc):
	x = -1.5
	y = -1.25
	igreki=[]
	przeskok = 0.001 * dokladnosc
	for iteracja in range(wysokosc):
		y = round(y+przeskok,3)
		iksy=[] 
		x = -1.5
		for iteracja2 in range(szerokosc):
			x = round(x+przeskok,3)
			zespolona=zamianaNazespolone((x,y))
			przyb = sprawdzenieCzyNalezyDoZbioru((zespolona),przyblizenie)
			iksy.append(przyb)
		igreki.append(iksy)
	return(igreki)		

def zmianaPozycji(x,y):

	penup()
	setposition(x,y)
	pendown()



def rysujTablice(dokladnosc,zmienna):
	wysokosc = 2500//dokladnosc
	szerokosc = 3000//dokladnosc
	tablica = tworzenieTablicy((-0.123 + 0.745j),wysokosc,szerokosc,dokladnosc)
	for i in tablica:
		zapamietana = 0
		for j in range(len(i)):
			if (i[j] >=6 ):
				zapamietana = j
		i[zapamietana]="stop"		
	for y in range(wysokosc):
		for x in range(szerokosc):
			mnoznikY=625/wysokosc
			mnoznikX =750/szerokosc
			zmianaPozycji(mnoznikX * x-375,mnoznikY *y-312)
			powtarzalnosc = tablica[y][x]
			if (powtarzalnosc == "stop"):
				break
			elif (powtarzalnosc == 0):
				dot(dokladnosc,"black")
			elif (powtarzalnosc <=6):
				pass	
			else:
				try:
					dot(dokladnosc,(255-(powtarzalnosc-3)*6,255-(powtarzalnosc-3)*6,255-(powtarzalnosc-3)))			
				except:
					dot(dokladnosc,(0,0,0))			
		
rysujTablice(4,(-0,73 + 0,19j))


input()





