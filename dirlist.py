from PyInquirer import prompt

import os, glob

os.chdir('./')

questions1 = [{
    'type': 'list',
    'name': 'dir',
    'message': 'Which dir you want'
}]

questions2 = [{
    'type': 'list',
    'name': 'continue',
    'message': 'you wanna continue',
    'choices': ['Yes', 'No'],
}]
 
def pDir(dirs) -> list:
    dir_list = [ f for f in dirs]
    return dir_list

def continue_navigate():
    answer = prompt(questions2)
    return answer['continue']
    
def navigate():
    questions1[0]['choices'] = glob.glob('**/')
    answer = prompt(questions1)
    os.chdir(answer['dir'])
    if continue_navigate():
        try:
            navigate()
        except IndexError as e:
            os.system('explorer.exe .')
    else:
        os.system('explorer.exe .')
if __name__ == '__main__':
    navigate()
    