## 구현(Implementation)
## Baekjoon 22859 HTML 파싱
## https://www.acmicpc.net/problem/22859

HTML = input()
PARSING = []

def find_tag(html):
    starts = []
    ends = []

    for i in range(len(html)):
        if html[i] == '<':
            starts.append(i)
        elif html[i] == '>':
            ends.append(i)

    return (starts, ends)


def open_html(tags, html):

    starts, ends = tags[0], tags[1]

    p_start, p_end = 0, 0

    for i in range(len(starts)):
        start = starts[i]
        end = ends[i]

        if "<div title=" in html[start:end+1]:
            print_div_title(html[start:end+1])

        if "<p>" in html[start:end+1]:
            p_start = end
        elif "</p>" in html[start:end+1]:
            p_end = start+1
            print_p(html[p_start : p_end])
    

def print_div_title(html):
    PARSING.append("title : " + html[html.index('"')+1:html.rindex('"')])

def print_p(html):
    starts, ends = find_tag(html)
    pivot = 0
    p_pivot = 0
    switching = False
    texts = ""

    for i in range(len(starts)):
        start = starts[i]
        end = ends[i]
        
        texts += html[end+1 : start]
        
    texts = ' '.join(texts.split())
    
    PARSING.append(texts)

open_html(find_tag(HTML), HTML)

print("\n".join(PARSING))