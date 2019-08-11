# Rudolph


[![Generic badge](https://img.shields.io/badge/CLOUD-READY-GREEN.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/TEST-READY-GREEN.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/LINUX-ONLY-GREEN.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/CROSS_PLATFORM-READY-GREEN.svg)](https://shields.io/)


<b>Rudolph</b> a is CLI app for creating ec2 like environments for deploying
and testing your apps it is pre-baked with CI/CD support and runs on
kubernetes and docker by default. It has its own web based terminal
and does not require external dependencies.

## Basic instructions :



    --create            will setup an environment to get you started
                        requires size of vm.
                        requires number of cpu to be allocated
                        requires which port to open.

    --purge             it will completely remove vm's which are not
                        working or stalled.

    --delete [VM ID]    it will remove all the data including the vm
                        from system hardware.

    --performance [VM]  shows system utility of vm (can be used while
                        testing load or scaling.)

## Options for Operating Systems in the container


- Ubuntu 14.04 
- Ubuntu 16.04
- Ubuntu 18.04
- Ubuntu 19.04
- centOS 6.10
- centOS 7
- Debian Jessie
- Debian Stretch


## Options for frameworks

- Spring-boot
- Flask-App
- Django


## TODO
    - allow custom jenkins pipeline 
    - support dynamic ip change
    - create and support load testing env
    - Streaming server and FTP server

## CONTACT 
    mail ( sarkar.anurag@outlook.com )
    mail ( anishksaha1997@gmail.com )
