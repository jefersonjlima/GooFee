''' Actions Object '''

class Action:

    def __init__(self, config, args):
        self.config = config
        self.args = args

    def selectAction(self):
        if   self.args['option'] == 'UPDATE':
            print("UPDATE Mode")
        elif self.args['option'] == 'SHOW':
            None
        elif self.args['option'] == 'UP':
            None
        elif self.args['option'] == 'DOWN':
            None
        else:
            None


