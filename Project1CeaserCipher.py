import tkinter as tk
from tkinter import messagebox

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text

def handle_cipher():
    direction = direction_var.get()
    text = text_entry.get().lower()
    shift = int(shift_entry.get()) % 26
    result = ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
    messagebox.showinfo("Result", f"{direction.capitalize()}d text is: {result}")

# Create the GUI
window = tk.Tk()
window.title("Caesar Cipher")

# Set background color to black and text color to green
window.configure(bg="black")

tk.Label(window, text="Ceaser Cipher", fg="green", bg="black", font=("Courier", 20)).grid(row=0, column=0, columnspan=3, pady=10)

direction_var = tk.StringVar()
direction_var.set("encode")

label_direction = tk.Label(window, text="Choose operation:", fg="green", bg="black", font=("Courier", 12))
label_direction.grid(row=1, column=0, pady=5)

encode_radio = tk.Radiobutton(window, text="Encode", variable=direction_var, value="encode", fg="green", bg="black", font=("Courier", 12))
encode_radio.grid(row=1, column=1, pady=5)

decode_radio = tk.Radiobutton(window, text="Decode", variable=direction_var, value="decode", fg="green", bg="black", font=("Courier", 12))
decode_radio.grid(row=1, column=2, pady=5)

label_text = tk.Label(window, text="Enter your message:", fg="green", bg="black", font=("Courier", 12))
label_text.grid(row=2, column=0, pady=5)

text_entry = tk.Entry(window, bg="gray", fg="green", font=("Courier", 12))
text_entry.grid(row=2, column=1, columnspan=2, pady=5)

label_shift = tk.Label(window, text="Enter the shift number:", fg="green", bg="black", font=("Courier", 12))
label_shift.grid(row=3, column=0, pady=5)

shift_entry = tk.Entry(window, bg="gray", fg="green", font=("Courier", 12))
shift_entry.grid(row=3, column=1, columnspan=2, pady=5)

encrypt_button = tk.Button(window, text="Encrypt/Decrypt", command=handle_cipher, fg="black", bg="green", font=("Courier", 12))
encrypt_button.grid(row=4, column=1, pady=10)

window.mainloop()
