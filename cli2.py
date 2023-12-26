import random
import click
from card import Card

@click.group()
def cli():
    pass

@cli.command()
@click.argument("value", type=int)
def buy(value):
    serial = random.randint(0, 9999999999)
    card_number = Card.generate_card_number(serial, value)
    click.echo(f"Card Number: {card_number}")

@cli.command()
@click.argument("card_number", type=int)
def value(card_number):
    try:
        Card.validate_card_number(card_number)
    except ValueError as e:
        click.echo(e)
        return

    card_value = Card.check_value(card_number)
    click.echo(f"Card value: {card_value}")

@cli.command()
@click.argument("card_number", type=int)
def redeem(card_number):
    try:
        Card.validate_card_number(card_number)
    except ValueError as e:
        click.echo(e)
        return

    card_value = Card.redeem_card(card_number)
    click.echo(f"Card value: {card_value}")

@cli.command()
@click.argument("card_number", type=int)
def check(card_number):
    try:
        Card.validate_card_number(card_number)
    except ValueError as e:
        click.echo(e)
        return

    card_redeemed = Card.check_redemption(card_number)
    if card_redeemed:
        click.echo("Card has been redeemed.")
    else:
        click.echo("Card has not been redeemed.")




if __name__ == "__main__":
    cli()