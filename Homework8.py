#№1#
import re
text = input()
if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', text):
    print('private')
elif re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', text):
    print('taxi')
else:
    print('Faild')
#№2#
text = input()
print(len(re.findall(r'\b\w[\w-]*\b', text)))
#№3#
import re
def replace_time_with_tbd(text): 
    return re.sub(r'\b\d{2}:\d{2}(:\d{2})?\b',  '(TBD)',  text)
text = "Уважаемые! Если вы к 09:00 не вернёте чемодан,  то уже в 09:00:01 я за себя не отвечаю."
new = replace_time_with_tbd(text)
print(new)
