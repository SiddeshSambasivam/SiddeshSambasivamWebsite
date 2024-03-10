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

# A. Cryptography

An art and science of secret writing, encryping, or hiding of information from all but the intended recipient. **Cryptanalysis** is the art and science of breaking codes.

##### Basic Definitions

- **Plaintext** is the original message.
- **Ciphertext** is the encrypted message.
- **Cipher** is the algorithm used to encrypt the message.
- **Key** is the secret used to encrypt or decrypt a message.
- **Encryption** is the process of converting plaintext into ciphertext.
- **Decryption** is the process of converting ciphertext into plaintext.

{{% callout note %}}

- **Asymmetric cryptosystem** -- Two different keys are used to encrypt or decrypt a message
- **Symmetric cryptosystem** -- The same key is used to encrypt or decrypt a message

{{% /callout %}}

### 1. Types of Ciphers

- Substitution ciphers
- Transposition ciphers
- Product ciphers

### 2. Keys

- Key is used to both encrypt and decrypt a message.

### 3. Stream Ciphers

- A stream cipher is a cipher that encrypts a message one bit at a time.

  - Faster ans use less code

- **RC4** is the most widely used of all stream ciphers

### 4. Block Ciphers

- A block cipher is a cipher that encrypts a message one block (8- or 16-bit) at a time.

  - Slower but more secure

- Used for blocks of data, such as file transfer, e-mail, and database

- DES, 3DES, AES, RC5, Blowfish, etc.

* Electronic Code Book (ECB) mode

  - Each block is encrypted independently of the other blocks

* Cipher Block Chaining (CBC) mode

  - Each block is encrypted using the previous block

## B. Intrusion Detection and Prevention Systems

- Prevention -- Deter intrusions
- Detection -- Detect intrusions
- Response -- Respond to intrusions
- Correction -- Restore operations and prevent future intrusions

#### Types of IDPS

1. Network-based systems (NIDPS) - protecting network information assets
   - Resides in a computer connected to a segment of the network
   - Cannot analyze encrypted packets
2. Host-based systems (HIDPS) - protecting host information assets
   - Resides on a computer
   - Can analyze encrypted packets
   - _susceptible to DoS attacks_
3. Wireless IDPS
4. Network behaviour analysis IDPS

- **Honeypots:** decoy system to lure potential attackers
  - Divert attacker
  - Collect information about attacker
- **Honeynets:** network of honeypots

* **Padded cell system** -- protected honeypot

#### Trap-and-Trace Systems

- Techniques to detect an intrusion and trace it back to its source
- Trap consists of honeypots or a padded cell and alarm

- Enticement is legal but entrapment is not; entrapment is luring an individual into committing a crime to get convicted

* **Footprinting:** process of collecting publicly available information about a potential target
  - **Fingerprinting:** survey of target organization's internet addresses collected during the footprinting phase

**Operating system detection tools:** Ability to detect a target computer's OS is very valuable to an attacker.

- **Active vulnerability scanners:** examine networks for highly detailed information and initiate traffic to determine

- **Passive vulnerability scanners:** identify the vulnerable versions of both server and client software

- **Packet sniffers:** capture and analyze network traffic
  - Can also be used to eavesdrop on network traffic

# C. Access control and authentication

**Access control** is the process of restricting access to a resource based on the identity of the user.

Types of access control:

1. **Discretionary access control** -- Access is granted or denied based on the discretion of the owner of the resource (User)
2. **Non-discretionary access control** -- Access is granted or denied based on the discretion of the organisation

   1. Mandatory access control (MAC) -- Access is granted or denied based on the security level of the resource

   2. Role-based access control (RBAC) -- Access is granted or denied based on the role of the user

# D. Firewalls

1. Packet filtering firewalls -- Uses the packet header to determine whether to allow or deny the packet

   - Static filtering - Determined set of rules
   - Dynamic filtering - React to event and update or create rules on the fly
   - Stateful packet inspection (SPI) - Tracks the state of the connection

2. Application layer firewall -- installed on a dedicated computer; known as proxy server

3. MAC layer firewalls -- filtering decisions based on specific host computer’s identity

   - MAC addresses of specific host computers are linked to _access control list (ACL)_

### Firewall Architectures

1. Packet-filtering routers -- at boundary b/w internal and external networks
2. Dual-homed firewalls (bastion hosts)

   - Two network interface cards: one for internal network and one for external network
   - Uses network address translation (NAT) to create another barrier

3. Screened host firewalls
4. Screened subnet firewalls

### Virtual Private Networks (VPNs)

- **War Dialer:** Automatic phone-dialing program that dials every number in a configured range and records number if modem picks up

Three VPN technologies:

1. Trusted VPN
2. Secure VPN
3. Hybrid VPN

There are different modes of VPN operation:

1. Transport mode -- data within IP packet is encrypted. but IP header is not

   - Remote access worker connects to office network over internet

2. Tunnel mode -- Two perimeter tunnel servers to encrypt all traffic that will traverse unsecured network

   - reveals nothing about the true destination system
