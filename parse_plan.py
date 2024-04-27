from input import input_data
class parse_class:
    def __init__(self):
        self.parse_table = {0: {"id": "s5", "(": "s4", "E": 1, "T": 2, "F": 3},
                            1: {"+": "s6", "$": "accept"},
                            2: {"+": "r2", "*": "s7", ")": "r2", "$": "r2"},
                            3: {"+": "r4", "*": "r4", ")": "r4", "$": "r4", },
                            4: {"(": "s4", "id": "s5", "E": 8, "T": 2, "F": 3, },
                            5: {"+": "r6", "*": "r6", ")": "r6", "$": "r6", },
                            6: {"(": "s4", "id": "s5", "T": 9, "F": 3, },
                            7: {"(": "s4", "id": "s5", "F": 10, },
                            8: {"+": "s6", ")": "s11", },
                            9: {"+": "r1", "*": "s7", ")": "r1", "$": "r1", },
                            10: {"+": "r3", "*": "r3", ")": "r3", "$": "r3", },
                            11: {"+": "r5", "*": "r5", ")": "r5", "$": "r5", },
        }
                           
        self.reduce_table = {"r1": ("E", "E", "+", "T"), "r2": ("E", "T"), "r3": ("T", "T", "*", "F"), 
                             "r4": ("T", "F"), "r5": ("F", "(", "E", ")"), "r6": ("F", "id")}
        
        self.stack_state = [0]
        
        self.stack = [0]

    def parse_input(self):
        
        state = 0
        #split the input into separate tokens 
        input_string = input_data()
        split_string = input_string.split_string()

        for index in range (len(split_string)+6):
            parse_action = self.parse_table[state][split_string[0]]

            print(f"current parse_action: {parse_action}")

            if parse_action.startswith("s"):
                
                self.shift(split_string)
                state = int(parse_action[1:])
                self.stack_state.append(state)

                #print(f"state: {state}")
                print (f" state stack: {self.stack_state}")

            elif parse_action.startswith("r"):

                self.reduce(parse_action)
                state = self.stack_state[-1]

                #print(f"state: {state}")
                print (f" state stack: {self.stack_state}")
                
        return 0

    def shift(self, string):

        popped = string.pop(0)
        self.stack.append(popped)

        print(f"string: {string}")
        print(f"stack: {self.stack}")
        print (f" state stack: {self.stack_state}")
        return 0
    
    def reduce(self, parse_action):       
        reduce_action = self.reduce_table[parse_action] # get the reduce action -> r2

        print(f"reduce_action: {reduce_action}")
        #print(len(reduce_action))
        print(f"stack_state: {self.stack_state}")
        print (f" stack: {self.stack}")

        for _ in range(len(reduce_action)- 1):
            self.stack.pop()
            self.stack_state.pop(-1)
        
        print (f" stack: {self.stack}")
        print (f" state stack: {self.stack_state}")

        #self.stack_state.pop(-1)

        print (f" state stack: {self.stack_state}")
        print(f"reduce_action: {reduce_action}")

        new_state = self.parse_table[self.stack_state[-1]][reduce_action[0]]

        print (f"new_state: {new_state}")

        self.stack_state.append(new_state)
        self.stack.append(reduce_action[0])
        
        print (f" stack: {self.stack}")
        print(f"stack_state: {self.stack_state}")
        return 0
