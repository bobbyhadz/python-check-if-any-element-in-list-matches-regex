# Check if any element in a list matches Regex in Python

import re

prog = re.compile(r'[a-z]+')

my_list = ['!', '?', 'abc']


if any((match := prog.match(item)) for item in my_list):
    print('At least one list item matches regex')

    print(match.group(0))  # 👉️ 'abc'
else:
    print('No list items match regex')


print(prog.match('abc').group(0))  # 👉️ 'abc'