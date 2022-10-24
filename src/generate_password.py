import random, string

def generatePassword(length, lower_min = 0, upper_min = 0, number_min = 0, symbol_min = 0):
    ''' Function to generate random password. Saves you tons of cyber attacks

    INPUT
    -----
    length : Expected length of the password
    lower_min : Min count of lower letters to be in the password
    upper_min : Min count of upper letters to be in the password
    number_min : Min count of number to be in the password
    symbol_min : Min count of symbols to be in the password

    OUTPUT
    ------
    Password of length (length)

    ERRORS
    ------
    Throws assertion error if the sum of min count is less than the max length of the password

    '''
    assert length > (lower_min + upper_min + number_min + symbol_min)

    def gen_pass_n(type_, limit):
        '''
        Generates n random characters of the given type
        '''

        if limit:
            return random.sample(type_, limit)
        return []

    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    combined = lower_case + upper_case + numbers + symbols

    balance = length - (lower_min + upper_min + number_min + symbol_min)

    password = []
    password.extend(gen_pass_n(lower_case, lower_min))
    password.extend(gen_pass_n(upper_case, upper_min))
    password.extend(gen_pass_n(numbers, number_min))
    password.extend(gen_pass_n(symbols, symbol_min))
    password.extend(gen_pass_n(combined, balance))

    random.shuffle(password)

    return "".join(password)

print(generatePassword(10))
