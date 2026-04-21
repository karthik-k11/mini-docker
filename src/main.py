##Imports
import sys
import os


def run_command(command: str):
    print(f"Running command: {command}")

    pid = os.fork()

    if pid == 0:
        ##CHILD PROCESS

        try:
            ##Create new PID + Mount namespace
            os.unshare(os.CLONE_NEWPID | os.CLONE_NEWNS)
        except PermissionError:
            print("❌ Permission denied. Run with sudo.")
            sys.exit(1)

        ##Second fork
        pid2 = os.fork()

        if pid2 == 0:
            ##INNER CHILD

            try:
                args = command.split()
                os.execvp(args[0], args)

            except Exception as e:
                print(f"Execution failed: {e}")
                sys.exit(1)

        else:
            os.waitpid(pid2, 0)
            sys.exit(0)

    else:
        os.waitpid(pid, 0)


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