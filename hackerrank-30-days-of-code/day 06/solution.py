num_test = int(input())

for i in range(num_test):
    test_string = input()
    even_char = ''
    odd_char = ''

    for j in range(len(test_string)):
        if j % 2 == 0:
            even_char += test_string[j]
        else:
            odd_char += test_string[j]
    print('{} {}'.format(even_char, odd_char))
