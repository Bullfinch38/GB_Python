import re
valid_name = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$')
def email_parse(user_input):
    regexp = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$')
    result = regexp.match(user_input)
    if result:
        return dict(zip(['username', 'domain'], result.group().split('@')))
    raise ValueError(f'Wrong email {user_input}')

if __name__ == '__main__':
    user_input = input('Enter your email:\n')
    print(email_parse(user_input))