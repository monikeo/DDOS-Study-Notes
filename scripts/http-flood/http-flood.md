# HTTP Flood Attack

**What is an HTTP Fllod Attack?**

An **HTTP Flood** is a type of Distributed Denial-of-Service (DDoS)attack that targets web servers or applications by overwhelming them with HTTP request. The attacker uses a large number of HTTP request, often mimicking legitimate user behavior, to exhaust server resources and make the service unavailable to actual users.

## Principle of HTTP Flood

#### 1. HTTP Requests

- HTTP (HyperText Transfer Protocol) is the foundation of data communication of the web.
- HTTP flood attacks send GET or POST requests to the target, consuming bandwidth, CPU, and memory.

#### 2. Legitimacy Simulation

- Attackers often craft requests that appear legitimate, making it hard for systems to distinguish between attack traffic and real user traffic.

- For example:
    - **GET Request**: Retrieves web pages, images, or files.
    - **Post Request**: Sends data to the server (e.g., login forms, file uploads).

#### 3. Volume and Persistence

- The attack floods the server with a high volume of requests, which can overlaod web servers, databases, or application layers.
- Persistence involves maintaining long-lived connections (e.g., slow HTTP headers) to tie up resources.

#### 4. Distributed Nature

- Often carried out by a botnet (a network of compromised devices), making it harder to mitigate since request come from many IPs.

## How Does a HTTP Flood Workd?

#### 1. Preparation

- The attacker builds or controls a botnet of infected devices to generate traffic
- Alternatively, tools like LOIC, HOIC, or custom scripts can simulate floods from a single device (smaller-scale attacks).

#### 2. Request Generation

- The botnet or attacker sends repeated HTTP GET or POST requests to specific URLs or endpoints on the target server.
- Requests may target resource-intensive operations, such as dynamic database queries.

#### 3. Server Exhaustion

- Servers allocate memory, CPU, and I/O operations to process each request.
- if the volume of requests exceeds the server's capacity, legitimate traffic is delayed or denied.

#### 4. Amplification Techniques

- Attackers may send malformed or oversized requests.
- They may exploit application vulnerabilities to increase resource
  consumption (e.g., triggering excessive database queries).

