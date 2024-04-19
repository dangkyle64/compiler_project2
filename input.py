class input_data:
    
    def __init__(self):
        self.test1 = "(id+id)*id$"
        self.test2 = "id*id$"
        self.test3 = "(id*)$"

    #split the given input into parts to make it easier to compare the inputs
    def split_string(self):
        test = self.test1
        index = 0
        compare_id = "id"

        #initialize array to be returned
        test_input = []

        while index < len(test):
            if test[index:index+len(compare_id)] == compare_id:
                
                #append to array to better organize inputs for parse table comparison (ID HERE)
                test_input.append(compare_id)
                index += len(compare_id)
            else:
                #append to array to better organize inputs for parse table comparison (OTHER CHARACTERS HERE)
                test_input.append(test[index])
                index += 1
        
        return test_input