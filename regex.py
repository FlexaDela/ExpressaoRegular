import re

achar_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

email = [
        'joazinho@gmail.com',
         'cezar@hotmail.com',  
         'claudia@outlook.com',
         'cleber@.com',
         '@gmail.com',
         'souzinaldogmail.com'
        ]

email_valido = []
email_valido.append(re.findall('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email[0] if email else ''))

    