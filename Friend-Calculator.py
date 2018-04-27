sName1 = ''
sName2 = ''
vowels = 'aeiou'

sName1 = input ("First name: ")
sName2 = input ("Second name: ")

iName1 = 0
iName2 = 0

for sCharacter in sName1:
	if vowels.find(sCharacter) >= 0:
		iName1 += 10

for sCharacter in sName2:
	if vowels.find(sCharacter) >= 0:
		iName2 += 10

print ("Friend score: ", iName1+iName2)