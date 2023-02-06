#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Defines functions of the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """ exit the program"""
        raise SystemExit

    def do_EOF(self, args):
        """ exit the program"""
        raise SystemExit

    def do_help(self, args):
        """lists commands"""
        return super().do_help(args)

    def emptyline(self):
        """ empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
