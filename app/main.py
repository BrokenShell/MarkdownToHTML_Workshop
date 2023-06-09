from markdown2 import markdown


with open("README.md", "r") as file:
    text = file.read()

html = markdown(text, extras=["tables", "fenced-code-blocks"])

with open("README.html", "w") as file:
    file.write(html)
