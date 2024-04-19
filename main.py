from parse_tree import parse 
def main():

    parse_result = parse()
    parse_result.parse_action()

    return 0

if __name__ == "__main__":
    main()