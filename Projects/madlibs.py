"""
Mad Libs Project

You can make the story as long as you want, we decided not to as this is only
supposed to show you how you can write the program. 
"""

print("""
Welcome User! The goal of this game is to enter whatever type of word is asked of you,
and at the end a story will be generated based on the words that you provided!
""")

noun = input("Enter a noun: ")
verb_past_tense = input("Enter a past tense verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
plural_noun1 = input("Enter a plural noun: ")
plural_noun2 = input("Enter another plural noun: ")
place = input("Enter a place: ")
number = input("Enter a number greater than 1: ")
celebrity = input("Enter a celebrity's name: ")

# Create the Mad Libs story
story = f"""
Once upon a time in a {adjective} land, there lived a {noun}. One day, the {noun} {verb_past_tense} {adverb} 
through the {adjective} forest, carrying a bag of {plural_noun1}. This enchanted journey led the {noun} to 
the magical {place}, where {number} {plural_noun2} were scattered all around. And guess who was there too? 
None other than {celebrity} himself!
"""

# Print the completed Mad Libs story
print(f"\nMad Libs Story:\n{story}")
print("Thank you for playing! Hope to see you again soon!")
