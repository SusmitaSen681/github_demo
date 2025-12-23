class Tea:   
    
    def __init__(self,milk = "with", strength = "normal", type_ = "regular"):  
          self.milk = milk  
          self.strength = strength  
          self.type_ = type_  
            
    def preparing(self):  
         print(f"preparing {self.strength} {self.type_} chai {self.milk} milk. ")  
  
# chai = Tea(strength="strong",type_ = "masala")  
# chai.preparing()  
  
class MasalaChai(Tea):  
      
    def __init__(self, milk= "with",strength = "normal"):  
         Tea.__init__(self,type_= "masala" , milk=milk, strength=strength)  
      
    def adding_spices(self):  
        print("Adding Cadmom, Elachi, Cinamon")  
  
# masalatea = MasalaChai(strength= "strong")  
# masalatea.preparing() 
 
class LemonChai(Tea): 
     
    def __init__(self, strength="normal"): 
        super().__init__(type_ = "lemon", strength= strength, milk = "without") 
         
    def adding_lemon(self): 
        print("adding lemon") 
 
# lemonchai = LemonChai() 
# lemonchai.preparing() 
  
class ChaiWala: 
    Lemon = LemonChai 
    Masala = MasalaChai 
    Chai   = Tea

    def receiving_order(self, order): 
        self.order = order

        def is_denial(change):
            NO_WORDS = ["no", "nah", "nope", "none"]
            return [word for word in change.lower().split() if word in NO_WORDS]

        if "masala" in self.order.lower().split(): 

            change = input("our regular masala chai comes with milk & normal strength. Any change?")

            if not is_denial(change): 
                self.milk = input("Do You want without milk ?") 
                self.strength = input("Do You want less or more strength ?") 
                self.chai = self.Masala(milk= self.milk, strength= self.strength) 
            else: 
                self.chai = self.Masala() 
             
        elif "lemon" in self.order.lower().split(): 

            change = input("our regular lemon tea comes with normal strength. Any change? ")

            if not is_denial(change): 
                self.strength = input("Do You want less or more strength ?") 
                self.chai = self.Lemon(strength= self.strength) 
            else: 
                self.chai = self.Lemon() 

        elif "chai" in self.order.lower().split():
            change = input("our regular chai comes with milk & normal strength. Any change ?")

            if not is_denial(change): 
                self.milk = input("Do You want with or without milk ?") 
                self.strength = input("Do You want stronger or less stronger chai ?") 
                self.type_ = input("Do You want any chai other then regular, lemon or masala ?")
                self.chai = self.Chai(milk= self.milk, strength= self.strength, type_= self.type_) 
            else: 
                self.chai = self.Chai()

        else:
            print("We don't have that item.") 
            return None

    def __init__(self): 
        self.order = input("what is your order?\n")
        self.receiving_order(self.order)
        self.chai.preparing() 
             
    def serving(self):
        try:
            self.chai
        except:
            return None
        print("serving your order.")

shop = ChaiWala() 
shop.serving()
