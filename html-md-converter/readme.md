# html-2-md

This repository contains a Python script, \`converter.py\`, which converts between HTML and Markdown formats using the \`html2text\` and \`markdown\` libraries.

## Installation

To use the \`converter.py\` script, first install the required libraries using pip:

```bash
pip install html2text markdown
```

## Usage

The \`converter.py\` script can be run from the command line with the following arguments:

```bash
# For HTML to Markdown conversion
python converter.py html2md input.html output.md

# For Markdown to HTML conversion
python converter.py md2html input.md output.html
```

Replace \`input.html\`, \`output.md\`, \`input.md\`, and \`output.html\` with your actual input and output file paths.

## Customization

The \`converter.py\` script provides a starting point for HTML and Markdown conversion. You can further customize the script or the conversion options provided by the \`html2text\` and \`markdown\` libraries as needed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

Created by Mika Wisener-Brandt.
