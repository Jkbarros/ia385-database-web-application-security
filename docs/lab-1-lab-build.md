# Lab 1 Final

**Source:** [`Lab 1 Final.docx`](../archive/canvas-submissions/Lab%201%20Final.docx)  
**Course:** IA 385 - Database and Web Application Security (EMU)  
**Author:** Julio Barros

## Assignment 1: Lab Build

Julio Barros

Eastern Michigan University

IA 385: Database & Web App Security

Professor (or Dr.) Rachel Kinsella

9/24/2023

### Selecting Operational Systems

### First, I began by selecting my Windows and Linux systems. For the Windows server, I installed Windows Server 2022 because I already had an installation key for it, and I was more familiar with it from previous classes. Now, for the Linux platform, I initially started with Ubuntu. However, since it was an interface, I had never used before, I encountered some issues during the installation and system setup. Consequently, I decided to switch back to Kali, as I had prior experience with it and encountered no issues.

Installation Process for Windows Server

The installation process for Windows Server is straightforward if you already have the ISO downloaded. I simply opened my VMware and created a new virtual machine using the Windows Server ISO. During the setup, I chose 2 processors and 4 GB of memory, noting that my computer has an Intel i9 processor and 64 GB of RAM. I had used this setup configuration before without any problems when running multiple machines simultaneously. For storage, I selected a 60 GB NVMe drive, which was consistent with the hardware in my computer.

### Linux System

### As for the Linux situation, it can be a bit more complex and personalized for each machine. For instance, last winter, I encountered numerous issues with my Linux virtual machine, which would sometimes crash or stop working while I was running Windows machines. I discussed this with my girlfriend's brother, who mentioned experiencing similar issues. He managed to resolve them by increasing the number of processors from 4 to 5. Following his advice, I changed my configuration from 2 to 3 processors, and since then, I have not experienced any further crashes or shutdowns. The exact reason for this improvement remains unclear; some Reddit users suggested it might be related to BIOS settings or a conflict between my Intel processor and the virtual machine. However, since the current setup is working perfectly, I decided not to make any additional changes.

### For my Linux system, I configured it with 3 processors, 4 GB of memory, and 20 GB of SCSI storage. As for the Windows operating system, I opted for Windows 10 x64, as it is more stable and reliable than Windows 11 and experiences fewer glitches. After selecting my servers and operating systems, I had to configure the servers to enable communication between them and the operating system. Here's a quick tip I discovered: make sure that when you create the virtual machines, they all use the same boot method. For example, I set them all to boot using BIOS, as this reduces conflicts.

### IP Configuration and Servers Set Ups

Moving on to setting up all the machines, the first step was assigning IP addresses to each one:

Windows Server 1: 192.168.1.2

Windows Server 2: 192.168.1.3

Linux Server 1: 192.168.1.4

Linux Server 2: 192.168.1.5

Windows Workstation: 192.168.1.6

Subnet Mask: 255.255.255.0

Default Gateway: Default (left as default).

With these IP assignments in place, I proceeded to configure the machines further. I started by configuring the Windows servers, adding rules and features. I also joined both Windows servers to the same domain and promoted one server to be a member of this domain. Finally, I completed the setup by configuring the firewall to allow traffic between the servers.

Now, dealing with Linux is a bit more involved. Since my Linux distribution is Kali Ubuntu, the first task on my list was to check for updates using the command (sudo apt update). After completing this step, it prompted me to create a new user, set up a domain, generate an SSH key, and more. Once all these initial setup steps were completed, I proceeded to configure a basic firewall and ensure secure SSH access.

For those who are new to Linux, I have a valuable recommendation: consider installing Fail2Ban. It's a tool that automatically bans IP addresses that repeatedly fail authentication attempts. You can install it using the command (sudo apt install fail2ban). I always make sure to install Fail2Ban to enhance security and prevent potential attacks on my machines.

After this optional security step, I returned to complete the setup in the same domain as the Windows servers.

### References

YouTube. (2021, April 15). Install ubuntu server - full setup guide. YouTube. https://www.youtube.com/watch?v=K2m52F0S2w8&t=489s

YouTube. (2019, February 1). How to join Windows Server 2019 to an existing active directory domain. YouTube. https://www.youtube.com/watch?v=BEyNwwjo0u4

I want to learn how to make a linux server. Reddit. (n.d.). https://www.reddit.com/r/linuxquestions/comments/y69rwr/i_want_to_learn_how_to_make_a_linux_server/?share_id=AKeyqc22zLx295qh8gtzQ&utm_content=2&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1

YouTube. (2021, October 2). How to change the DHCP IP address range for VMware Workstation Virtual Machines. YouTube. https://www.youtube.com/watch?v=hkSnGdyJznA
