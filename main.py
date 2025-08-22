with open('input1.txt', 'r') as file:
    str_input_1 = file.read().strip().split('\n')

with open('input2.txt', 'r') as file:
    str_input_2 = file.read().strip().split('\n')

str_input_1.sort()
str_input_2.sort()
set_input_1 = set(str_input_1)
set_input_2 = set(str_input_2)

for str_input_1_element in str_input_1:
    if str_input_1_element not in set_input_2:
        print(str_input_1_element)
print('------')
for str_input_2_element in str_input_2:
    if str_input_2_element not in set_input_1:
        print(str_input_2_element)
