## Joe Murphy IT 2660 Assn 1

class Murph:
    # class attribute
    lastname = 'Murphy'

    # instance attribute
    def __init__(self, firstname, gndr, age_yrs):
        self.fname = firstname
        self.gender = gndr
        self.age = age_yrs

    def get_profile(self):
        attrs = self.__dict__
        return attrs

    def get_age(self):
        return self.age

        
#child class
class Kid(Murph):
    def __init__(self, firstname, gndr, age_yrs, a_skill):
        super().__init__(firstname, gndr, age_yrs)
        self.skill = a_skill

    def tell_skill(self):
        skill = f"{(self.get_profile())['fname']}'s skill is {(self.get_profile())['skill']}"
        return skill




dad = Murph('Joe', 'male', 35)
mom = Murph('Joannie', 'female', 26)
baby1 = Kid('Maria', 'female', 2, 'goofing')
baby2 = Kid('Eavy E', 'female', 1, 'being cute')

dadsage = (dad.get_profile())['age']

print(f"\nDad's demographics as a dict:\t {dad.get_profile()}")
print(f"Dad's age via the attribute dict: {(dad.get_profile())['age']} \t") # ...It's ugly but if you wanted to not write a get method for every attr, this is one way. 
print(f"Dad's age via a direct get method: {dad.get_age()}")

print(f"\nMom does all the hard work. Thanks {(mom.get_profile())['fname']}")

print(f"\nKids have skills that parents don't. {baby1.tell_skill()}")
print(f"\nKids have skills that parents don't. {baby2.tell_skill()}\n")


        
