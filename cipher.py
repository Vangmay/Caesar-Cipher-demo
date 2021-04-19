msg_index = []
Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shift = int(input("Enter the number for shift-size"))
Cipher = Alphabet[shift:] + Alphabet[:shift]
message = str(input("What message do you want to decode "))
def split(message):
    return [char for char in message]
message_split = split(message)
#taking character from split message and switching it to the cipher
for i in range(0,len(message_split)):
    if message_split[i] in Alphabet:
        msg_index.append(Alphabet.index(message_split[i]))
new_message = ''
for i in range(0,len(msg_index)):
    new_message += Cipher[msg_index[i]]
print('Decrypted: '+ message)
print('Encrypted: '+ new_message)
print('Key: ' + str(Cipher))
