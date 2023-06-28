def ask_yes_or_no(question: str) -> bool:
    user_input = input(f'{question} [Y/N]: ')
    if user_input.upper() == 'Y':
        return True
    elif user_input.upper() == 'N':
        return False
    else:
        print('Invalid response. Please indicate "Y" or "N".')
        return ask_user_yes_or_no(question)