import random
studentname = input("Please enter your full name\n")
studentid=input("Please enter your student ID\n ")

#-------the  that will take students name and ID number
print("Student Name:" + studentname)
print("Student ID:" + studentid)


#------- this function will randomly pciked the two topics student have to talk about
def ungoals():

    choosen1=['No poverty', 'Zero Hunger', 'Good health and wellbeing', 'Gender quality', 'Clean water and sanitation',
     'Affordable and clean energy', 'Decent work and economic growth', 'Industry innovation and infrastructure', 
     'reduced inequalities', 'Sustainable cities and communities', 'Responsible consumption and production', 'climate action',
     'life below water', 'Life on land', 'Peace justice and strong instituions', 'partnerships for the goals']

    choosen2=['No poverty', 'Zero Hunger', 'Good health and wellbeing', 'Gender quality', 'Clean water and sanitation',
     'Affordable and clean energy', 'Decent work and economic growth', 'Industry innovation and infrastructure', 
     'reduced inequalities', 'Sustainable cities and communities', 'Responsible consumption and production', 'climate action',
     'life below water', 'Life on land', 'Peace justice and strong instituions', 'partnerships for the goals']

    for i in range(1):
        choosen1=random.choice(choosen1)
        choosen2=random.choice(choosen2)
        print("Your choices:")
        print("Choice 1:" + choosen1)
        print("Choice 2:" +choosen2)
        break

ungoals()
