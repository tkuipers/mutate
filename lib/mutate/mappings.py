import tree_sitter
import tree_sitter_python
import tree_sitter_go
import mimetypes
from pathlib import Path

python: tree_sitter.Language = tree_sitter.Language(tree_sitter_python.language())
go: tree_sitter.Language = tree_sitter.Language(tree_sitter_go.language())

language_bindings: dict[str, tree_sitter.Language] = {
  'text/x-python': python,
  'text/x-go': go,
}

class Mappings:
  def __init__(self):
    mimetypes.add_type('text/x-go', '.go')
    # mimetypes.add_type('text/x-python', '.py')
    # mimetypes.add_type('text/x-php', '.php')
    # mimetypes.add_type('text/x-java', '.java')
    # mimetypes.add_type('text/x-csharp', '.cs')
    # mimetypes.add_type('text/x-c', '.c')
    # mimetypes.add_type('text/x-cpp', '.cpp')
    # mimetypes.add_type('text/x-ruby', '.rb')
    # mimetypes.add_type('text/x-rust', '.rs')

  def get_language(self, path: Path) -> tree_sitter.Language:
    mime_type, _ = mimetypes.guess_type(path)
    return language_bindings.get(mime_type, None)

