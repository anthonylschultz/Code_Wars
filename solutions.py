# 20200405

# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 21445 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321


# refactored
def Descending_order(num):
    return int("".join(sorted(str(num), reverse = True)))

num = 23894
def descending_order(num):
    x = str(num)
    y = [int(i) for i in x]
    y.sort(reverse = True)
    integer = int("".join(map(str, y)))
    return integer # convert back to int


# 20200402
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
