##Imports
import sys
import os


def run_command(command: str):

    print(f"Running command: {command}")

    ##fork process
    pid = os.fork()

    if pid == 0:
        ##CHILD PROCESS
        try:
            ##Split command into list
            args = command.split()

            ##Replace current process with new program
            os.execvp(args[0], args)

        except Exception as e:
            print(f"Execution failed: {e}")
            sys.exit(1)

    else:
        ##PARENT PROCESS
        _, status = os.waitpid(pid, 0)

        exit_code = os.WEXITSTATUS(status)

        if exit_code != 0:
            print(f"Error: Command failed with exit code {exit_code}")
            sys.exit(exit_code)

##Main function
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