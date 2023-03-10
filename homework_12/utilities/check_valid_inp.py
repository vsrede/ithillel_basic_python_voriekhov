def get_input_str(prompt=None, options=None):
    if prompt is None:
        prompt = 'Enter something...: '
    a = ''
    while True:
        a = input(prompt)
        if options:
            if a in options:
                print(options[a])
                return True
            else:
                print('Try again, valid enter "y" or "n": ')
