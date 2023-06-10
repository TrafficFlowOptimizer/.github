from subprocess import run, STDOUT, PIPE, DEVNULL
from os import getcwd
from sys import argv

def fetch_all():
    run("git fetch")
    run("git fetch", cwd="../frontend")
    run("git fetch", cwd="../backend")
    run("git fetch", cwd="../car-recognition-model")
    run("git fetch", cwd="../database")
    run("git fetch", cwd="../optimizer")
    
def pull_all():
    run("git pull")
    run("git pull", cwd="../frontend")
    run("git pull", cwd="../backend")
    run("git pull", cwd="../car-recognition-model")
    run("git pull", cwd="../database")
    run("git pull", cwd="../optimizer")

def docker_run(repos):
    if repos[0] == "1": run("docker compose up -d", cwd="../database")
    if repos[1] == "1": run("docker compose up -d", cwd="../optimizer")

def docker_rebuild_and_run(repos):
    if repos[0] == "1": run("docker compose up -d --build --force-recreate --no-deps", cwd="../database")
    if repos[1] == "1": run("docker compose up -d --build --force-recreate --no-deps", cwd="../optimizer")

if __name__ == "__main__":
    if len(argv) == 1 or argv[1] == "-h" or argv[1] == "--help":
        print("what do you want to do?")
        print("fetch all repos - fetch")
        print("pull all repos - pull")
        print("run docker containers - docker xy")
        print("rebuild and run docker containers - redocker xy")
        print("x - database, y - optimizer")
        print("so running database and NOT starting optimizer - docker 10")
    elif getcwd().split("\\")[-1] != ".github": print("run from org/.github directory")
    elif argv[1] == "fetch": fetch_all()
    elif argv[1] == "pull": pull_all()
    elif argv[1] == "docker": docker_run(argv[2])
    elif argv[1] == "redocker": docker_rebuild_and_run(argv[2])
        