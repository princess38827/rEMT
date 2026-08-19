with open('index.html', 'r') as f:
    content = f.read()
    
# Check what's missing
has_body_close = '</body>' in content
has_html_close = '</html>' in content
has_script = '<script' in content

print(f"Has </body>: {has_body_close}")
print(f"Has </html>: {has_html_close}")
print(f"Has <script>: {has_script}")
print(f"\nFile ends with: {repr(content[-100:])}")
