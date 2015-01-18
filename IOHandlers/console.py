import abc
from IOHandlers.IOBase import IOBase
import getpass

class ConsoleHandler(IOBase):
    ''' Handle input and outpt between aineko core and the console. '''
    def __init__(self, consoleSettings):
        self.console_prompt = consoleSettings['prompt']
        self.messageOut(consoleSettings['initial_greeting'])
        self.messageOut(consoleSettings['prompt'])

    def messageIn(self, customPrompt=None, charsRequired=False):
        ''' customPrompt - specify a custom prompt for the required input, such as 'Enter Password:'
        '''
        userInput = ''

        while True:
            if customPrompt is None:
                userInput = input(self.console_prompt)
            else:
                userInput = input(customPrompt)
        
            if not charsRequired:
                break
            elif charsRequired and userInput != '':
                break
            else:
                self.messageOut("You must enter a value to continue.")
    
        return userInput

    def passwordIn(self, customPrompt):
        return getpass.getpass(customPrompt)

    def messageOut(self, msg):
        print(msg)
