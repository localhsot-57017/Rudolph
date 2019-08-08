# Rudolph

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

<ul>
    <li> Ubuntu 14.04 </li>
    <li> Ubuntu 16.04 </li>
    <li> Ubuntu 18.04 </li>
    <li> Ubuntu 19.04 </li>
    <li> centOS 6.10 </li>
    <li> centOS 7 </li>
    <li> Debian Jessie </li>
    <li> Debian Stretch </li>
</ul>

## Options for frameworks
<ul>
    <li> Spring-Boot </li>
    <li> Flask (Python 2) </li>
    <li> Flask (Python 3) </li>
</ul>
    

## IN CURRENT TEST RELEASE 

To Install - pip install -i https://test.pypi.org/simple/ maggi


## TODO
    - allow custom jenkins pipeline 
    - penetration tests to be added
    - support dynamic ip change
    - create and support load testing env
    - Streaming server and FTP server

## CONTACT 
    mail ( sarkar.anurag@outlook.com )
    mail ( anishksaha1997@gmail.com )
