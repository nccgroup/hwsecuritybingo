#!/usr/bin/env python

"""
Hardware Security Bingo Card Generator

Authors: Jeremy Boone & Rob Wood, NCC Group

Note: This project was originally forked from https://github.com/hrs/bingo.git
"""

import random, sys

head = \
"""<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">
<html lang=\"en\">\n<head>
<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">
<title>Hardware Security Bingo</title>
<style type=\"text/css\">
    body { font-size: 12px; }
    table { margin: 40px auto; border-spacing: 1px; }
    .newpage { page-break-after:always; }
    tr { height: 140px; }
    td { text-align: center; border: thin black solid; padding: 10px; width: 120px; }
</style>
</head>\n
<body>\n"""


def generateTable(terms, pagebreak):
    ts = terms[:12] + ["<img src=\"HW_logo.png\" width=\"80\">"] + terms[12:24]
    if pagebreak:
        res = "<table class=\"newpage\">\n"
    else:
        res = "<table>\n"
    res += "<tr><th height=\"40px\" colspan=\"5\"><font size=\"6\">Hardware Security Bingo</font></th></tr>"
    for i, term in enumerate(ts):
        if i % 5 == 0:
            res += "\t<tr>\n"
        res += "\t\t<td>" + term + "</td>\n"
        if i % 5 == 4:
            res += "\t</tr>\n"
    res += "</table>\n"
    return res


# Parse command line
if len(sys.argv) == 3:
    out_file_name = sys.argv[1]
    num_cards     = int(sys.argv[2])
elif len(sys.argv) == 2:
    out_file_name = sys.argv[1]
    num_cards     = 1
else:
    print "USAGE: " + sys.argv[0], " [output HTML file] [# of cards]"
    sys.exit(1)

# Read the terms file
in_file = open("bingo.txt", 'r')
terms = [line.strip() for line in in_file.readlines()]
terms = filter(lambda x: x != "", terms)
in_file.close()

# Write the output html file(s)
out_file = open(out_file_name, 'w')
out_file.write(head)
for i in range(num_cards):
    random.shuffle(terms)
    if i != num_cards - 1:
        out_file.write(generateTable(terms, True))
    else:
        out_file.write(generateTable(terms, False))
out_file.write("</body></html>")
out_file.close()


