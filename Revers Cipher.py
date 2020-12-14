# Revers Cipher

message = input('What is your message?')

translated = ''

i = len(message) - 1

while i >= 0:
        translated = translated + message[i]
        i = i -1

print(translated)

print()
answer = input('Do you want to reverse it? [y/n]')

translated2 = ''

i = len(translated) - 1

if answer == 'y':
    while i >= 0:
        translated2 = translated2 + translated[i]
        i = i -1

print(translated2)