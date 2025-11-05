import sys
import re 







# Rules

# 1. #, ##, ###, coresponds to <h1>, <h2>, etc
# alternatively == underneath makes it a h1 at least 2 -- for h2

# 2. Paragraphs are separated by a blank line, new lines are


def convert_emphasis(text:str)->str:
    pass 

def convert_paragraph(text:str)->str:
    pass 

def convert_headings(text:str)->str:
    lines = text.split('\n')
    result = []
    i = 0

    while i<len(lines):

        line = lines[i].strip()

        match = re.match(r'^(#{1,6})\s+(.*)$',line)
        if match:
            level = len(match.group(1))
            content = match.group(2).strip()
            result.append(f"<h{level}>{content}</h{level}>")
        elif i+1<len(lines):
            next = lines[i+1].rstrip()
            if re.match(r'^[=]{2,}\s*$',next):
                result.append(f"<h1>{line.strip()}</h1>")
                i+=1
            elif re.match(r'^[-]{2,}\s*$',next):
                result.append(f"<h2>{line.strip()}</h2>")
                i+=1
            else:
                result.append(line)
        else:
            result.append(line)
        i+=1 
    return '\n'.join(result)
                
    pass 

def convert_ordered_list(text: str)->str:
    pass 

def convert_unordered_list(text: str)->str:
    pass 

def convert_code(text:str)->str:
    pass 

def convert_link(text:str)->str:
    pass 

def convert(text: str)->str:
    pass


def main_script():
    # command line args are either length 1 or length 2

    if len(sys.argv)==2:
        in_file = sys.argv[1]
        out_file = "filename.html"
    elif len(sys.argv)==3:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
    else:
        raise Exception("Invalid number of arguments")