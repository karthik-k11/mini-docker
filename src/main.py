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