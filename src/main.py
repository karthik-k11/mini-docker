##Imports
import sys
import os
import subprocess


def setup_mount_namespace():
    subprocess.run(
        ["mount", "--make-rprivate", "/"],
        check=True
    )


def setup_chroot():
    new_root = "container_root"

    try:
        os.chroot(new_root)
        os.chdir("/")
    except Exception as e:
        print(f"chroot failed: {e}")
        sys.exit(1)


def run_command(args):
    print(f"Running command: {' '.join(args)}")

    pid = os.fork()

    if pid == 0:
        ##CHILD PROCESS

        try:
            os.unshare(os.CLONE_NEWNS)
        except PermissionError:
            print("Permission denied. Run with sudo.")
            sys.exit(1)

        setup_mount_namespace()
        setup_chroot()

        try:
            ##Apply CPU priority
            os.nice(10)

            ##Execute command directly
            os.execvp(args[0], args)

        except Exception as e:
            print(f"Execution failed: {e}")
            sys.exit(1)

    else:
        os.waitpid(pid, 0)

##Main function()
def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py run <command> [args...]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "run":
        args = sys.argv[2:]
        run_command(args)

    else:
        print(f"Unknown command: {action}")
        sys.exit(1)


if __name__ == "__main__":
    main()