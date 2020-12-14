import re 

print('*'*40)
print ('**' + ' '*9 + 'Welcome to MadLibs' + ' '*9 + '**')
print ('**' +' '*36 +  '**')
print ('**' + '  ' + 'Please fill in the template and   ' + '**')
print ('**' + '  ' + 'read the magical adventure that' + '   ' + '**')
print ('**' + '  ' + 'follows.' + ' '*26 +  '**')
print ('**' +' '*36 +  '**')
print('*'*40)



def read_template(path):
    """[Passed a file path, read file and return the contents as a string, raise FileNotFoundError if file path is incorrect.]

    Args:
        path ([open]): [Read file path, return the contents of the file as a single string. ]

    Raises:
        FileNotFoundError: [Raise error if the file path is incorrect.]
    """      
    try:
        with open(path, 'r') as path_string:
            contents = path_string.read()
            returned_string = str(contents)
            print(returned_string)
            return(returned_string)
    except FileNotFoundError:
        raise FileNotFoundError('File not found')
        

def parse_template(string):
    """[Takes in a string, returns two separate values. Returns a a string with language parts removed and a list of the removed language parts. ]

    Args:
        string ([string]): [String value with language parts in curly brackets. ]
    """    
    parse = re.findall(r'\{.*?\}', string)
    final_list = []
    for i in parse:
        string_edit = (i[1:-1])
        final_list.append(string_edit)
    correct_list = tuple(final_list)
    print("CORRECT_LIST", correct_list)
    template = re.sub(r'\{.*?\}', "{}", string)
    print("TEMPLATE", template)
    return(template, correct_list)


