
# EDITOR STATE
markdown = """"""

# FILES
output_file_name = "output.md"

# OPTIONS
option_help = "!help"
option_done = "!done"

# MESSAGES
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

# MAPPING: INPUT TO MESSAGE
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


# OPTION IMPLEMENTATION
def apply_option_help():
    print(msg_help)


def apply_option_done():
    file = open(output_file_name, 'w+')
    file.write(markdown)
    file.close()


# INPUT IMPLEMENTATION
def input_text(title_type):
    print(title_types_msgs[title_type], end='')
    return input()


def input_level():
    while True:
        level = int(input_text(level_title_type))
        if not 1 <= level <= 6:
            print(msg_level_error)
            continue
        else:
            return level


def input_row(row_number):
    print(f'Row #{row_number}: ', end='')
    return input()


def input_rows():
    while True:
        print(msg_rows, end='')
        rows = int(input())
        if not rows > 0:
            print(msg_rows_error)
        else:
            return rows


# FORMATTER IMPLEMENTATION
def format_header():
    level = input_level()
    text = input_text(text_title_type)
    conditional_new_line = ''
    if markdown != """""":
        conditional_new_line = '\n'
    return f'{conditional_new_line}{"#" * level} {text}{format_new_line()}'


def format_bold():
    text = input_text(text_title_type)
    return f'**{text}**'


def format_plain():
    return input_text(text_title_type)


def format_inline_code():
    text = input_text(text_title_type)
    return f'`{text}`'


def format_new_line():
    return '\n'


def format_link():
    label = input_text(label_title_type)
    url = input_text(url_title_type)
    return f'[{label}]({url})'


def format_italic():
    text = input_text(text_title_type)
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
    option_help: apply_option_help,
    option_done: apply_option_done
}


# GATE: FORMATTERS
def apply_formatter(formatter):
    return formatters[formatter]()


# GATE: OPTIONS
def apply_option(option):
    options[option]()


# ENTRANCE
while True:
    choice = input_text(formatter_title_type)
    if choice in formatters:
        markdown += apply_formatter(choice)
    elif choice in options:
        apply_option(choice)
        if choice == option_done:
            break
    else:
        print(msg_unknown_formatting)
        continue

    print(markdown)
