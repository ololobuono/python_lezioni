secure_password = 'Password_sicura'
username = input('Qual è il tuo username? ')
user_pwd = input('Inserisci una password: ')
if user_pwd == secure_password:
    print('Benvenuto ' + username)
else:
    print('Password non corretta')