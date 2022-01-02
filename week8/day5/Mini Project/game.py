import random

class Game:
    results = {"win": 0, "loss": 0, "draw": 0}
    
    def get_user_item(self):
        item = input("Please pick your weapon = rock, paper, scissors: ")
        while True:
            if item not in ["rock", "paper", "scissors"]:
                input("Sorry but input is invalid, try again.")
            else:
                return item


    def get_computer_item(self):
        computer_item = random.choice(self.options)
        return computer_item


    def get_game_result(self,user_item, computer_item):
        if user_item == "rock" and computer_item == "rock":
            return "draw"
        if user_item == "rock" and computer_item == "paper":
            return "loss"
        if user_item == "rock" and computer_item == "scissors":
            return "win"

        if user_item == "paper" and computer_item == "paper":
            return "draw"
        if user_item == "paper" and computer_item == "rock":
            return "win"
        if user_item == "paper" and computer_item == "scissors":
            return "loss"

        if user_item == "scissors" and computer_item == "scissors":
            return "draw"
        if user_item == "scissors" and computer_item == "paper":
            return "win"
        if user_item == "scissors" and computer_item == "rock":
            return "loss"

 
    def play(self):
        user_item = self.get_user_item
        computer_item = self.get_computer_item
        print(f"You picked {user_item}. The computer picked {computer_item}.")
        if self.get_game_result(user_item, computer_item) == "draw":
            self.results["draw"] += 1
            print("It's a draw!")
        elif self.get_game_result(user_item, computer_item) == "win":
            self.results["win"] += 1
            print("You win!")
        elif self.get_game_result(user_item, computer_item) == "loss":
            self.results["loss"] += 1
            print("You lose!")
