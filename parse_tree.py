class parse:
    def __init__(self):
        self.test1 = "(id+id)*id$"
        self.test2 = "id*id$"
        self.test3 = "(id*)$"

    
    def parse_action(self):
        test = self.test1
        compare_id = "id"
        index = 0
        while index < len(test):
            if test[index:index+len(compare_id)] == compare_id:
                print(f"{compare_id}, {index}")
                index += len(compare_id)
                
            else:
                print(f"{test[index]}, {index}")
                index += 1

        return 0