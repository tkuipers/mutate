from pathlib import Path

from tree_sitter._binding import Parser

from lib.mutate.mappings import Mappings


class Mutator:
  def __init__(self):
    self.mappings = Mappings()

  def mutate_file(self, file: Path, rate: float) -> str:
    language = self.mappings.get_language(file)
    assert language is not None, f"Unsupported language: {file}"
    parser = Parser(language)
    with open(file, "r") as f:
      source = f.read()
    tree = parser.parse(bytes(source, "utf8"))
    root = tree.root_node
    print(root)