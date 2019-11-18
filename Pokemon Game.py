class Pokemon(object):
  def __init__(self, name, level, typ):
    self.name = name
    self.level = level
    self.typ = typ
    self.health = level*4
    self.maxhealth = level * 4
    self.is_KO = False
  def __repr__(self):
    return "The pokemon {}. He is level {}.".format(self.name,self.health,self.level)
  def lose_health(self,amount):
    self.amount = amount
    if self.health <= 0:
      self.knockout()
    else:
        self.health -= amount
        print("You lost {} HP. Current HP: ".format(amount, self.health))
  def gain_health(self, amount):
    self.amount = amount
    if self.amount + self.health > self.maxhealth:
      self.health = self.maxhealth
      print("Your health is full.")
    else:
      self.health += amount
      print("You gained {} HP. Current HP: ".format(amount, self.maxhealth))
  def knockout(self):
    self.is_KO = True
  def revive(self):
    self.is_KO = False
    print("Your Pokemon is revived!")
    return 
  def attack(self,other_pokemon): #can put arguments for fire water and grass later
    damage = 5
    self.other_Pokemon = other_pokemon
    if self.typ == other_pokemon.typ:
      damage = 5 - (0.5*other_pokemon.level)
    other_pokemon.lose_health(damage)
    print("You hit for {} HP".format(damage))

class Charmander(Pokemon):
    def __init__(self, level):
        super().__init__("Charmander", level, "Fire")

class Squirtle(Pokemon):
    def __init__(self, level):
        super().__init__("Squirtle", level, "Water")

class Bulbasaur(Pokemon):
    def __init__(self, level):
        super().__init__("Bulbasaur", level, "Grass")

class Trainer(Pokemon):
  def __init__(self,pokemons,potions,name):
    self.pokemons = pokemons
    self.potions = potions
    self.current_pokemon = 0
    self.name = name
  def __refr__(self):
    return "Your name is {}. Your pokemon team is: {},{},{}. You have {} potions".format(self.name,self.pokemons[0],self.pokemons[1],self.pokemons[3], self.potions)
  def use_potion(self):
    if self.potion > 0:
      self.potion -=1
      if self.is_KO == True:
        print("Your Pokemon cannot be healed it is currently unconscious.")
      else:
        self.health += 10
        print("You gave your pokemon {} hp.".format(health))
  def attack_trainer(self, other_trainer):
    my_current_pokemon = self.pokemons[self.current_pokemon]
    self.other_trainer = other_trainer
    their_current_pokemon=other_trainer.pokemons[other_trainer.current_pokemon]
    my_current_pokemon.attack(their_current_pokemon)
  def switch(self,which_pokemon): #which_pokemon is an integer
    self.which_pokemon = which_pokemon
    if self.which_pokemon > len(self.pokemons):
      print("You did not select a pokemon.")
    else:
    	self.current_pokemon = self.which_pokemon

a = Pokemon(5)
b = Squirtle(5)
c = Bulbasaur(7)
trainer1 = Trainer([a,b,c], 3, "Alex")

print(trainer1)