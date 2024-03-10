---
title: Cybersecurity

date: 2022-09-15

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

# Lecture 1

- ARPANET: Advanced Research Projects Agency Network
  - **Problem:** No safety procedures for dial-up connections to the network; Nonexistent user identification and authentication.

_Rand Report R-608_ - Started the study of computer security and identified the role of management and policy issues in it.

- **MULTICS:** Multiplexed Information and Computing Service
  - First OS with security integrated into core functions.

##### CIA Triad:

1. Confidentiality
   - Snooping
   - Traffic Analysis
2. Integrity
   - Modification
   - Masquerading
   - Replaying
   - Repudiation
3. Availability
   - Denial of Service
   - Service Interruption

{{% callout note %}}

**Masquerading:** Pretending to be someone else.

{{% /callout %}}

##### Critical Characteristics of information:

1. Availability
2. Accuracy
3. Authenticity
4. Confidentiality
5. Integrity
6. Utility
7. Possession

### Balancing Security and Access

1. Bottom-up approach

   - Begins at grassroots level where systems administrators and attempt to improve security of their systems.

2. Top-down approach

   - Begins at upper management level; Issue policy, procedures, and processes

### Data responsibilities

1. Data owner
2. Data custodian
3. Data user

## Lecture 2A - The Need for Security

### Social Engineering

- Phishing: Attempt to gain personal info; apparent legitimate communication hides embedded code that redirects user to third-party site.

- **Network intrusion** technique based on trickery.

### Software Attacks

1. Malwares

   - Viruses
     - Piggybacks on other executable files
     - Gets activated when host program executes
   - Worms
     - Crawls from host to host without any assistance
     - Internet may have to be shut down due to a infestation of a worm
   - Trojan Horses - Disguised as helpful, interesting, or useful programs.

2. Backdoors - Gaining access to system or network using known or previously unknown/newly discovered access mechanism

3. DoS and DDos
4. Packet Sniffer: Monitors network traffic and captures packets.
5. Spoofing: Assumes a trusted IP address.
6. Pharming: Attacks browser's address bar to redirect users to an illegitimate site.
7. Man-in-the-middle: Attacker intercepts communication between two parties.

**Open Web Application Security Project (OWASP)** is dedicated to helping organizations create/operate trustworthy software and publishes a list of top security risks.

## Lecture 3A - Legal, Ethical, and Professional Issues in Information Security

**Liability** exposure refers to unnecessary risk that an organization exposes itself to when it fails to take action to prevent harm.

- Laws: Rules that are enforced by the government
- Ethics: Rules that are enforced by society
- Cultural mores: Rules that are enforced by a particular group

- Policies: Managerial directives specifying acceptable and unacceptable behavior

**Relevant singapore laws:** Computer misuse and cybersecurity act.

**Deterrence:** Method for preventing illegal or unethical activites. For eg. Laws, policies, technical controls.

## Lecture 3B - Planning for Security

- Information security planning and governance

  - Governance
    - Practices exercised by board and executive management
  - Goals
    - Strategic alignment
    - Risk management
    - Resource management
    - Performance measures
    - Value delivery

- Policy, standards, and practice

  - Should never contradict law
  - Policy is the organizational law that dictates acceptable and unacceptable behavior.

- Security models
  - ISO 27000 series
  - NIST Security models

#### Design of security architecture

Levels of controls:

1. Management
2. Operational
3. Technical

##### Defense in depth

- Layered approach to security
- Demilitarized zone (DMZ) - external and interal filtering router to connect untrusted network to trusted network.

##### Security perimeter

- Border of security protecting internal systems from outside threats
  - Does not protect against internal attacks from employee threats or onsite physical threats

##### Security Education, Training, and Awareness Program (SETA)

SETA is a control measure designed to reduce accidental security breaches.

#### Continuity Strategies

1. Incident response plans - focuses on immediate response;
   - Identification, classification and response to an accident
2. Disaster recovery plans - Focuses on restoring systems after disasters occur;
   - Actions taken to prepare for and recovery from the impact of an incident
3. Business continuity plans - Concurrently with DRP;
   - Ensures that critical business functions continue if a catastrophic event occurs

### Contingency Planning (CP) Process

1. Develop CP policy statement
2. Conduct business impact analysis
3. Identify preventive controls
4. Create contingency strategies
5. Develop contingency plans
6. Ensure plan testing, training, and exercises
7. Ensure plan maintenance

#### CP Policy

- Introductory statement of philosophical perspective
- Statement of scope/purpose
- Call for periodic risk assessment/BIA
- Specification of CP’s major components
- Call for/guidance in the selection of recovery options
- Requirement to test the various plans regularly
- Identification of key regulations and standards
- Identification of key people responsible for CP operations
- Challenge to the organization members for support
- Administrative information
