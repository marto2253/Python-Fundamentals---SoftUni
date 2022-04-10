def html_exercise():
    title = input()
    article = input()
    print(f'<h1>\n    {title}\n</h1>')
    print(f'<article>\n    {article}\n</article>')
    items = input().split()
    while items[0] != 'end':
        print(f'<div>\n    {" ".join(items)}\n</div>')

        items = input().split()

html_exercise()