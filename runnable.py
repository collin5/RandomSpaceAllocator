# @Author: collins
# @Date:   2017-06-09T11:36:19+03:00
# @Last modified by:   collins
# @Last modified time: 2017-06-13T14:07:20+03:00

"""
Usage:
    create_room <room_name>...
    add_person <person_firstname> <person_lastname> <FELLOW_or_STAFF> [<wants_accommodation>]

Options:
    --version

"""

from cmd import Cmd
from docopt import docopt, DocoptExit
import sys
from modules.middleware.amityinterface import AmityInterface
from modules.middleware.const import Action

version = 0
intro = """"
Type \'help\' for instructions
"""


class Cli(Cmd):
    def __init__(self):
        super(Cli, self).__init__()

    @staticmethod
    @AmityInterface
    def call_amity(action=None, *args):
        pass

    def with_docopt(func):

        def execute(*args, **kwargs):
            # set args & function name as system arguments for docopt
            sys.argv = [func.__name__[3:]] + list(args)[1:]

            sys.argv = sys.argv if 'create_room' in sys.argv else sys.argv[0].split(
            ) + sys.argv[1].split()
            try:
                doc_Args = docopt(func.__doc__, version=version)
                # Add func name which is previously stripped off
                # Also remove do_ prefix from function name
                doc_Args.update({func.__name__[3:]: True})

                if 'create_room' in doc_Args:

                    Cli.call_amity(Action.CREATE_ROOM, doc_Args['<room_name>'])

                if 'add_person' in doc_Args:
                    fname, lname = doc_Args['<person_firstname>'], doc_Args['<person_lastname>']
                    type, accomodation = doc_Args['<FELLOW_or_STAFF>'], True if '[<wants_accomodation>]' in doc_Args else False
                    Cli.call_amity(Action.ADD_PERSON, fname,
                                   lname, type, accomodation)
            except DocoptExit as e:
                print("Invalid command")
        return execute

    @with_docopt
    def do_create_room(self, args):
        """Usage: create_room <room_name>..."""

    @with_docopt
    def do_add_person(self, args):
        """Usage: add_person <person_firstname> <person_lastname> <FELLOW_or_STAFF> [<wants_accommodation>] """
    @with_docopt
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <person_identifier> <new_roomname>"""

    @with_docopt
    def do_load_people(self, args):
        pass

    @with_docopt
    def do_print_allocations(self, args):
        pass

    @with_docopt
    def do_print_unallocated(self, args):
        pass

    @with_docopt
    def do_print_room(self, args):
        pass

    @with_docopt
    def do_save_state(self, args):
        pass

    @with_docopt
    def do_load_state(self, args):
        pass

    def do_version(self, args):
        """Show the version of the program"""
        print("Version {} ".format(str(version)))

    def do_quit(self, args):
        """Quits the program"""
        raise SystemExit


if __name__ == '__main__':
    cli = Cli()
    cli.prompt = " Amity $ "
    cli.cmdloop(intro)
