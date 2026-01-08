import random

def get_player_choice(choices):
	prompt = "Enter your choice (rock/paper/scissors or 0=rock,1=scissors,2=paper): "
	while True:
		try:
			s = input(prompt).strip().lower()
		except (EOFError, KeyboardInterrupt):
			print("\nExiting.")
			return None
		if s == "":
			print("Please enter a choice.")
			continue
		if s in ("0", "1", "2"):
			return int(s)
		if s in choices:
			return choices.index(s)
		# single-letter shortcuts: r, p, s
		if s[0] in ("r", "p", "s"):
			if s[0] == 'r':
				return 0
			if s[0] == 's':
				return 1
			if s[0] == 'p':
				return 2
		# common variation
		if s.startswith("scissor"):
			return 1
		print("Invalid choice: '{}' . Try again.".format(s))


def main():
	# 0=rock, 1=scissors, 2=paper
	choices = ["rock", "scissors", "paper"]
	player_wins = [(0, 1), (1, 2), (2, 0)]
	print("Welcome to Rock-Paper-Scissors!")
	while True:
		player = get_player_choice(choices)
		if player is None:
			break
		computer = random.randint(0, 2)
		print("Your choice: {} ({})".format(player, choices[player]))
		print("Computer choice: {} ({})".format(computer, choices[computer]))

		if player == computer:
			print("Result: Draw")
		elif (player, computer) in player_wins:
			print("Result: You win!")
		else:
			print("Result: You lose.")

		try:
			again = input("Play again? [y/N]: ").strip().lower()
		except (EOFError, KeyboardInterrupt):
			print("\nGoodbye.")
			break
		if again not in ("y", "yes"):
			print("Thanks for playing!")
			break


if __name__ == "__main__":
	main()

