import math

class Category:
    
    def __init__(self, name) : # ? Could this be deleted?
        self.name = name
        self.ledger = []

    def __str__(self) :
        return self.printSummary()

    # Accepts an amount and optional description, and append it to 'ledger'
    def deposit(self, amount, description=''): 
        newDeposit = {"amount": amount, "description": description}
        self.ledger.append(newDeposit)

    # Loop over ledger to sum all amounts 
    def get_balance(self) :
        founds = 0
        for item in self.ledger :
            founds += item['amount']
        return founds

    # Check if there is enough money to withdraw or transfer
    def check_funds(self, amount) :
        founds = self.get_balance()        
        return True if amount <= founds else False    

    # If there is enough money to withdraw, call 'deposit' sending a negative 'amount'
    def withdraw(self, amount, description='') :
        if self.check_funds(amount) : 
            self.deposit(-amount, description)
            return True
        else : 
            return False

    # Check if there is enough money to transfer from 'self.ledger' to 'destinationCat.ledger'
    def transfer(self, amount, destinationCat) :
        if self.check_funds(amount) : 
            self.withdraw(amount, "Transfer to " + destinationCat.name)
            destinationCat.deposit(amount, "Transfer from " + self.name)
            return True
        else : 
            return False

    def printSummary(self) : 
        # Calculate amount of askterisks and concatenate them to 'summary'
        countAsterisk, extraAsterisk = divmod((30-len(self.name))/2, 1)
        summary = int(countAsterisk)*'*' + self.name + int(countAsterisk)*'*' + ('*' if extraAsterisk else '') + '\n'

        # Concatenate each item
        for item in self.ledger : 
            summary += item['description'][:23]             # adding first 23 characters of description
            if len(item['description']) < 23 :              # if description is not 23 chars long, filling with spaces
                summary += (23-len(item['description']))*' ' 
            if len(str(float(item['amount']))) <= 6 :       # considering 7 digits a max numuber
                summary += (6-len("{:.2f}".format(float(item['amount'])))+1)*' ' + "{:.2f}".format(float(item['amount']))
            else :                                          # if number is greater than 7 digits then is Not a valid Number
                '    NvN'
            summary += '\n'

        # Concatenate Total
        summary += 'Total: ' + "{:.2f}".format(float(self.get_balance()))

        return summary

def create_spend_chart(categories):
    withdrawsPerCategory = []
    totalWithdraws = 0

    for category in categories :                    # for each category sent in list...
        totalPerCategory = 0

        # Calculation of withdraws per category
        for item in category.ledger :               # check for each item in ledger...
            if item['amount'] < 0 :                 # if the record is a withdraw
                totalPerCategory += -item['amount'] # add withdraws per category to 'totalPerCategory'
                totalWithdraws += -item['amount']   # .. and all withdraws to 'totalWithdraws' (negatives to handle in positive int)
        
        withdrawsPerCategory.append({"name" : category.name, "total" : totalPerCategory})
        
    # Concatenate histogram
    histogram = 'Percentage spent by category\n'
    maxLenName = 0

    for i in reversed(range(0, 101, 10)) :

        # Concatenate Y axis metrics
        if i == 100 :                   # Depending on the amount of characters... 
            histogram += str(i)
        elif i < 100 and i >= 10 :      # ...is the amount of whithe spaces...
            histogram += ' ' + str(i) 
        else :                          # ... to precede the number (percentage).
            histogram += '  ' + str(i)
        histogram += '|'

        # Concatenate bars
        for category in withdrawsPerCategory : 

            # Logic to concatenate bars ('o' characters)
            charToPrint = ' '           # default character to print is ' ' 
            percentage = math.trunc(category['total']*100/totalWithdraws)
            if percentage >= i :
                charToPrint = 'o'       # but, if percentage matches the current position of i, print 'o'
            
            histogram += ' ' + charToPrint + ' ' # concatenate the 'charToPrint'

            # get the max length of the category names to assamble X axis metrics
            maxLenName = len(category['name']) if len(category['name']) > maxLenName else maxLenName

        histogram  += ' \n'

    # Concatenate dashes
    histogram += 4*' ' + ((len(withdrawsPerCategory)*3)+1)*'-'

    # Concatenate X axis metrics (names)
    for i in range(maxLenName):
        histogram += '\n' + 4*' '
        for category in withdrawsPerCategory : 
            if len(category['name']) > i :
                histogram += ' ' + category['name'][i] + ' '
            else : 
                histogram += 3*' '

        histogram  += ' '

    return histogram