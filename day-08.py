alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("type encode or decode :\n").lower()
text=input("type your message:\n").lower()
shift=int(input("type the shift number:\n"))

def encrypt(original_text,shift_amount):
    cipher_text=""
    for letter in original_text:
        shifted_position=alphabet.index(letter)+shift_amount
        shifted_position=shifted_position%len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"here is the encoded result:{cipher_text}")    
        
    
def decrypt(original_text,shift_amount):
    output_text=""
    for letter in original_text:
        shifted_position=alphabet.index(letter)- shift_amount
        shifted_position=shifted_position%len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"here is the encoded result:{output_text}")    
        
        
def caesar(original_text,shift_amount,encode_or_decode):
    output_text=""
    for letter in original_text:
        
        if encode_or_decode=="decode":
            shift_amount*=-1
        
        
        shifted_position=alphabet.index(letter)- shift_amount
        shifted_position=shifted_position%len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"here is the {encode_or_decode} result:{output_text}")    
        

caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)







 