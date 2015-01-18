'''
    Interprets input, sends data for additional processing by relevant modules, then
    submits results for output.
'''

class Processor:
    def __init__ (self, behaviourSettings):
        self.commandInitiator = behaviourSettings['command_initiator']
        self.shutDownMsg = behaviourSettings['shutdown_msg']
        self.shutDown = False

    def handleInput(self, data):  
        if data.startswith(self.commandInitiator):
            commandOutput = self.parseCommand(data)
            return commandOutput
 
        elif (data):
            return "Thanks for your input."

        else:
            return "Did you say something?"

    #Execute commands and return the outcome
    def parseCommand(self, data):
        if data.startswith(self.commandInitiator + "exit"):
            self.shutDown = True
            return self.shutDownMsg
        else:
            return "Your command was not recognized."
