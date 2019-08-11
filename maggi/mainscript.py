from docopt import docopt
import click
import pyfiglet
from utils.prune import prune
from utils.create import createbox
from utils.connector import dockin
from utils.instabox import buildlinux
from utils.move import copy,start

import locale
locale.setlocale(locale.LC_ALL, str('en_US.UTF-8'))


usage = '''

Rudolph CLI.

Usage:
 mainscript.py --create
 mainscript.py --testprint
 mainscript.py --purge
 mainscript.py --delete

'''

args = docopt(usage)


def main():
        print(pyfiglet.figlet_format("Rudolph", font = "slant"))

        if args['--create'] :
            print("Baking fresh VM.....")
            os_choice = click.prompt("""
            Select an OS of your choice (Choose an index) ==>
            1. Ubuntu 14.04
            2. Ubuntu 16.04
            3. Ubuntu 18.04
            4. Ubuntu 19.04
            5. centOS 6.10
            6. centOS 7
            7. Debian Jessie
            8. Debian Stretch
            """, default=2)
            if os_choice == 1:
                os = 'instantbox/ubuntu:14.04'
            elif os_choice == 2:
                os = 'instantbox/ubuntu:16.04'
            elif os_choice == 3:
                os = 'instantbox/ubuntu:18.04'
            elif os_choice == 4:
                os = 'instantbox/ubuntu:19.04'
            elif os_choice == 5:
                os = 'instantbox/centos:6.10'
            elif os_choice == 6:
                os = 'instantbox/centos:7'
            elif os_choice == 7:
                os = 'instantbox/debian:jessie'
            elif os_choice == 8:
                os = 'instantbox/debian:stretch'
            else:
                print("Invalid choice")
                exit()
            print("\n")
            proj_choice = click.prompt("""
            Select the type of project  ==> 
            1. Spring-Boot
            2. Flask (Python3)
            3. Flask (Python2)
            """, default =1)
            path = click.prompt("Please enter where the base directory is to be installed ")
            print("✅")
            cpu = click.prompt("Enter the number of CPU cores to dedicate ", default = 2)
            print("✅")
            mem = click.prompt("Enter the memory in MB ", default = 512)
            print("✅")
            port = click.prompt("Enter the port number ", default = 15178)
            print("✅")
            directory = click.prompt("Enter the project directory ")
            print("✅")
            file2run = click.prompt("Enter the main file to run")
            print("✅")
            print(os,cpu,mem,port)
            buildlinux(path)
            id, link = createbox(os,cpu,mem,port)
            dockin(id,directory,proj_choice)
            start(id,directory,file2run,proj_choice)
            print("The id created = " + id)
            #copy(directory, link + ":")
            print("✅")
            #click.launch(link)
            
        if args['--testprint'] :
            print('Hello there, docopt successful !!!!')
        
        if args['--purge'] :
            prune()
            print("cleaning all the Linux machines")
            print("😴")
        
        
                    

if __name__ == "__main__":
        main()
