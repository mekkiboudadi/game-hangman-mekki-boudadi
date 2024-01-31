import random 
words=['good','bad','ugly','mekki','boudadi']
#اختيار عشواءي للحاسوب
random_word=random.choice(words)

how=[]
#حجز_بعدد احرف الكلمة مت الحاسوب
for x in random_word:
    how.append('_')
print(how)
#تحويل ادخال الحاسوب الي ليست مع عمل لوب للادخال 
z=6

while how != list(random_word) :
 #زر الادخال للمستخدم 
 if z > 0:
  guessed=input('please guess a letter : ')
 #تغيير العلامة_ بالحرف المدخل ادا كان صحيح 
  for position in range(len(random_word)):
     if random_word[position]== guessed:
         how[position]=guessed
         #الطريقة الثانية  
        #del how [position]
        #how.insert(position,guessed)
  if guessed not in list(random_word):
   z-=1
  print(f"The remaining attempts are here: {z}")      
  print(how)
  if z == 1 :
      print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
  elif z==2 :
      print( '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
  elif z==3 :
      print( '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
  elif z==4:
      print( '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
  elif z==5:
      print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
  elif z==0:
      print( '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
  else:
      print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
else:
     print('''
      ****************************************
      ****************************************
      ************you is winer****************
      ****************************************
      ****************************************
      ''')
