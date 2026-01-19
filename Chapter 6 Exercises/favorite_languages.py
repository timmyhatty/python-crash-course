# 6-6: Polling

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c++',
    'edward' : 'rust',
    'phil' : 'python'
}
taken_survey = ['jen', 'edward', 'johnathan', 'brian']

for person in taken_survey:
    if person in favorite_languages.keys():
        print(f'Thank you {person.title()} for taking the survey!')
    else:
        print(f"You've yet to take the survey, {person.title()}. Please take it immediately")