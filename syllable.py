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
			if (word[i] == 'a' and word[i-1] == 'i') or (word[i] in vowels and word[i-1] not in vowels):
				tmp += 1	
		if word[len(word) - 1] == 'e' and not word[len(word) - 2] == 'l':
			tmp -= 1
		if word[len(word)-2] == 's' and word[len(word)-1] == 'm':
			tmp += 1
		if tmp == 0:
			tmp += 1
		syl += tmp
	return syl
import sys
print( syllables(sys.argv[1]) )
