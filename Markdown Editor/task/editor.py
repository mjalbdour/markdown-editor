
msg_help = """Available formatters: plain bold italic header link inline-code new-line
Special commands: !help !done"""
msg_formatter = "Choose a formatter: "
msg_text = "Text: "
msg_level = "Level: "
msg_label = "Label: "
msg_url = "URL: "
msg_row = "Row "
msg_rows = "Number of rows: "
msg_unknown_formatting = "Unknown formatting type or command"
msg_level_error = "The level should be within the range of 1 to 6"
msg_rows_error = "The number of rows should be greater than zero"

formatter_title_type = "Formatter"
text_title_type = "Text"
level_title_type = "Level"
label_title_type = "Label"
url_title_type = "URL"
rows_title_type = "Rows"
title_types_msgs = {
    formatter_title_type: msg_formatter,
    text_title_type: msg_text,
    level_title_type: msg_level,
    label_title_type: msg_label,
    url_title_type: msg_url,
    rows_title_type: msg_rows
}

option_help = "!help"
option_done = "!done"
options = {option_help, option_done}

markdown = """"""


def text_input(title_type):
    print(title_types_msgs[title_type], end='')
    return input()


def level_input():
    while True:
        level = int(text_input(level_title_type))
        if not 1 <= level <= 6:
            print(msg_level_error)
            continue
        else:
            return level


def row_input(row_number):
    print(f'Row #{row_number}: ', end='')
    return input()


def rows_input():
    while True:
        print(msg_rows, end='')
        rows = int(input())
        if not rows > 0:
            print(msg_rows_error)
        else:
            return rows


def header_formatter():
    level = level_input()
    text = text_input("Text")
    conditional_new_line = ''
    if markdown != """""":
        conditional_new_line = '\n'
    return f'{conditional_new_line}{"#" * level} {text}{new_line_formatter()}'


def bold_formatter():
    text = text_input("Text")
    return f'**{text}**'


def plain_formatter():
    return text_input(text_title_type)


def inline_code_formatter():
    text = text_input(text_title_type)
    return f'`{text}`'


def new_line_formatter():
    return '\n'


def link_formatter():
    label = text_input(label_title_type)
    url = text_input(url_title_type)
    return f'[{label}]({url})'


def italic_formatter():
    text = text_input("Text")
    return f'*{text}*'


def list_formatter(ordered=True):
    rows = rows_input()
    string = ""
    if markdown != """""":
        string += '\n'
    for i in range(1, rows + 1):
        text = row_input(i)
        if ordered:
            string += f'{i}. {text}\n'
        else:
            string += f'* {text}\n'

    return string


formatters = {
    "plain": plain_formatter,
    "bold": bold_formatter,
    "italic": italic_formatter,
    "header": header_formatter,
    "link": link_formatter,
    "inline-code": inline_code_formatter,
    "new-line": new_line_formatter,
    "ordered-list": lambda: list_formatter(),
    "unordered-list": lambda: list_formatter(ordered=False),
}


def apply_formatter(formatter):
    return formatters[formatter]()


while True:
    choice = text_input(formatter_title_type)
    if choice in formatters:
        markdown += apply_formatter(choice)
    elif choice in options:
        if choice == option_help:
            print(msg_help)
        elif choice == option_done:
            break
    else:
        print(msg_unknown_formatting)
        continue

    print(markdown)
