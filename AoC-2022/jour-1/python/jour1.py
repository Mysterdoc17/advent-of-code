#-------------------------------------------------------------Généralités-----------------------------------------------------------------------------#

# déclaration de la liste des calories
liste_calories = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# déclaration des variables - elf1 à elf5
elf1 = [0, 0, 0, 0, 0]
elf2 = [0, 0, 0, 0, 0]
elf3 = [0, 0, 0, 0, 0]
elf4 = [0, 0, 0, 0, 0]
elf5 = [0, 0, 0, 0, 0]

#---------------------processus pour affecter un donnée d'entrée aux variables des elfs avec une demande à l'utilisateur------------------------------#

# affichage de la liste des calories
print("Voici la liste des calories : ", liste_calories)


# affectation de la donnée d'entrée en fonction du rang de i
for i in range(0, 5):
    q1 = int(input("Choisissez un nombre parmi la liste ci-dessus : "))
    # processus pour i = 0
    if i == 0:
        if q1 == liste_calories[0]:
            elf1[0] = q1

        if q1 == liste_calories[1]:
            elf1[0] = q1

        if q1 == liste_calories[2]:
            elf1[0] = q1
        
        if q1 == liste_calories[3]:
            elf2[0] = q1

        if q1 == liste_calories[4]:
            elf3[0] = q1
        
        if q1 == liste_calories[5]:
            elf3[0] = q1
        
        if q1 == liste_calories[6]:
            elf4[0] = q1
        
        if q1 == liste_calories[7]:
            elf4[0] = q1

        if q1 == liste_calories[8]:
            elf4[0] = q1
        
        if q1 == liste_calories[9]:
            elf5[0] = q1
    
    # processus pour i = 1
    if i == 1:
        if q1 == liste_calories[0]:
            elf1[1] = q1

        if q1 == liste_calories[1]:
            elf1[1] = q1

        if q1 == liste_calories[2]:
            elf1[1] = q1
        
        if q1 == liste_calories[3]:
            elf2[1] = q1

        if q1 == liste_calories[4]:
            elf3[1] = q1
        
        if q1 == liste_calories[5]:
            elf3[1] = q1
        
        if q1 == liste_calories[6]:
            elf4[1] = q1
        
        if q1 == liste_calories[7]:
            elf4[1] = q1

        if q1 == liste_calories[8]:
            elf4[1] = q1
        
        if q1 == liste_calories[9]:
            elf5[1] = q1
    
    # processus pour i = 2
    if i == 2:
        if q1 == liste_calories[0]:
            elf1[2] = q1

        if q1 == liste_calories[1]:
            elf1[2] = q1

        if q1 == liste_calories[2]:
            elf1[2] = q1
        
        if q1 == liste_calories[3]:
            elf2[2] = q1

        if q1 == liste_calories[4]:
            elf3[2] = q1
        
        if q1 == liste_calories[5]:
            elf3[2] = q1
        
        if q1 == liste_calories[6]:
            elf4[2] = q1
        
        if q1 == liste_calories[7]:
            elf4[2] = q1

        if q1 == liste_calories[8]:
            elf4[2] = q1
        
        if q1 == liste_calories[9]:
            elf5[2] = q1
    
    # processus pour i = 3
    if i == 3:
        if q1 == liste_calories[0]:
            elf1[3] = q1

        if q1 == liste_calories[1]:
            elf1[3] = q1

        if q1 == liste_calories[2]:
            elf1[3] = q1
        
        if q1 == liste_calories[3]:
            elf2[3] = q1

        if q1 == liste_calories[4]:
            elf3[3] = q1
        
        if q1 == liste_calories[5]:
            elf3[3] = q1
        
        if q1 == liste_calories[6]:
            elf4[3] = q1
        
        if q1 == liste_calories[7]:
            elf4[3] = q1

        if q1 == liste_calories[8]:
            elf4[3] = q1
        
        if q1 == liste_calories[9]:
            elf5[3] = q1
        
    # processus pour i = 4
    if i == 4:
        if q1 == liste_calories[0]:
            elf1[4] = q1

        if q1 == liste_calories[1]:
            elf1[4] = q1

        if q1 == liste_calories[2]:
            elf1[4] = q1
        
        if q1 == liste_calories[3]:
            elf2[4] = q1

        if q1 == liste_calories[4]:
            elf3[4] = q1
        
        if q1 == liste_calories[5]:
            elf3[4] = q1
        
        if q1 == liste_calories[6]:
            elf4[4] = q1
        
        if q1 == liste_calories[7]:
            elf4[4] = q1

        if q1 == liste_calories[8]:
            elf4[4] = q1
        
        if q1 == liste_calories[9]:
            elf5[4] = q1

#-----------------------------------------------------------------vérifications-----------------------------------------------------------------------#

# si elf1

#-------------------------------------------------------------------Debug-----------------------------------------------------------------------------#

# débug - affichage des variables des elfs
print("Voilà la liste de ce que porte les elfs", elf1, elf2, elf3, elf4, elf5)