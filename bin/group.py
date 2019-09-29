import argparse
import sys
import json
from typing import List

from logger import get_logger

from lib.grouper import FlatGroupError
from lib.grouper import FlatGroup

logger = get_logger(__name__)


class Cli:
    """
    Class to encapsulate app execution through CLI
    """

    def __init__(self, stdin=None, stdout=None):
        """
        Uses default stdin/stdout if its not provided
        :param stdin:
        :param stdout:
        """
        self.stdin = stdin or sys.stdin
        self.stdout = stdout or sys.stdout

    def run_from_argv(self, argv: List):
        """
        Execute application by taking args from command line
        :param argv:
        :return:
        """
        parser = self.create_parser()
        args = parser.parse_args(argv)
        try:
            self.execute(args)
        except FlatGroupError as e:
            logger.error(e)
            sys.exit(-1)

    def create_parser(self):
        """
        Define arguments
        :return:
        """
        parser = argparse.ArgumentParser(
            description='Group list of dictionaries'
        )
        parser.add_argument(
            'keys',
            metavar='key',
            nargs='+',
            help='List of keys. Space separated. '
                 'For example: city currency'
        )

        return parser

    def execute(self, args):
        """
        Execute CLI application
        :param args:
        :return:
        """
        data = self.read()
        flat_group = FlatGroup(args.keys)
        data = flat_group.group(data)
        self.write(data)

    def read(self):
        """
        Read and convert from JSON
        :return:
        """
        return json.loads(self.stdin.read())

    def write(self, data):
        """
        Covert to JSON and write
        :param data:
        :return:
        """
        self.stdout.write(json.dumps(data))
        self.stdout.write('\n')


if __name__ == '__main__':
    cli = Cli()
    cli.run_from_argv(sys.argv[1:])
