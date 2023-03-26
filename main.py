'''
py trainer
created by: Arlo Gittings
created on: 2023-03-26
updated by: Arlo Gittings
updated on: 2023-03-26
description:
    A modularized trainer, concentrating in a few practical areas or 
    types. In particular memorization, key concepts, kata, spot the bug
    and what is the outcome.

'''
def get_command():
    command_string = input('}> ')
    return command_string.split()

def parse_command(commands):
    return True if commands != [] else False 


def main():
    running = True
    while running:
        running = parse_command(get_command())


if __name__ == '__main__':
    main()
