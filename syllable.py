def syllabify(word):
	syllables = []
	vowels = 'aeiouy'
	words = word.lower().strip('.:?!').split(" ")
        for i in range(0, len(words)):
                tmp = []
		track = 0
                word = words[i]
                if word[0] in vowels:
			track += 1
			while word[track] not in vowels:
				track = track +  1
				print track
				if track == len(word):
					break
			print track	
			syllables.append(word[0: track + 1])
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
