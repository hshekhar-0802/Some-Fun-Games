import math
import random

class BoardGame:
    def __init__(self):
        self.properties=[{},{'Name':'Start','Price':int(0),'Owner':int(0),'Type':'Start'},{'Name':'Mumbai','Price':int(8500),'Owner':int(0),'Type':'Property'},{'Name':'Water Works','Price':int(3200),'Owner':int(0),'Type':'Service'},{'Name':'Railways','Price':int(9500),'Owner':int(0),'Type':'Transport'},{'Name':'Ahmedabad','Price':int(4000),'Owner':int(0),'Type':'Property'},{'Name':'Income Tax','Price':int(0),'Owner':int(0),'Type':'Tax'},{'Name':'Indore','Price':int(1500),'Owner':int(0),'Type':'Property'},{'Name':'Chance','Price':int(0),'Owner':int(0),'Type':'Chance'},{'Name':'Jaipur','Price':int(3000),'Owner':int(0),'Type':'Property'},{'Name':'Jail','Price':int(0),'Owner':int(0),'Type':'Jail'},{'Name':'Delhi','Price':int(6000),'Owner':int(0),'Type':'Property'},{'Name':'Chandigarh','Price':int(2500),'Owner':int(0),'Type':'Property'},{'Name':'Electric Company','Price':int(2500),'Owner':int(0),'Type':'Service'},{'Name':'BEST','Price':int(3500),'Owner':int(0),'Type':'Transport'},{'Name':'Shimla','Price':int(2200),'Owner':int(0),'Type':'Property'},{'Name':'Amritsar','Price':int(3300),'Owner':int(0),'Type':'Property'},{'Name':'Community Chest','Price':int(0),'Owner':int(0),'Type':'Community_Chest'},{'Name':'Srinagar','Price':int(5000),'Owner':int(0),'Type':'Property'},{'Name':'Club','Price':int(0),'Owner':int(0),'Type':'Club'},{'Name':'Agra','Price':int(2500),'Owner':int(0),'Type':'Property'},{'Name':'Chance','Price':int(0),'Owner':int(0),'Type':'Chance'},{'Name':'Kanpur','Price':int(4000),'Owner':int(0),'Type':'Property'},{'Name':'Patna','Price':int(2000),'Owner':int(0),'Type':'Property'},{'Name':'Darjeeling','Price':int(2500),'Owner':int(0),'Type':'Property'},{'Name':'Air India','Price':int(10500),'Owner':int(0),'Type':'Transport'},{'Name':'Kolkata','Price':int(6500),'Owner':int(0),'Type':'Property'},{'Name':'Hyderabad','Price':int(3500),'Owner':int(0),'Type':'Property'},{'Name':'Rest House','Price':int(0),'Owner':int(0),'Type':'Rest_House'},{'Name':'Chennai','Price':int(7000),'Owner':int(0),'Type':'Property'},{'Name':'Community Chest','Price':int(0),'Owner':int(0),'Type':'Community_Chest'},{'Name':'Bengaluru','Price':int(4000),'Owner':int(0),'Type':'Property'},{'Name':'Wealth Tax','Price':int(0),'Owner':int(0),'Type':'Tax'},{'Name':'Mysore','Price':int(2500),'Owner':int(0),'Type':'Property'},{'Name':'Cochin','Price':int(3000),'Owner':int(0),'Type':'Property'},{'Name':'Motor Boat','Price':int(5500),'Owner':int(0),'Type':'Transport'},{'Name':'Goa','Price':int(4000),'Owner':int(0),'Type':'Property'}]
    
    def start(self,player):
        i=0
    
    def property(self,player):
        global curr_player
        global Players
        global bankrupt
        pos=player.curr_pos
        if(player.id==self.properties[pos]['Owner'] and player.start_crossed>=2):
            if(player.holdings[self.properties[pos]['Name']]=='No house'):
                dec=input("Do you want to build a house ?(Y/N)").upper()
                if(dec not in 'YN'):
                    while(dec not in 'YN'):
                        dec=input("Wrong input! Please try again..(Y/N)").upper()
                if(dec=='Y'):
                    player.build_house(self)
        elif(player.id==self.properties[pos]['Owner'] and player.start_crossed<2):
            print("You need to cross Start at least 2 times to be eligible to build house.")
        elif(not(self.properties[pos]['Owner']==0)):
            owner=Players[self.properties[pos]['Owner']-1]
            amount=self.properties[pos]['Price']*(0.1)
            if(owner.holdings[self.properties[pos]['Name']]=='House'):
                amount=amount*2
            if(amount%100>50):
                amount=round(amount,-2)-100
            else:
                amount=round(amount,-2)
            player.pay_rent(owner,amount)
        else:
            dec=input("Do you want to buy the holding ?(Y/N) Not buying will lead to paying INR 1000 to the bank.")
            if(dec not in 'YN'):
                while(dec not in 'YN'):
                    dec=input("Wrong input! Please try again..(Y/N)").upper()
            if(dec=='Y'):
                player.buy_holding(self)
            else:
                player.pay_bank(1000)
                
    def transport(self,player):
        global curr_player
        global Players
        global bankrupt
        pos=player.curr_pos
        if(not(player.id==self.properties[pos]['Owner']) and self.properties[pos]['Owner']>0):
            owner=Players[self.properties[pos]['Owner']-1]
            amount=self.properties[pos]['Price']*(0.1)
            if(amount%100>50):
                amount=round(amount,-2)-100
            else:
                amount=round(amount,-2)
            player.pay_rent(owner,amount)
        elif(not(player.id==self.properties[pos]['Owner']) and self.properties[pos]['Owner']==0):
            amt=player.money
            dec=input("Do you want to buy the holding ?(Y/N) Not buying will lead to paying INR 1000 to the bank.")
            if(dec not in 'YN'):
                while(dec not in 'YN'):
                    dec=input("Wrong input! Please try again..(Y/N)").upper()
            if(dec=='Y'):
                player.buy_holding(self)
            else:
                player.pay_bank(1000)
    
    def tax(self,player):
        global curr_player
        global Players
        global bankrupt
        pos=player.curr_pos
        if(self.properties[pos]['Name']=='Income Tax'):
            amount=0.1*player.rent
            if(amount%100>50):
                amount=round(amount,-2)-100
            else:
                amount=round(amount,-2)
            player.pay_bank(amount)
        else:
            player.pay_bank(200)
    
    def club(self,player):
        player.pay_bank(200)
    
    def rest(self,player):
        player.jail=True
        player.pay_bank(100)
        
    def jail(self,player):
        player.jail=True
        player.pay_bank(1500)
    
    def chance(self,player,throw):
        global curr_player
        global Players
        global bankrupt
        amount=[0,0,2000,2500,1000,1000,1500,2000,3000,1500,0,3000,0]
        if(throw%2==0 and throw<10):
            if throw==2:
                print("Loss in share market Rs 2000")
            elif throw==4:
                print("Fine for accident due to driving under liquor influence Rs 1000")
            elif throw==6:
                print("House repairs Rs 1500")
            elif throw==8:
                print("Loss due to fire in godown Rs 3000")
            player.pay_bank(amount[throw])
        elif(throw==10):
            print("Go to jail")
            self.jail(player)
            player.curr_pos=10
        elif(throw==12):
            print("Go to rest house, you cannot play next turn")
            self.rest(player)
            player.curr_pos=28
        elif(throw%2==1 and not(throw==9)):
            if throw==3:
                print("Lottery prize Rs2500")
            elif throw ==5:
                print("You have won the crossword competetion prize Rs 1000")
            elif throw==7:
                print("You won a jackpot of Rs 2000")
            elif throw==11:
                print("Prize of bes tperformance in Exports, Rs 3000")
            player.get_from_bank(amount[throw])
        else:
            print("Go back to Mumbai. If you have to pass starting point, collect Rs 1500 and go to Darjeeling")
            player.curr_pos=24
            player.start_crossed+=1
            player.get_from_bank(1500)
            self.property(player)
    
    def community_chest(self,player,throw):
        global curr_player
        global Players
        global bankrupt
        amount=[0,0,500,0,2500,1000,2000,2000,0,50,1500,1500,3000]
        if(throw%2==0 and (throw not in [2,8])):
            if throw==4:
                print("First prize in reality TV show Rs 2500")
            elif throw ==6:
                print("Income tax refund Rs 2000")
            elif throw==10:
                print("Recieve interest on shares Rs 1500")
            elif throw==12:
                print("Sale of stocks, collect Rs3000")
            player.get_from_bank(amount[throw])
        elif(throw%2==1 and (throw not in [3,9])):
            if throw ==5:
                print("School and medical fees Rs 1000")
            elif throw==7:
                print("Marriage celebration Rs 2000")
            elif throw==11:
                print("Pay insurance premium Rs 1500") 
            player.pay_bank(amount[throw])
        elif(throw==2):
            print("It is your birthday, collect Rs 500 form each player")
            for i in Players:
                if not(i.id==player.id):
                   i.pay_player(player,500)
        elif(throw==8):
            print("Go to rest house, you cannot play next turn")
            self.rest(player)
            player.curr_pos=28
        elif(throw==3):
            print("Go to jail")
            self.jail(player)
            player.curr_pos=10
        elif(throw==9):
            print("Make general repair on all your properties: For each house pay Rs 50")
            houses=0
            for i in player.holdings:
                if(player.holdings[i]=='House'):
                    houses=houses+1
            amount=houses*50
            player.pay_bank(amount)
              
              
              
              
              
class Player:
    def __init__(self,name,id):
        self.id=id
        self.name=name
        self.rent=0
        self.curr_pos=1
        self.jail=False
        self.start_crossed=0
        self.holdings={}
        self.started=False
        self.networth=0
        self.money=int(15000)
        self.to_bank=0
        self.from_bank=0
    
    def next_player(self):
        global curr_player
        global Players
        global bankrupt
        if self.id==len(Players):
            curr_player=1
        else:
            curr_player+=1
    
    def dice(self):
        r1=random.randint(1,6)
        r2=random.randint(1,6)
        print("Dice 1: "+str(r1)+"   Dice 2: "+ str(r2))
        return r1+r2
    
    def show_money(self):
        print("Current Balance: INR ",self.money)

    def turn(self,Board,throw=0):
        global curr_player
        global Players
        global bankrupt
        name=Players[curr_player-1].name
        print(f"It is Player-{curr_player}: "+name+"'s turn")
        dec=input("Do you want to mortgage your property ?(Y/N)").upper()
        while(dec not in 'YN'):
            dec=input("Wrong input! Please try again..(Y/N)").upper()
        if(dec=='Y' and len(self.holdings)>0):
            self.sell_holding(Board)
        elif(dec=='Y' and len(self.holdings)==0):
            print("You do not have any current holdings.")
        self.show_pos(Board)
        self.show_money()
        if(self.started==True):
            input("Press Enter to roll the dice: ")
            throw=self.dice()
        self.change_pos(throw,Board)
        if Board.properties[self.curr_pos]['Type']=="Start":
            Board.start(self)
        elif Board.properties[self.curr_pos]['Type']=="Property":
            Board.property(self)
        elif Board.properties[self.curr_pos]['Type']=="Service":
            Board.transport(self)
        elif Board.properties[self.curr_pos]['Type']=="Transport":
            Board.transport(self)
        elif Board.properties[self.curr_pos]['Type']=="Tax":
            Board.tax(self)
        elif Board.properties[self.curr_pos]['Type']=="Chance":
            Board.chance(self,throw)
        elif Board.properties[self.curr_pos]['Type']=="Community_Chest":
            Board.community_chest(self,throw)
        elif Board.properties[self.curr_pos]['Type']=="Club":
            Board.club(self)
        elif Board.properties[self.curr_pos]['Type']=="Rest_House":
            Board.rest(self)
        elif Board.properties[self.curr_pos]['Type']=="Jail":
            Board.jail(self)

    def pay_rent(self,to,amount):
        global curr_player
        global Players
        global bankrupt
        if self.money>=amount:
            self.money-=amount
            to.money+=amount
            to.rent+=amount
            print("Amount transferred: ",amount)
            print(self.name+"'s balance: "+str(self.money))
            print(to.name+"'s balance: "+str(to.money))
        else:
            print(self.name+", you do not have enough money.")
            if (len(self.holdings)>0):
                self.sell_holding(Board)
                self.pay_rent(to,amount)
            else:
                to.money+=self.money
                to.rent=self.money
                self.money-=amount
                print(self.name+" is bankrupt!")
                print("Game Over....!")
                bankrupt=True
    
    def pay_player(self,to,amount):
        global curr_player
        global Players
        global bankrupt
        if self.money>=amount:
            self.money-=amount
            to.money+=amount
            print("Amount transferred: ",amount)
            print(self.name+"'s balance: "+str(self.money))
            print(to.name+"'s balance: "+str(to.money)) 
        else:
            print(self.name+" ,you do not have enough money")
            if (len(self.holdings)>0):
                self.sell_holding(Board)
                self.pay_player(to,amount)
            else:
                to.money+=self.money
                self.money-=amount
                print(self.name+" is bankrupt!")
                print("Game Over....!")
                bankrupt=True
    
    def pay_bank(self,amount):
        global curr_player
        global Players
        global bankrupt
        if self.money>=amount:
            self.money-=amount
            self.to_bank+=amount
            print("Payment transferred: "+str(amount))
            print(self.name+"'s balance: "+str(self.money))
        else:
            print(self.name+",you do not have enough money")
            if len(self.holdings)>0:
                self.sell_holding(Board)
                self.pay_bank(amount)
            else:
                self.money-=amount
                print(self.name+" is bankrupt!")
                print("Game Over....!")
                bankrupt=True

    def change_pos(self,throw,Board):
        global curr_player
        global Players
        global bankrupt
        self.curr_pos+=throw
        if self.curr_pos>36:
            self.curr_pos=self.curr_pos%36
            self.start_crossed+=1
            print("You passed the Start.")
            self.get_from_bank(1500)
        print("New location: ",Board.properties[self.curr_pos]['Name'])
        print("Price of site :"+str(Board.properties[self.curr_pos]['Price']))
    
    def show_pos(self,Board):
        print ("Current location: ",Board.properties[self.curr_pos]['Name'])
    
    def show_holdings(self):
        for i in self.holdings:
            print(i+": "+self.holdings[i])

    def buy_holding(self,Board):
        global curr_player
        global Players
        global bankrupt
        if self.money>=Board.properties[self.curr_pos]['Price']:
            self.money-=Board.properties[self.curr_pos]['Price']
            self.holdings[Board.properties[self.curr_pos]['Name']]="No house"
            Board.properties[self.curr_pos]['Owner']=self.id
            print("Congratulations! You have bought the holding.")
            self.show_money()
            self.networth+=Board.properties[self.curr_pos]['Price']
        else:
            dec=input("You do not have enough money. Do you want to mortgage your property ?(Y/N)").upper()
            while(dec not in 'YN'):
                dec=input("Wrong input! Please try again..(Y/N)").upper()
            if(dec=='Y' and len(self.holdings)>0):
                self.sell_holding(Board)
                self.buy_holding(Board)
            elif(dec=='Y' and len(self.holdings)==0):
                print("You do not have any current holdings.")
                self.pay_bank(1000)
            else:
                self.pay_bank(1000)
    
    def sell_holding(self,Board):
        global curr_player
        global Players
        global bankrupt
        amount=0
        print("You have the following holdings :")
        self.show_holdings()
        name_holding=input("Enter the name of the holding you want to sell: ")
        if name_holding in self.holdings:
            index=0
            for j in range(1,len(Board.properties)):
                if Board.properties[j]['Name']==name_holding:
                    temp1=Board.properties[j]['Price']/2
                    index=j
            sell_price=(temp1//100)*100
            self.money=self.money+sell_price
            del self.holdings[name_holding]
            self.networth-=temp1*2
            Board.properties[index]['Owner']=0
            print("Amount transferred from bank: "+str(sell_price))
            self.show_money()
        else:
            print("You do not own that holding. Try Again..")
            self.sell_holding(Board)
    
    def get_from_bank(self,amount):
        self.money+=amount
        self.from_bank+=amount
        print("Amount received from bank: ",amount)
        print(self.name+"'s balance: "+str(self.money))
             
    def build_house(self,Board):
        global curr_player
        global Players
        global bankrupt
        if self.start_crossed>=2:
            if Board.properties[self.curr_pos]['Name'] in self.holdings:
                if self.money>=500:
                    self.holdings[Board.properties[self.curr_pos]['Name']]="House"
                    self.money-=500
                else:
                    dec=input("You do not have enough money. Do you want to mortgage your property ?(Y/N)").upper()
                    while(dec not in 'YN'):
                        dec=input("Wrong input! Please try again..(Y/N)").upper()
                    if(dec=='Y' and len(self.holdings)>0):
                        self.sell_holding(Board)
                        self.build_house(Board)
                    elif(dec=='Y' and len(self.holdings)==0):
                        print("You do not have any current holdings.")
            else:
                print("This holding does not belong to you.")
        else:
            print("You have not crossed the start position enough times.")

        
Players=[]
def initialize_game():
    global curr_player
    global Players
    global bankrupt
    players=int(input("How many players? "))
    if 2<=players<=4:
        for i in range(players):
            name=input("Enter player name: ")
            Players.append(Player(name,i+1))
    else:
        print("Number of players should be from 2 to 4. Please try again !")
        initialize_game()
    print("                         INITIAL STATUS OF THE GAME               ")
    print("The name of players are:-")
    for i in range(len(Players)):
        print(Players[i].name)
    print("Initial amount of cash with each player is Rs.15000")
Board=BoardGame()
initialize_game()
curr_player=1
bankrupt=False
while(not bankrupt):
    if Players[curr_player-1].started:
        if Players[curr_player-1].jail==True:
            print("You cannot play in this turn!")
            Players[curr_player-1].jail=False
            Players[curr_player-1].next_player()
        else:
            Players[curr_player-1].turn(Board)
            Players[curr_player-1].next_player()
    else:
        throw=Players[curr_player-1].dice()
        if throw>=10:
            Players[curr_player-1].turn(Board,throw)
            Players[curr_player-1].started=True
            Players[curr_player-1].next_player()
        else:
            print("Try again in your next turn")
            Players[curr_player-1].next_player()
    if(curr_player==1):
        print("---------------------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------------------")
        dec=input("Enter 'Show' to view all the player details or anything else to continue playing: ").upper()
        if dec=='SHOW':
            for i in range(len(Players)):
                print(f"PLAYER-{i+1}: "+Players[i].name)
                Players[i].show_money()
                print("Crossed start: "+str(Players[i].start_crossed))
                Players[i].show_holdings()
                Players[i].show_pos(Board)
                print("Amount earned from rent: "+str(Players[i].rent))
                print("Amount paid to the bank so far: "+str(Players[i].to_bank))
                print("Amount received from the bank so far: "+str(Players[i].from_bank))
                print("--------------------------------------------------------------")
    else:
        print("--------------------------------------------------------------")
max_net_worth=-1e8
l=-1
print("---------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------")
print("Net-worths of the Players:")
for i in range(len(Players)):
    print(f"Player{i+1}: {Players[i].name} : INR {Players[i].networth+Players[i].money}")
    if max_net_worth==Players[i].networth:
        if len(Players[i].holdings)>len(Players[l].holdings):
            max_net_worth=Players[i].networth
            l=i
    elif Players[i].networth>max_net_worth:
        max_net_worth=Players[i].networth
        l=i

print(f"Winner: {Players[l].name}")