from fr_parser import Parser


def main() -> None:
    p = Parser('https://freelance.habr.com/tasks', 'ts')
    p.start_parse()


if __name__ == '__main__':
    main()
