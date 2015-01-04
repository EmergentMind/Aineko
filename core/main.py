'''
    Interprets input, sends data for additional processing by relevant modules, then submits results for output.
'''
import settings

class Processor:
    def __init__ (self):
        self.shutDown = False

    def handleInput(self, data):  
        if data.startswith("!!"):
            commandOutput = self.parseCommand(data)
            return commandOutput
 
        elif (data):
            return "Thanks for your input."

        else:
            return "Did you say something?"

    #Execute commands and return the outcome
    def parseCommand(self, data):
        if data.startswith("!!exit"):
            self.shutDown = True
            return settings.SHUTDOWN_MSG
        else:
            return "Your command was not recognized."

class Result:
    def __init__(self):
        self.DataProcessed = False
        self.Origin
        self.Message
