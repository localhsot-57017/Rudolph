import os 
import subprocess


def copy(directory_path, instantbox_url_path_source):
    print("copying data to VM")
    subprocess.run(['scp', '-v', directory_path , instantbox_url_path_source])


# copy("/Users/oyo/Desktop/a.cpp", "anurag.sarkar1@10.15.14.22:")