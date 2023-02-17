''' Google Feed Object '''

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from dataclasses import dataclass, field
import configparser
import logging

from ..action.options import Action
from .token import TokenTest

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-o", "--option", default="UPDATE",
                    help="Option [UPDATE] or [SHOW]")
parser.add_argument("-d", "--days", default=3,
                    type=int, help="Number de days to check event after now")
args = vars(parser.parse_args())

# Simple log
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
# config structure
@dataclass
class Config:
    version: str = ''
    credentials: str = ''
    token: str = ''

class GetEvents:

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.config = Config()
        self.load_cfg_file('init.cfg')
        self.config.version = self.cfg['GERAL']['version']
        self.config.credentials = self.cfg['PATHES']['credentials']
        self.config.token = self.cfg['PATHES']['credentials']
#        self.run()

    def load_cfg_file(self, cfg_path) -> None:
        self.cfg = configparser.ConfigParser()
        self.cfg.read(cfg_path)

    def token_exist(self):


    def run(self) -> None:
        # select action to iniciate
        Act = Action(self.config, args)
