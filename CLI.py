import cmd
import random
from card import Card

class CLI(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = ">> "
        self.intro = "Welcome to the card machine!"
    def do_value(self, arg):
        """Check the value of a card."""
        card_number = int(arg)
        try:
            Card.validate_card_number(card_number)
        except ValueError as e:
            print(e)
            return

        card_value = Card.check_value(card_number)
        print(f"Card value: {card_value}")

    def do_redeem(self, arg):
        """Redeem a card."""
        card_number = int(arg)
        try:
            Card.validate_card_number(card_number)
        except ValueError as e:
            print(e)
            return

        card_value = Card.redeem_card(card_number)
        print(f"Card value: {card_value}")

    def do_check(self, arg):
        """Check if a card has been redeemed."""
        card_number = int(arg)
        try:
            Card.validate_card_number(card_number)
        except ValueError as e:
            print(e)
            return

        card_redeemed = Card.check_redemption(card_number)
        if card_redeemed:
            print("Card has been redeemed.")
        else:
            print("Card has not been redeemed.")


    def do_buy(self, arg):
        """Buy a card."""
        card_serial = random.randint(0, 9_999_999_999) # random number between 0 and 9999999999
        card_value = int(arg)
        try:
            Card.validate_card_value(card_value)
        except ValueError as e:
            print(e)
            return

        card_number = Card.generate_card_number(card_serial, card_value)
        print(f"Card number: {card_number}")

    def do_exit(self, arg):
        """Exit the program."""
        print("Exiting...")
        return True

if __name__ == "__main__":
    CLI().cmdloop()