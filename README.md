# PassBird - Python Password Generator

PassBird is a password generator that generates strong and secure passwords. 

## Getting Started

### Installation

```
pip install passbird
```

To clone the current 'master' branch of PassBird, run the following command inside your desired directory:

```
git clone https://github.com/jrt345/PassBird.git
```

## Usage

```console
Usage: passbird [OPTIONS]

Options:
  -l, --length INTEGER RANGE  Length of password  [1<=x<=255]
  -c, --count INTEGER RANGE   Print number of passwords at once  [default: 1;x>=1]
  -uc, --include_uppercase    Include uppercase letters
  -lc, --include_lowercase    Include lowercase letters
  -num, --include_numbers     Include numbers
  -sym, --include_symbols     Include symbols letters
  --help                      Show this message and exit.
```

## Built With

* [Click](https://palletsprojects.com/p/click/) - Command line interface toolkit

## Versioning

PassBird uses [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/jrt345/PassBird/tags).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/jrt345/PassBird/blob/master/LICENSE) file for details
