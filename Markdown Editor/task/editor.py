
msg_help = """Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done"""
msg_choose_formatter = "Choose a formatter:"
msg_unknown_formatting = "Unknown formatting type or command"

option_help = "!help"
option_done = "!done"

formatters = {"plain", "bold", "italic",
              "header", "link", "inline-code",
              "ordered-list", "unordered-list", "new-line"}

while True:
    print(msg_choose_formatter, end='')
    choice = input()
    if choice in formatters:
        continue
    elif choice == option_help:
        print(msg_help)
    elif choice == option_done:
        break
    elif choice not in formatters:
        print(msg_unknown_formatting)
