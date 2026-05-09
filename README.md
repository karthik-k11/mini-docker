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
Limitations


Conclusion 


