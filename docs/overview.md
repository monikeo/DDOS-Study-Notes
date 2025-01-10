# Overview of DDoS Attacks and Defense

## Introduction

**Distributed Denial of Service (DDoS)** attacks are one of the most common and disruptive types of cyber attack. These attacks overwhelm the target system with a flood of internet traffic, making it unavailable to legitimate users. While often associated with malicious intent, DDoS attacks can also serve as a tool for demonstrating the vulnerabilities of a network or testing its resilience.

This document serves as an introduction of DDoS, covering its basic concepts, characteristics, and the various forms of attack. It will also touch on the general defense mechanisms used to mitigate or stop DDoS attacks.

## What is a DDoS Attack?

A **Distributed Denial of Service (DDoS)** attack is a malicious attempt to disrupt the normal traffic of a targeted server, service, or network by overwhelming it with a flood of Internet traffic. DDoS attacks typically come from a distributed network of compromised devices (a botnet), making them much harder to defend against compared to traditional DoS (Denial of Service) attacks, which come from a single source.

### Key Characteristics

1. **Distributed Nature**: Unlike a traditional DoS attack that comes from a single source, DDoS attacks use multiple, often thousands or millions, of compromised devices (referred to as botnets) to generate massive amounts of traffic.
2. **High Traffic Volumn**: The attack involves sending high volumes of traffic to a server or network, exceeding its capacity to handle legitimate requests.
3. **Targeting System Resources**: DDoS attacks aim to exhaust the resources of the target system, including CPU, memory, bandwidth, or application-layer resources.
4. **Degraded Performance or Unavailability**: The result is often degraded performance (e.g., slow response times) or total unavailability or the target system.

## Common Types of DDoS Attacks

DDoS attacks come in various forms. Here are some of the most common attack types:

### 1. Vulumetric Attacks

These are designed to overshelm the target's network or server by flooding it with massive amounts of traffic.
- **Examples**: UDP Fllod, ICMP Flood, DNS Amplification.
- **Impact**: Consumes bandwidth, leading to a network outage.

### 2. Protocol Attacks

These attacks exploit weaknesses in the protocols used to communicate over the internet.
- **Example**: SYN Flood, Ping of Death, Smurf Attack.
- **Impact**: Consumes server resources and can overshelm a firewall or load balancer.

### 3. Application Layer Attacks

These attacks target specific applications or services that are running on a server. They are designed to exhaust server resources, such as memory or processing power.
- **Examples**: HTTP Flood, Slowloris.
- **Impact**: The server becomes unresponsive to legitimate user requests.

## The Anatomy of a DDoS Attack

To better understand how DDoS attacks work, it's useful to break them down into key phases:

### 1. Reconnaissance (Target Indentification)

The attacker begins by identifying a vulnerable target. This could be a server, a network infrastructure, or even an application. The attacker may conduct reconnaissance using open-source intelligence (OSINT), scanning for weak spots like exposed services or systems that lack proper protection.

### 2. Botnet Recruitment (Botnet Creation)

To launch a large-scale attack, the attacker requires a botnet, A botnet is a network of compromised machines (often called zombies) that can be remotely controlled. These machines can be infected through various means, such as phishing emails or explorting vulnerabilities in software.

### 3. Launch the Attack

Once the botnet is read, the attacker commands it to begin sending malicious traffic to the target. This can be done in waves to avoid detection and mitigation strategies. The traffic often overwhelms the target's resources, leading to service disruption.

### 4. Amplification (In Some Cases)

In some attacks, the attacker may use amplification techniques, where they leverage a third-party server (e.g., DNS, NTP) to send a much larger response to the target using a small query from the botnet.

## DDoS Attack Motivations

DDoS attacks can be launched for various reasons, including but not limited to:
- **Cybercrime**: Extortion attems, where attackers demand payment to stop the attack
- **Hacktivism**: Political or social causes motivating the attack, often to silence opposition or disrupt business operations.
- **Competitor Disruption**: Businesses may use DDoS attacks to damage competitors's reputation or distrupt their services.
- **Demonstration of Power**: Some attackers may launch DDoS attacks simply to prove they can overwhelm a target.


## DDoS Mitigation Strategies

Mitigation DDoS attacks requires a multi-layered approach, as there is no single solution to stop them entirely. Here are some of the common strategies used to defend against DDoS:

### 1. Traffic Filtering


