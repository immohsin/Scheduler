
class Task:
    def __init__(self, callback, priority, args=None):
        self.callback = callback
        self.priority = priority
        self.args = args

    def __call__(self):
        self.callback(*self.args)

    def prioritize(self):
        return self.priority, self.callback, self.args
