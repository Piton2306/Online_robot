from dict_path_name import d
from params import path_in
import shutil


f = {'Acquirer3': ['0020100.txt'],
     'Cleaner': ['0080400.exe'],
     'EMSTransfer': ['0081800.exe'],
     'GateMC': ['0081500.exe'],
     'GateMIR': ['0081600.exe'],
     'GateVisa3': ['0773200.exe'],
     'GateWay4': ['0081900.exe'],
     'ISO2': ['0121000.dll'],
     'Issuer': ['0049200.exe'],
     'MUX': ['MUXTerminal.1.18.wsdl', 'MUXTerminal.1.18.xsd'],
     'MUXGate': ['0193000.exe', 'muxgate.ini.example'],
     'NDC': ['0143500.dll', '0143800.exe', '0143900.exe', 'config.ini.example'],
     'NdcUI': ['0210205.exe', 'SrvMod_NDCUI.ini.example'],
     'RuUI': ['0220300.exe'],
     'SERVICE': ['0050700.dll'],
     'SrvMod': ['0210105.exe', 'SrvMod.ini.example'],
     'SuperMon': ['0140400.exe', 'supermon.ini.example'],
     'TSD\\LDD\\online': ['D10.lds', 'D10.ldx', 'D10_EN.lds', 'D10_EN.ldx', 'D31.lds',
                          'D31.ldx'],
     'TSD': ['LDD', 'online.html', 'SQL', 'ucdata.tsd'],
     'TSD\\SQL\\online': ['ACQ.pkg', 'EMS.pkg', 'EMS_3CARDR.pkg', 'EMS_SKB.pkg',
                          'iss.pkg'],
     'XML': ['common_types.xsd', 'psbxml.xsd', 't_status_code.xsd'],
     'XModEditor': ['0080700.exe', 'xmodeditor.ini.example']}

file = '0020100.txt'
for keys, values_all in f.items():
    if file in values_all:
        print(f'{path_in}\\{keys}')
        shutil.copyfile(file, f'{path_in}\\{file}')
