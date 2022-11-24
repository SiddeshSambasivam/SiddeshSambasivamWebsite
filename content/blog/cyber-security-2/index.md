---
title: Cybersecurity

date: 2022-10-02

math: true
diagram: true
highlight: true
toc: true
type: page

image:
  placement: 1
  caption: ""

summary:

_build:
  render: always
  list: never
---

# A. Hardware and Physical Security

Files are usually fragmented into smaller pieces and stored on different disks. Therefore, the process of defragmention can improve the performance of accessing files.

##### what happens when files are created?

1. Entry is made into the File Allocation Table (FAT) to indicate the location of the file.
2. The directory entry is made to indicate file name, size, and the link to the FAT entry.
3. The data is written to the data area

##### what happens when files are deleted?

1. FAT entry for the file is zeroed out and the space is marked as free.
2. First character of the directory entry file name is changed to a special character (e.g., \*).
   - Nothing is done to the data area

##### what happens when files are restored?

1. FAT entry is linked again to the location of the file.
2. The first character of the directory entry file name is changed to a legal character.
   - Nothing is done to the data area

{{% callout note %}}

**Safety Measures -- Disposing or sharing hard drives**

- just formatting a disk does not erase the data, only the address tables;
- Always perform disk sanitization or overwriting with random bits before disposing of a disk;

{{% /callout %}}

- Physical security is also called _infrastructure security_.

# B. Security and Personnel

- Security awareness, training and education programs are important in limiting an organization's liability
- Security awareness policy document -- emphasize the importance of security awareness

- Chief information security officer (CISO) -- responsible for the overall security of the organization; reports to the Chief information officer

For major incidents, a company must convene a computer security incident response team (CSIRT) to investigate the incident and determine the extent of the damage.

- Different stages of a computer security incident response team (CSIRT)
  - Preparation
  - Detection
  - Stopping
  - Repairing
  - Punishing the attacker
  - Lessons learned
