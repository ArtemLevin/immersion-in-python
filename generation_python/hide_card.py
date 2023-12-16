card = '905 678123 45612 56'

def hide_card(card):
    return "*"*12+card.replace(' ', '')[-4:]

print(hide_card(card))