import random

class Player:
    
    def __init__(self, name):
       
        self.name = name
        self.points = 300
        

    def choose_if_hi_lo(self):
        
        while True:
            option = input("Will the next card be higher or lower? [h/l]: ")
            if option.lower() == "h" or option.lower() == "l":
                break
            else:
                print("Please type select a right option!\n")
        return option
        

    def able_to_play(self):
            
            if self.points > 0:
                return True
            else:
                return False

class Director:
   

    def __init__(self):
       
        self.keep_playing = True
        self.player = Player("Hey")
        self.one_card = 0
        self.what_you_deserve = 0
        
        

    def start_game(self):
       
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            
    def get_a_card(self):
       
        self.one_card = random.randint(1,13)


    def can_play(self):
           
            if self.player.able_to_play():
                return True
            else:
                return False


    def get_inputs(self):
        
        
        if self.one_card < 1:
            self.get_a_card()
        
        
        previous_card = self.one_card
        print(f'\nThe previous card was: {previous_card}')
        answer = self.player.choose_if_hi_lo()
        self.get_a_card()
        current_card = self.one_card
        print(f'The next card is: {current_card}')

        if (answer == "h") and (current_card > previous_card):
            self.what_you_deserve = 100
        elif (answer == "l") and (current_card < previous_card):
            self.what_you_deserve = 100
        else:
            self.what_you_deserve = -75


    def do_updates(self):
        
        self.player.points += self.what_you_deserve


    def do_outputs(self):
       
        if self.player.points < 0:
            self.player.points = 0

        print(f'Your score : {self.player.points}')

        
        if self.can_play():
            while True:
                choice = input(f"'{self.player.name}',  you want to continue? [y/n] ")
                if choice.lower() == "y":
                    print('\n')
                    self.keep_playing = True
                    break
                elif choice.lower() == "n":
                    print(f'\nGame Over!!')
                    self.keep_playing = False     
                    break
                else:
                    print(f'Please select a right option!')
        else:
            print('\nGame Over. But thank you for playing, please try again!')
            self.keep_playing = False