import os
from params import *
import shutil
from dict_path_name import d

d = {}


def write_text(new_file: str, text: str):
    """
    Запись текста
    :param new_file: имя файла куда записывать тест
    :param text: текст который нужно записать
    """
    with open(new_file, 'a') as n_f:
        n_f.write(text)
        # n_f.write('\n')
        n_f.close()


def read_readme(path_name_readme: str, name_readme: str):
    """
    Чтение README.txt перекодировка в utf-8
    :param path_name_readme: путь к файлу
    :param name_readme: имя файла для чтения Readme
    :return list: Возвращает текст файла
    """
    if name_readme.lower() == 'readme' or name_readme.lower() == 'readme.txt':
        with open(path_name_readme, 'r', encoding="utf-8") as file:
            try:
                return file.read()
            except UnicodeDecodeError:
                with open(path_name_readme, 'r') as file:
                    return file.read()
    else:
        return name_readme


# def list_name_build(path):
#     """
#     Вывод списка имён папок обновлений по дате
#     :param path: путь к папкам с обновлениями
#     :return content: Возвращает отсортированный список папок с датой
#     """
#     content = os.listdir(path)
#     content.sort(reverse=False)
#     return content


def dict_write_path_name(path):
    """
    Запись в dict_path_name.py словаря ключ=путь, значение=список файлов,
    в значении 'readme.txt''readme' на первом месте
    :param path: путь к папкам с обновлениями
    """
    content = os.listdir(path)
    for file in content:
        name_path_catalog = f'{path}\\{file}'
        if os.path.isdir(name_path_catalog):  # Является ли путь каталогом
            dict_write_path_name(name_path_catalog)
        else:
            if 'readme.txt' in content:
                content.remove('readme.txt')
                # content.insert(0, 'readme.txt') # вставка вначало
                content.append('readme.txt')
            if 'readme' in content:
                content.remove('readme')
                # content.insert(0, 'readme') # вставка вначало
                content.append('readme')
            d[path] = content
    try:
        os.remove('dict_path_name.py')
        write_text(f"dict_path_name.py", f'd = {d}')
    except FileNotFoundError:
        write_text(f"dict_path_name.py", f'd = {d}')


def save_all_readme(name_file_out: str, dict_file: dict):
    """
    Запись собранной readme с
    :param name_file_out: Имя файла
    :param dict_file: Словарь с файлами
    """
    sorted_dict_file = dict(sorted(dict_file.items(), reverse=True))
    try:
        os.remove(name_file_out)
    except FileNotFoundError:
        pass
    date_path_one = ''
    for keys, values_all in sorted_dict_file.items():  # цикл по ключам
        date_path_two = keys[24:32]
        path_keys = keys
        if date_path_one != date_path_two:
            write_text(name_file_out, f'----------------{date_path_two}-----------------')
            date_path_one = date_path_two
        for values_one in values_all:  # цикл по значениям
            if values_one != 'readme' and values_one != 'readme.txt':
                write_text(name_file_out, '\n')
                path_keys = f'{keys}\{values_one}'
                write_text(name_file_out,f'{path_keys}\n')
                write_text(name_file_out, f'ДОБАВЛЕН ФАЙЛ:{values_one}\n ')
            else:
                write_text(name_file_out, '\n')
                path_keys = f'{keys}\{values_one}'
                write_text(name_file_out, read_readme(path_keys, values_one))
        write_text(name_file_out, '\n')
        # write_text(name_file_out, '\n')
    dict_write_path_name(path_out)



if __name__ == "__main__":
    dict_write_path_name(path_out)
    save_all_readme(readme_name_all, d)
    shutil.copyfile(readme_name_all,f'{path_in}\\{readme_name_all}')