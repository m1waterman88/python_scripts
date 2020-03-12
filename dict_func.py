def dict_func(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
        'mod': lambda: x % y,
        'exp': lambda: x**y,
    }.get(operator, lambda: None)()

x, y = 5, 2

add = dict_func('add', x, y)
sub = dict_func('sub', x, y)
mul = dict_func('mul', x, y)
div = dict_func('div', x, y)
mod = dict_func('mod', x, y)
exp = dict_func('exp', x, y)
non = dict_func('non', x, y)

print(f"{x, y = }\
      \n{add = }\
      \n{sub = }\
      \n{mul = }\
      \n{div = }\
      \n{mod = }\
      \n{exp = }\
      \n{non = }"
      )
