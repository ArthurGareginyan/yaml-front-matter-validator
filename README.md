# YAML Front Matter Validator

The `yaml-front-matter-validator` is a Python script that validates the YAML front matter in markdown (`.md`) files. The script recursively searches through a specified directory, parsing the YAML front matter of each markdown file, and outputs an error message along with the file path if there's a YAML syntax error.

## Installation

Before running the script, you need to install its dependencies. It requires Python and PyYAML. 

You can install PyYAML using pip:

pip install -r requirements.txt


## Usage

You can use the script by running the following command from your terminal:

python yaml_front_matter_validator.py /path/to/your/directory


Replace `/path/to/your/directory` with the path of the directory you want to search.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the MIT license.
