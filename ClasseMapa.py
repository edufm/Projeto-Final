
from tkinter import *
import numpy as np

window = Tk()
window.title("Magic Trap")
window.configure(bg="black")
window.geometry('1366x728')

from ClasseEnemys import Enemys
from ClasseGun import Gun
from ClassePlayer import Player
import ClasseImagens

class Mapa():
    def __init__(self, matriz, b, gadjets, Waves, LEnemys):
        self.matriz = matriz
        self.b = b
        self.gadjets = gadjets
        self.Waves = Waves
        self.LEnemys = LEnemys
    
    def Start_Game(X, L):
        
        if X == 1:
            L[0].destroy()
            L[1].destroy()
            L[2].destroy()
            
        Map = Mapa(np.zeros([15, 27]), [], [], 0, [])    
        
        Pistol = Gun(100,7,7,1,"Shoot")        
        Lguns = [Pistol]
        
        pl = Player(20, Lguns[0], [7,13], [7, 0, 0])
        
        Map.matriz[7][13] = 1
        Mapa.load_map(Map, window, pl)
        Player.set_player(pl)
        
        Mapa.gui(window, Map)
        
        window.mainloop()

    def detect_click(self, m, pl):
        
        X = m[0]
        Y = m[1]
        Xp = pl.pos[0]
        Yp = pl.pos[1]
        
        b = self.b
        V = self.matriz[X][Y] == 0
        G = self.matriz[X][Y] > 99
        GN = int(self.matriz[X][Y]) - 100
        
        if (G or V) and X+1 == Xp and Y == Yp:
            if G:
                Gun.Pick_Weapon(GN, pl)
            #Adiciona o player no novo lugar
            self.matriz[X][Y] = 1
            b[X][Y].config(image=ClasseImagens.player[3])
            b[X][Y].image = ClasseImagens.player[3]
            #Remove o "Rastro" do player
            self.matriz[Xp][Y] = 0
            b[Xp][Yp].config(image=ClasseImagens.Tiles[self.Waves])
            b[Xp][Yp].image = ClasseImagens.Tiles[self.Waves]
            pl.pos = [X,Y]
            
        if (G or V) and X-1 == Xp and Y == Yp:
            if G:
                Gun.Pick_Weapon(GN, pl)                
            self.matriz[X][Y] = 1
            b[X][Y].config(image=ClasseImagens.player[0])
            b[X][Y].image = ClasseImagens.player[0]
            self.matriz[Xp][Y] = 0
            b[Xp][Yp].config(image=ClasseImagens.Tiles[self.Waves])
            b[Xp][Yp].image = ClasseImagens.Tiles[self.Waves]
            pl.pos = [X,Y]

        if (G or V) and Y+1 == Yp and X == Xp:
            if G:
                Gun.Pick_Weapon(GN, pl)
            self.matriz[X][Y] = 1
            b[X][Y].config(image=ClasseImagens.player[2])
            b[X][Y].image = ClasseImagens.player[2]
            self.matriz[X][Yp] = 0
            b[Xp][Yp].config(image= ClasseImagens.Tiles[self.Waves])
            b[Xp][Yp].image = ClasseImagens.Tiles[self.Waves]
            pl.pos = [X,Y]
            
        if (G or V) == 0 and Y-1 == Yp and X == Xp:
            if G:
                Gun.Pick_Weapon(GN, pl)
            self.matriz[X][Y] = 1
            b[X][Y].config(image= ClasseImagens.player[1])
            b[X][Y].image = ClasseImagens.player[1]
            self.matriz[X][Yp] = 0
            b[Xp][Yp].config(image= ClasseImagens.Tiles[self.Waves])
            b[Xp][Yp].image = ClasseImagens.Tiles[self.Waves]
            pl.pos = [X,Y]
            
        if self.matriz[X][Y] >= 2 and self.matriz[X][Y] < 99:
            Enemys.Take_Damage([X,Y], pl, self)
        
        Mapa.Aiturn(self.LEnemys, pl ,self)
        
        Mapa.updategui(self, self.gadjets, pl)
        
        if ((len(self.LEnemys)) == 0):
            self.Waves += 1
            Enemys.cria_inimigos(self.Waves, self)
            Mapa.update_map(self, pl)        
        
        self.gera_itens(ClasseImagens.guns)
            
        
    def gera_itens(self, imgguns):
        Gun.Gerar_Guns(self, imgguns)
        
    def Aiturn(enemys, pl, Map):
        for i in enemys:
            Enemys.jogada(i, pl, Map)

    def update_map(Map, pl):
        for i in range (15):
            for j in range(27):
                Map.b[i][j].config(image=ClasseImagens.Tiles[Map.Waves])
                Map.b[i][j].image = ClasseImagens.Tiles[Map.Waves]
                
        Map.b[pl.pos[0]][pl.pos[1]].config(image = ClasseImagens.player[0])
        Map.b[pl.pos[0]][pl.pos[1]].image = ClasseImagens.player[0]
    
    def Botão_de_arma(pl, Map, X):
        if X == 0:
            pass
            mostrarange(pl, Map)
        if X == 1:
            pass
            mostrarange(pl, Map)
        if X == 2:
            pass
            mostrarange(pl, Map)
        
    def mostrarange(pl, Map):
        passw
    
    def load_map(self, window, pl):
        
        for i in range(15):
            self.b.append([])
            for j in range(27):
                button = Button(window, text=' ',command= lambda m=[i,j]: self.detect_click(m, pl))
                button.grid(row=i+1, column=j, sticky=W+E+S+N)
                button.config(image=ClasseImagens.Tiles[0])
                button.configure(height = 36, width = 36,bg = "black")
                button.image = ClasseImagens.Tiles[0]
                self.b[i].append(button)
                        
        self.b[7][13].config(image = ClasseImagens.player[0])
        self.b[7][13].image = ClasseImagens.player[0]
        self.b[7][13].configure(highlightbackground="red", highlightcolor="red")
                
    def gui(window, Map):
        
        vida = Label(window)
        vida.configure(text="Life:",font=("castelar"),bg = "black",foreground = "white")
        vida.configure(height = 2 , width = 4)
        vida.grid(row=16,column=0)
        botãodevida1 = Button(window)
        botãodevida1.configure(bg="light blue")
        botãodevida1.configure(height = 2 , width = 20)
        botãodevida1.grid(row= 16,columnspan = 7)
        time = Label(window)
        time.configure(text="Time : {0}s".format(2.5),font=("castelar"),bg = "black",foreground="white")
        time.configure(height = 2, width = 8)
        time.grid(row= 16, column = 11,columnspan=100)
        wave = Label(window)
        wave.configure(text="Wave : {0}".format(1),font=("castelar"),bg = "black",foreground="white")
        wave.configure(height = 2, width = 7)
        wave.grid(row= 1, column = 28, columnspan= 2)
        nomejogo = Label(window)
        nomejogo.configure(text="I´ll survive" , font= ("Times",20),bg = "black",foreground="white")
        nomejogo.grid(row = 0 ,columnspan =100)
        
        Map.gadjets.append(vida)
        Map.gadjets.append(botãodevida1)
        Map.gadjets.append(time)
        Map.gadjets.append(wave)
        Map.gadjets.append(nomejogo)
        #Botões de armas
        Pistolb = Button(window)
        Pistolb.configure(height = 36, width = 36, state = 'disabled')
        Pistolb.configure(image = ClasseImagens.guns[0])
        Pistolb.image = ClasseImagens.guns[0]
        Pistolb.grid(row = 5, column = 28, columnspan = 2)
        
        Pammo = Label(window)
        Pammo.configure(text="Ammo :   x{0}".format(0),font=("castelar"),bg = "black",foreground = "white")
        Pammo.configure(height = 2, width = 15)
        Pammo.grid(row= 5, column = 30)
        
        shotgunb = Button(window)
        shotgunb.configure(height = 36, width = 36, state = 'disabled')
        shotgunb.configure(image = ClasseImagens.guns[1])
        shotgunb.image = ClasseImagens.guns[1]
        shotgunb.grid(row = 7, column = 28, columnspan = 2)
        
        shotammo = Label(window)
        shotammo.configure(text="Ammo :   x{0}".format(0),font=("castelar"),bg = "black",foreground = "white")
        shotammo.configure(height = 2, width = 15)
        shotammo.grid(row= 7, column = 30)
        
        Sniperb = Button(window)
        Sniperb.configure(height = 36, width = 36, state = 'disabled')
        Sniperb.configure(image = ClasseImagens.guns[2])
        Sniperb.image = ClasseImagens.guns[2]
        Sniperb.grid(row = 9, column = 28, columnspan = 2)
        
        snipeammo = Label(window)
        snipeammo.configure(text="Ammo :   x{0}".format(0),font=("castelar"),bg = "black",foreground = "white")
        snipeammo.configure(height = 2, width = 15)
        snipeammo.grid(row= 9, column = 30)
        
        Map.gadjets.append(Pistolb)
        Map.gadjets.append(Pammo)
        Map.gadjets.append(shotgunb)
        Map.gadjets.append(shotammo)
        Map.gadjets.append(Sniperb)
        Map.gadjets.append(snipeammo)
         
    def updategui(Map, gadjets, pl):
        if pl.health <= 0:
            for i in range(15):
                for j in range(27):
                    Map.b[i][j].destroy()
            for i in gadjets:
                i.destroy()
            
            youdied = Label(window)
            youdied.config(text = "Whatta shame, you died!!", height = 5, width = 36,bg="black",foreground="red",font=("castelar",40))
            
            youdied.place(x=130, y=40)
    
            giveup = Button(window)
            giveup.config(command =lambda: Mapa.Exit())
            exiit = PhotoImage(file=".\\Imagens\\Sprites\\exit.png")
            giveup.image = exiit
            giveup.config(image=exiit,bg="black")
            giveup.place(x=525, y= 300)
            
            restart = Button(window)
            restart.config(command =lambda: Mapa.Start_Game(1, [youdied, restart, giveup]))
            restartt = PhotoImage(file=".\\Imagens\\Sprites\\reset-button-hi.png")
            restart.image = restartt
            restart.config(image=restartt,bg="black")
            restart.place(x=525, y= 500)
                      
        gadjets[1].configure(height = 2 , width = pl.health)
        gadjets[2].configure(text="Time : {0}s".format(2.5),font=("castelar"),bg = "black",foreground="white")
        gadjets[3].configure(text="Wave : {0}".format(Map.Waves),font=("castelar"),bg = "black",foreground="white")
        
        if pl.inv[0] > 0:
            gadjets[5].config(state = 'active')
        
        if pl.inv[1] > 0:
            gadjets[7].config(state = 'active')
            
        if pl.inv[2] > 0:
            gadjets[9].config(state = 'active')
        
        gadjets[6].config(text = 'Ammo X{0}'.format(pl.inv[0]))        
        gadjets[8].config(text = 'Ammo X{0}'.format(pl.inv[1]))
        gadjets[10].config(text = 'Ammo X{0}'.format(pl.inv[2]))
        
    def Exit():
        window.destroy()