import os
import sys
import json
import argparse
import logging

logging.basicConfig(filename = "raker.log", level=logging.DEBUG)

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

parser.add_argument('--source',
	help="Source file to load the sources from. The file should be in CSV format, with a source name and the source url.",
	nargs=1,
	required=True,
	metavar="SOURCE.CSV"
)

def run():
    global parser, logger
    args = parser.parse_args()
    if not os.path.isfile(args.source[0]):
        logger.error("Sources were not found. Exiting.")
        sys.exit(0)
    else:
        logger.info("Attempting source load")
    from .models import Source
    from .scraping import scrape_sources
    # print("Attempting source load")
    Source.load(args.source[0])
    # print("Starting scraper")
    scrape_sources()
