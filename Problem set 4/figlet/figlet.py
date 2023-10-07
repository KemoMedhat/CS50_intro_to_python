from pyfiglet import Figlet
import sys

figlet = Figlet()
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        figlet.setFont(font=sys.argv[2])
        text = input()
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
