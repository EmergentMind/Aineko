import settings

class ConsoleHandler(object):
  def __init__(self):
    self.console_prompt = settings.PROMPT
    self.messageOut(settings.INITIAL_GREETING)

  def messageIn(self):
    return input(self.console_prompt)

  def messageOut(self, msg):
    print(msg)