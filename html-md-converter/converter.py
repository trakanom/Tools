import html2text
import markdown
import sys


def html_to_markdown(html):
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False
    markdown_text = converter.handle(html)
    return markdown_text


def markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python converter.py [html2md | md2html] input_file output_file")
        sys.exit(1)

    operation = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    with open(input_file, "r", encoding="utf-8") as f:
        input_content = f.read()

    if operation == "html2md":
        output_content = html_to_markdown(input_content)
    elif operation == "md2html":
        output_content = markdown_to_html(input_content)
    else:
        print("Invalid operation. Use 'html2md' or 'md2html'.")
        sys.exit(1)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_content)

    print("Conversion completed.")
