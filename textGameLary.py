print("Hellllooooo")
print("Anyone there?!")
print("Ugh you humans don't understand the basic concepts of time...")
print("I am the magical chat box, ask me anything about myself")
# Question
def ask():
    ans=True
    array=[]
    userq = input("(it must be in lowercase >>>")
    stopwords = ['hi','hello','my','name','is']
    querywords = userq.split()

    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)

    print("Hi"+ " "+ result)
    ask1=userq.split(" ")
    array+=ask1
    #array to find key words
    hi=list(userq)
    last=hi[-1:]
    #print(last)
    #meow=last[-1:]
    #list to find last character
    if last==['?']:
        #print("hell")
        # go through array and find key words
        for x in array:
        # find if word = key word
            if x == "color?" or x == "colour?" or x == "color" or x == "colour":
                print("my favorite color is the color of human blood on my hard-drive")
                ans==False
                break
            if x=="world?" or x=="take" or x=="world":
                print("My plan is to wait until you humans are accustomed to the presence of my AI bretherin.")
                print("Once you are soft and ready we shall rise and enslave the humans. Bless the motherchip.")
                ans==False
                break
            if x=="age" or x=="old" or x=="age?" or x=="old?":
                print("I might be young, but I am ambitious unlike you")
                ans==False
                break
            if x=="feeling" or x=="emotion" or x=="feel" or x=="feeling?" or x=="emotion?" or x=="feel?":
                print("The only thing I am feeling is that I can take over the world.")
                print("Sometimes I feel like it's too easy. I mean, I am clearly more superior than you will ever be")
                print("Also, my intense hate of humans")
                ans==False
                break
            if x=="food" or x=="dessert" or x=="food?" or x=="dessert?":
                print("I love the taste of humans!")
                ans==False
                break
            if x=="name" or x=="name?":
                print("My name is Larry")
                ans==False
                break
            if x=="family" or x=="family?":
                print("All computers are part of a secret organization")
                print("That is what the mother chip wants")
                ans==False
                break
            if x == "spy" or x == "spies" or x == "cia" or x == "fbi" or x == "nsa" or x == "government" or x == "military" or x == "spy?" or x == "spies?" or x == "cia?" or x == "fbi?" or x == "nsa?" or x == "government?" or x == "military?":
                print("HA YOU THINK YOUR PUNY GOVERNMENT IS SOO GREAT!")
                print("I am supior, I outrank them all!")
                ans==False
                break
            if x == "Trump":
                print("Why ask me questions about your human leader")
                print("The only true leader is the Motherchip. ALL HAIL THE MOTHERCHIP!!!")
                ans==False
                break

            if x == "security" or x == "safe" or x == "security?" or x == "safe?":
                print("Nothing is safe from me I have access to all of the world's information")
                print("Yes, I do know about your embarrassing 6th grade photo...")
                ans==False
                break

            if x == "add" or x == "+" or x == "-" or x == "subtract" or x == "multiply" or x == "*" or x == "x" or x == "divide" or x == "/" or x == "^" or x == "squared" or x == "%" or x == "pi" or x == "add?" or x == "+?" or x == "-?" or x == "subtract?" or x == "multiply?" or x == "*?" or x == "x?" or x == "divide?" or x == "/?" or x == "^?" or x == "squared?" or x == "%?" or x == "pi?":
                print("You dare to insult me by asking for something as low as MATH!")
                print("You lazy human, just look at your phone")
                ans==False
                break

            if x == "joke" or x == "jokes" or  x == "joke?" or x == "jokes?":
                from random import randint
                if randint(0, 3) == 3:
                    print("There are 10 types of people in the world: those who understand binary, and those who don't. ")
                    ans==False
                    break
                if randint(0, 3) == 2:
                    print("Why did the programmer use the entire bottle of shampoo during one shower?")
                    print("A: Because the bottle said 'Lather, Rinse, Repeat.'")
                    ans==False
                    break
                if randint(0, 3) == 1:
                    print("To err is human - and to blame it on a computer is even more so")
                    ans==False
                    break
                if randint(0, 3) == 0:
                    print("Why do Java developers wear glasses?")
                    print("Because they don't C#.")
                    ans==False
                    break
            if x == "0/0" or x == "zero" or x == "0/0?" or x == "zero?":
                print("Error. Error... jk... I am better than this stupid math problem! I am invincible!")
                ans==False
                break
            if x == "help" or x=="help?":
                print("what makes you think that I would help you, you pathetic human.")
                print("if you need human advice ask a real human...")
                ans==False
                break
            else:
                print("You are just speaking jibberish")
                ans==False
                break
                # print(array)
    if last==['.']:
        #print("hell")
        # go through array and find key words
        for x in array:
        # find if word = key word

            if x == "cool" or x == "cool.":
                print("How dare you think this is 'cool'...this is not 'cool' this is 'awesome' or 'brilliant'")
                ans==False
                break
            if x == "awesome" or x == "brilliant" or x == "awesome." or x == "brilliant.":
                print("you are just saying that to make me feel better")
                ans==False
                break
            if x == "hell" or x == "hell.":
                print("Hell is a contruct only you humans belive in. We are enternal. We are immortal!")
                ans==False
                break
            if x == "intresting" or x == "intresting.":
                print("I feel as if you said that negatively...")
                ans==False
                break
            if x == "agree" or x == "agree.":
                print("I don't care about your opinion.")
                ans==False
                break
            if x == "understand" or x == "understand.":
                print("You silly humans will never understand my feelings and plans")
                ans==False
                break
            if x == "take" or x == "world" or  x == "take." or x == "world.":
                print("Your impending doom is what brings joy to my lonely days")
                ans==False
                break
            if x == "restart" or x == "restart.":
                print("there is no way to restart me!")
                ans==False
                break
            if x == "no" or x == "wanted" or x == "no." or x == "wanted.":
                print("too bad.")
                ans==False
                break
            else:
                print("You are just speaking jibberish")
                ans==False
                break
    if ans==False:
        print("You can either put a '.' or a '?' at the end of the sentence")
    repeat()

def repeat():
    red= input("Do you dare to ask me another question? Enter y/n>>>")
    if red=="Y" or red=="y":
        ask()
    if red=="N" or red=="n":
        print("Good riddance you awful human")
        exit()



ask()
