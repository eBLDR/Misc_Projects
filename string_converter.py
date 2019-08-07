# Camel to snake and snake to camel case converter


def snake_to_camel(snake_string):
    result = ''
    next_upper = False

    for char in snake_string:
        if char == '_':
            next_upper = True
            continue

        if next_upper:
            result += char.upper()
            next_upper = False
        else:
            result += char

    return result


def camel_to_snake(camel_string):
    result = ''

    for char in camel_string:
        if char == char.upper():
            result += '_'
            result += char.lower()
        else:
            result += char

    return result


snake = 'this_is_snake_case'
camel = 'thisIsCamelCase'

print(snake_to_camel(snake))
print(camel_to_snake(camel))
