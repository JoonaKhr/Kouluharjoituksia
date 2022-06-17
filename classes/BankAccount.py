class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def set_owner(self, new_owner):
        self.owner = new_owner

    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount
    
    # Print olio hakee nyt tämän
    def __str__(self):
        return f"""
                Bank Account:
                Owner: {self.owner}
                Balance: {self.balance}
                """
    # Tarkoitus antaa suuntaa muille ohjelmoijille
    def __repr__(self):
        return f"BankAccount(owner='{self.owner}' balance={self.balance})"