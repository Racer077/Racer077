#№1#
import re
text = input()
print(f'новая строчка:{text.replace('н', '!')}, кол-во символов:{len(max(re.findall(r'н+', text)))}')
#№2#
def extract_inside_brackets(s):
    start = s.find('(')
    end = s.find(')', start)
    if start != -1 and end != -1:
        result = s[start + 1:end]
        print(result)
    else:
        print("Скобки не найдены.")
input_string = "Тест (внутри скобок)."
extract_inside_brackets(input_string)
#№3#
import re
text = input().lower()
print(re.findall(r'\bа\w+я\b', text))
