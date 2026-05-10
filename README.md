# Mini Docker - Container Runtime from Scratch

A minimal container runtime built from scratch using Python and Linux primitives such as namespaces, `fork`, `exec`, and `chroot`.

This project demonstrates the fundamental concepts behind containerization and how Docker-like systems work internally without relying on Docker itself.

---

## Overview

The project implements a lightweight container runtime capable of:

- Running commands inside isolated environments
- Creating isolated filesystem views
- Managing processes using low-level Linux APIs
- Providing a simple CLI similar to `docker run`
- Demonstrating core container concepts for educational purposes

The implementation focuses on understanding operating system internals rather than production-grade container orchestration.

---

## Features

### Process Management
- Process creation using `fork()`
- Program execution using `execvp()`
- Parent-child process lifecycle handling

### Filesystem Isolation
- Filesystem isolation using `chroot`
- Separate root filesystem for container processes
- Minimal container filesystem setup

### Namespace Isolation
- Mount namespace isolation using `os.unshare`
- Private mount propagation using `mount --make-rprivate`

### Resource Control
- Basic CPU scheduling control using `os.nice`

### Command-Line Interface
- Custom CLI similar to Docker
- Support for command arguments
- Error handling and validation

---

## Concepts Implemented

This project demonstrates the following Linux and containerization concepts:

- Linux processes
- `fork` and `exec`
- Filesystem isolation
- Mount namespaces
- `chroot`
- Process execution
- Shared libraries and binary dependencies
- CPU scheduling priority
- Container runtime basics

---

## Project Structure

```text
mini-docker/
├── src/
│   └── main.py
├── container_root/
│   ├── bin/
│   ├── lib/
│   └── lib64/
├── README.md
└── .gitignore
```

### How It Works
The runtime follows this workflow:
Parse CLI input
Create a child process using fork()
Create a mount namespace
Configure mount propagation
Change the process root using chroot
Apply CPU priority using nice
Execute the requested command using execvp()
This creates an isolated execution environment similar to how containers operate internally.


### Requirements
Linux or WSL2
Python 3
Root privileges (sudo)

### Setup
Clone Repository
```bash
git clone <your-repo-url>
cd mini-docker
```

Create Minimal Container Filesystem
```bash
mkdir -p container_root/bin
mkdir -p container_root/lib
mkdir -p container_root/lib64
```
#### Copy Required Libraries
Use ldd to inspect dependencies:
```bash
ldd /bin/ls
```
#### Copy required libraries into:
```bash
container_root/lib/
container_root/lib64/
```

### Usage
Run a Command
```bash
sudo python3 src/main.py run ls
```
Run Command with Arguments
```bash
sudo python3 src/main.py run ls -l
```
Run Inside Container Root
```bash
sudo python3 src/main.py run ls /
```
Run Echo
```bash
sudo python3 src/main.py run echo hello world
```

Example Output
```bash
$ sudo python3 src/main.py run ls
bin  lib  lib64
```
Resource Control Example
Run a CPU-intensive process:
```bash
sudo python3 src/main.py run yes
```

### Similarities to Docker
This project implements several concepts used in real container runtimes:
- Filesystem isolation using chroot
- Namespace isolation
- Process isolation concepts
- Container-style CLI workflow
- Isolated execution environments

### Limitations
This is an educational implementation and does not include:
- Full PID namespace support
- Network namespaces
- cgroups-based resource limits
- OverlayFS image layering
- Container lifecycle management
- Security hardening
- Production-grade isolation
- WSL limitations also affect some namespace features.

### Future Improvements
- Possible future enhancements include:
- Full PID namespace support
- Network namespace implementation
- cgroups integration
- OverlayFS support
- Container IDs and lifecycle management
- Better filesystem image management
- Shell support inside containers

### Key Learning Outcomes
This project helped explore:
- How containers work internally
- Linux process management
- Namespace isolation
- Filesystem isolation techniques
- Low-level operating system concepts
- Container runtime architecture