# def int_return(num):
#     return num
# k = int_return(3)
# print(k)
#
# def change(sentence):
#     new_string = sentence + " Nice to meet you"
#     return new_string
#
# z = change("Hello")
# print(z)

# def accum(lst):
#     sum = 0
#     for number in lst:
#         sum += number
#     return sum

def accum(lst):
    num = (lambda number: number * number)
    powersum = 0
    for number in lst:
        powersum += num(number)
    return powersum

print(accum([1,2,3,4,5,6,7,8,9,10]))
