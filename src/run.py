# Run script to GooFee
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from goofee import Action

# options
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-o", "--option", default="UPDATE", help="Option [UPDATE] or [SHOW]")
parser.add_argument("-d", "--days", default=3, type=int, help="Number de days to check event after now")
args = vars(parser.parse_args())


if __name__ == '__main__':
    action = Actions("", args)


