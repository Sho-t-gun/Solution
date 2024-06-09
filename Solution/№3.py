import random

class Cat:
    def __init__(self, num_kittens):
        self.girls = random.randint(0, num_kittens)
        self.boys = num_kittens - self.girls

    def girls_count(self):
        return self.girls

    def boys_count(self):
        return self.boys

cat = Cat(15)
print(cat.girls_count())
print(cat.boys_count())
