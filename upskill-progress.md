# DevOps & Cloud Upskilling Progress

## About Me
- Complete beginner to DevOps, cloud infrastructure, and containerisation
- Have some Python scripting experience (log analyser, login detector scripts)
- Working on a work device — security conscious, prefer minimal permissions
- Goal: gain technical competency across cloud, cloud security, DevOps, and infrastructure roles
- Target role: Cloud & DevOps Engineer (Azure, Kubernetes, GitHub Actions)
- Secondary interest: Cybersecurity GRC roles
- Certifications to target in order: AZ-900 → AZ-104 → AZ-500 → CKA

## How I like to work with Claude
- Explain what every command and piece of code does — not just what to type
- Cover why it matters and real-world applicability
- Use simple analogies to make concepts stick
- Do not skip explanations to save time — understanding is the priority

## Environment
- OS: Windows 11 (work device)
- Code editor: VS Code
- Cloud environment: GitHub Codespaces (Docker pre-installed, no local Docker)
- GitHub username: aosman99
- Repo: github.com/aosman99/security-upskill
- GitHub auth: Fine-grained PAT (scoped to security-upskill repo, Contents: Read/Write)

## Completed Sessions

### Session 1: Dockerise a Python Script
**What was covered:**
- What Docker is and the problem it solves ("works on my machine")
- Images vs containers (recipe vs the cooked meal)
- Writing a Dockerfile — FROM, WORKDIR, COPY, RUN, CMD
- Building an image: `docker build -t log-analyzer .`
- Running a container: `docker run log-analyzer`
- Volume mounts: `docker run -v $(pwd)/access.log:/app/access.log log-analyzer`
- Difference between baking data into an image vs injecting it at runtime
- Pushed repo to GitHub using a fine-grained PAT (secure approach for work device)

**Files created:**
- `Dockerfile`
- `requirements.txt`
- `.dockerignore`

**Key concepts to remember:**
- Docker image = static recipe, reusable, identical everywhere
- Docker container = running instance of that recipe
- Volume mount = inject data at runtime instead of baking it in

---

### Session 2: GitHub Actions — Automated CI/CD
**What was covered:**
- What CI/CD is — Continuous Integration / Continuous Deployment
- GitHub Actions as an automation tool triggered by events (e.g. git push)
- Writing a workflow file: trigger, runner machine, steps
- How `actions/checkout@v4` works (pre-built Action from GitHub marketplace)
- Reading GitHub Actions logs — each Dockerfile instruction as a numbered step
- The difference between CI (build and test automatically) and CD (deploy automatically)
- Security scanning mentioned as a future topic (Trivy, Snyk)
- Docker Hub does not filter content — org-level controls and image scanning fill that gap

**Files created:**
- `.github/workflows/docker-build.yml`

**Key concepts to remember:**
- Push code → GitHub spins up clean Ubuntu machine → runs workflow steps → reports pass/fail
- Workflow file = trigger + machine + ordered steps
- Actions tab on GitHub = your debugging tool when builds fail

---

### Session 3: Linux Command Line Fundamentals

**What was covered:**
- Navigating the filesystem: `pwd`, `ls`, `ls -la`, `cd`, `cd ..`, `cd ~`
- Reading files: `cat`, `less`, `head -n 20`, `tail -n 20`, `tail -f` (live log watching)
- Writing files: `echo`, `>` (overwrite), `>>` (append), `touch`, `cat > file << 'EOF'`
- Deleting: `rm`, `rm -r` (recursive — permanent, no recycle bin)
- Permissions deep dive: the 10-character string, three groups (owner/group/other), rwx values
- `chmod` with symbolic (`+x`) and numeric (`644`, `755`, `600`) notation
- Processes: `ps aux`, `top`, `kill`, `kill -9`
- Piping: `|` chains command output as input to the next command
- Searching: `grep`, `grep -r`, `grep -i`, `grep -n`, `find`
- Redirection: `>` and `>>` to write to files
- Package management: `apt update`, `apt install`, `sudo`
- Key insight: local files (e.g. auth.log) don't exist in Codespaces unless committed to git

**Key concepts to remember:**

**Permissions:**
- 10 characters: `[type][owner-rwx][group-rwx][other-rwx]`
- `-` in a slot = that permission is absent (not a choice — each slot is fixed: r=4, w=2, x=1)
- `chmod 600` = private (owner read/write only) — use for SSH keys, secrets
- `chmod 644` = normal file (owner read/write, everyone read)
- `chmod 755` = executable/directory (owner full, everyone read+execute)
- "Permission denied" on a script = missing `x` → fix with `chmod +x filename`
- SSH rejects private keys with permissions wider than `600`

**Piping:**
- Unix philosophy: small tools that do one thing well, composed via `|`
- `grep "Failed" auth.log | awk '{print $11}' | sort | uniq -c | sort -rn` — attacker ranking from a log file
- CI/CD pipelines (GitHub Actions) follow the same mental model: each step feeds the next
- Shell pipes = quick investigation; Python scripts = repeatable, shareable logic

**Real-world scenarios covered:**
- Script won't run → `chmod +x script.sh`
- SSH key rejected → `chmod 600 key.pem`
- Web server can't serve files → `chmod 644` so the server user can read them
- Count failed logins: `grep "Failed" auth.log | wc -l`
- Find attackers by IP: `grep "Failed" auth.log | awk '{print $11}' | sort | uniq -c | sort -rn`

---

## Session 4: To Do — Networking Basics

**Why:** Everything in cloud and DevOps is networked. You cannot configure Azure, Kubernetes, or security rules without understanding how traffic flows — IP addresses, DNS, ports, HTTP, and firewalls are the vocabulary of every cloud job.

**What to cover:**
- IP addresses — what they are, IPv4 vs IPv6, public vs private
- Subnets and CIDR notation (what `10.0.0.0/24` means)
- DNS — how a domain name becomes an IP address (the phone book analogy)
- HTTP vs HTTPS — request/response cycle, status codes, TLS
- Ports — what they are, why they matter, common ones (22, 80, 443, 3000, 8080)
- Firewalls and Network Security Groups (NSGs) — allow/deny rules
- Load balancers — distributing traffic across multiple servers
- How a browser request travels from your laptop to a web server and back
- Real-world relevance: Azure VNets, Kubernetes Services, GitHub Actions runners

**Hands-on to prepare:**
- No setup needed — this is concept-heavy with some terminal commands (`curl`, `nslookup`, `ping`)
- Run these in your Codespace to see DNS and HTTP in action:
  ```bash
  curl -I https://github.com
  nslookup github.com
  ping -c 4 github.com
  ```

---

## Roadmap Ahead

| Session | Topic |
|---|---|
| 1 | Docker basics ✓ |
| 2 | GitHub Actions / CI/CD ✓ |
| 3 | Linux command line fundamentals ✓ |
| 4 | Networking basics (IP, DNS, HTTP, ports, firewalls) |
| 5 | Azure fundamentals |
| 6 | Azure security (IAM, RBAC, Key Vault) |
| 7 | Kubernetes basics |
| 8+ | Terraform, deeper Kubernetes, cloud security specialisation |
