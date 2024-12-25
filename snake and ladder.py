import random

class SnakesAndLadders:
    def __init__(self, size=10, snakes=None, ladders=None, players=2):
        self.size = size
        self.board = [0] * (size * size + 1)
        self.snakes = snakes if snakes else {}
        self.ladders = ladders if ladders else {}
        self.players = ['Player ' + str(i + 1) for i in range(players)]
        self.positions = {player: 0 for player in self.players}
        self.winner = None

    def setup_board(self):
        for start, end in self.snakes.items():
            self.board[start] = end
        for start, end in self.ladders.items():
            self.board[start] = end

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player):
        if self.winner:
            return

        dice_roll = self.roll_dice()
        print(f"{player} rolled a {dice_roll}")
        current_position = self.positions[player]
        new_position = current_position + dice_roll

        if new_position > self.size * self.size:
            print(f"{player} can't move, roll exceeds board size.")
            return

        # Check for snakes or ladders
        if new_position in self.snakes:
            print(f"{player} stepped on a snake! Sliding down from {new_position} to {self.snakes[new_position]}.")
            new_position = self.snakes[new_position]
        elif new_position in self.ladders:
            print(f"{player} climbed a ladder! Moving up from {new_position} to {self.ladders[new_position]}.")
            new_position = self.ladders[new_position]

        # Check for win
        if new_position == self.size * self.size:
            self.winner = player
            print(f"🎉 {player} reaches 100 and wins the game!")
        else:
            print(f"{player} moves to {new_position}")

        self.positions[player] = new_position

    def play_turn(self):
        for player in self.players:
            if self.winner:
                break
            input(f"{player}'s turn! Press Enter to roll the dice...")
            self.move_player(player)
            print()

    def play_game(self):
        print("Welcome to Snakes and Ladders!")
        print(f"Board size: {self.size}x{self.size}")
        print(f"Players: {', '.join(self.players)}")
        print("Game begins!")
        print()

        while not self.winner:
            self.play_turn()

if __name__ == "__main__":
    snakes = {
        14: 7,
        31: 26,
        78: 39,
        99: 1
    }
    ladders = {
        3: 22,
        8: 30,
        28: 84,
        58: 77
    }
    game = SnakesAndLadders(snakes=snakes, ladders=ladders)
    game.setup_board()
    game.play_game()
