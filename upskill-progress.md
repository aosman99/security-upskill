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

## Session 3: To Do — Linux Command Line Fundamentals

**Why:** Almost all cloud infrastructure runs on Linux. Every tool in this roadmap assumes comfort with the Linux command line. This is non-negotiable foundation.

**What to cover:**
- Navigating the filesystem (cd, ls, pwd, mkdir, rm)
- Reading and writing files (cat, echo, touch, nano)
- Permissions (chmod, chown, ls -la — what rwx means)
- Processes (ps, kill, top)
- Piping and redirection (|, >, >>)
- Searching (grep, find)
- Package management (apt install)
- Why Linux is used everywhere in cloud/DevOps (not Windows)

**Environment:** Use the Codespace terminal — it's already running Linux (Ubuntu)

---

## Roadmap Ahead

| Session | Topic |
|---|---|
| 1 | Docker basics ✓ |
| 2 | GitHub Actions / CI/CD ✓ |
| 3 | Linux command line fundamentals |
| 4 | Networking basics (IP, DNS, HTTP, firewalls) |
| 5 | Azure fundamentals |
| 6 | Azure security (IAM, RBAC, Key Vault) |
| 7 | Kubernetes basics |
| 8+ | Terraform, deeper Kubernetes, cloud security specialisation |
