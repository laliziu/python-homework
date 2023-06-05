import os
import shutil

def input_number(text) -> int:
    print(text, end='')
    while True:
        try:
            number = int(input())
        except ValueError:
            print('Пожалуйста введите число - ', end='')
            continue
        else:
            break
    return number

def horiz_line(text):
    print(('=' * ((len(text)*2)-1)) if type(text) == str else ('=' * max(list(map(lambda a: len(a),text)))))
    print(*text)
    print(('=' * ((len(text)*2)-1)) if type(text) == str else ('=' * max(list(map(lambda a: len(a),text)))))

def search_del_mod_func(users_finded_list, modify=None):
    if users_finded_list:
        horiz_line(list(map(lambda num, usr: f'\n{num}. {usr[:-1]}\n', range(1, len(users_finded_list) + 1), users_finded_list)))
        if modify != 's':
            while True:
                match key_choose_user := input('\nВЫХОД - чтобы завершить \nВыберите контакт - ').lower():
                    case num if num.isdigit() and (int(num) in range(1,len(users_finded_list) + 1)):
                        user_for_del = users_finded_list[int(key_choose_user) - 1]
                        with open('task1.txt', 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                        with open('task1.txt', 'w', encoding='utf-8') as f:
                            for line in lines:
                                if user_for_del not in line:
                                    f.write(line)
                                elif modify == 'm':
                                    while True:
                                        modify_choose_list = ['1. фамилия', '2. имя', '3. отчество', '4. телефон', '5. полностью']
                                        print(*list(map(lambda a: f'\n{a}', modify_choose_list)))
                                        match modify_choose := input_number('\nКакие данные редактируем? '):
                                            case num if num in range(1,5):
                                                modify_line_list = line.split()
                                                modify_line_list[modify_choose - 1] = input('Введите новые данные - ')
                                                new_data = ' '.join(modify_line_list)
                                                f.write(f'{new_data}\n')
                                                break
                                            case 5:
                                                new_data = input('Отредактируйте новые данные полностью - ')
                                                f.write(f'{new_data}\n')
                                                break
                                            case _:
                                                horiz_line('Ошибка ввода! Введите от 1 до 5!')
                        break
                    case 'выход' | 'quit' | 'exit' | 'ds[jl':
                        break
                    case _:
                        horiz_line('Ошибка ввода!')
    else:
        horiz_line('Никто не найден!')

def single_or_multy_search(text, num):
    with open('task1.txt', 'r', encoding='utf-8') as f:
        file = f.readlines()
        search = input(text).lower()
        match num:
            case 4:
                filter_func = lambda usr: line in usr.lower() if (len(search.split()) > 1) else search in usr.lower()
            case _:
                filter_func = lambda usr: line in (usr.lower().split())[num] if (len(search.split()) > 1) else search in (usr.lower().split())[num]
                print(len(search.split()))
        if len(search.split()) > 1:
            search_list = set()
            for line in set(search.split()):
                search_list = search_list.union(set(filter(filter_func, file)))
            return list(search_list)
        else:
            return list(filter(filter_func, file))

def search_delete_modify_user(option=None, modify = None):
    if option is not None:
        menu_main_info(option)
    menu_search('Характеристика поиска:')
    search_choose_list = ['фамилию', 'имя', 'отчество', 'телефон', 'ключевое(ые) слово(а)']
    while True:
        match action := input('\nВыберите опцию поиска - '):
            case num if action.isdigit() and int(num) in range(1, 6):
                search_del_mod_func(single_or_multy_search(f'Введите {search_choose_list[int(num) - 1]} - ', (int(num) - 1)), modify)
                menu_main_info(option)
                menu_search('Характеристика поиска:')
            case '6' | 'выход' | 'quit' | 'exit' | 'menu' | 'main' | 'main menu' | 'menu main' | 'ds[jl':
                break
            case _:
                horiz_line('!!!Нет такой функции!!!')
                menu_main_info(option)
                menu_search('Характеристика поиска:')

def add_user(option=None):
    if option is not None:
        menu_main_info(option)
    with open('task1.txt', 'a', encoding='utf-8') as f:
        match new_data := input('ВЫХОД - возврат в меню \nВведите по формату Фамилия Имя Отчество Телефон - '):
            case 'выход' | 'quit' | 'exit' | 'menu' | 'main' | 'main menu' | 'menu main' | 'ds[jl':
                return
            case _:
                f.write(f'{new_data}\n')

def read_all_users(option=None):
    if option is not None:
        menu_main_info(option)
    with open('task1.txt', 'r', encoding='utf-8') as f:
        users_all_list = list(map(lambda a: a[:-1], f.readlines()))
        horiz_line(list(map(lambda num, usr: f'\n{num}. {usr}\n', range(1,len(users_all_list) + 1), users_all_list)))

def menu_search(text):
    menu_search_list = [text,
                        '1. По фамилии',
                        '2. По имени',
                        '3. По отчеству',
                        '4. По телефону',
                        '5. Любое совпадение',
                        '6. В главное меню']
    print(*map(lambda a: f'\n{a} ', menu_search_list))

def menu_main_info(option=None):
    menu_main_list = ['1. Показать все контакты',
                      '2. Добавить контакт',
                      '3. Поиск контакта',
                      '4. Удалить контакт',
                      '5. Редактировать контакт',
                      '6. Выход',
                      '7. Главное меню']
    if (option is not None) and (option in range(1, 7)):
        horiz_line(' '.join((menu_main_list[option - 1].split())[1:]))
    else:
        horiz_line(' '.join((menu_main_list[6].split())[1:]))
        print(*map(lambda a: f'\n{a} ', menu_main_list[:6]))

def menu_main():
    menu_main_info()
    while True:
        match user_action := input("\nВыберите функцию, через цифру - ").lower():
            case '1' | 'показать' | 'show':
                read_all_users(1)
                menu_main_info()
            case '2' | 'добавить' | 'add':
                add_user(2)
                menu_main_info()
            case '3' | 'поиск' | 'search':
                search_delete_modify_user(3, 's')
                menu_main_info()
            case '4' | 'удалить' | 'del' | 'delete':
                search_delete_modify_user(4, 'd')
                menu_main_info()
            case '5' | 'редактировать' | 'modify' | 'edit':
                search_delete_modify_user(5, 'm')
                menu_main_info()
            case '6' | 'выход' | 'quit' | 'exit' | 'ds[jl':
                menu_main_info(6)
                break
            case _:
                horiz_line('!!!Нет такой функции!!!')
                menu_main_info()

menu_main()
