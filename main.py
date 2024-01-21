import re
end = True
while end:
    table = {
    '000':'0',
    '001':'1',
    '010':'2',
    '011':'3',
    '100':'4',
    '101':'5',
    '110':'6',
    '111':'7'
    }
    def translate_notation(Binary):
        oct = ''
        while len(Binary)%3 != 0:
            Binary = '0' + Binary
        
        Binary = re.findall(r'\d\d\d',Binary)
        for i in range(len(Binary)):
            if Binary[i] in table.keys():
                oct += table.get(Binary[i])
        return Binary, '.'.join(oct)
        
            
    print(translate_notation(str(input('Введите двоичное число: '))))
    if str(input('Хотите прекратить?')) == 'Да':
        end = False