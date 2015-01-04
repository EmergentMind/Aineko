''' Handle input and outpt between aineko core and the console. '''

import abc
from IOHandlers.IOBase import IOBase
import settings
import getpass

class ConsoleHandler(IOBase):
    def __init__(self):
        self.console_prompt = settings.PROMPT
        self.messageOut(settings.INITIAL_GREETING)
        self.messageOut(settings.PROMPT)

    def messageIn(self, customPrompt=None, charsRequired=False):
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
