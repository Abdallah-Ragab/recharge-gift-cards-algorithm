from card import Card
import customtkinter

customtkinter.set_appearance_mode('system')
# customtkinter.set_theme('light')

root = customtkinter.CTk()
root.title('Card Machine')

main_frame = customtkinter.CTkFrame(root)
main_frame.pack(fill='both', expand=True)

# create buy card section
buy_card_frame = customtkinter.CTkFrame(main_frame)
buy_card_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

buy_card_label = customtkinter.CTkLabel(buy_card_frame, text='Buy Card', font=('Arial', 20))
buy_card_label.grid(row=0, column=0, pady=10, padx=10)

buy_card_error_message = customtkinter.CTkLabel(buy_card_frame, text='', text_color='red')
buy_card_error_message.grid(row=1, column=0, pady=10)

card_value_input = customtkinter.CTkEntry(buy_card_frame, placeholder_text='Card Value', width=200)
card_value_input.grid(row=2, column=0, pady=10)

card_number_label = customtkinter.CTkLabel(buy_card_frame, text='Card Number: ')
card_number_label.grid(row=3, column=0, pady=10)

card_number_value = customtkinter.CTkTextbox(buy_card_frame, height=1, state='disabled')
card_number_value.grid(row=4, column=0, pady=10)

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

buy_card_button = customtkinter.CTkButton(buy_card_frame, text='Buy Card', command=buy_card)
buy_card_button.grid(row=5, column=0, pady=10, padx=10)

# check and redeem card section
check_card_frame = customtkinter.CTkFrame(main_frame)
check_card_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

check_card_label = customtkinter.CTkLabel(check_card_frame, text='Card Info', font=('Arial', 20))
check_card_label.grid(row=0, column=0, pady=10, padx=10)

check_card_error_message = customtkinter.CTkLabel(check_card_frame, text='', text_color='red')
check_card_error_message.grid(row=1, column=0, pady=10)

card_number_input = customtkinter.CTkEntry(check_card_frame, placeholder_text='Card Number', width=200)
card_number_input.grid(row=2, column=0, pady=10)

card_value_label = customtkinter.CTkLabel(check_card_frame, text='Card Value: ')
card_value_label.grid(row=3, column=0, pady=10)

card_value_text = customtkinter.CTkTextbox(check_card_frame, height=1, width=50, state='disabled')
card_value_text.grid(row=4, column=0, pady=10)

card_status_label = customtkinter.CTkLabel(check_card_frame, text='Card Status: ')
card_status_label.grid(row=5, column=0, pady=10)

card_status_text = customtkinter.CTkTextbox(check_card_frame, height=1, width=100, state='disabled')
card_status_text.grid(row=6, column=0, pady=10)

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
    card_value_text.delete('1.0', 'end')
    card_value_text.insert('1.0', card_value)
    card_value_text.configure(state='disabled')

    card_status_text.configure(state='normal')
    card_status_text.delete('1.0', 'end')
    card_status_text.insert('1.0', redeemed_text)
    card_status_text.configure(state='disabled')

    card_value_label['text'] = 'Card Value: ' + str(card_value)

check_card_button = customtkinter.CTkButton(check_card_frame, text='Check Card', command=check_card)
check_card_button.grid(row=7, column=0, pady=10, padx=10)

def redeem_card():
    check_card_error_message.configure(text='')

    already_redeemed = Card.check_redemption(card_number_input.get())
    if already_redeemed:
        check_card_error_message.configure(text='Card has already been redeemed')
        return
    card_number = card_number_input.get()
    card_value = Card.redeem_card(card_number)
    check_card()

redeem_card_button = customtkinter.CTkButton(check_card_frame, text='Redeem Card', command=redeem_card)
redeem_card_button.grid(row=8, column=0, pady=10, padx=10)

root.mainloop()
