import customtkinter
from tkinter import messagebox
import re

customtkinter.set_appearance_mode("system")

GogoRoot = customtkinter.CTk()
GogoRoot.geometry("500x600")
GogoRoot.title("Gogo Encoder and Decoder")

# Encoder function
def encode_utf8(input_thing):
    utf8_bytes = input_thing.encode('utf-8')
    utf8_thing = ''.join(f"\\{oct(byte)[2:].zfill(3)}" for byte in utf8_bytes)
    return utf8_thing

def encode_hex(input_thing):
    utf8_bytes = input_thing.encode('utf-8')
    hex_thing = ' '.join(f"{byte:02X}" for byte in utf8_bytes)
    return hex_thing

# Decoder function
def decode_utf8(utf8):
    bytes_thing = re.sub(r'\\(\d{3})', lambda x: chr(int(x.group(1), 8)), utf8)
    return bytes_thing.encode('latin1')

def decode_hex(hex):
    hex_thing = hex.replace(" ", "")
    return bytes.fromhex(hex_thing)

def decode_thing(input_thing):
    try:
        if re.match(r'\\\d{3}', input_thing):
            byte_thing = decode_utf8(input_thing)
        else:
            byte_thing = decode_hex(input_thing)
        return byte_thing.decode('utf-8')
    except Exception as e:
        return f"Error in decoding: {e}"

# Encoder pop up
def Encoder():
    input_text = prompt1.get()
    if input_text:
        utf8_encoded = encode_utf8(input_text)
        hex_encoded = encode_hex(input_text)
        result = f"UTF-8 Encoded: {utf8_encoded}\nHex Encoded: {hex_encoded}"
        GogoRoot.clipboard_clear()
        GogoRoot.clipboard_append(f"{utf8_encoded} {hex_encoded}")
        GogoRoot.update()
        messagebox.showinfo("Encoded string", result)

# Decoder pop up
def Decoder():
    input_text = prompt2.get()
    if input_text:
        decoded_text = decode_thing(input_text)
        GogoRoot.clipboard_clear()
        GogoRoot.clipboard_append(decoded_text)
        GogoRoot.update()
        messagebox.showinfo("Decoded string", decoded_text)

main_title = customtkinter.CTkLabel(master=GogoRoot, text="Gogo Encoder and Decoder", font=("NotoSans", 28, "bold"))
main_title.pack(pady=20)

# Encoder frame
FrameEncoder = customtkinter.CTkFrame(master=GogoRoot, border_width=2)
FrameEncoder.pack(pady=10, padx=20, fill="both", expand=True)

sub_title1 = customtkinter.CTkLabel(master=FrameEncoder, text="Gogo Encoder", font=("NotoSans", 20))
sub_title1.pack(pady=12, padx=10)

prompt1 = customtkinter.CTkEntry(master=FrameEncoder, placeholder_text="test")
prompt1.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=FrameEncoder, text="Encode", command=Encoder)
button1.pack(pady=12, padx=10)

# Decoder frame
FrameDecoder = customtkinter.CTkFrame(master=GogoRoot, border_width=2)
FrameDecoder.pack(pady=10, padx=20, fill="both", expand=True)

sub_title2 = customtkinter.CTkLabel(master=FrameDecoder, text="Gogo Decoder", font=("NotoSans", 20))
sub_title2.pack(pady=12, padx=10)

prompt2 = customtkinter.CTkEntry(master=FrameDecoder, placeholder_text="74 65 73 74")
prompt2.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=FrameDecoder, text="Decode", command=Decoder)
button2.pack(pady=12, padx=10)

GogoRoot.mainloop()
