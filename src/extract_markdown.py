import re
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)


if __name__ == "__main__":
    print(extract_markdown_images("This is text with an ![image](image.png) This is text with a [link](https://www.google.com)"))