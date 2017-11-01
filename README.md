# Crawlyn

Crawlyn is an experimental crawler to scrape internal links and email addresses from websites, including obfuscated email addresses. This project is for educational purposes only.

## Installation

``pip install git+https://github.com/iamcryptoki/crawlyn.git``

## Usage

**Basic usage:**

``$ crawlyn https://www.example.com/``

``$ crawlyn https://www.example.com/ https://fakedomain.org/``

The results are printed to the console in JSON format.

**Save results to a JSON file:**

``$ crawlyn https://www.example.com/ --output /path/to/results.json``

## To Do

* Performance improvements.
* Phone numbers scraping.
* Unit tests.

## License

This code is released under a free software [license](LICENSE.txt) and you are welcome to fork it.
