class parse:
    def __init__(self):
        self.test1 = "(id+id)*id$"
        self.test2 = "id*id$"
        self.test3 = "(id*)$"

    
    def parse_action(self):
        test = self.test1

        for char in test:
            print(char)
        
        return 0