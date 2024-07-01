# Versionsnummern in Softwarename entfernen
import re

def text(reg_ex, txt):
    try:
        with open(txt, 'r') as text:
            ext = ''
            for line in text:
                ext += re.sub(reg_ex, '', line)
            return ext
    except Exception as e:
        print('!!!',e, '!!!')
        
txt = 'regex/software_name.txt'
reg_ex = r'\-?\s?[v]?\s?(\d{1,}\.)+\d{1,}([-+]\d{1,})?'
print(text(reg_ex, txt))