#from graphics import graphics
def hat(type):
    print("       ~-~ ")
    print("     /-~-~-\ ")
    if type =="left":
        print(" ___/_______\ ")
    elif type =="right":
        print("    /_______\___")
    elif type == "both":
        print(" ___/_______\___ ")
    elif type =="front":
        print("    /_______\ ")
def head(length, eyes):
    if length == "True":
        print('   "|"""""""|" ')
        print('   "| '+str(eyes)+'   ' + str(eyes) + ' |"')
        print('   "|   V   |"')
        print('   "|  ~~~  |"')
        print('   " \_____/ "')
    elif length =="False":
        print("    |'''''''|")
        print("    | "+str(eyes)+"   "+str(eyes)+" |")
        print("    |   V   |")
        print("    |  ~~~  |")
        print("     \_____/")
def arms (character):
    print("  0"+str(character)*3 +"|---|" + str(character)*3 + "0")
def torso (length):
    i = 0
    while i < length:
        print("      |-X-|")
        i+=1
def legs(length):
    i = 0
    e = 5
    u = 1
    print("      HHHHH")
    while i < length:
        print(" " * e + "///" + " " * u + "\\\\\\ ")
        i+=1
        e-=1
        u+=2
def feet(foot):
    print(str(foot) + "       " + str(foot))
print("----- AVATAR -----")
avatar=""
#obj = graphics(700,300, 'Three Squares')
while not(avatar=="exit") and not(avatar=="custom") and not(avatar=="Jeff") and not(avatar=="Jane") and not(avatar=="Chris"):
    avatar = str(input("Select an Avatar or create your own:\n"))
if avatar == "Jeff":
    hat("both")
    head("False","0")
    print("      |-X-|")
    arms("=")
    torso(4)
    legs(2)
    feet("#HHH#")
elif avatar == "Jane":
    hat("right")
    head("True", "*")
    arms("T")
    torso(2)
    legs(3)
    feet("<|||>")
elif avatar == "Chris":
    hat("front")
    head("False", "U")
    print("      |-X-|")
    arms("W")
    torso(2)
    legs(4)
    feet("<>-<>")
elif avatar == "exit":
    exit()
elif avatar == "custom":
    print("Answer the following questions to create a custom avatar")
    hat_style=str(input("Hat style ?\n"))
    eye = str(input("Character for eyes ?\n"))
    hair = str(input("Long hair (True/False) ?\n"))
    arm_character = str(input("Arm style ?\n"))
    torso_height = int(input("Torso length ?\n"))
    legs_height = int(input("Leg length (1-4) ?\n"))
    shoe = str(input("Shoe look ?\n\n"))
    hat(hat_style)
    head(hair, eye)
    arms(arm_character)
    torso(torso_height)
    legs(legs_height)
    feet(shoe)
