# 6-12: Extensions

# This program will ask the user for their name and what their favorite programming language is
loop_control = 'y'

favorite_languages = {}

while loop_control == 'y':
    name = input("What's your name: ").lower()
    language = input("What's your favorite programming language: ").lower()
    favorite_languages[name] = language

    loop_control = input('Would you like to run the program again (y/Y): ').lower()

# List the names of each language and who's favorite language it is
print("\nSurvey Results\n--------------\n")

languages = set(favorite_languages.values())
languages = sorted(languages)

for language in languages:
    print(f"{language.title()}")
    print("  Favorite of:")

    for person in favorite_languages.keys():
        if favorite_languages[person] == language:
            print(f'    {person.title()}')
        


# List the most popular favorite language in the survey
counts = {}

for language in favorite_languages.values():
    if language not in counts:
        counts[language] = 1
    else:
        counts[language] += 1

most_popular = None
highest_count = 0

for language, count in counts.items():
    if count > highest_count:
        highest_count = count
        most_popular = language

print(f'\nMost Popular Language: {most_popular.title()}')