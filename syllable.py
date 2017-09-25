#natural language processing update
def syllabify(word):
	syllables = []
	vowels = 'aeiouy'
	words = word.lower().strip('.:?!').split(" ")
	for i in range(0, len(words)):
    		tmp = []
     		word = words[i]								# isolate word
		track = 0
		if word[0] not in vowels:						#check if first letter isn't a vowel, this requires special case
			for j in range (len(word)):
				if word[j] in vowels:
					for k in range(j+1, len(word)):			#takes first syllable to be first vowel and all surrounding consonants
						if word[k] in vowels:
							track = k
							tmp.append(word[:k])
							break
						elif (k == len(word) - 1) and tmp == []:		#in case word is monosyllabic and has only one vowel
							tmp.append(word)
							pass
			for j in range(track, len(word)):
				if word[j] in vowels:
					for k in range(j+1, len(word)):
						if word[k] in vowels:
							tmp.append(word[track : k])
							track = k
							break
						elif k == len(word) - 1:
							tmp.append(word[track:])
							pass


		syllables.append(tmp)
	return syllables


def syllables(word):
	syl = 0
	vowels = 'aeiouy' #I know that y technically isn't a vowel
	words = word.lower().strip('.:?!').split(" ")
	for i in range(0, len(words)):
		tmp = 0
		word = words[i]
		if word[0] in vowels:
			tmp += 1
		for i in range(1, len(word)):
			if ((word[i] == 'a'or word[i] == 'o') and word[i-1] == 'i') or (word[i] in vowels and word[i-1] not in vowels) or (word[i] == 'i' and (word[i-1] == 'u')):
				tmp += 1
		if word[len(word) - 1] == 'e' and not word[len(word) - 2] == 'l':
			tmp -= 1
		if word[len(word) -2] == 'e' and (word[len(word)-1] == 'd' or word[len(word)-1] == 's'):
			tmp -=1
		if word[len(word)-2] == 's' and word[len(word)-1] == 'm':
			tmp += 1
		if tmp == 0:
			tmp += 1
		syl += tmp
	return syl
import sys
print( syllabify(sys.argv[1]) )
