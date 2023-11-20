from tkinter import Label
print('CONNECTED')


class SubTranslator:
    
    def __init__(self , origin_file):
        with open (origin_file) as file:

            lines = file.readlines()

            for line in lines:
                line = str(line)
                line = line.rstrip()
                if (line.startswith('0')) or (line.startswith('1')) or (line.startswith('2')) or (line.startswith('3')) or (line.startswith('4')) or (line.startswith('5')) or (line.startswith('6')) or (line.startswith('7'))or (line.startswith('8')) or (line.startswith('9')):
                    with open ('J:\PYTHON CODES\PEOJECTS\Subtitle translator\Translated SubFile\MARATHI.str' , 'a' , encoding='utf-8') as file:
                        file.write(f'{line}\n')

                    print(line)
                else:
                    line = 'jkni<>'+ line

                
                    
                    with open ('J:\PYTHON CODES\PEOJECTS\Subtitle translator\Translated SubFile\MARATHI.str' , 'a' , encoding='utf-8') as file:
                        file.write(f'{line}\n')
        
                    print(line)

