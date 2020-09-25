"""
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]

html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()
"""

"""
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

parser = MyHTMLParser()

for i in range(int(input())):
    parser.feed(input())
"""

# Parse and print the tags and attributes of some html contents

def splitTags(rawHtml):
    if not rawHtml or ("<" not in rawHtml and ">" not in rawHtml):
        yield
    openPtr = rawHtml.index("<")
    closePtr = rawHtml[openPtr:].index(">") + openPtr
    while True:
        if rawHtml[openPtr:openPtr+4] == "<!--":
            closePtr = rawHtml[openPtr:].index("-->") + openPtr + 2
        yield rawHtml[openPtr:closePtr+1]
        if "<" not in rawHtml[closePtr:] and ">" not in rawHtml[closePtr+1:]:
            break
        openPtr = rawHtml[closePtr:].index("<") + closePtr
        closePtr = rawHtml[openPtr:].index(">") + openPtr

def parseHTML(html):
    htmlList = splitTags(html)
    ans = ""
    for tag in htmlList:
        if tag[:2] == "</" or tag[:4] == "<!--":
            continue
        parts = tag[1:-1].split(" ")
        ans += parts[0] + "\n"
        #print(parts[0])
        parts = parts[1:]
        for attribute in parts:
            try:
                tmp = attribute.split("=")
                x = tmp[1].index("\"")
                attrVal = tmp[1][x+1:x + tmp[1][x+1:].index("\"")+1]
                #print("->", tmp[0], ">", attrVal)
                ans += "-> " + tmp[0] + " > " + attrVal + "\n"
            except Exception as e:
                #print(e)
                continue
    return ans


if __name__=="__main__":
    tests = ["<head><title>HTML</title></head><object type=\"application/x-flash\" data=\"your-file.swf\" width=\"0\" height=\"0\"><!-- <param name=\"movie\" value=\"your-file.swf\" /> --><param name=\"quality\" value=\"high\"/></object>"]
    for test in tests:
        print(parseHTML(test))