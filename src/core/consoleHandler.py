import settings

class ConsoleHandler(object):
  
  def __init__(self):
    self.console_prompt = settings.PROMPT
    self.userInput = False
    
  def listener(self):
    self.Output(settings.INITIAL_GREETING)
    
    while True:
      self.userInput = self.getInput()
     
      if (self.ExitCheck(self.userInput)):
        self.Output("Goodbye.")
        break
      elif (self.userInput):
        self.Output("Thanks for your input.")
        continue
      else:
        self.Output("Did you say something?")
        continue
        
  def getInput(self):
    newInput = input(self.console_prompt)
    return newInput
     
  def Output(self, response):
    print (response)

  def ExitCheck(self, curInput):
    if (curInput == settings.COMMAND_INITIATOR + "exit"):
      return True
    else:
      return False 


