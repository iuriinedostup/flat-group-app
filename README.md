# Group flat list of dictionaries
1. CLI application to group a list of dictionaries by provided keys
2. Simple REST API to use library

## Business problem
Given flat list of dictionaries application should create a dictionary with data grouped by key.
To solve this problem application uses sort by key and group by key techniques.
It invokes sorting and grouping logic recursively until all keys are used.

To control CLI application there is ArgumentParser configured.
For REST API `flask_rest` is used. The endpoint is `/group?key=<key1>[&key=<key2>]`

## Getting Started
Follow installation steps to start using the application.

### Prerequisites

- python 3.6+
- virtualenv

### Installing

To install application execute `make setup`
It will create virtual environment and install dependencies.
You may also need to setup `PYTHONPATH` to the root of project directory.

## Usage
Application can be used as:
- CLI
- REST API

### CLI application
Make sure you have activated your virtual environment.
To test your JSON data execute:

```bash
cat input.json | python bin/group.py currency country
```

You may also forward output to file.

### REST API

Rest API is powered by flask-rest application.
To start webserver execute:
```bash
python bin/api.py
```

API is available at `http://localhost:5000` by default.
To group data issue a POST request:
```bash
curl -X POST \
  --url 'http://localhost:5000/group?key=country&key=currency' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Basic my_secret_token' \
  --data '[{"country":"US","city":"New York","currency":"USD","amount":100},{"country":"DE","city":"Munich","currency":"EUR","amount":20},{"country":"DE","city":"Berlin","currency":"EUR","amount":11.4},{"country":"NL","city":"Amsterdam","currency":"EUR","amount":8.9},{"country":"UK","city": "London","currency":"GBP","amount": 12.2}]' 
```

## Development

Make sure you have path to this application in your `PYTHONPATH` 
or run scripts from the project root so `PYTHONPATH` will be updated automatically

### Tests

To run code style checker and execute tests:
```bash
make test
```

There are bunch of unit tests to test some application logic and execution flow.
Also, there are integration tests to assert how components are being 
used together as real application runs.

## Author

* **Iurii Nedostup** - yuriy.nedostup@gmail.com
