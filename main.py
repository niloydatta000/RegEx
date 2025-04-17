# main script to run the regex helper
# user input guide

from regex.regex_helper import explain, search_by_description, regex_patterns


if __name__ == "__main__":
    user_input = input("Enter a regex pattern or description: ").strip()
    if user_input in regex_patterns:
        print(explain(user_input))
    else:
        print("Searching for description...")
        results = search_by_description(user_input)
        for result in results:
            print(result)