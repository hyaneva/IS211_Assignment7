#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
import argparse

class Die:
    def __init__(self, seed=0):
        random.seed(seed)
    
    def roll(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def add_to_score(self, points):
        self.score += points
    
    def reset_score(self):
        self.score = 0

class Game:
    def __init__(self, num_players=2, target_score=100):
        self.target_score = target_score
        self.die = Die(seed=0)
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.current_player_idx = 0
    
    def switch_turn(self):
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
    
    def play_turn(self):
        player = self.players[self.current_player_idx]
        turn_total = 0
        
        while True:
            roll = self.die.roll()
            print(f"{player.name} rolled: {roll}")
            
            if roll == 1:
                print(f"{player.name} loses this turn's points!")
                break  #End turn without adding points
            
            turn_total += roll
            print(f"{player.name}'s turn total: {turn_total}, Current score: {player.score}")
            
            decision = input("Roll again (r) or hold (h)? ").lower()
            if decision == 'h':
                player.add_to_score(turn_total)
                break
        
        print(f"{player.name}'s total score: {player.score}\n")
        self.switch_turn()
    
    def play_game(self):
        print("Welcome to Pig!")
        while all(player.score < self.target_score for player in self.players):
            self.play_turn()
        
        winner = max(self.players, key=lambda p: p.score)
        print(f"{winner.name} wins with {winner.score} points!")
    
    def reset_game(self):
        for player in self.players:
            player.reset_score()
        self.current_player_idx = 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--numPlayers", type=int, default=2, help="Number of players in the game")
    args = parser.parse_args()
    
    while True:
        game = Game(num_players=args.numPlayers)
        game.play_game()
        
        replay = input("Play again? (y/n): ").lower()
        if replay != 'y':
            break
        game.reset_game()


# In[ ]:




