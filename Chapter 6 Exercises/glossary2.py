# 6-4: Glossary 2

programming_words = {
    'variable' : 'a container to store data',
    'while loop' : 'a loop that continues while a condition is true',
    'for loop' : 'a loop that continues for a set number of times',
    'boolean' : 'true or false',
    'if-statement' : 'a conditional that will on execute if a specific condition is met'
}

for word, definition in programming_words.items():
    print(f'{word.title()}:\n  {definition}')