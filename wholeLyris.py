# The-Ants-Go-Marching.

number = ["one", "two", "three", "four", "five",
              "six", "seven", "eight", "nine", "ten"]

antAct = ["suck his thumb,", "tie his shoe,", "climb a tree,",
                 "shut the door,", "take a dive,", "pick up sticks,",
                 "talk to Kevin," , "jump the gate,", "swing on a vine,",
                 "say 'The End',"]

def nByN(i):
        return "The ants go marching "+number[i]+" by "+number[i]+", hurrah! hurrah!\n"

def nByN1(i):
        return "The ants go marching "+ number[i]+" by "+number[i]+",\n"
        
def antActive(i):
        return "The little one stops to "+antAct[i]+"\n"

def repeat():
    return "And they all go marching down...\n"+"In the ground...\n"+"To get out...\n"+"Of the rain.\n"+"Boom! Boom! Boom!\n"

def lyris():
    for i in range (10):
        print (nByN(i)*2+nByN1(i)+antActive(i)+repeat())

lyris()
