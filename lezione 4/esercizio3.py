name = input('Qual è il tuo nome? ')
age = int(input('Quanti anni hai? '))
secure_password = 'Password_sicura'
if age >= 18:
    print('Benvenuto ' + name + ' ')
    user_pwd = input('Inserisci una password: ')
    if user_pwd == secure_password:
        print('Benvenuto ' + name)
    else:
        print('Password non corretta')
else:
    print('Ci spiace ' + name + ', ma non puoi accedere perchè sei minorenne')
