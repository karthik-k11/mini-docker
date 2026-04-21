##Imports
import sys
import os
import subprocess


def setup_mount_namespace():

    subprocess.run(
        ["mount", "--make-rprivate", "/"],
        check=True
    )


def run_command(command: str):
    print(f"Running command: {command}")

    pid = os.fork()

    if pid == 0:
        ##CHILD PROCESS

        try:
            ##Only mount namespace 
            os.unshare(os.CLONE_NEWNS)
        except PermissionError:
            print("Permission denied. Run with sudo.")
            sys.exit(1)

        ##Setup mount namespace
        setup_mount_namespace()

        try:
            args = command.split()
            os.execvp(args[0], args)
        except Exception as e:
            print(f"Execution failed: {e}")
            sys.exit(1)

    else:
        os.waitpid(pid, 0)

##Main function()
def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py run <command>")
        sys.exit(1)

    action = sys.argv[1]

    if action == "run":
        command = sys.argv[2]
        run_command(command)
    else:
        print(f"Unknown command: {action}")
        sys.exit(1)


if __name__ == "__main__":
    main()