## needs frequency detector probably using count

def makeAnagram(array_1, array_2):
    a = array_1
    b = array_2
    i = 0
    q = str()

    for letter_a in a:
        if letter_a not in b:
            i += 1
        if letter_a in b and letter_a not in q:
            a_count = a.count(letter_a)
            b_count = b.count(letter_a)
            i += a_count - b_count
            q += letter_a

    for letter_b in b:
        if letter_b not in a:
            i += 1

    print(i)

this = 'bibgig'
that = 'blg'

makeAnagram(this, that)
