from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        destination = self.dest
        relative_to_source = path.relative_to(self.source)
        directory = destination / relative_to_source
        directory.mkdir(parents = True, exist_ok = True)

    def build():
        self.dest.mkdir(parents = True, exist_ok = True)
