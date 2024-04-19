from input import input_data

class parse:
    def __init__(self):
        self.test1 = ''
    
    def parse_action(self):

        parse_string = input_data()
        result = parse_string.split_string()
        print(result)
        return 0