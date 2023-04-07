"""

██╗░░░░░░█████╗░███╗░░░███╗░█████╗░
██║░░░░░██╔══██╗████╗░████║██╔══██╗
██║░░░░░██║░░██║██╔████╔██║███████║
██║░░░░░██║░░██║██║╚██╔╝██║██╔══██║
███████╗╚█████╔╝██║░╚═╝░██║██║░░██║
╚══════╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝

Made by <Muhammed Alkohawaldeh> aka Twister_Froste
copyritgh <Muhammed Alkohawaldeh> <20232-4-1>
"""

import pyautogui as pg
from time import sleep, time
from random import randint, choice 

global num_of_msg

num_of_msg: int = 0
w_start: float = time()
w_end: float = time()

def total():
    """
    Test Function
    """
    
    
    print(f"Total Massages: {num_of_msg}")
    print(f"Total time: {w_end - w_start}")
    

def real_sentence():
    """Real sentence generater"""

    real_sentence_list: list[str] = ["amazing", "I liked the background", "Nice picture, I wish you success", "Wow, amazing picture",
                                     "I see no competitors", "Nice, worke", "I hope that's help", "No Pain, No Gain", "You are the best!",
                                     "Keep trying!", "You can do it!", "I will stay by your side!", "Believe in yourself!", "Dream it! Wish it! Do it!", 
                                     "Be optimistic!", "Do not give up!", "Be patient", "Everything is possible", "Be positive!", "Stop wishing! Start doing!", 
                                     "Follow your heart but do not forget to take your brain with you", "Do not be afraid to fail, just keep trying", "If you change nothing, nothing will change", 
                                     "Think positively", "Do not go back!", "Well done!", "Great job!", "Actions speak louder than words", "Every new day is another chance to change your life", 
                                     "Hard work beats talent when talent doesn't work hard", " It doesn't matter how slowly you go as long as you don't stop", "It wasn't raining when Noah built the ark", 
                                     "Sometimes you win, sometimes you learn", "Mistakes is the proof that you are trying", "Win !!", "I like it", "Good job", "Nice", "@Jaber Mahmoud Yassin", "@Sari Radwan",
                                     "...", "@Fajer Shorbase", "@Karam Alnaimat", "@Hashem Almahermeh", "@Ahmad Gemze", "@eJaber_on_FIRE", "@Rafat Zeaton", "@Omar Maani", "This is what I'm took about",
                                     "....", "The best pic.", "Give me the source", "Loma was here ^_^", "Loma is the best", "Don't try to stop me", "I will not be out of serves", "Like what I excpect",
                                     "This is the truth", "Nothing will change", "Be usefull and put a like ^_^", "This comments is for searching stuff", "Winners !!", "I wil be always there", "Like, comment and share plz.",
                                     "You can't expect me !_!", "I'll be here as long as there's electricity", "I can't be defeated", "I studied it well", "You will lose competitors"]
    
    rand_sentence: str = real_sentence_list[randint(0, len(real_sentence_list) - 1)]
    
    return rand_sentence

def fake_sentence(length):
    """Fake sentence generater"""

    rand_sentence: str = ""

    fake_sentence_list: str = "1234567890-_=+qwertyuiop[]asdfghjkl;'\zxcvbnm,./<`!@#$%^&*()QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?"
    
    for i in range(length):
        
        rand_sentence += choice(fake_sentence_list[randint(0, len(fake_sentence_list) -1)])

    return rand_sentence

def generater(fake_length: int):
    """generate the finally sentence"""

    fake: str = fake_sentence(fake_length)
    real: str = real_sentence()

    mix: list[str] = [fake, real]

    return choice(mix)


def writer(msg_time: int, length: int = 7):
    """
    Main function that write the comments on facebook.
    """
    
    num_of_msg: int = 0
    x = 1

    while True:
        


        try:
            
            start = time()

            sleep(1)

            msg = generater(length)

            if msg[0] == "@":
                
                pg.typewrite(f"{msg}")
                sleep(1)
                pg.typewrite("\n\n")
                sleep(msg_time)
                end = time()

                num_of_msg = num_of_msg + 1
                print(f"Massage Send: {num_of_msg}")
                print(f"Comment per second: {end-start} sec", end="\n\n")

                if num_of_msg == 300 or num_of_msg == 300*x:
                    print(f"Break Time!, After {num_of_msg} Massage")
                    x += 1
                    sleep(502)
            else:

                pg.typewrite(f"{msg}")
                sleep(1)
                pg.typewrite("\n")
                sleep(msg_time)
                end = time()



                num_of_msg = num_of_msg + 1
                print(f"Massage Send: {num_of_msg}")
                print(f"Comment per second: {end-start} sec", end="\n\n")

                if num_of_msg == 300 or num_of_msg == 300*x:
                    print(f"Break Time!, After {num_of_msg} Massage")
                    x += 1
                    sleep(502)

        except Exception as ex:

            total()
            print(f"""Something want wrong !!


            
            Error value: 
                    {ex}""", sep="\n\n")
    

writer(18)

# (3) good -> [613 msg] in {72 min 39 sec}

# (18) Perfect -> [infinity] in [infinity]