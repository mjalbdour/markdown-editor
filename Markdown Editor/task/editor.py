# EDITOR STATE
markdown = """"""

# FILES
OUTPUT_FILE_NAME = "output.md"

# OPTIONS
OPTION_HELP = "!help"
OPTION_DONE = "!done"

# MESSAGES
MSG_HELP = """Available formatters: plain bold italic header link inline-code new-line
Special commands: !help !done"""
MSG_FORMATTER = "Choose a formatter: "
MSG_TEXT = "Text: "
MSG_LEVEL = "Level: "
MSG_LABEL = "Label: "
MSG_URL = "URL: "
MSG_ROW = "Row "
MSG_ROWS = "Number of rows: "
MSG_ERROR_LEVEL = "The level should be within the range of 1 to 6"
MSG_ERROR_ROWS = "The number of rows should be greater than zero"
MSG_UNKNOWN_FORMATTING = "Unknown formatting type or command"

# MAPPING: INPUT TO MESSAGE
TITLE_FORMATTER = "Formatter"
TITLE_TEXT = "Text"
TITLE_LEVEL = "Level"
TITLE_LABEL = "Label"
TITLE_URL = "URL"
TITLE_ROWS = "Rows"
title_types_msgs = {
    TITLE_FORMATTER: MSG_FORMATTER,
    TITLE_TEXT: MSG_TEXT,
    TITLE_LEVEL: MSG_LEVEL,
    TITLE_LABEL: MSG_LABEL,
    TITLE_URL: MSG_URL,
    TITLE_ROWS: MSG_ROWS
}


# IMPLEMENTATION: OPTIONS
def apply_option_help():
    print(MSG_HELP)


def apply_option_done():
    file = open(OUTPUT_FILE_NAME, 'w+')
    file.write(markdown)
    file.close()


# IMPLEMENTATION: INPUTS
def input_text(title_type):
    print(title_types_msgs[title_type], end='')
    return input()


def input_level():
    while True:
        level = int(input_text(TITLE_LEVEL))
        if not 1 <= level <= 6:
            print(MSG_ERROR_LEVEL)
            continue
        else:
            return level


def input_row(row_number):
    print(f'Row #{row_number}: ', end='')
    return input()


def input_rows():
    while True:
        print(MSG_ROWS, end='')
        rows = int(input())
        if not rows > 0:
            print(MSG_ERROR_ROWS)
        else:
            return rows


# IMPLEMENTATION: FORMATTERS
def format_header():
    level = input_level()
    text = input_text(TITLE_TEXT)
    conditional_new_line = ''
    if markdown != """""":
        conditional_new_line = '\n'
    return f'{conditional_new_line}{"#" * level} {text}{format_new_line()}'


def format_bold():
    text = input_text(TITLE_TEXT)
    return f'**{text}**'


def format_plain():
    return input_text(TITLE_TEXT)


def format_inline_code():
    text = input_text(TITLE_TEXT)
    return f'`{text}`'


def format_new_line():
    return '\n'


def format_link():
    label = input_text(TITLE_LABEL)
    url = input_text(TITLE_URL)
    return f'[{label}]({url})'


def format_italic():
    text = input_text(TITLE_TEXT)
    return f'*{text}*'


def format_list(ordered=True):
    rows = input_rows()
    string = ""
    if markdown != """""":
        string += '\n'
    for i in range(1, rows + 1):
        text = input_row(i)
        if ordered:
            string += f'{i}. {text}\n'
        else:
            string += f'* {text}\n'

    return string


# MAPPING: FORMATTER TO IMPLEMENTATION
formatters = {
    "plain": format_plain,
    "bold": format_bold,
    "italic": format_italic,
    "header": format_header,
    "link": format_link,
    "inline-code": format_inline_code,
    "new-line": format_new_line,
    "ordered-list": lambda: format_list(),
    "unordered-list": lambda: format_list(ordered=False)
}

# MAPPING: OPTION TO IMPLEMENTATION
options = {
    OPTION_HELP: apply_option_help,
    OPTION_DONE: apply_option_done
}


# GATE: FORMATTERS
def apply_formatter(formatter):
    return formatters[formatter]()


# GATE: OPTIONS
def apply_option(option):
    options[option]()


# ENTRANCE
while True:
    choice = input_text(TITLE_FORMATTER)
    if choice in formatters:
        markdown += apply_formatter(choice)
    elif choice in options:
        apply_option(choice)
        if choice == OPTION_DONE:
            break
    else:
        print(MSG_UNKNOWN_FORMATTING)
        continue

    print(markdown)
