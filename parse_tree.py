from input import input_data

##https://jsmachines.sourceforge.net/machines/slr.html use this 
class parse:
    def __init__(self):
        self.test1 = ''
        #production rules + table goes here
        self.states = {
            "state_0": {
                "(": "s4",
                "id": "s5",
                "E": "1",
                "T": "2",
                "F": "3",
            },

            "state_1": {
                "+": "s6",
                "$": "accept",
            },

            "state_2": {
                "+": "r2",
                "*": "s7",
                ")": "r2",
                "$": "r2",
            },

            "state_3": {
                "+": "r4",
                "*": "r4",
                ")": "r4",
                "$": "r4",
            },

            "state_4": {
                "(": "s4",
                "id": "s5",
                "E": "8",
                "T": "2",
                "F": "3",
            },

            "state_5": {
                "+": "r6",
                "*": "r6",
                ")": "r6",
                "$": "r6",
            },

            "state_6": {
                "(": "s4",
                "id": "s5",
                "T": "9",
                "F": "3",

            },

            "state_7": {
                "(": "s4",
                "id": "s5",
                "F": "10",
            },

            "state_8": {
                "+": "s6",
                ")": "s11",
            },

            "state_9": {
                "+": "r1",
                "*": "s7",
                ")": "r1",
                "$": "r1",
            },

            "state_10": {
                "+": "r3",
                "*": "r3",
                ")": "r3",
                "$": "r3",
            },

            "state_11": {
                "+": "r5",
                "*": "r5",
                ")": "r5",
                "$": "r5",
            },

        }

        self.reduce_table = {
            "r1": ("E", "E"),
            "r2": ("E", "E", "+", "T"),
            "r3": ("T", "T", "*", "F"),
            "r4": ("T", "F"),
            "r5": ("F", "(", "E", ")"),
            "r6": ("F", "id"),
        }
    
    def parse_action(self):
        index = 1
        state = "state_0" 
        stack = [0]

        #initalize input string to get the input array values
        parse_string = input_data()
        input_array = parse_string.split_string()

        #loop until the input string is complete
        while index != 10:
            
            #Put input from the front of input_array in to compare with parse table
            parse_table_action = self.parse_table(state, input_array[0])
            
            print(f"Steps: {index} ,Stack: {stack} , Input: {input_array} , Action: {parse_table_action}")
            index += 1

            if "s" in parse_table_action:

                #check for which state program is in based on action
                if "3" in parse_table_action:
                    state = "state_3"         
                
                if "4" in parse_table_action:
                    state = "state_4"

                if "5" in parse_table_action:
                    state = "state_5"

                if "6" in parse_table_action:
                    state = "state_6"

                if "7" in parse_table_action:
                    state = "state_7"

                if "10" in parse_table_action:
                    state = "state_10"

                #pop initial value inside of array and append into the stack
                popped_value = input_array.pop(0)
                stack.append(popped_value)

            if "r" in parse_table_action:
                
                reduce_compare = self.reduce_table[parse_table_action]
                print (f"reduce: {len(reduce_compare)}")
                for _ in range(len(reduce_compare)):
                        print(f"stack: {stack}")
                        if stack:
                            stack.pop()
                
                left_side = reduce_compare[0]
                stack.append(left_side)
                print(stack)
                state = self.get_next_state(state, left_side)
                print(state)
                """
                reduce_table = {
                "id": "F",
                "F": "T",
                "T": "E",
                "E": "E'"
                }

                #pop the old value in the stack
                popped_stack = stack.pop(-1)
                #print(f"Popped stack: {popped_stack}")

                #compare the values to the reduce table
                next_stack_state = reduce_table.get(popped_stack, "invalid")
                #print (f"Next stack state: {next_stack_state}")

                #append new value into the stack
                stack.append(next_stack_state)

                if "F" in next_stack_state:
                    state = "state_3"
                if "T" in next_stack_state:
                    state = "state_2"
                """

            print(state)
        #print final result
        #print (f"Steps: {index+2} ,\nStack: {stack} , \nInput: {input_array} , \nAction: ")
        return 0
    
    def parse_table(self, current_state, current_input):
        
        #Compare input value with table, return action
        compare_with_dictionary = self.states.get(current_state, {})
        #print(compare_with_dictionary)

        #Get the key and value from the compared values, return invalid if not found
        next_state = compare_with_dictionary.get(current_input, 'invalid')
        #print(next_state)

        return next_state
    
    def get_next_state(self, current_state, value):
        next_state = self.states[current_state].get(value)

        if next_state is not None and next_state.startswith("s"):
            return int(next_state[1:])
        else:
            return next_state
   