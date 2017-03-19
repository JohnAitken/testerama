
def main():
    print ('Shall we play a game?')
    settingoff = 'Oasis are shit'
    triggered = False
    while not triggered:
            guess = (input('Say a thing: '))
            if guess == settingoff:
                print('triggered')
                triggered = True
            elif guess == ('Conspiracies!'):
                print ('Nearly... try again')
            else:
                print('Triggered')
main()
