# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Coin:
    def __init__(self, rare=False, clean=True, head=True, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)
        self.is_rare = rare
        self.is_clean = clean
        self.head = head

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
            self.color = self.rusty_color
        
    def clean(self):
            self.color = self.clean_color

    def __del__(self):
        print ("coin spent!")

    def flip(self):
        head_options = [True, False]
        choice = random.choice(head_options)
        self.head = choice
    
    def __str__ (self):
        if self.original_value >=1:
            return "{} Coin".format (int(self.original_value))
        else:
            return "{}p Coin". format (int(self.original_value * 100))
        
        
class Two_Rupee1(Coin):
    def __init__(self):
        data = { "original_value": 2.00,
        "clean_color":"steel",
        "rusty_color":"brownish",
        "num_edges": 11,
        "diameter" : 23.00,
        "weight": 26,
        }
        super().__init__(**data)
    
class Two_Rupee(Coin):
    def __init__(self):
        data = { "original_value": 2.00,
        "clean_color":"steel",
        "rusty_color":"brownish",
        "num_edges": 11,
        "diameter" : 23.00,
        "weight": 26,
        }
        super().__init__(True, **data)
        
    
rupee1 = Two_Rupee1()
print (rupee1.value)

rupee = Two_Rupee()
#rupee1.color
#rupee1.clean()
#rupee1.color
print (rupee.value)

        
    

