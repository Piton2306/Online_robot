import os

from dict_path_name import d

path = 'd:\\ROBO_ONLINE\\ALL_FILE'


def write_text(new_file: str, text: str):
    """
    Запись текста
    :param new_file: имя файла куда записывать тест
    :param text: текст который нужно записать
    """
    with open(new_file, 'a') as n_f:
        n_f.write('\n')
        n_f.write(text)
        n_f.close()


def read_readme(path_name_readme: str):
    """
    Чтение README.txt
    :param path_name_readme: имя файла для чтения Readme
    :return list: Возвращает прочитанный файл
    """
    with open(path_name_readme, 'r', encoding="utf-8") as file:
        try:
            return file.read()
        except UnicodeDecodeError:
            with open(path_name_readme, 'r') as file:
                return file.read()


def list_name_build(path):
    """
    Вывод списка имён папок обновлений по дате
    :param path: путь к папкам с обновлениями
    :return content: Возвращает отсортированный список папок с датой
    """
    content = os.listdir(path)
    content.sort(reverse=False)
    return content


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
                content.append('readme.txt')
            d[path] = content
    try:
        os.remove('dict_path_name.py')
        write_text(f"dict_path_name.py", f'd = {d}')
    except FileNotFoundError:
        write_text(f"dict_path_name.py", f'd = {d}')


dict_write_path_name(path)
