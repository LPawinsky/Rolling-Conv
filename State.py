class State:
    def __init__(self, path, output_path, version):
        self.path = path
        self.output_path = output_path
        self.version = version

    def update_path(self, val):
        self.path = val

    def update_output(self, val):
        self.output_path = val

    def reset_state(self):
        self.path = None
        self.output = None
    
