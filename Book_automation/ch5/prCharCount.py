import pprint
# this module is for nice output

message = 'In the grim dark future of 41st millenium there is only war. Burn the witch, Kill the heretic, destroy mutant.'

count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# pprint.pprint(count)

print(pprint.pformat(count))
