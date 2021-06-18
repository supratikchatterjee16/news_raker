import os
import sys
import json
import argparse
import logging

logging.basicConfig(filename = "raker.log", level=logging.DEBUG)

CURRENT_DIRECTORY = os.getcwd()

config = {
    "DATABASE_URI" : "sqlite:///" + os.path.join(os.getcwd(), 'raker.db')
}

# initiate logger
logger = logging.getLogger(__name__)

# creating parser object
class ArgsParser(argparse.ArgumentParser):
	def error(self, message):# Modified to show help text on error
		sys.stderr.write('\033[0;31merror: %s\n\n\033[0m' % message)
		self.print_help()
		sys.exit(2)

parser = ArgsParser()
# adding arguments

parser.add_argument('-s', '--sources',
	help="Source file to load the sources from. The file should be in CSV format, with a source name and the source url.",
    required=False,
    nargs=1,
	metavar="SOURCE.CSV"
)

parser.add_argument('-t', '--test',
    help='This tests the given URL printing what it sees',
    nargs=1,
    required=False,
    metavar="TEST URL"
)

def run():
    global parser, logger
    args = parser.parse_args()
    logger.info("Initiatialising")
    if args.test is not None:
        from .scanner import scan
        for src in args.test:
            urls = scan(src, debug=True)
        return

    if args.sources is not None:
        source = args.sources[0]
        if not os.path.isfile(args.sources[0]):
            logger.error("Sources were not found. Exiting.")
            sys.exit(0)
        else:
            logger.info("Attempting source load")
        from .models import Source
        from .scraping import scrape_sources
        # print("Attempting source load")
        Source.load(args.sources[0])
        # print("Starting scraper")
        scrape_sources()
        return
    parser.print_help()
