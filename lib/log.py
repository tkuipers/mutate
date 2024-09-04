from cleo.commands.command import Command
from cleo.io.outputs.output import Verbosity


class Log:
  def __init__(self, cleo: Command, log_name: str):
    self.log_name = log_name
    self.cleo = cleo

  def error(self, message: str):
    self.cleo.line_error(message, "error", verbosity=Verbosity.NORMAL)

  def warn(self, message: str):
    self.cleo.line(message, "warning", verbosity=Verbosity.NORMAL)

  def info(self, message: str):
    self.cleo.line(message, "info", verbosity=Verbosity.NORMAL)

  def comment(self, message: str):
    self.cleo.line(message, "comment", verbosity=Verbosity.VERBOSE)

  def debug(self, message: str):
    self.cleo.line(message, "debug", verbosity=Verbosity.VERY_VERBOSE)
