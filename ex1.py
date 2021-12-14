# dia 14/12/2021

'''Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Given an array of integers, return a new array such that each
element at index i of the new array is the product of all the
numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?'''

lista = [1,2,3,4,5]
nova = []
soma = 1

for i in lista:
    for j in lista:
        if lista.index(i) != lista.index(j):
            soma = soma * j
    nova.append(soma)
    soma = 1
print(nova)

output: [120, 60, 40, 30, 24]
