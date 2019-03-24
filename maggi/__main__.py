#!/usr/bin/env python3


import click
import pyfiglet
import inquirer

from maggi.utils.connector import dockin
from maggi.utils.create import createbox
from maggi.utils.delete import clean
from maggi.utils.instabox import buildlinux
from maggi.utils.prune import prune


@click.command()
@click.option('--create',
              is_flag=True,
              help='setup a VM for running deployment tools/tests very similar to an EC2 instance',)
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
        cpu = click.prompt("please enter number of cpu core to dedicate :")
        mem = click.prompt("plese enter the memory in MB : ", default="512", confirmation_prompt=True)
        port = click.prompt("please enter the port to access : ", default="15178", confirmation_prompt=True)
        print(os, cpu, mem, port)
        buildlinux(path)
        id, link = createbox(os, cpu, mem, port)
        dockin(id)
        click.launch(link)

    if purge:
        prune()
        print("cleaning all instant linux machines ")

    if delete:
        vals = click.prompt("delete container [Y/n]", confirmation_prompt=True)
        if vals.lower() == 'y' or vals.lower() == 'yes':
            click.echo(click.style('deleting ' + delete, fg='red', blink=True))
            clean(delete)
        else :
            click.echo(click.style('aborting', fg='green'))



if __name__ == "__main__":

    main()