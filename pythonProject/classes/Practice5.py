class Animal:

    def __init__(self):
        self.name = " "
        self.sound = " "

    #Getter and Setter

    def setName(self,name,sound):
        self.name = name
        self.sound = sound

    def getName(self):
        return self.name

    def getSound(self):
        return self.sound

    #this is optional and not nessesary
    #def setSound(self, sound):
    #   self.sound = sound