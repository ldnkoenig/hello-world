sAlphabet = 'abcdefghijklmnopqrstuvwxyz'
key = -3
sMessage = input('Enter message: ')
sNewMessage = ''
for sCharacter in sMessage:
	position = sAlphabet.find(sCharacter)
	newPosition = (position + key)%26
	sNewMessage += sAlphabet[newPosition]

print (sNewMessage)