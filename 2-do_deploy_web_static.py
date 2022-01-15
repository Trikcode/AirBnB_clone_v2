#!/usr/bin/python3
""" compress files """
from fabric.api import *
import os
env.hosts = ['35.231.216.93', '35.196.0.213']


def do_deploy(archive_path):
    """ decompress files after sending """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path[9:-4]
        arch_dest = "/data/web_static/releases/" + filename + "/"
        run("sudo mkdir -p {}".format(arch_dest))
        run("sudo ls {}".format(arch_dest))
        run("sudo tar -xvzf {} {}".format(archive_path, arch_dest))
        run("sudo rm -R {}".format(archive_path))
        run("sudo ln -sf /data/web_static/releases/{}/ \
            /data/web_static/current".format(filename))
        return True
    except:
        return False
