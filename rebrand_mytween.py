import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Text replacements preserving case where possible
    content = re.sub(r'mytween\.io', 'mytweenai.com', content, flags=re.IGNORECASE)
    content = re.sub(r'x\.com/mytween_io', 'x.com/mytweenai', content, flags=re.IGNORECASE)
    
    content = re.sub(r'Robinhood Chain', 'Solana', content, flags=re.IGNORECASE)
    content = re.sub(r'Robinhood', 'pump.fun', content, flags=re.IGNORECASE)
    content = re.sub(r'USDG', 'SOL', content, flags=re.IGNORECASE)
    
    # Names
    content = re.sub(r'Tween(?=[^a-zA-Z])', 'MyTween AI', content)
    content = re.sub(r'tween(?=[^a-zA-Z])', 'mytweenai', content)
    
    # Contract Address
    content = content.replace('0x41767e1ebb68b93bafa65b634ade89cd3a857777', 'coming soon on pump.fun')

    # Fix layout title if needed
    content = content.replace('<title>mytweenai ·', '<title>MyTween AI ·')
    content = content.replace('content="mytweenai ·', 'content="MyTween AI ·')

    # Remove dynamic Next.js data that could cause errors
    content = re.sub(r'<script>self\.__next_f\.push.*?</script>', '', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

def main():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(('.html', '.js', '.json', '.webmanifest')):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
