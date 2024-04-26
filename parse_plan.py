from input import input_data

class parse_class:
    def __init__(self):
        self.parse_table = {0: {"id": "s5", "(": "s4", "E": 1, "T": 2, "F": 3},
                            1: {"+": "s6", "$": "accept"},
                            2: {"+": "r2", "*": "s7", ")": "r2", "$": "r2"},
                            3: {"+": "r4", "*": "r4", ")": "r4", "$": "r4", },
                            4: {"(": "s4", "id": "s5", "E": "8", "T": "2", "F": "3", },
                            5: {"+": "r6", "*": "r6", ")": "r6", "$": "r6", },
                            6: {"(": "s4", "id": "s5", "T": "9", "F": "3", },
                            7: {"(": "s4", "id": "s5", "F": "10", },
                            8: {"+": "s6", ")": "s11", },
                            9: {"+": "r1", "*": "s7", ")": "r1", "$": "r1", },
                            10: {"+": "r3", "*": "r3", ")": "r3", "$": "r3", },
                            11: {"+": "r5", "*": "r5", ")": "r5", "$": "r5", },
        }
                           
        self.reduce_table = {"r1": ("E", "E", "+", "T"), "r2": ("E", "T"), "r3": ("T", "T", "*", "F"), 
                             "r4": ("T", "F"), "r5": ("F", "(", "E", ")"), "r6": ("F", "id")}
        
        self.stack = [0]

    def parse_input(self):
        
        state = 0
        #split the input into separate tokens 
        input_string = input_data()
        split_string = input_string.split_string()

        for index in range (len(split_string)):
            parse_action = self.parse_table[state][split_string[0]]

            print(f"current parse_action: {parse_action}")

            if parse_action.startswith("s"):
                self.shift(split_string)
                state = int (parse_action[1:])

        return 0

    def shift(self, string):

        popped = string.pop(0)
        self.stack.append(popped)

        print(string)
        print(self.stack)
        return 0
    
    def reduce():
        return 0
    
    
"""

read each section and compare to chart

return action 

shift function
    check if s is there
    pop the input into the stack
    use the number to go to the right state

reduce function
    check if r is there
    check the stack and compare to the action
    pop out as many needed from the reduction
    take the state from the last point


"""
