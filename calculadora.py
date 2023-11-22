Operação = input('''
Por favor, digite a operação matemática que você deseja concluir:

''')

number_1 = int(input('Entre com o primmeiro numero: '))
number_2 = int(input('Entre com o segundo numero: '))

print('{} + {} = '.format(number_1, number_2))
print(number_1 + number_2)

print('{} - {} = '.format(number_1, number_2))
print(number_1 - number_2)

print('{} * {} = '.format(number_1, number_2))
print(number_1 * number_2)

print('{} / {} = '.format(number_1, number_2))
print(number_1 / number_2)