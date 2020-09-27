

#Extra Credit Part 1 have completed

import tkinter as tk
import random

#FIRST: Implement and test your Pokemon class below
class Pokemon:
    print("Implement this and then remove this print statement")
    def __init__(self,dex=0,name='',catch_rate=0,speed=0):
        self.dex = dex
        self.name = name
        self.catch_rate = catch_rate
        self.speed = speed
        self.photo = tk.PhotoImage(file = 'sprites/'+str(self.dex)+'.gif')
    def __str__(self):
        return str(self.name)

        
#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        print("In SafariSimulator init")
        self.pokedex=[]
        fp = open('pokedex.csv')
        lines = fp.readlines()
        lines = lines[1:]
        for line in lines:
            line = line.strip()
            ele = line.split(',')
            dex = int(ele[0])
            name = ele[1]
            catch_rate = int(ele[2])
            speed = int(ele[3])
            self.pokedex.append(Pokemon(dex,name,catch_rate,speed))
        fp.close()
        self.safari_balls = 30
        self.caught_Pokemon = []
        #Read in the data file from pokedex.csv at some point here
        #It's up to you how you store and handle the data 
        #(e.g., list, dictionary, etc.),
        #but you must use your Pokemon class in some capacity
        #Initialize any instance variables you want to keep track of

        #DO NOT MODIFY: These lines set window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()
        self.createWidgets()
        #Call nextPokemon() method here to initialize your first random pokemon
        self.nextPokemon()
       
    def createWidgets(self):
        print("In createWidgets")
        #See the image in the instructions for the general layout required
        
        #You need to create an additional "throwButton"
        self.throwButton = tk.Button(self)
        self.throwButton["text"] = "Throw Safari Ball (%s left)"%(self.safari_balls)
        self.throwButton["command"] = self.throwBall
        self.throwButton.pack()
        
        #"Run Away" button has been completed for you as an example:
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.pack()

        #A label for status messages has been completed for you as an example:
        self.messageLabel = tk.Label(bg="grey")
        self.messageLabel.pack(fill="x", padx=5, pady=5)

        #You need to create two additional labels:

        #Complete and pack the pokemonImageLabel here.
        self.pokemonImageLabel = tk.Label(bg="white")
        self.pokemonImageLabel.pack(fill="x", padx=5, pady=5)

        #Complete and pack the catchProbLabel here.
        self.catchProbLabel = tk.Label(bg="grey")
        self.catchProbLabel.pack(fill="x", padx=5, pady=5)

        self.runawayLabel = tk.Label(bg="grey")
        self.runawayLabel.pack(fill="x", padx=5, pady=5)

        
      
    def nextPokemon(self):
        print("In nextPokemon")
        #This method must:
            #Choose a random pokemon
        self.next_Pokemon = random.choice(self.pokedex)
            #Get the info for the appropriate pokemon
            #Ensure text in messageLabel and catchProbLabel matches the pokemon
        self.messageLabel['text'] = 'You encounter a wild '+str(self.next_Pokemon.name)
        self.catchProbLabel['text'] = 'Your chance of catching it is '+str(int((min((self.next_Pokemon.catch_rate+1), 151) / 449.5)*100))+'%!'
        self.runawayLabel['text'] = "It's likelihood of running away is "+str(int((2*self.next_Pokemon.speed)/256*100))+'%!'


            #Change the pokemonImageLabel to show the right pokemon
        self.next_Pokemon.photo= tk.PhotoImage(file = 'sprites/'+str(self.next_Pokemon.dex)+'.gif')
        self.pokemonImageLabel['image'] = self.next_Pokemon.photo
        #Hint: to see how to create an image, look at the documentation 
        #for the PhotoImage/Label classes in tkinter.
        
        #Once you generate a PhotoImage object, it can be displayed 
        #by setting self.pokemonImageLabel["image"] to it
        
        #Note: the PhotoImage object MUST be stored as an instance
        #variable for some object (you can just set it to self.photo).
        #Not doing this will, for weird memory reasons, cause the image 
        #to not be displayed.
        
    def throwBall(self):
        print("In throwBall")
        self.safari_balls -= 1
        self.throwButton["text"] = "Throw Safari Ball (%s left)"%(self.safari_balls)
        
        #This method must:

            #Decrement the number of balls remaining
            #Try to catch the pokemon
            #Check to see if endAdventure() should be called

        #To determine whether or not a pokemon is caught, generate a random
        #number between 0 and 1, using random.random().  If this number is
        #less than min((catchRate+1), 151) / 449.5, then it is caught. 
        #catchRate is the integer in the Catch Rate column in pokedex.csv, 
        #for whatever pokemon is being targetted.
        a = random.random()
        a = a*100
        runawayProb = int((2*self.next_Pokemon.speed)/256*100)
        prob = int((min((self.next_Pokemon.catch_rate+1), 151) / 449.5)*100)  
        if self.safari_balls > 0:
            if a < prob:
                self.caught_Pokemon.append(self.next_Pokemon)
                self.nextPokemon()
                #print (self.caught_Pokemon)
            else:
                if (a >= prob) and (a >= runawayProb) :
                    self.messageLabel['text'] = 'Aargh! It escaped! '
                elif a < runawayProb:
                    self.messageLabel['text'] = 'Aargh! It ran away! '
                    self.pokemonImageLabel.config(image='')
                    self.after(1000,self.nextPokemon)
        else:
            self.endAdventure()
            
            
        #Don't forget to update the throwButton's text to reflect one 
        #less Safari Ball (even if the pokemon is not caught, it still 
        #wastes a ball).
        
        #If the pokemon is not caught, you must change the messageLabel
        #text to "Aargh! It escaped!"
        
        #Don't forget to call nextPokemon to generate a new pokemon 
        #if this one is caught.
        
    def endAdventure(self):
        print("In endAdventure")
        if self.safari_balls == 0:
            self.messageLabel['text'] = "You're all out of balls, hope you had fun!"
            self.throwButton.pack_forget()
            self.runButton.pack_forget()
            self.pokemonImageLabel.pack_forget()
            self.runawayLabel.pack_forget()
            a = '\n'
            for i in self.caught_Pokemon:
                a += i.name + '\n'
            if self.caught_Pokemon != []:
                self.catchProbLabel['text'] = 'You caught '+str(len(self.caught_Pokemon))+' Pokémon:'+ a
            else:
                self.catchProbLabel['text'] ='Oops, you caught 0 Pokémon.'
                 
        #This method must: 

        #Display adventure completion message
        #List captured pokemon

        #Hint: to remove a widget from the layout, you can call the 
        #pack_forget() method.
        
        #For example, self.pokemonImageLabel.pack_forget() removes 
        #the pokemon image.


#DO NOT MODIFY: These lines start your app
app = SafariSimulator(tk.Tk())
app.mainloop()

