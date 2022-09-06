class Employee:
    organization = "Microsoft"

    def _inti_(self, name, salary=0):
        self.name = name
        self.name = salary
    
    #instance method
    def give_raise(self, amount):
        self.salary += amount
        return f"{self.name} has been given a {amount} raise"