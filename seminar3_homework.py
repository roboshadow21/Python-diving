from collections import Counter


# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

source_li = [1, 2, 1, "hi", 4, 5, "hi", 2, (1, 2)]
result_li = []

for el in source_li:
    if source_li.count(el) > 1:
        result_li.append(el)

print(list(set(result_li)))


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

text = """       
          The keyword def introduces a function definition. It must be followed by the function name and " \
       "the parenthesized list of formal parameters. The statements that form the body of the function " \
       "start at the next line, and must be indented. The first statement of the function body can 
       optionally be a string literal; this string 
       literal is the function’s documentation string, or docstring. (More about docstrings can be 
        found in the section Documentation Strings.) 
        There are tools which use docstrings to automatically produce 
        online or printed documentation, or to let the user interactively browse through code; 
        it’s good practice to include docstrings in code that you write, so make a habit of it.

        The execution of a function introduces a new symbol table used for the local variables of the function. 
        More precisely, all variable assignments in a function store the value in the local symbol table; 
        whereas variable references first look in the local symbol table, then in the local symbol tables 
        of enclosing functions, then in the global symbol table, and finally in the table of built-in names. 
        Thus, global variables and variables of enclosing functions cannot be directly assigned a value 
        within a function (unless, for global variables, named in a global statement, or, for 
        variables of enclosing functions, named in a nonlocal statement), although they may be referenced.

        The actual parameters (arguments) to a function call are introduced in the local symbol table of 
        the called function when it is called; thus, arguments are passed using call by value 
        (where the value is always an object reference, not the value of the object). 1 When a function calls 
        another function, or calls itself recursively, a new local symbol table is created for that call.

        A function definition associates the function name with the function object in the current symbol table. 
        The interpreter recognizes the object pointed to by that name as a user-defined function. 
        Other names can also point to that same function object and can also be used to access the function
        """

result = Counter(text.split())

print(Counter(result).most_common(10))


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

my_dict = {
    "compass": 2,
    "tent": 15,
    "knife": 5,
    "socks": 4,
    "food": 12,
    "lighter": 6,
    "map": 1,
    "phone": 7,
    "rifle": 9
}

MAX_WEIGHT = 20
spam = 0
final_lst = []

for key, value in my_dict.items():
    if spam + value <= MAX_WEIGHT:
        spam += value
        final_lst.append(key)

print(final_lst)

sorted_values = dict(sorted(my_dict.items(), key=lambda x: -x[1]))
for key, value in sorted_values.items():
    if value <= MAX_WEIGHT:
        print(key, sep='/n')
        MAX_WEIGHT -= value
