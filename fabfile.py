from fabric.api import settings, abort, run, cd, sudo, put, env, prompt, get, local
from fabric.contrib.project import rsync_project
import time

env.backup_directory = "../backups"

def dryrun():
    env.rsync_dryrun = True

def nodelete():
    env.rsync_delete = False

def dev():
    env.hosts = ["test.rabash.net"]
    env.user = "rabash"
    env.i = "~/.ssh/id_rsa.pub"
    env.rsync_source = "./_site/"
    env.rsync_target = "/var/www/sites/djurensratt/prototyp"
    env.rsync_excludes = []
    env.rsync_delete = True
    env.rsync_dryrun = False
    env.backup_name = "djurensratt_proto_"

def prepare_deploy():
    local("find . -name \".DS_Store\" -depth -exec rm {} \;")

def deploy():
    extra_opts = ""
    if env.rsync_dryrun == True:
        extra_opts = extra_opts + "--dry-run"
    rsync_project(env.rsync_target, env.rsync_source, env.rsync_excludes, env.rsync_delete, extra_opts)

def backup():
    backup_file = env.backup_directory + "/" + env.backup_name + time.strftime("%Y%m%d%H%M%S")
    run("tar zcvf {0}.tar.gz {1}".format(backup_file, env.rsync_target))