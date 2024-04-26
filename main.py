from parse_tree import parse
from parse_plan import parse_class
def main():

    #parse_result = parse()
    #parse_result.parse_action()

    parse_test = parse_class()
    parse_test.parse_input()

if __name__ == "__main__":
    main()