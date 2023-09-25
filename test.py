d = {'d:\\ROBO_ONLINE\\ALL_FILE\\20230619_220_41\\GateVisa3': ['0773200.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230712_220_41\\NDC': ['config.ini.example', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230616_220_41\\Acquirer3': ['0020100.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230616_220_41\\EMSTransfer': ['0081800.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230616_220_41\\ISO2': ['0121000.dll', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230616_220_41\\MUXGate': ['0193000.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230616_220_41\\NDC': ['0143500.dll', '0143800.exe', 'readme'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230616_220_41\\SERVICE': ['0050700.dll', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230616_220_41\\SQL\\online': ['ACQ.pkg', 'iss.pkg', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230621_220_41\\NDC': ['0143900.exe', 'readme'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230623_220_41\\GateMC': ['0081500.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230623_220_41\\GateMIR': ['0081600.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230623_220_41\\GateVisa3': ['0773200.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230623_220_41\\GateWay4': ['0081900.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230627_220_41\\MUX': ['MUXTerminal.1.17.wsdl', 'MUXTerminal.1.17.xsd', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230627_220_41\\SQL\\online': ['EMS.pkg', 'EMS_3CARDR.pkg', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230629_220_41\\Issuer': ['0049200.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230710_220_41\\MUX': ['MUXTerminal.1.18.wsdl', 'MUXTerminal.1.18.xsd', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230711_220_41\\Issuer': ['0049200.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230711_220_41\\LDD\\Online': ['D31.lds', 'D31.ldx', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230711_220_41\\MUXGate': ['muxgate.ini.example', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230711_220_41\\NdcUI': ['0210205.exe', 'SrvMod_NDCUI.ini.example', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230711_220_41\\Online\\Cleaner': ['0080400.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230711_220_41\\RuUI': ['0220300.exe', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230711_220_41\\SrvMod': ['0210105.exe', 'D10.lds', 'D10.ldx', 'D10_EN.lds',
                                                            'D10_EN.ldx', 'SrvMod.ini.example', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230711_220_41\\SuperMon': ['0140400.exe', 'supermon.ini.example', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230711_220_41\\XModEditor': ['0080700.exe', 'xmodeditor.ini.example', 'readme.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230713_220_41\\SQL\\catalog': ['222.txt'],
     'd:\\ROBO_ONLINE\\ALL_FILE\\20230713_220_41\\SQL\\online': ['EMS_SKB.pkg', 'readme.txt']}
d = dict(sorted(d.items(),reverse=True))
print(d)
# rooms = {5: "Rm 403", 0: "Rm 201", 3: 'hjjhjh', 8: "Rm 503"}
# rooms1 = dict(sorted(rooms.items()))
# print(rooms1)
# def read_readme(path_name_readme: str, name_readme: str):
#     """
#     Чтение README.txt перекодировка в utf-8
#     :param path_name_readme: имя файла для чтения Readme
#     :return list: Возвращает текст файла
#     """
#     if name_readme.lower() == 'readme' or name_readme.lower() == 'readme.txt':
#         with open(path_name_readme, 'r', encoding="utf-8") as file:
#             try:
#                 return file.read()
#             except UnicodeDecodeError:
#                 with open(path_name_readme, 'r') as file:
#                     return file.read()
#     else:
#         return name_readme
#
#
# def write_text(new_file: str, text: str):
#     """
#     Запись текста
#     :param new_file: имя файла куда записывать тест
#     :param text: текст который нужно записать
#     """
#     with open(new_file, 'a') as n_f:
#         n_f.write(text)
#         # n_f.write('\n')
#         n_f.close()
#
#
# name_file_out = 'readme_all.txt'
# os.remove(name_file_out)
# date_path_one = ''
# for keys, values_all in d.items():  # цикл по ключам
#     date_path_two = keys[24:32]
#     path_keys = keys
#     print(path_keys)
#     if date_path_one != date_path_two:
#         write_text(name_file_out, f'----{date_path_two}----')
#         date_path_one = date_path_two
#     for values_one in values_all:  # цикл по значениям
#         if values_one != 'readme' and values_one != 'readme.txt':
#             write_text(name_file_out, '\n')
#             path_keys = f'{keys}\{values_one}'
#             write_text(name_file_out, f'Добавлен файл:{values_one} ')
#         else:
#             write_text(name_file_out, '\n')
#             path_keys = f'{keys}\{values_one}'
#             write_text(name_file_out, read_readme(path_keys, values_one))
#     write_text(name_file_out, '\n')
#     write_text(name_file_out, '\n')
