import math

class Vigur:
    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self,x,y): 
        # Þinn kóði hér
        self.head = 0
        self.x = x
        self.y = y

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):
        if self.head == 0:
            print("[{} {}]".format(self.x, self.y))
        elif self.head == 1:
            print("[-{} {}]".format(self.y, self.x))
            

    # Fall sem skilar lengd
    def lengd(self):
        lengd_c_veldi = self.x**2 + self.y**2
        lengd_c = float("{0:.2f}".format(math.sqrt(lengd_c_veldi)))
        return lengd_c
        
    # Fall sem skilar hallatölu
    def halli(self):
        if self.x != 0:
            return self.y / self.x
        else:
            print("Enginn hallatala")

    # Fall sem skilar þvervigri
    def þvervigur(self):
        self.head = 1
        return self
    
    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):  
        stefnuhorn = float("{0:.1f}".format(math.degrees(math.atan(self.y/self.x))))
        return stefnuhorn
        
    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self,v):
        cos_v = (self.x * v.x) + (self.y * v.y) / math.sqrt(self.x**2 + self.y**2) * math.sqrt(v.x**2 + v.y**2)
        horn_milli_vigra = math.degrees(math.acos(cos_v))
        return horn_milli_vigra
        
    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self,v):
        self.head = 0
        self.x += v.x
        self.y += v.y
        return self

# Keyrsluforrit
v1 = Vigur(1,3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = v1.þvervigur()
print("Þvervigur: " , end=" ")
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())
v2 = Vigur(-3,1)
print("Horn milli vigra: " , v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: " , end=" ")
v3.prenta()

