MAGGI

MAGGi a is CLI app for creating ec2 like environments for deploying
and testing your apps it is pre-baked with CI/CD support and runs on
kubernetes and docker by default. It has its own web based terminal
and does not require external dependencies.

To use maggi :



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


IN CURRENT TEST RELEASE 
To Install - pip install -i https://test.pypi.org/simple/ maggi


TODO
    - create jenkins pipeline and git hooks
    - penetration tests to be added
    - support dynamic ip change
    - create and support load testing env
    - Streaming server and FTP server

CONTACT 
    mail ( sarkar.anurag@outlook.com )
