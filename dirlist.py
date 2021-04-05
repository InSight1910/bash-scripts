from PyInquirer import prompt
import os, glob, pyperclip



os.chdir('./')

questions1 = [{
    'type': 'list',
    'name': 'dir',
    'message': 'Which dir you want'
}]

question2 = [
    {
        'type': 'confirm',
        'name': 'explorer',
        'message': 'Open explorer',
        'default': False
    }
]




 
def pDir() -> list:
    dir_list = [ f for f in glob.glob("**/")]
    return dir_list
    
def continue_nav():
    answer = prompt(question2)
    return answer['explorer']

def navigate():
    questions1[0]['choices'] = glob.glob('**/')
    questions1[0]['choices'].insert(0, './')
    questions1[0]['choices'].insert(1, '../')
    answer = prompt(questions1)
    os.chdir(answer['dir'])
    if answer['dir'] == './': 
        if continue_nav():
            os.system('explorer.exe .')
        pyperclip.copy(os.getcwd().replace(' ', '\\ '))
        return
        
    try:
        navigate()
    except IndexError as e:
        os.system('explorer.exe .')

if __name__ == '__main__':
    navigate()
    
    
    