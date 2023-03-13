import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def dict(val): 
    if val in data:
        return data[val]
    elif val.capitalize() in data:
        return data[val.capitalize()]
    elif len(get_close_matches(val, data.keys())) > 0:
        YN = input("Did you mean %s instead ? Enter Y if yes, or N if no " % get_close_matches(val, data.keys())[0])
        if YN == "Y".lower() :
            return data[get_close_matches(val, data.keys())[0]]
        elif YN == "N".lower():
            return 'word not found double check'   
        else:
            return  'Didnt understand your entry'
    else:
         return  'The word doesnt exits'

word = input('Enter your word: ').lower()
output = dict(word)
if type(output) == list:
     for item in output:
        print(item)
else:
       print(output)