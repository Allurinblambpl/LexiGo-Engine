class ScriptRunner:
    def __init__(self):
        self.scripts = []

    def load_script(self, script):
        """Load a script (a Python file)."""
        with open(script, 'r') as file:
            self.scripts.append(file.read())

    def execute_scripts(self):
        """Execute all loaded scripts."""
        for script in self.scripts:
            exec(script)
