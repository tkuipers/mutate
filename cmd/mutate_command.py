from cleo.commands.command import Command
from cleo.helpers import argument, option
from lib.log import Log

import os
from pathlib import Path
import mimetypes

from lib.mutate.mappings import Mappings
from lib.mutate.mutator import Mutator

def safe_reference(file_path: Path) -> Path:
  path = Path(file_path)
  path = path.expanduser()
  path = path.resolve()
  return path
class MutateCommand(Command):
  name = "mutate"
  description = "Mutate a source file"
  arguments = [
    argument(
      "file",
      description="The file you would like to mutate",
      optional=False
    )
  ]
  options = [
    option(
      "rate",
      "r",
      description="The mutation rate, a percentage.",
      flag=False,
      default=0.05,
    )
  ]

  def __init__(self):
    super().__init__()
    self.log = Log(self, "mutate")

  def handle(self):
    file = self.argument("file")
    rate = self.option("rate")
    # convert rate to float
    rate = float(rate)
    assert rate <= 1, "Cannot set the rate above 1"
    assert rate >= 0, "Cannot set the rate below 0"
    file = safe_reference(file)
    assert file.exists(), f"File does not exist: {file}"
    self.log.info(f"Mutating file: {file}")
    mutator = Mutator()
    mutator.mutate_file(file, rate)


