
def syllabify(word):
	syllables = []
	vowels = 'aeiouy'
	words = word.lower().strip('.:?!').split(" ")
        for i in range(0, len(words)):
                tmp = []
                word = words[i]
		for j in range(0, len(word)):
			print('a')
			if word[j] in vowels and not j == len(word):
				print('b')
                        	track = j+1

				
				while word[track] not in vowels:
                                        print('c')
                                        track = track +  1
                                        print track
                                        if track == len(word)-1 and word[track] in vowels:
                                                tmp.append(word[track])
                                                break
                                        elif word[track] in vowels:
                                                tmp.append(word[j:(track+1)])
                                                break
			else:
				print 'd'



#                        	while word[track-1] not in vowels:
 #                               	print('c')
#					track = track +  1
 #                               	print track
  #                              	if track == len(word)-1 and word[track] in vowels:
#						tmp.append(word[track])
#						break
#					elif word[track] in vowels:
#						tmp.append(word[j:(track+1)])
 #                                       	break
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
