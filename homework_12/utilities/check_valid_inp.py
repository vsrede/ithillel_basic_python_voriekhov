def get_input_str(prompt=None, options=None):
    while True:
        user_input = input(prompt) if prompt else input()
        if not options:
            return user_input
        if user_input in options:
            return options[user_input]
        print('Try again. Valid options are: {}'.format(', '.join(options.keys())))
