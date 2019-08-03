#!/usr/bin/env python3


import click
import pyfiglet
import inquirer

from utils.connector import dockin
from utils.create import createbox
from utils.delete import clean
from utils.instabox import buildlinux
from utils.prune import prune
from utils.move import copy, start

import locale
locale.setlocale(locale.LC_ALL, str('en_US.UTF-8'))

@click.command()
@click.option('--create',
              is_flag=True,
              help='setup a VM for running deployment tools/tests very similar to an cloud instance',)
@click.option('--performance',
              help = "see load on VM instances " )
@click.option('--purge',
              help = "remove all instances instantly",
              is_flag=True)
@click.option('--delete',
              help = "remove a particular VM")
def main(create, performance, purge, delete):
    print(pyfiglet.figlet_format("MAGGI", font = "slant") )

    if create:
        print("baking vm")
        path = click.prompt("please enter where base directory to be installed : ", default="/Users/oyo")

        # os. cpu, mem, port
        available_os = [
            inquirer.List('os',
                          message="What os do you need?",
                          choices=['instantbox/ubuntu:14.04',
                                   'instantbox/ubuntu:16.04',
                                   'instantbox/ubuntu:18.04',
                                   'instantbox/ubuntu:19.04',
                                   'instantbox/centos:6.10',
                                   'instantbox/centos:7',
                                   'instantbox/debian:jessie',
                                   'instantbox/debian:stretch'],
                          ),
        ]
        os = inquirer.prompt(available_os)['os']
        cpu = click.prompt("Please enter number of cpu core to dedicate : ", default="2")
        print("✅")
        mem = click.prompt("Please enter the memory in MB : ", default="512", confirmation_prompt=True)
        print("✅")
        port = click.prompt("Please enter the port to access : ", default="15178", confirmation_prompt=True)
        print("✅")
        directory = click.prompt("Please enter the project file directory")
        print("✅")
        file2run = click.prompt("Please enter the main file to run")
        print("✅")
        print(os, cpu, mem, port)
        available_backend_framework = [
            inquirer.List('framework',
                          message="What backend framework do you need?",
                          choices=['java:spring-boot',
                                   'python3:Flask',
                                   'python3:Django',
                                   'python2:Flask',
                                   'python2:Django',
                                   'Ruby:Rails'],
                          ),
        ]
        framework = inquirer.prompt(available_backend_framework)['framework']
        buildlinux(path)
        print("✅")
        id, link = createbox(os, cpu, mem, port)
        dockin(id, framework)
        copy(directory, id)
        start(id, directory, file2run, framework)
        print("✅")
        click.launch(link)

    if purge:
        prune()
        print("cleaning all instant linux machines ")
        print("😴")

    if delete:
        vals = click.prompt("delete container [Y/n]", confirmation_prompt=True)
        if vals.lower() == 'y' or vals.lower() == 'yes':
            click.echo(click.style('deleting ' + delete, fg='red', blink=True))
            clean(delete)
        else :
            click.echo(click.style('aborting', fg='green'))



if __name__ == "__main__":

    main()