#! usr/bin/env python

import subprocess
from django.utils.crypto import get_random_string

secret_key = get_random_string(40)

CONFIG = f'DEBUG=True\n' \
         f'SECRET_KEY={secret_key}'

with open('.env', 'w') as env_config:
    env_config.write(CONFIG)

print('Success!\nYour newly generated .env file:\n')
result = subprocess.run(['cat', '.env'])
