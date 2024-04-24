from input import input_data

##https://jsmachines.sourceforge.net/machines/slr.html use this 
class parse:
    def __init__(self):
        self.test1 = ''
    
    def parse_action(self):
        #initalize stack array 
        stack = []

        #initalize input string to get the input array values
        parse_string = input_data()
        input_array = parse_string.split_string()

        #loop until the input string is complete
        for index in range(len(input_array)):
            print (f"Steps: {index+1} ,\nStack: {stack} , \nInput: {input_array} , \nAction: ")

            #pop initial value inside of array and append into the stack
            popped_value = input_array.pop(0)
            stack.append(popped_value)
        
        #print final result
        print (f"Steps: {index+2} ,\nStack: {stack} , \nInput: {input_array} , \nAction: ")
        return 0
    
    def parse_table():
        
        #production rules + table goes here
        states = {
            "state_0": {
                "(": "s4",
                "id": "s5",
                "E": "state_1",
                "T": "state_2",
                "F": "state_3",
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
                "E": "state_8",
                "T":  "state_2",
                "F": "state_3",
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
                "T": "state_9",
                "F": "state_3",

            },

            "state_7": {
                "(": "s4",
                "id": "s5",
                "F": "state_10",
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

        return 0
    """
    state counter which would tell us which state it would be in
    take the current input and move along the states 
    look at stack and the input to see if it is valid among one of the states 
    if true, pop out of the input and into the stack
    see if the action is reduce (r5) or shift(s5)
    if reduce, read the production rules and adjust the stack if necessary 
    """

    """
    example: id + id * id
    step 1, stack 0, input id + id * id $, action s5
    step 2, stack 0, id 5, input + id * id $, action r6
    """

    """ MAYBE CREATE AN OBJECT TO HOLD THESE
    def __init__(self):
    self.stack = stack1 (figure out which stack can look through and can't)
    self.step = 0 (add one everytime an action is completed)
    self.stack = "0id5" 
    self.input = "+id*id$"
    self.action = r6
    """

    """
    check which state we are in (state 0)
    look at input (id + id * id)
    compare that to the LR table (id -> s5)
    do the action (shift the id into the stack)
    in that state is there other actions to do (reduce production 4, reduce production 2) 
    """

    """
    read the periods to figure out which production rules go where to compare properly 
    """

    """
    shift means pop()
    reduce means change values in stack
    """