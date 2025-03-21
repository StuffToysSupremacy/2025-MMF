# Functions go here
def string_check(question, valid_ans_list=('yes','no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main routine go here
# payment_ans = ['cash', 'credit']

while True:
    want_instructions = string_check("Do you want to see the instructions? ")
    print(f"You chose {want_instructions}")
    print()

# payment_method = string_check("Payment method: ", payment_ans, 2)
# print(f"You choose {payment_method}")


