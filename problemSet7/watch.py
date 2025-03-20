import re, sys

def main():
    print(parse(input("HTML: ")))
    sys.exit()

def parse(str):
    pattern = r'src="(https?://)(w?w?w?\.?)(youtube)(\.com)/embed(/\w*)'
    match = re.search(pattern, str)
    domain, w, protocol = '','',''

    if match:
        ##print(match.group(1),match.group(2),match.group(3),match.group(4),match.group(5))
        if match.group(3) == "youtube":
            domain = "youtu.be"
        if match.group(1) == 'http://' or match.group(1) == 'https://' :
            protocol = 'https://'
        if match.group(2) != 'www.':
            w = ''
        url = protocol + w + domain + match.group(5)
        return url
    else:
        return None
main()

