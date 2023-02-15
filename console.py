#!/usr/bin/python3
"""Entry to command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
import models
import json


class HBNBCommand(cmd.Cmd):
    """
    Defines functions of the command interpreter
    """
    prompt = '(hbnb) '
    class_list = {'BaseModel': BaseModel, 'State': State, 'City': City,
                  'Amenity': Amenity, 'Place': Place, 'Review': Review,
                  'User': User}

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
        if len(args) == 0:
            print("** class name missing **")
        elif args in self.class_list:
            obj = self.class_list[args]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance"""
        class_name, object_id = None, None
        args = args.split(' ')
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            object_id = args[1]
        if not class_name:
            print('** class name missing **')
        elif not object_id:
            print('** instance id missing **')
        elif not self.class_list.get(class_name):
            print("** class doesn't exist **")
        else:
            c = class_name + "." + object_id
            obj = models.storage.all().get(c)
            if not obj:
                print('** no instance found **')
            else:
                print(obj)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        class_name, object_id = None, None
        args = args.split(' ')
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            object_id = args[1]
        if not class_name:
            print('** class name missing **')
        elif not object_id:
            print('** instance id missing **')
        elif not self.class_list.get(class_name):
            print("** class doesn't exist **")
        else:
            c = class_name + "." + object_id
            obj = models.storage.all().get(c)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[c]
                models.storage.save()

    def do_all(self, args):
        """ Prints all string representation of all instances"""
        if not args:
            print([str(value) for key, value in models.storage.all().items()])
        else:
            if not self.class_list.get(args):
                print("** class doesn't exist **")
                return False
            print([str(value) for key, value in models.storage.all().items()
                   if type(value) is self.class_list.get(args)])

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file)"""
        args = args.split(' ', 3)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif not self.class_list.get(args[0]):
            print("** class doesn't exist **")
        else:
            k = args[0] + "." + args[1]
            obj = storage.all().get(k)
            if obj is None:
                print("** no instance found **")
            else:
                setattr(obj, args[2], args[3])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
