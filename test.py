import shutil
import os
from params import path_in

# f = {'Acquirer3': ['0020100.exe'],
#      'Cleaner': ['0080400.exe'],
#      'EMSTransfer': ['0081800.exe'],
#      'GateMC': ['0081500.exe'],
#      'GateMIR': ['0081600.exe'],
#      'GateVisa3': ['0773200.exe'],
#      'GateWay4': ['0081900.exe'],
#      'ISO2': ['0121000.dll'],
#      'Issuer': ['0049200.exe'],
#      'MUX': ['MUXTerminal.1.18.wsdl', 'MUXTerminal.1.18.xsd'],
#      'MUXGate': ['0193000.exe', 'muxgate.ini.example'],
#      'NDC': ['0143500.dll', '0143800.exe', '0143900.exe', 'config.ini.example'],
#      'NdcUI': ['0210205.exe', 'SrvMod_NDCUI.ini.example'],
#      'RuUI': ['0220300.exe'],
#      'SERVICE': ['0050700.dll'],
#      'SrvMod': ['0210105.exe', 'SrvMod.ini.example'],
#      'SuperMon': ['0140400.exe', 'supermon.ini.example'],
#      'TSD\\LDD\\online': ['D10.lds', 'D10.ldx', 'D10_EN.lds', 'D10_EN.ldx', 'D31.lds',
#                           'D31.ldx'],
#      'TSD': ['LDD', 'online.html', 'SQL', 'ucdata.tsd'],
#      'TSD\\SQL\\online': ['ACQ.pkg', 'EMS.pkg', 'EMS_3CARDR.pkg', 'EMS_SKB.pkg',
#                           'iss.pkg'],
#      'XML': ['common_types.xsd', 'psbxml.xsd', 't_status_code.xsd'],
#      'XModEditor': ['0080700.exe', 'xmodeditor.ini.example']}

f = {'TSD\\LDD\\online': ['D10.lds', 'D10.ldx', 'D10_EN.lds', 'D10_EN.ldx', 'D31.lds',
                          'D31.ldx'],
     'TSD': ['LDD', 'online.html', 'SQL', 'ucdata.tsd'],
     'TSD\\SQL\\online': ['ACQ.pkg', 'EMS.pkg', 'EMS_3CARDR.pkg', 'EMS_SKB.pkg',
                          'iss.pkg'],
     'XML': ['common_types.xsd', 'psbxml.xsd', 't_status_code.xsd'],
     'XModEditor': ['0080700.exe', 'xmodeditor.ini.example']}

path_file_out = 'd:\\ROBO_ONLINE\\all_out\\20230713_220_41\\SQL\\online'
file = 'EMS_SKB.pkg'


def save_file_in(path_file_out, name_file):
    for keys, values_all in f.items():
        if name_file in values_all:
            path = f'{path_in}\\{keys}'
            path_file_and_name = f'{path_file_out}\\{name_file}'
            print(path_file_and_name)
            try:
                os.makedirs(path)
                shutil.copyfile(path_file_and_name, f'{path}\\{name_file}')
                # os.remove(path_file_and_name)
            except FileExistsError:
                shutil.copyfile(path_file_and_name, f'{path}\\{name_file}')


save_file_in(path_file_out, file)
# os.makedirs('d:\\ROBO_ONLINE\\all_in\\TSD\\SQL\\online')
