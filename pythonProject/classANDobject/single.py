class Animal:

    def __init__(self,sound):
        self.sound = sound

    def getSound(self):
        return self.sound

    def sound(self):
        return -1

class Cat(Animal):

    def __init__(self,breed,sound,new_sound):
        self.breed = breed
        super(Cat,self).__init__(sound)

    def getBreed(self):
        return self.breed

    def sound(self):
        print("Hello Kitty",+breed)



c = Cat('persian','meow','newmeow')
print(c.sound())

