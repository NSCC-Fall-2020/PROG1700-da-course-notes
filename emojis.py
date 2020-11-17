import sys

emojis = {
    'smile': '\U0001F600',
    'santa': '\U0001F385',
    'elf': '\U0001F9DD',
    'poop': '\U0001F4A9'
}


def show_emoji(name="poop"):
    print(emojis[name], end='')


def print_help():
    print("Usage: emojis.py <name> ...")


def main():
    if len(sys.argv) > 1:

        if sys.argv[1] == "-h":
            print_help()
            sys.exit(0)

        for name in sys.argv[1:]:
            if name in emojis:
                show_emoji(name)
            else:
                print()
                print('Unknown emoji name.')
                sys.exit(-1)
    else:
        print_help()


if __name__ == "__main__":
    main()