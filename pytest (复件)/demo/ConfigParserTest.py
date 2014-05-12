__author__ = 'gengjie'
import ConfigParser
import logging

parser = ConfigParser.ConfigParser()
parser.read("./steam.desktop")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("./test.log")
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(fmt)
logger.addHandler(fh)
print '*' * 100
print parser.get("Desktop Entry", "Name")
logger.info("some log message about this desktop entry...")
print '*' * 100
for section in parser.sections():
    print section
    for option in parser.options(section):
        print option, parser.get(section, option)

new_section = "Desktop Action Comments"
parser.add_section(new_section)
parser.set(new_section, 'comments', 'copy rights by Steam')
parser.write(open("./test.log", "wb"))