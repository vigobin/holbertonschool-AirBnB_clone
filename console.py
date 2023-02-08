#!/usr/bin/python3
"""Entry to command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
import models
import json


class HBNBCommand(cmd.Cmd):
    """
    Defines functions of the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseMode"""
        if args is None:
            print("** class name missing **")
        elif args not in storage.classes():
            print("** class doesn't exist **")
        else:
            class_instance = storage.classes()[args]()
            class_instance.save()
            print(class_instance.id)

    def do_show(self, args):
        """ Prints the string representation of an instance"""
        if args is None:
            print("** class name missing **")
        else:
            parse = args.split(' ')
            if parse[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(parse) < 2:
                print("** instance id missing **")
            else:
                key = parse[0] + "." + parse[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if args is None:
            print("** class name missing **")
        else:
            parse = args.split(' ')
            if parse[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(parse) < 2:
                print("** instance id missing **")
            else:
                key = parse[0] + "." + parse[1]
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, args):
        """ Prints all string representation of all instances"""
        if args is None:
            parse = args.split(' ')
            if parse[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                print("")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
