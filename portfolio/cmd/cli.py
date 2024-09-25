#  Copyright (c) 2024.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import argparse
import logging

from portfolio.templates import about
from portfolio.templates import certificates
from portfolio.templates import education
from portfolio.templates import experience
from portfolio.templates import help
from portfolio.templates import social

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)

templates = {
    "about": about,
    "experience": experience,
    "certificates": certificates,
    "social": social,
    "education": education,
}

HELP = help.TEMPLATE % {
    "about": about.HELP,
    "experience": experience.HELP,
    "certificates": certificates.HELP,
    "social": social.HELP,
    "education": education.HELP
}

parser = argparse.ArgumentParser(
    description="Portfolio CLI <daipham.3213@gmail.com>",
    prog="portfolio", usage="%(prog)s [options]", epilog="Enjoy the CLI!",
    formatter_class=argparse.RawTextHelpFormatter, add_help=True
)
parser.add_argument("option", type=str, choices=templates.keys(), help=HELP)


def main():
    args = parser.parse_args()
    option = templates[args.option]

    template = option.TEMPLATE
    LOG.info(template)
