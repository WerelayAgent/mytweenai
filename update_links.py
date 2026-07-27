import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('href="/sign-up"', 'href="/signup.html"')
content = content.replace('href="/sign-in"', 'href="/signup.html"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated links in index.html')
