"""Python functions for JavaScript Trials 1."""

def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums
    
print(get_all_evens([7, 8, 10, 1, 2, 2]))


def get_odd_indices(items):
    
    odd_indices = []
 
    for i in range(len(items)):
        if i % 2 == 1:
            odd_indices.append(items[i])
    return odd_indices

print(get_odd_indices([1, 'hello', True, 500]))


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f'{i}. {item}')

        i += 1

print_as_numbered_list([1, 'hello', True])


def get_range(start, stop):
    nums = []

    for i in range(start, stop, 1):
        nums.append(i)
    
    return nums

print(get_range(0, 5))


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')

        else:
            chars.append(letter)
    
    return ''.join(chars)

print(censor_vowels('hello world'))


def snake_to_camel(string):
    camelCase = []

    for word in string.split("_"):
        camelCase.append(f'{word[0].upper()}{word[1:]}')
    
    return "".join(camelCase)

print(snake_to_camel('hello_world'))


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
