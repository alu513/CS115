'''
Created on _______________________
@author:   Alexander Lu
Pledge:    I pledge my Honor that I have abided by the Stevens Honor System

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day
    
    def tomorrow(self):
        '''changes the calling object so that it represents one 
        calendar day after the date it originally represented'''
                
        if self.day==DAYS_IN_MONTH[self.month]:
            if self.isLeapYear()==True:
                if self.month==2 and self.day==28:
                    self.day=29
                else:
                    if self.month==12:
                        self.day=1
                        self.month = 1
                        self.year = self.year+1
                    else:
                        self.month = self.month+1
                        self.day=1
              
            elif self.isLeapYear()==False:  
                if self.month==12:
                    self.day=1
                    self.month = 1
                    self.year = self.year+1
                else:
                    self.month = self.month+1
                    self.day=1
        elif self.month==2 and self.day==29:
                    self.day=1
                    self.month=3        
        else:
            self.day=self.day+1
     
    def yesterday(self):
        '''changes the calling object so that it represents one 
        calendar day before the date it originally represented'''
                
        if self.day==1:
            if self.month==1:
                self.month = 12
                self.year = self.year-1
                self.day = 31
            elif self.isLeapYear()==True and self.month==3:
                self.month = 2
                self.day=29
            else:
                self.day=DAYS_IN_MONTH[self.month-1]
                self.month=self.month-1
        else:
            self.day=self.day-1
    
    def addNDays(self,N):
        '''changes the calling object so that it represents N 
        calendar days after the date it originally represented'''
        print(self)
        for _ in range(N):
            self.tomorrow()
            print(self)
            
    def subNDays(self,N):        
        '''changes the calling object so that it represents N 
        calendar days before the date it originally represented'''
        print(self)
        for _ in range(N):
            self.yesterday()
            print(self)
            
    def isBefore(self, d2):
        '''returns True if the calling object is a calendar date 
        before the input named d2'''
        d = d2.copy()
        if self.year<d.year:
            return True
        elif self.month<d.month and self.year<=d.year:
            return True
        elif self.day<d.day and self.month<=d.month and self.year<=d.year:
            return True
        return False
    
    def isAfter(self, d2):
        '''returns True if the calling object is a calendar date 
        after the input named d2'''
        d = d2.copy()
        if self.year>d.year:
            return True
        elif self.month>d.month and self.year>=d.year:
            return True
        elif self.day>d.day and self.month>=d.month and self.year>=d.year:
            return True
        return False
    
    def diff(self, d2):
        '''returns an integer representing the number of days between self and d2'''
        day1=self.copy()
        day2=d2.copy()
        count = 0
        if day1.equals(day2):
            return count
        if day1.isBefore(day2) == True:
            while day1.isBefore(day2):
                day2.yesterday()
                count+=1
            return count*-1
        if day1.isAfter(day2) == True:
            while day1.isAfter(day2):
                day2.tomorrow()
                count+=1
            return count
        
    def helper(self):
        'returns the doomsday date closest to the given date'
        lst = [1,2,3,4,5,6,7,8,9,10,11,12]
        lst2 = [3,28,14,4,9,6,11,8,5,10,7,12]
        lst4 = [4,29,14,4,9,6,11,8,5,10,7,12]
        if self.isLeapYear():
            for x in lst:
                if self.month == x:
                    a = Date(lst[x-1],lst4[x-1],self.year)
        else:
            for x in lst:
                if self.month == x:
                    a = Date(lst[x-1],lst2[x-1],self.year)
        return a
    
     
    def helper2(self):
        'returns the doomsday(a known date) for the year'
        a = self.year-((self.year//100)*100)
        b=int(a/12)
        c = abs(a-12*b)
        e = int(c/4) 
        d = 0
        
        if (self.year//100)%4==0:
            d = 2
        elif (self.year//100)%4==1:
            d = 0
        elif (self.year//100)%4==2:
            d = 5
        elif (self.year//100)%4==3:
            d = 3
        
            
        f = (b+c+e+d)%7
            
        return f
    
    def dow(self):
        '''return a string that indicates the day of the week 
        (dow) of the object (of type Date) that calls it.'''
        a = self.helper()
        b = self.helper2()
        c = ''
        e = abs(self.diff(a))%7
        
        for x in range(e):
            if self.diff(a)<0:
                if b>0:
                    b = b-1
                elif b==0:
                    b = 6
            else:
                if b<6:
                    b = b+1
                elif b==6:
                    b = 0
        if b==0:
            c = 'Sunday'
        elif b==1:
            c = 'Monday'
        elif b==2:
            c = 'Tuesday'
        elif b==3:
            c = 'Wednesday'
        elif b==4:
            c = 'Thursday'
        elif b==5:
            c = 'Friday'
        elif b==6:
            c = 'Saturday' 
        return c
    

           
            
        
        
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
