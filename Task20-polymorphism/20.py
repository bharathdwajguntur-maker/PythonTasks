#--------Runtime Polymorphism + Single inheritance-------------

#Example-1:

class Shirt:
    def fabric(self):
        print("Cotton")
class Tshirt(Shirt):
    def fabric(self):
        print("Poly Cotton")
t=Tshirt()
t.fabric()

s=Shirt()
s.fabric()



#Example-2:

class WhiteBook:
    def paperType(self):
        print("White Note Book")
class RuleBook(WhiteBook):
    def paperType(self):
        print("Rule Note Book")
w=WhiteBook()
w.paperType()

r=RuleBook()
r.paperType()


#--------Runtime Polymorphism + Multilevel inheritance-------------

#Example-1:

class LPG:
    def petroleum(self):
        print(" Liquified Petrolium Gas extracted from Petroleum for cooking and fuel gas")
class Naphtha(LPG):
    def petroleum(self):
        print(" Naphtha extracted from Petroleum for petro-chemical products")
class Gasoline(Naphtha):
    def petroleum(self):
        print(" Gasoline extracted from Petroleum for vehicle fuel")
class Kerosine(Gasoline):
    def petroleum(self):
        print(" Kerosine extracted from Petroleum for jet and heating fuel")
l=LPG()
l.petroleum()
n=Naphtha()
n.petroleum()
g=Gasoline()
g.petroleum()
k=Kerosine()
k.petroleum()




#Example-2:

class Rain:
    def water(self):
        print("Rain water")
class Streams(Rain):
    def water(self):
        print("Rain water flows as tiny streams")
class Rivers(Streams):
    def water(self):
        print("Streams form as Rivers")
class Sea(Rivers):
    def water(self):
        print("Rivers form/merged into Sea")
r=Rain()
r.water()
str=Streams()
str.water()
riv=Rivers()
riv.water()
s=Sea()
s.water()





# --------Runtime Polymorphism + Hierarchial inheritance-------------

# Example-1:

class Electricity():
    def current(self):
        print("I can run electrical machines/products")
class Fan(Electricity):
    def current(self):
        print("Fan is running by using electricity")
class Light(Electricity):
    def current(self):
        print("Light is glowing by using electricity")
e=Electricity()
f=Fan()
l=Light()
e.current()
f.current()
l.current()



#Example-2:

class ArtificialIntelligence():
    def AI(self):
        print("Artificial Intelligence")
class ChatGpt(ArtificialIntelligence):
    def AI(self):
        print("Chat GPT")
class Gemini(ArtificialIntelligence):
    def AI(self):
        print("Gemini AI")
a=ArtificialIntelligence()
c=ChatGpt()
g=Gemini()
a.AI()
c.AI()
g.AI()



# --------Runtime Polymorphism + Multiple inheritance-------------

# Example-1:

class Copper():
    def metal(self):
        print("Copper Metal")
class Zinc():
    def metal(self):
        print("Zinc Metal")
class Brass(Copper,Zinc):
    def metal(self):
        print("Copper + Zinc = Brass")
c=Copper()
z=Zinc()
b=Brass()
c.metal()
z.metal()
b.metal()


# Example-2:

class Cement():
    def material(self):
        print("Cement powder")
class Water():
    def material(self):
        print("Water")
class CementPaste(Cement,Water):
    def material(self):
        print("Cement + Water = Cement Paste")
c=Cement()
w=Water()
cp=CementPaste()
c.material()
w.material()
cp.material()



# --------Runtime Polymorphism + Hybrid inheritance-------------

# Example-1:

class ElectronicDevice():
    def gadget(self):
        print("Electronic Device")
class Computer(ElectronicDevice):
    def gadget(self):
        print("Computer")
class Laptop(Computer):
    def gadget(self):
        print("Laptop")
class Desktop(Computer):
    def gadget(self):
        print("Desktop")
class Gaming(Laptop):
    def gadget(self):
        print("Gaming Laptop")
class Business(Laptop):
    def gadget(self):
        print("Business Laptop")
e=ElectronicDevice()
c=Computer()
l=Laptop()
d=Desktop()
g=Gaming()
b=Business()
e.gadget()
c.gadget()
l.gadget()
d.gadget()
g.gadget()
b.gadget()



# Example-2:

class ElectricalMachine():
    def motor(self):
        print("Electrical Machine")
class Motors(ElectricalMachine):
    def motor(self):
        print("Electrical Motor")
class ACM(Motors):
    def motor(self):
        print("AC Motor")
class DCM(Motors):
    def motor(self):
        print("DC Motor")
class Induction(ACM):
    def motor(self):
        print("Induction Motor")
class Synchronous(ACM):
    def motor(self):
        print("Synchronous motor")
e=ElectricalMachine()
m=Motors()
a=ACM()
d=DCM()
i=Induction()
s=Synchronous()
e.motor()
m.motor()
a.motor()
d.motor()
i.motor()
s.motor()