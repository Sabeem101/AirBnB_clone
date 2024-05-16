#!/usr/bin/python3

"""
Console program that contains the entry point
for the command interpreter.
"""

import cmd
import json
import re
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter entry point.
    """
    prompt = "(hbnb) "
    ent_classes = ["BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"]
    strs_attrs = ["name", "first_name", "last_name", "email"
                "password", "description", "text", "user_id",
                "state_id", "city_id", "place_id", "amenity_id"]
    ints_attrs = ["max_guests", "number_rooms",
                "number_bathrooms", "price_by_night"]
    floats_attrs = ["longtitude", "latitude"]

    def do_EOF(self, arg):
        """
        EOF is a command to exit the program,
        Using Ctrl+D.
        """
        return True

    def do_quit(self, arg):
        """
        Exits the program using quit.
        """
        return True

    def emptyline(self):
        """
        Having an empty line and hitting ENTER,
        doesn't execute anything and prints a new prompts.
        """
        pass

    def validate(self, arg, _id_flag=False, _att_flag=False):
        """
        Validates the arguments that are passed to the commands.
        """
        Args = arg.split()
        Leng = len(arg.split())
        if Leng == 0:
            print("** class name missing **")
            return False
        if Leng < 2 and _id_flag:
            print("** instance id missing **")
            return False
        if Leng == 2 and _att_flag:
            print("** attribute name missing **")
            return False
        if Leng == 3 and _att_flag:
            print("** value missing **")
            return False
        if Args[0] not in HBNBCommand.ent_classes:
            print("** class doesn't exist **")
            return False
        if _id_flag and Args[0]+"."+Args[1] not in storage.all():
            print("** no instance found **")
            return False
        return True
    
    def itcasts(self, arg):
        """
        Casts a string to float or integer of possible.
        """
        try:
            if "." in arg:
                arg = float(arg)
            else:
                arg = int(arg)
        except ValueError:
            pass
        return arg

    def executes(self, arg):
        """
        Parsing helper function.
        """
        procs = {
                "all": self.do_all,
                "count": self.count,
                "create": self.do_create,
                "destroy": self.do_destroy,
                "show": self.do_show,
                "update": self.do_update
        }
        equiv = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        Args = equiv[0][0]+" "+equiv[0][2]
        plist = Args.split(", ")
        plist[0] = plist[0].replace('"', "").replace("'", "")
        if len(plist) > 1:
            plist[1] = plist[1].replace('"', "").replace("'", "")
        Args = " ".join(plist)
        if equiv[0][1] in procs:
            procs[equiv[0][1]](Args)

    def empty_cmd(self, arg):
        """
        A program in case of no command found.
        """
        equiv = re.findall(r"^(\w+)\.(\w+)\((.*)\)", arg)
        if len(equiv) != 0 and equiv[0][1] == "update" and "{" in arg:
            pdict = re.search(r'{([^}]+)}', arg).group()
            pdict = json.loads(pdict.replace("'", '"'))
            for x, y in pdict.items():
                _arg = arg.split("{")[0]+x+", "+str(y)+")"
                self.executes(_arg)
        elif len(equiv) != 0:
            self.executes(arg)

    def do_create(self, arg):
        """
        Creates a new instance.
            Usage: create <class name>
        """
        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Place": Place,
                "Amenity": Amenity,
                "Review": Review
        }
        if self.validate(arg):
            Args = arg.split()
            if Args[0] in classes:
                latest = classes[Args[0]]()
            storage.save()
            print(latest.id)

    def do_show(self, arg):
        """
        Shows the string representation of the chosen instance.
            Usage: show <class name> <id>.
        """
        if self.validate(arg, True):
            Args = arg.split()
            Keys = Args[0]+"."+Args[1]
            print(storage.all()[Keys])

    def do_destroy(self, arg):
        """
        Deletes a chosen instance.
            Usage: destroy <class name> <id>.
        """
        if self.validate(arg, True):
            Args = arg.split()
            Keys = Args[0]+"."+Args[1]
            del storage.all()[Keys]
            storage.save()

    def do_all(self, arg):
        """
        Prints all the string representations of all instances
        based on the class name or not.
            Usages: all <class name> / all.
        """
        Args = arg.split()
        Leng = len(Args)
        prv_list = []
        if Leng >= 1:
            if Args[0] not in HBNBCommand.ent_classes:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if Args[0] in key:
                    prv_list.append(str(value))
        else:
            for key, value in storage.all().items():
                prv_list.append(str(value))
        print(prv_list)

    def do_update(self, arg):
        """
        Updates an instance by updating attributes,
        or adding new ones.
            Usage: update <class name> <id> <attribute name> / <attribute value>
        """
        if self.validate(arg, True, True):
            Args = arg.split()
            Keys = Args[0]+"."+Args[1]
            if Args[3].startswith('"'):
                equiv = re.search(r'"([^"]+)"', arg).group(1)
            elif Args[3].startswith("'"):
                equiv = re.search(r'\'([^\']+\'', arg).group(1)
            else:
                equiv = Args[3]
            if Args[2] in HBNBCommand.strs_attrs:
                setattr(storage.all()[Keys], Args[2], str(equiv))
            elif Args[2] in HBNBCommand.ints_attrs:
                setattr(storage.all()[Keys], Args[2], int(equiv))
            elif Args[2] in HBNBCommand.floats_attrs:
                setattr(storage.all()[Keys], Args[2], float(equiv))
            else:
                setattr(storage.all()[Keys], Args[2], self.itcasts(equiv))
            storage.save()

    def count(self, arg):
        """
        Counts the number of instances of a class.
            Usage: <class name>.count()
        """
        count = 0
        for key in storage.all():
            if arg[:-1] in key:
                count += 1
        print(count)

    def do_clear(self, arg):
        """
        Clears the data storage.
            Usage: clear.
        """
        storage.all().clear()
        self.do_all(arg)
        print("** All data have been cleared. **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
