import numpy as np

class Toss():

    def __init__(self, prob):
        self.balance = 1000
        self.heads = 0
        self.tails = 0
        self.mult = 0
        self.bet = 100
        self.prob = prob
        self.list = [self.balance]

    def toss(self):
        odd = np.random.rand()
        if odd >= self.prob:
            self.heads += 1
            self.balance += self.bet
            self.list.append(self.balance)
            self.mult = 0
            self.bet = 100
        else:
            self.tails += 1
            self.balance += -self.bet
            self.list.append(self.balance)
            self.mult += 1
            self.bet = 100*(2**self.mult)

fart = Toss(0.5)

c = 0
while c != 50:
    fart.toss()
    c += 1
print(f"HEADS   TAILS\n  {fart.heads}       {fart.tails}\n{round((fart.heads/(fart.heads + fart.tails))*100, 2)}%   {round((fart.tails/(fart.heads + fart.tails))*100, 2)}%\n   {fart.balance}")
#print(fart.list)
