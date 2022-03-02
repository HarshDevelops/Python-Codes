import random


logo = ''' 
    _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                    |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(logo)
print()
print()

word_list = [
    'abruptly', 
    'absurd', 
    'abyss', 
    'affix', 
    'askew', 
    'avenue', 
    'awkward', 
    'axiom', 
    'azure', 
    'bagpipes', 
    'bandwagon', 
    'banjo', 
    'bayou', 
    'beekeeper', 
    'bikini', 
    'blitz', 
    'blizzard', 
    'boggle', 
    'bookworm', 
    'boxcar', 
    'boxful', 
    'buckaroo', 
    'buffalo', 
    'buffoon', 
    'buxom', 
    'buzzard', 
    'buzzing', 
    'buzzwords', 
    'caliph', 
    'cobweb', 
    'cockiness', 
    'croquet', 
    'crypt', 
    'curacao', 
    'cycle', 
    'daiquiri', 
    'dirndl', 
    'disavow', 
    'dizzying', 
    'duplex', 
    'dwarves', 
    'embezzle', 
    'equip', 
    'espionage', 
    'euouae', 
    'exodus', 
    'faking', 
    'fishhook', 
    'fixable', 
    'fjord', 
    'flapjack', 
    'flopping', 
    'fluffiness', 
    'flyby', 
    'foxglove', 
    'frazzled', 
    'frizzled', 
    'fuchsia', 
    'funny', 
    'gabby', 
    'galaxy', 
    'galvanize', 
    'gazebo', 
    'giaour', 
    'gizmo', 
    'glowworm', 
    'glyph', 
    'gnarly', 
    'gnostic', 
    'gossip', 
    'grogginess', 
    'haiku', 
    'haphazard', 
    'hyphen', 
    'iatrogenic', 
    'icebox', 
    'injury', 
    'ivory', 
    'ivy', 
    'jackpot', 
    'jaundice', 
    'jawbreaker', 
    'jaywalk', 
    'jazziest', 
    'jazzy', 
    'jelly', 
    'jigsaw', 
    'jinx', 
    'jiujitsu', 
    'jockey', 
    'jogging', 
    'joking', 
    'jovial', 
    'joyful', 
    'juicy', 
    'jukebox', 
    'jumbo', 
    'kayak', 
    'kazoo', 
    'keyhole', 
    'khaki', 
    'kilobyte', 
    'kiosk', 
    'kitsch', 
    'kiwifruit', 
    'klutz', 
    'knapsack', 
    'larynx', 
    'lengths', 
    'lucky', 
    'luxury', 
    'lymph', 
    'marquis', 
    'matrix', 
    'megahertz', 
    'microwave', 
    'mnemonic', 
    'mystify', 
    'naphtha', 
    'nightclub', 
    'nowadays', 
    'numbskull', 
    'nymph', 
    'onyx', 
    'ovary', 
    'oxidize', 
    'oxygen', 
    'pajama', 
    'peekaboo', 
    'phlegm', 
    'pixel', 
    'pizazz', 
    'pneumonia', 
    'polka', 
    'pshaw', 
    'psyche', 
    'puppy', 
    'puzzling', 
    'quartz', 
    'queue', 
    'quips', 
    'quixotic', 
    'quiz', 
    'quizzes', 
    'quorum', 
    'razzmatazz', 
    'rhubarb', 
    'rhythm', 
    'rickshaw', 
    'schnapps', 
    'scratch', 
    'shiv', 
    'snazzy', 
    'sphinx', 
    'spritz', 
    'squawk', 
    'staff', 
    'strength', 
    'strengths', 
    'stretch', 
    'stronghold', 
    'stymied', 
    'subway', 
    'swivel', 
    'syndrome', 
    'thriftless', 
    'thumbscrew', 
    'topaz', 
    'transcript', 
    'transgress', 
    'transplant', 
    'triphthong', 
    'twelfth', 
    'twelfths', 
    'unknown', 
    'unworthy', 
    'unzip', 
    'uptown', 
    'vaporize', 
    'vixen', 
    'vodka', 
    'voodoo', 
    'vortex', 
    'voyeurism', 
    'walkway', 
    'waltz', 
    'wave', 
    'wavy', 
    'waxy', 
    'wellspring', 
    'wheezy', 
    'whiskey', 
    'whizzing', 
    'whomever', 
    'wimpy', 
    'witchcraft', 
    'wizard', 
    'woozy', 
    'wristwatch', 
    'wyvern', 
    'xylophone', 
    'yachtsman', 
    'yippee', 
    'yoked', 
    'youthful', 
    'yummy', 
    'zephyr', 
    'zigzag', 
    'zigzagging', 
    'zilch', 
    'zipper', 
    'zodiac', 
    'zombie', 
    ]

chosen_word = random.choice(word_list)
def func():
    blank = ["_"]*len(chosen_word)
    lives = 6
    out=False
    check=""    
    while(blank.count("_") > 0 and out==False ):
        print()
        print(f"---------------------LIVES: {lives}---------------------")
        print()
        guess = input("Enter a letter: ").lower()
        if(len(guess)>1):
            print("Enter Only One Letter!")
            func()
        else:
            if(guess in chosen_word and check.count(guess)>=1):
                print("You Have Already Guessed This Letter!")
                print(blank)
            else:
                for i in range(0, len(guess)):
                    flag = False
                    for j in range(0, len(chosen_word)):
                        if(guess[i] == chosen_word[j]):
                            blank[j] = chosen_word[j]
                            flag = True
                            check+=guess[i]
                        else:
                            continue
                    print(blank)

                    if(flag == False):
                        print("No Match")
                        print(stages[lives])
                        lives -= 1
                        print()
                        if(lives<0):
                            print("---------------------You LOSE!---------------------")
                            print(f"-----------The Correct Word Was: {chosen_word}----------------")
                            out=True
    else:
        if(blank.count("_")==0 and out==False):
            print("---------------------You WON!---------------------")

func()