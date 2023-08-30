import os

path = 'd:\\ROBO_ONLINE\\ALL_FILE'
os.remove('rea.txt')

def add_new_readme(new_file: str, text: str):
    """
    Запись нового файла из Readme.txt
    :param new_file: имя файла куда записывать Readme
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


def readme_out_text_in(path_readme: str, file_readme: str):
    path_out = f'{path_readme}\\{file_readme}'
    path_in = 'readme8.txt'
    # print(f'Из {path_out}\nВ {path_in}')
    if file_readme.upper() == "README.TXT":
        with open(path_out, 'r') as file:
            for item in file:
                print(path_in)
                print(item)


def read_file(path):
    """
    Вывод списка имён папок обновлений по дате
    :param path: путь к папкам с обновлениями
    """
    content = os.listdir(path)
    for file in content:
        name_path_catalog = f'{path}\\{file}'
        if os.path.isdir(name_path_catalog):  # Является ли путь каталогом
            read_file(name_path_catalog)
        else:
            if file.upper() == "README.TXT":
                print(path, file)
                text = read_readme(name_path_catalog)
                add_new_readme('rea.txt',path)
                add_new_readme('rea.txt',text)
                print(text)


read_file(path)
