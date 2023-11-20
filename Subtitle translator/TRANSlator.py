from deep_translator import GoogleTranslator
print('CONNECTED')


with open ('F:\AOT Season 1\\aotS01E02.srt') as file:
    lines = file.readlines()

    for line in lines:
        line = str(line)
        line = line.rstrip()
        if (line.startswith('0')) or (line.startswith('1')) or (line.startswith('2')) or (line.startswith('3')) or (line.startswith('4')) or (line.startswith('5')) or (line.startswith('6')) or (line.startswith('7'))or (line.startswith('8')) or (line.startswith('9')):
            with open ('MARATHI.srt' , 'a' , encoding='utf-8') as file:
                file.write(f'{line}\n')

            print(line)
        else:
            line = 'jkni<>'+ line
            result = GoogleTranslator(source='auto',target= 'mr').translate(line)
            tr_line = result.split('<>')
            line = tr_line[1]
        
            
            with open ('MARATHI.srt' , 'a' , encoding='utf-8') as file:
                file.write(f'{line}\n')
        
            print(line)
        