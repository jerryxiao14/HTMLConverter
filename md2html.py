import sys
import re 





# Rules

# 1. #, ##, ###, coresponds to <h1>, <h2>, etc
# alternatively == underneath makes it a h1 at least 2 -- for h2

# 2. Paragraphs are separated by a blank line, new lines are


def convert_emphasis(text:str)->str:
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<em><strong>\1</strong></em>', text)
    #print(f'after first bold sub text is {text}')
    text = re.sub(r'(?<!\w)___(.+?)___(?!\w)', r'<em><strong>\1</strong></em>', text)
    #print(f'after sub __ text is {text}')

    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    #print(f'after first bold sub text is {text}')
    text = re.sub(r'(?<!\w)__(.+?)__(?!\w)', r'<strong>\1</strong>', text)
    #print(f'after sub __ text is {text}')


    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'(?<!\w)_(.+?)_(?!\w)', r'<em>\1</em>', text)
    #print(f'after substituting em text is {text}')

    return text 

def convert_paragraph(text:str)->str:
    blocks = re.split(r'\n\s*\n', text)
    print(f'blocks are {blocks}')
    result = []

    for block in blocks:
        block = block.strip() 
        if len(block)==0:
            continue
        print(f'block is {block}')
        if re.match(r'^\s*<(h\d|ul|ol|li|p|/ul|/ol|/li)',block):
            match = re.match(r'^\s*(<.*>.*</.*>)(.*)$', block, re.DOTALL)

            if match:
                html_part = match.group(1).strip()
                rest = match.group(2).strip()
                result.append(html_part)
                if rest:
                    rest = rest.replace('\n','<br>')
                    result.append(f'<p>{rest}</p>')
            else:
                result.append(block)
        else:
            block = block.replace('\n','<br>')
            result.append(f'<p>{block}</p>')

    return '\n'.join(result)

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
                
def convert_ordered_list(text: str)->str:
    lines = text.split('\n')
    result = []
    
    inside_list = 0 

    for line in lines:
        match = re.match(r'^\s*\d+\.\s+(.*)',line)
        if match:
            if not inside_list:
                result.append('<ol>')
                inside_list^=1
            item = match.group(1).strip()
            result.append(f'    <li>{item}</li>')
        else:
            if inside_list:
                result.append('</ol>')
                inside_list^=1 
            result.append(line)
    if inside_list:
        result.append('</ol>')
    
    return '\n'.join(result)

def convert_unordered_list(text: str)->str:
    lines = text.split('\n')
    result = []
    inside_list = 0 

    for line in lines:
        match = re.match(r'^\s*[-\*+]\s+(.*)',line)
        if match:
            if not inside_list:
                result.append('<ul>')
                inside_list^=1 
            item = match.group(1).strip()
            result.append(f'    <li>{item}</li>')
        else:
            if inside_list:
                result.append('</ul>')
                inside_list^=1 
            result.append(line)
    if inside_list:
        result.append('</ul>')
    
    return '\n'.join(result)

def convert_code(text:str)->str:
    text = re.sub(r'(`{1,2})(.+?)\1',r'<code>\2</code>',text)
    return text

def convert_link(text:str)->str:
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text 

def convert(text: str) -> str:
    text = convert_code(text)

    text = convert_link(text)

    text = convert_emphasis(text)

    text = convert_headings(text)

    text = convert_unordered_list(text)
    text = convert_ordered_list(text)

    text = convert_paragraph(text)

    return text


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
    
    try:
        with open(in_file, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
    except FileNotFoundError:
        print(f"Error: file '{in_file}' not found.")
        sys.exit(1)

    # Convert Markdown to HTML
    html_text = convert(markdown_text)

    # Write the output HTML file
    try:
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(html_text)
        print(f"Successfully wrote HTML to '{out_file}'.")
    except Exception as e:
        print(f"Error writing file '{out_file}': {e}")
        sys.exit(1)
        