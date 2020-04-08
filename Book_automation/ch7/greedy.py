import re

#this defines GREEDY regexp (if he finds 5, we will chose 5)
greedyHaRegex = re.compile(r'(Bu){3,5}')

subi1 = greedyHaRegex.search('ej20 sound BuBuBuBuBu')

print(subi1.group())

# this defines NON_GREEDY ; found 5, chooses 3.
nongreedyHaRegex = re.compile(r'(Bu){3,5}?')
subi2 = nongreedyHaRegex.search('ej25 too BuBuBuBuBu')

print(subi2.group())