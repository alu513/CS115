'''
Created on Nov 17, 2016

@author: Alex Lu
'''
'I pledge my Honor that I have abided by the Stevens Honor System'

class QuadraticEquation(object): 
    
    def __init__(self,a,b,c):
        
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        a = float(a)
        b = float(b)
        c = float(c)
        self.__a = a
        self.__b = b
        self.__c = c
        
    @property
    def a(self):
        return self.__a 
    
    @property
    def b(self):
        return self.__b
    
    @property
    def c(self):
        return self.__c   
    
    
    def discriminant(self):
        return (self.b*self.b-4.0*self.a*self.c)
    
    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.__b+self.discriminant()**(1/2))/(2.0*self.__a)
    
    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.__b-self.discriminant()**(1/2))/(2.0*self.__a)
        
    def __str__(self):
        x = str(self.__a) + 'x^2'
        q = ' + '
        w = ' + '
        y = str(self.__b) + 'x'
        z = str(self.__c) + ' = 0'
        
        if self.__a<0:
            x = '-' + x
        if self.__b<0:
            q = ' - '  
            y = str(((self.__b)*(self.__b))**(1/2)) + 'x'
        if self.__c<0:
            w = ' - ' 
            z = str(((self.__c)*(self.__c))**(1/2)) + ' = 0' 
        if self.__b==0:
            y = ''
            q = ''
        if self.__c==0:
            z = ' = 0'
            w = ''
        if self.__a==1: 
            x = 'x^2'
        if self.__a==-1:
            x = '-x^2'
        if self.__b==1 or self.__b==-1:
            y = 'x'
            
        return x+q+y+w+z
        
       
    