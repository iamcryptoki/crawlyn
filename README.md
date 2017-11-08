# Crawlyn

Experimental crawler to grab data from websites, including:

* Internal links.
* Plain-text and obfuscated email addresses.

This project is for educational purposes only.

## Installation

``pip install git+https://github.com/iamcryptoki/crawlyn.git``

## Usage

**Basic usage:**

``$ crawlyn https://www.example.com/``

``$ crawlyn https://www.example.com/ https://fakedomain.org/``

The results are printed to the console in JSON format.

**Save results to a file:**

``$ crawlyn https://www.example.com/ --output /path/to/results.json``

**Running Crawlyn with a proxy:**

``$ crawlyn https://www.example.com/ --proxyhost 127.0.0.1 --proxyport 9999 --proxytype=socks5``

Both proxy host address and port number needs to be set.

Default proxy type: http.

**Running Crawlyn with Tor:**

``$ crawlyn https://www.example.com/ --tor``

## License

This code is released under a free software [license](LICENSE.txt) and you are welcome to fork it.
