# dia 13/12/2021

'''Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''

lista = [10,15,3,7]
k=25
def checagem(lista):
    for i in lista:
        for j in lista:
            if i + j == k and lista.index(i) != lista.index(j):
                return True
            
print(checagem(lista))
