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
        self.step = 0

####################################################################################

    def parse_input(self):
        
        state = 0

        #split the input into separate tokens 
        input_string = input_data()
        split_string = input_string.split_string()

        #loop through the array of tokens given 
        for index in range (len(split_string)+12):

            #compare token to the parse table and return an action

            if split_string[0] in self.parse_table[state]:
                parse_action = self.parse_table[state][split_string[0]]

            else:
                print(f"String invalid")
                return 0                

            #print(f"current parse_action: {parse_action}")

            #look for parse_action shift
            if parse_action.startswith("s"):
                
                self.shift(split_string)

                #take the integer from the parse_action since its our new state
                state = int(parse_action[1:])

                #store the new state into the state_stack
                self.stack_state.append(state)

                #print(f"state: {state}")
                #print (f" state stack: {self.stack_state}")

                self.step += 1
                print (f"Step: {self.step}, Stack: {self.stack}, Input: {split_string}, Action: {parse_action}")
            #look for parse_action reduce
            elif parse_action.startswith("r"):
                self.reduce(parse_action)

                #after reducing, take the last known state from stack_state
                state = self.stack_state[-1]

                #print(f"state: {state}")
                #print (f" state stack: {self.stack_state}")

                self.step += 1
                print (f"Step: {self.step}, Stack: {self.stack}, Input: {split_string}, Action: {parse_action}")
            #look for accept which means the string is accepted
            elif "accept" in parse_action:
                self.step += 1
                print (f"Step: {self.step}, Stack: {self.stack}, Input: {split_string}, Action: {parse_action}")
                print ("Input accepted")
                return 0
            
            #if string is invalid based on the parse table
            else:
                print ("String not accepted")
                
        return 0

    def shift(self, string):

        #pop the first instance in the array 
        popped = string.pop(0)

        #append into the stack
        self.stack.append(popped)

        #print(f"string: {string}")
        #print(f"stack: {self.stack}")
        #print (f" state stack: {self.stack_state}")
        return 0
    
    def reduce(self, parse_action):

        #get the reduction rule from the parse action and reduction table
        reduce_action = self.reduce_table[parse_action] 

        #print(f"reduce_action: {reduce_action}")
        #print(len(reduce_action))
        #print(f"stack_state: {self.stack_state}")
        #print (f" stack: {self.stack}")

        #loop based on how many characters on right side of the reduction rule
        for _ in range(len(reduce_action)- 1):

            #pop old value out of the stack
            self.stack.pop()

            #pop old states out of stack_state to find next valid state
            self.stack_state.pop(-1)
        
        #print (f" stack: {self.stack}")
        #print (f" state stack: {self.stack_state}")
        #print (f" state stack: {self.stack_state}")
        #print(f"reduce_action: {reduce_action}")


        #find the next valid state using the stack_state and the reduction replacement
        new_state = self.parse_table[self.stack_state[-1]][reduce_action[0]]

        #print (f"new_state: {new_state}")

        #append new state into the stack_state
        self.stack_state.append(new_state)

        #replace the old popped value with the reduction rule result
        self.stack.append(reduce_action[0])

        #print (f" stack: {self.stack}")
        #print(f"stack_state: {self.stack_state}")
        return 0
