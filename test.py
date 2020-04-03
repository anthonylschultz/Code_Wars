str = "Jędrzej Błądziński"
def correct_polish_letters(str): 
    '''
    parameter:
    str

    returns:
    str with replaced polish characters
    '''

    lst_ = []
    polish = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś':'s', 'ź': 'z', 'ż': 'z'}
    for i in str:
        if i in polish.keys():
            str = str.replace(i, polish[i])
    return str



solution("camelCasing")  ==  "camel Casing"
str = "camelCasing"
def solution(str):
    for i in str:
        new_str = str.split(i.isupper())
    return new_str


    for i in str:
        if i.isupper():
            new_str = str.split(i.isupper())
        return new_str
