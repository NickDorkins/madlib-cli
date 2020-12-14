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
      
    try:
        with open(path, 'r') as path_string:
            contents = path_string.read()
            returned_string = str(contents)
            print(returned_string)
            return(returned_string)
    except FileNotFoundError:
        raise FileNotFoundError('File not found')
        

def parse_template(string):
    # [{]w\[}] 
    #s[s.find("{")+1:s.find("}")]
    # language_parts = []
    # parse = str.split('Adjective', 'Noun')
    #  list --> remove curly --> tuple
    # for i in parse:
    # string_edit = parse.remove("'", "", *)
    # while { in parse: parse.remove({)
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
    
    # template = string.remove
    # iterate through for loop
    # Remove first and last elements per iteration
    # return string without culy brackets 
    # print(string_edit)


parse_template("It was a {Adjective} and {Adjective} {Noun}.")