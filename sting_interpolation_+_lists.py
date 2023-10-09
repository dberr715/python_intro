word_list = [{"noun": "", "verb": "", "adjective": ""}]

noun = input("Type a singular noun")
verb = input("Type a past-tense verb")
adjective = input("Type an adjective")

print(
    "The %s %s frolicked in the fields. Then it %s into the woods"
    % (adjective, noun, verb)
)
