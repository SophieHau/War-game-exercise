from cards import *

class Game():
	def __init__(self):
		self.deck = Deck()
		self.user_hand = Hand()
		self.computer_hand = Hand()
		self.user_points = 0
		self.computer_points = 0

	def create_hands(self):
		self.deck.shuffle()
		self.draw = input("The deck has been shuffled, write 'd' to draw your hand: ")
		if self.draw == 'd':
			self.user_hand.cards = self.deck.draw(26)
			print("Here's your hand :\n {}".format(self.user_hand.cards))
			self.computer_hand.cards = self.deck.draw(26)

	def play(self):
		user_input = input("write 'p' to play a card: ")
		if user_input == 'p':
			self.user_hand.shuffle()
			self.user_card = self.user_hand.draw(1)
			print("You played the {}".format(self.user_card[0]))
			self.computer_hand.shuffle()
			self.computer_card = self.computer_hand.draw(1)
			print("The computer plays {}".format(self.computer_card[0]))

	def winner(self):
		
		if self.user_card > self.computer_card:
			self.user_points += 1
			print("You win! You have now {} points".format(self.user_points))

		elif self.user_card < self.computer_card:
			self.computer_points += 1
			print("The computer wins! He has now {} points".format(self.computer_points))

		elif self.user_card	== computer_card:
			print("Nobody wins, play again!")

			
g = Game()
g.create_hands()
while len(g.user_hand.cards) > 0:
	g.play()
	g.winner()
if g.user_points > g.computer_points:
	print("Game over. You win with {} points while the computer got only {} points".format(g.user_points, g.computer_points))
elif g.user_points < g.computer_points:
	print("Game over. The computer wins with {} points while you got only {} points".format(g.computer_points, g.user_points))
else:
	print("Its a tie!")


