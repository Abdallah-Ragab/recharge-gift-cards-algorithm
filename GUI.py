from card import Card
import customtkinter as ctk

# Set appearance mode
ctk.set_appearance_mode('system')
def redeem_card():
    check_card_error_message.configure(text='')
    card_number = card_number_input.get()
    already_redeemed = Card.check_redemption(card_number)
    if already_redeemed:
        check_card_error_message.configure(text='Card has already been redeemed')
        return
    card_value = Card.redeem_card(card_number)
    check_card()

def check_card():
    check_card_error_message.configure(text='')
    card_number = card_number_input.get()
    try:
        card_serial, card_value = Card.get_card_info(card_number)
    except ValueError as e:
        check_card_error_message.configure(text=str(e))
        return

    redeemed = Card.check_redemption(card_number)
    redeemed_text = 'Redeemed' if redeemed else 'Not Redeemed'

    card_value_text.configure(state='normal')
    card_status_text.configure(state='normal')
    card_value_text.delete('1.0', 'end')
    card_value_text.insert('1.0', card_value)
    card_status_text.delete('1.0', 'end')
    card_status_text.insert('1.0', redeemed_text)
    card_value_text.configure(state='disabled')
    card_status_text.configure(state='disabled')

    card_value_label['text'] = 'Card Value: ' + str(card_value)

def buy_card():
    buy_card_error_message.configure(text='')
    card_value = int(card_value_input.get())
    try:
        Card.validate_card_value(card_value)
    except ValueError as e:
        buy_card_error_message.configure(text=str(e))
        return

    card = Card.generate_card_number(card_value)
    card_number_value.configure(state='normal')
    card_number_value.delete('1.0', 'end')
    card_number_value.insert('1.0', card)
    card_number_value.configure(state='disabled')
    card_value_input.delete(0, 'end')

def create_label(frame, text, font = 'Arial', font_size = 20, row=0, column=0, pady=10, padx=10, text_color=None, wraplength=0):
    label = ctk.CTkLabel(frame, text=text, font=(font, font_size), wraplength=wraplength)
    label.grid(row=row, column=column, pady=pady, padx=padx)
    if text_color:
        label.configure(text_color=text_color)
    return label


def create_entry(frame, placeholder_text, width=140, height=28, row=0, column=0, pady=10, padx=10, font_size=12, font='Arial'):
    entry = ctk.CTkEntry(frame, placeholder_text=placeholder_text, width=width, height=height, font=(font, font_size))
    entry.grid(row=row, column=column, pady=pady, padx=padx)
    return entry

def create_textbox(frame, height, width, state, row=0, column=0, pady=10, font_size=12, font='Arial'):
    textbox = ctk.CTkTextbox(frame, height=height, width=width, state=state, font=(font, font_size))
    textbox.grid(row=row, column=column, pady=pady)
    return textbox

def create_button(frame, text, command, row=0, column=0, pady=10, padx=10, width=140, height=28, font_size=12, font='Arial'):
    button = ctk.CTkButton(frame, text=text, command=command, width=width, height=height, font=(font, font_size))
    button.grid(row=row, column=column, pady=pady, padx=padx)
    return button

# Create the main window
root = ctk.CTk()
root.title('Recharge Cards System')

# Create main frame
main_frame = ctk.CTkFrame(root)
main_frame.pack(fill='both', expand=True)

title_label = create_label(main_frame, 'Recharge Cards System', font_size=40, pady=10)
title_label.grid(row=0, column=0, columnspan=2)

# Create buy card section
buy_card_frame = ctk.CTkFrame(main_frame)
buy_card_frame.grid(row=2, column=0, sticky='nsew', padx=30, pady=20)

buy_card_label = create_label(buy_card_frame, 'Buy Card', font_size=30, pady=20)
buy_card_error_message = create_label(buy_card_frame, '', font_size=12, text_color='red', row=1, wraplength=250)
card_value_input = create_entry(buy_card_frame, 'Card Value', 240, row=2, padx=30,height=35, font_size=16)
buy_card_button = create_button(buy_card_frame, 'Buy Card', buy_card, row=3, width=240, height=40, pady=20, font_size=16)
card_number_label = create_label(buy_card_frame, 'Card Number', row=4, font_size=16, pady=0)
card_number_value = create_textbox(buy_card_frame, 1, 240, 'disabled', row=5)

# Create check and redeem card section
check_card_frame = ctk.CTkFrame(main_frame)
check_card_frame.grid(row=2, column=1, sticky='nsew', padx=30, pady=20)

check_card_label = create_label(check_card_frame, 'Card Info', font_size=30, pady=20)
check_card_error_message = create_label(check_card_frame, '', font_size=12, text_color='red', row=1, wraplength=250)
card_number_input = create_entry(check_card_frame, 'Card Number', 240, row=2, padx=30, height=35, font_size=16)
check_card_button = create_button(check_card_frame, 'Check Card', check_card, row=3, width=240, height=40, pady=20, font_size=16)
card_value_label = create_label(check_card_frame, 'Card Value', row=4,font_size=16, pady=0)
card_value_text = create_textbox(check_card_frame, 1, 260, 'disabled', row=5)
card_status_label = create_label(check_card_frame, 'Card Status:', row=6, font_size=16, pady=0)
card_status_text = create_textbox(check_card_frame, 1, 260, 'disabled', row=7)
redeem_card_button = create_button(check_card_frame, 'Redeem Card', redeem_card, row=8, width=240, padx=30, height=35, font_size=16)


root.mainloop()
