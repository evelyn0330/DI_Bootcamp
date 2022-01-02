from game import Game

def get_user_menu_choice():
    choice = input('''
    Menu:
    (g) Play a new game
    (s) Show scores
    (x) Quit
    Option here: ''')

    while True:
        if choice not in ["g", "s", "x"]:
            print("Sorry but input is invalid.")
        return choice


def print_results(results):
    print("These are the results")
    for key, value in Game.results.items():
       print(f"{key}: {value}")

   


def main():
    menu = get_user_menu_choice
    while True:
       if menu == "x":
          print("Byeeeee! Thanks for playing. Come back again soon!")
       elif menu == "g":
           new_game = Game
           new_game.play()
       elif menu == "s":
          print_results(Game.results)
          

main()
