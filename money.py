# pylint: disable=unidiomatic-typecheck,unnecessary-pass

class DifferentCurrencyError(Exception):
    pass

class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """
    def __init__(self, name, code, symbol=None, digits=2):
        """
        Parameters:
        - name -- the English name of the currency
        - code -- the ISO 4217 three-letter code for the currency
        - symbol - optional symbol used to designate currency
        - digits -- number of significant digits used
        """
        self.name = name
        self.code = code
        self.symbol = symbol
        self.digits = digits

    def __str__(self):
        """
        Should return the currency code, or code with symbol in parentheses.
        """
        if self.symbol: #add what varies to the conditional 
            return f"{self.code} ({self.symbol})" 
        else:
            return f"{self.code}"

    def __eq__(self, other): 
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name and
                self.code == other.code and self.symbol == other.symbol and
                self.digits == other.digits)

class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """
    def __init__(self, amount, currency):
        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
        self.amount = amount
        self.currency = currency
        
       
        
    def __str__(self): #reads strings
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """
        if self.currency.symbol:
            return f"{self.currency.symbol}{self.amount:.{self.currency.digits}f}"
        else:
            return f"{self.currency.code} {self.amount:.{self.currency.digits}f}"
# When do we need the front and back f? f string synatax based on string and digits

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.amount == other.amount and
                self.currency == other.currency)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency == other.currency:
            total = self.amount + other.amount
            currency = self.currency #defined local in Money
            sum = Money(total, currency)
            return sum
        else:
          raise DifferentCurrencyError

    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency == other.currency:
            total = self.amount - other.amount
            currency = self.currency #defined local in Money
            difference = Money(total, currency)
            return difference
        else:
          raise DifferentCurrencyError

    def mul(self, multiplier): #have to use both parameters
        """
        Multiply a money object by a number to get a new money object.
        """
        #if self.currency == other.currency: only using one currency.. don't need this like
        total = self.amount * multiplier
        currency = self.currency
        product = Money(total, currency)
        return product


    def div(self, divisor): #have to use both parameters
        """
        Divide a money object by a number to get a new money object.
        """
        #if self.currency == other.currency:
        total = self.amount / divisor
        currency = self.currency
        quotient = Money(total, currency)
        return quotient

