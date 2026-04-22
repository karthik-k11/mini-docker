##Imports
import sys
import os
import subprocess


def setup_mount_namespace():
    try:
        subprocess.run(
            ["mount", "--make-rprivate", "/"],
            check=True
        )
    except subprocess.CalledProcessError:
        print("Failed to configure mount namespace")
        sys.exit(1)


def setup_chroot():
    new_root = "container_root"

    if not os.path.exists(new_root):
        print("container_root not found. Did you set up Day 5?")
        sys.exit(1)

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
            print("Permission denied. Use sudo.")
            sys.exit(1)

        setup_mount_namespace()
        setup_chroot()

        try:
            os.nice(10)
            os.execvp(args[0], args)
        except FileNotFoundError:
            print(f"Command not found inside container: {args[0]}")
            sys.exit(1)
        except Exception as e:
            print(f"Execution error: {e}")
            sys.exit(1)

    else:
        _, status = os.waitpid(pid, 0)
        exit_code = os.WEXITSTATUS(status)

        if exit_code != 0:
            print(f"Process exited with code {exit_code}")


def print_usage():
    print("\nUsage:")
    print("  python3 src/main.py run <command> [args...]")
    print("\nExample:")
    print("  python3 src/main.py run ls -l\n")


def main():
    if len(sys.argv) < 2:
        print("No command provided")
        print_usage()
        sys.exit(1)

    action = sys.argv[1]

    if action == "run":
        if len(sys.argv) < 3:
            print("No command specified")
            print_usage()
            sys.exit(1)

        args = sys.argv[2:]
        run_command(args)

    else:
        print(f"Unknown action: {action}")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()