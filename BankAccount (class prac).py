class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "This bank account belongs to {}. Balance: {}".format(self.name, self.balance)
  def show_balance(self):
    print ("Current balance: {}".format(self.balance))
  def deposit(self,amount):
    self.amount = amount
    if amount <= 0:
      print("Error insufficient deposit.")
      return
    else:
      print ("You are depositing {}".format(amount))
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    self.amount = amount
    if amount > self.balance:
      print("Insufficient funds.")
      return
    else:
      print("You are withdrawing: {}".format(amount))
      self.balance -= amount
      self.show_balance()
my_account = BankAccount("Alex") 
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)
      
    
    
    