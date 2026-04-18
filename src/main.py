##imports
import sys
import subprocess

def run_command(command: str):
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True
        )
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with exit code {e.returncode}")
        sys.exit(e.returncode)

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py run <command>")
        sys.exit(1)

    action = sys.argv[1]

    if action == "run":
        command = sys.argv[2]
        print(f"Running command: {command}")
        run_command(command)
    else:
        print(f"Unknown command: {action}")
        sys.exit(1)


if __name__ == "__main__":
    main()