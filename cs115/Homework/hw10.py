'''
Created on Nov 14, 2016

@author: Alex Lu and Matthew Koroluk
'''
'I pledge my Honor that I have abided by the Stevens Honor System'

D = {}
file = 'musicrecplus.txt'
inputs = ['q', 'e', 'r', 'p', 'h', 'm']

def read_prefs(filename):
    '''Assume filename is path to an existing file in the format above.
       Print each user name and a list of the user's prefs. Reads the file'''
    input_file = open(filename, 'r')   # Open the file for reading.
    for line in input_file:# Get one line at a time.
        if line != '\n':
            user, artists = line.split(':')
            artists = artists.split(',')
            for i in range(len(artists)):
                artists[i] = artists[i].strip()
            user = user.strip()
            D[user]=artists
    input_file.close() # Important - do not forget to close the file
read_prefs('musicrecplus.txt')
print(D)
D['Name3']=['A4','A5','A6']
D['Name4']=['A6','A7','A8']
# Writing a file.
def write_prefs(filename):
    '''Open existing or new file named filename.
       Write SAMPLE_FILE_CONTENT to it.'''
    output_file = open(filename, 'w')
    line = []
    for user in D:
        s = user+':'
        for artist in D[user]:
            s = s + artist+','
        line+=[s[:-1]]
    for l in line:
        output_file.write(l + '\n')
    output_file.close()
write_prefs('musicrecplus.txt')

def musicRec():
    'the main function of the program that connects all the helper functions'
    read_prefs(file)
    while(1):
        menu()
        user_input = input('Enter a menu key: ')
        if user_input not in inputs:
            print('UNACCCEEEPTAAAABLLLLLLEEEE, please enter a proper value!')
        elif user_input =='q':
            break
        elif user_input == 'e':
            enter_prefs()
        elif user_input == 'r':
            get_recs()
        elif user_input == 'p':
            show_pop()
        elif user_input == 'h':
            how_pop()
        elif user_input == 'm': #I refrained from using else so that more functions could be added more easily if wanted.
            most_likes()
        write_prefs(file)
            
def enter_prefs():
    'allows the user to enter a username and enter their artist preferences. If the user is already in the dictionary, then their preferences get replaced'
    user = input('Please enter a username: ').strip().title()
    artists = []
    while(1):
        a = input('Enter a prefered artist (or Q to finish): ').strip().title()
        if a == 'Q':
            break
        artists.append(a)
    D[user] = artists

def menu():
    'prints the menu'
    print("""Enter a letter to choose an option:
e - enter preferences
r - get recommendations
p - show most popular artists
h - how popular is the most popular
m - which user has the most likes
q - save and quit""")
    
def get_recs():
    'recommends artists based on the users current preferences and how many match with other users'
    user = input('Please enter a username: ').strip().title()
    L = compare(user)
    best_match = max_matches(L)
    prefs = D[best_match]
    rec = drop_matches(prefs, D[user])
    rec2 = drop_matches2(rec, D[user])
    print(rec2)
    
def count_matches(list1, list2):
    'counts the number of matches between 2 lists'
    count = 0
    for x in list1:
        for y in list2:
            if x==y:
                count+=1
    return count

def compare(user):
    'returns a list within a list, with each list containing the user and the number of matches'
    L = []
    for x in D:
        if x!=user:
            L+=[[x,count_matches(D[user], D[x])]]
    
    return L

def max_matches(L):
    'returns the user with the most matches'
    max = 0
    a = ''
    for x in L:
        if x[1]>max:
            max = x[1]
            a=x[0]
    return a

def drop_matches(list1,list2):
    'removes all the matches between list1 and list2 and returns a new list'
    list1.sort()
    list2.sort()
    result = []
    i = 0
    j = 0
    while i<len(list1) and j<len(list2):
        if list1[i] == list2[j]:
            i+=1
            j+=1
        elif list1[i]<list2[j]: 
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+=1
    while i<len(list1):
        result.append(list1[i])
        i+=1
    while j<len(list2):
        result.append(list2[j])
        j+=1
    return result

def drop_matches2(rec,original):
    'removes the artists in the recommended list that are already in the users original list of artists'
    result = []
    for x in rec:
        if x not in original:
            result.append(x)
    return result              

def most_likes():
    'returns the user with the most artists in their preferences unless they have a $ sign at the end of their user tag'
    max = 0
    a=''
    for x in D:
        if len(D[x])>max:
            if x[-1]!='$':
                max = len(D[x])
                a = x
    print(a)

def show_pop():
    'prints the most popular artist/artists in a list'
    L = []
    max = 0
    a = helper1()
    b = helper3(a)
    for x in b:
        if x[1]>max:
            max=x[1]
    for y in b:
        if y[1]==max:
            L+=[y[0]]
    print(L)
        
    
def helper1():
    'Makes a list of all the artists'                      
    L=[]
    for x in D:
        for y in D[x]:
            L.append(y)
    return L

def helper2(x,L):
    'counts the number of x in list L'
    count = 0
    for a in L:
        if a==x:
            count+=1
    return count

def helper3(a):
    'returns a list of lists. Each list contains the artist and how many times they appear in the text file'
    L=[]
    for x in helper4(a):
        L+=[[x,helper2(x, a)]]
    return L
    
def helper4(L):
    'removes duplicates in list L'
    result = []
    for x in L:
        if x not in result:
            result.append(x)
    return result

def how_pop():
    'prints how many users like the most popular artist'
    L = []
    max = 0
    a = helper1()
    b = helper3(a)
    for x in b:
        if x[1]>max:
            max=x[1]
    for y in b:
        if y[1]==max:
            L+=[y[1]]
    if len(L)>1:
        print("There is a tie for most popular")
    else:
        print(max)
        

musicRec()
        