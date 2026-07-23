# ☁️ Azure Interview Preparation Guide
### Senior Cloud Architect & Azure Interview Coach Edition

> **Target Audience:** Azure Developer | Cloud Engineer | Full Stack Developer
> **Levels Covered:** Beginner (0–2 yrs) · Intermediate (2–5 yrs)
> **Last Updated:** June 2026

---

## 📋 Table of Contents

1. [Beginner Level — Top 25 Questions](#-beginner-level-top-25-questions)
2. [Intermediate Level — Top 25 Questions](#-intermediate-level-top-25-questions)
3. [Scenario-Based Questions](#-scenario-based-questions)
4. [Rapid Fire Questions](#-rapid-fire-questions)
5. [Mini Cheat Sheet](#-mini-cheat-sheet)

---

## 🟢 Beginner Level: Top 25 Questions (0–2 Years)

---

### Q1. What is Microsoft Azure?

**🎯 Short Answer**
Azure is Microsoft's cloud computing platform offering 200+ services including compute, storage, networking, databases, AI, and DevOps tools delivered over the internet on a pay-as-you-go model.

**💬 Detailed Answer**

Azure supports:
- **IaaS** — VMs, storage, networking (you manage OS/apps)
- **PaaS** — App Services, Azure SQL (Microsoft manages infrastructure)
- **SaaS** — Microsoft 365, Dynamics 365 (fully managed)
- **Serverless** — Azure Functions, Logic Apps

```
Cloud Service Models:
┌──────────────────────────────────────────────┐
│ SaaS  → Office 365, Dynamics, Teams          │
│ PaaS  → App Service, Azure SQL, AKS          │
│ IaaS  → Virtual Machines, VNet, Disk Storage │
│ On-Premises → You manage everything          │
└──────────────────────────────────────────────┘
```

**🌍 Real-World Example**
A startup builds their e-commerce site using Azure App Service (PaaS) for the web app, Azure SQL for the database, and Blob Storage for product images — paying only for what they use.

**❓ Follow-up Questions**
- What is the difference between IaaS, PaaS, and SaaS?
- How is Azure different from AWS or GCP?
- What is the Azure shared responsibility model?

**⚠️ Common Mistakes to Avoid**
- Don't confuse Azure with Azure Active Directory — Azure AD is one specific service
- Don't say "Azure is just VMs" — it has 200+ services

---

### Q2. What are Azure Regions and Availability Zones?

**🎯 Short Answer**
Azure Regions are geographic locations with data centers. Availability Zones (AZs) are physically separate data centers within a region, providing high availability and fault tolerance.

**💬 Detailed Answer**

**Azure Regions:** 60+ globally (East US, West Europe, Southeast Asia)

**Availability Zones:**
- Minimum 3 separate physical locations per region
- Each zone has independent power, cooling, networking
- 99.99% SLA for VMs across zones

```
Azure Region: East US
├── Availability Zone 1 (Data Center A)
├── Availability Zone 2 (Data Center B)
└── Availability Zone 3 (Data Center C)
```

**Region Pairs:** Every region is paired with another 300+ miles away for geo-redundant DR (e.g., East US ↔ West US)

**🌍 Real-World Example**
A bank deploys across 3 AZs in UK South. When Zone 1 loses power, Zones 2 and 3 continue serving customers — zero downtime.

**❓ Follow-up Questions**
- What is the difference between a Region and a Geography in Azure?
- What services support Availability Zones?
- What are Azure Region Pairs?

**⚠️ Common Mistakes to Avoid**
- Don't confuse Availability Zones with Availability Sets (Sets = within one data center)
- Not all services support AZs — always check

---

### Q3. What are Resource Groups in Azure?

**🎯 Short Answer**
A Resource Group is a logical container for related Azure resources (VMs, databases, storage). Deleting a resource group removes all resources inside it.

**💬 Detailed Answer**

- Every Azure resource MUST belong to exactly one resource group
- Resources in a group can be in different regions
- Apply tags, RBAC, and policies at resource group level

```
Resource Group: ecommerce-prod-rg
├── Virtual Machine (East US)
├── Azure SQL Database (East US)
├── Storage Account (West US)   ← can be different region
└── App Service (East US)
```

**Best Practices:** Group by lifecycle, environment (dev/staging/prod), or application

**🌍 Real-World Example**
Team creates `shop-dev-rg`, `shop-staging-rg`, `shop-prod-rg`. Deleting `shop-dev-rg` removes all dev resources in one action.

**❓ Follow-up Questions**
- Can a resource be moved between resource groups?
- What is the difference between a resource group and a subscription?

**⚠️ Common Mistakes to Avoid**
- Don't put all resources in one resource group — hard to manage lifecycle
- Don't use the default resource group — create purpose-specific ones

---

### Q4. What is the Azure Portal?

**🎯 Short Answer**
The Azure Portal (`portal.azure.com`) is a web-based GUI for creating, managing, and monitoring Azure resources. Also supports Azure Cloud Shell for CLI access.

**💬 Detailed Answer**

| Tool | Best For |
|------|----------|
| Azure Portal | Visual management, beginners |
| Azure CLI | Scripting, automation |
| Azure PowerShell | Windows admins |
| ARM Templates / Bicep | Infrastructure as Code |
| Terraform | Multi-cloud IaC |

**🌍 Real-World Example**
A junior dev uses the Portal to create a storage account, upload files, configure CORS, and view logs — all visually without CLI.

**❓ Follow-up Questions**
- What is Azure Cloud Shell?
- What is the difference between Azure Portal and Azure CLI?

**⚠️ Common Mistakes to Avoid**
- Don't rely solely on Portal for production — use IaC for repeatability
- Don't share Azure Portal credentials — use RBAC and individual accounts

---

### Q5. What are ARM Templates?

**🎯 Short Answer**
ARM (Azure Resource Manager) Templates are JSON files defining Azure infrastructure as code. Deploy resources consistently and repeatably across environments.

**💬 Detailed Answer**

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "resources": [{
    "type": "Microsoft.Storage/storageAccounts",
    "apiVersion": "2021-02-01",
    "name": "mystorageacct",
    "location": "[resourceGroup().location]",
    "sku": { "name": "Standard_LRS" },
    "kind": "StorageV2"
  }]
}
```

**Bicep (Modern Alternative — much cleaner):**
```bicep
resource storageAccount 'Microsoft.Storage/storageAccounts@2021-02-01' = {
  name: 'mystorageacct'
  location: resourceGroup().location
  sku: { name: 'Standard_LRS' }
  kind: 'StorageV2'
}
```

Key: **Idempotent** — running same template twice = same result

**🌍 Real-World Example**
DevOps team uses ARM templates to deploy identical infrastructure across dev/staging/prod. One command, consistent results.

**❓ Follow-up Questions**
- What is Bicep and how does it relate to ARM Templates?
- What is the difference between incremental and complete deployment mode?

**⚠️ Common Mistakes to Avoid**
- ARM Templates are verbose JSON — prefer Bicep for new projects
- Don't hardcode secrets — use Key Vault references

---

### Q6. How does Azure Pricing work?

**🎯 Short Answer**
Azure uses pay-as-you-go. Costs vary by resource type, region, tier, and consumption. Reserved Instances and Spot VMs offer significant discounts.

**💬 Detailed Answer**

| Model | Description | Savings |
|-------|-------------|---------|
| Pay-as-you-go | Billed by second/hour/GB | Baseline |
| Reserved Instances | 1 or 3 year commitment | Up to 72% off |
| Spot VMs | Unused capacity | Up to 90% off (can be evicted) |
| Dev/Test pricing | Non-production | ~50% off |
| Azure Hybrid Benefit | Existing Windows/SQL licenses | Up to 40% off |

**Cost tools:** Azure Pricing Calculator, Azure Cost Management, Azure Advisor

**🌍 Real-World Example**
Reporting job (8 hrs/day) switches to Spot VMs → 85% savings. Production database on 1-year Reserved Instance → 40% savings.

**⚠️ Common Mistakes to Avoid**
- Don't forget egress costs — data out of Azure is NOT free
- Don't leave unused resources running

---

### Q7. What is an Azure Virtual Machine (VM)?

**🎯 Short Answer**
Azure VM is an IaaS service providing virtualized computing resources. You choose the OS, size (CPU/RAM), and storage. Azure runs it on physical hardware.

**💬 Detailed Answer**

**VM Series:**
| Series | Purpose |
|--------|---------|
| B-series | Burstable, dev/test |
| D-series | General purpose |
| E-series | Memory optimized, databases |
| F-series | Compute optimized |
| N-series | GPU, ML/AI |

**VM Lifecycle:**
```
Create → Running → Stop (Deallocated) → Delete
         ↑                ↓
      Start ←─────────────
```

> ⚠️ "Stopped" ≠ "Deallocated" — Stopped VM STILL charges compute!

**🌍 Real-World Example**
Dev team uses Standard_B2s (2 vCPU, 4GB) for test env, running Mon–Fri 9AM–6PM with Auto-Shutdown → 70% cost reduction.

**❓ Follow-up Questions**
- What is the difference between stopped and deallocated?
- How do you connect to Linux VM (SSH) and Windows VM (RDP)?

**⚠️ Common Mistakes to Avoid**
- Don't stop without deallocating — you'll still be billed
- Don't expose port 22/3389 to internet — use Azure Bastion

---

### Q8. What are VM Scale Sets?

**🎯 Short Answer**
VM Scale Sets automatically deploy and manage a group of identical VMs that scale in/out based on demand or schedule.

**💬 Detailed Answer**

```
Scale Set (Min: 2, Max: 10)
        Load Balancer
       /      |      \
    VM-1   VM-2   VM-3  ← auto-scales to VM-4, VM-5...
```

**Scaling Policies:** Manual | Scheduled | Metric-based (CPU, memory, queue length)

**🌍 Real-World Example**
Streaming platform uses Scale Set for video encoding workers. During live events: 50 VMs. After event: scales to 5 VMs in minutes.

**❓ Follow-up Questions**
- What is the difference between VM Scale Sets and Availability Sets?
- What is flexible orchestration mode?

**⚠️ Common Mistakes to Avoid**
- Don't store local state on Scale Set VMs — use external storage
- Scale-in removes VMs — local session data is lost

---

### Q9. What is Azure App Service?

**🎯 Short Answer**
Fully managed PaaS for hosting web apps, REST APIs, and mobile backends in any language (Python, .NET, Node.js, Java, PHP) without managing infrastructure.

**💬 Detailed Answer**

**App Service Plans:**
| Tier | Use Case |
|------|----------|
| Free/Shared | Dev/test |
| Basic | Custom domains, manual scale |
| Standard | Auto-scale, deployment slots |
| Premium | VNet integration |
| Isolated | Dedicated hardware |

**Deployment Slots:**
```
Production Slot (app.azurewebsites.net)
     ↑ Swap (zero-downtime)
Staging Slot  → deploy + test → swap to production
```

**🌍 Real-World Example**
FastAPI backend on App Service. Push to staging → test → slot swap to production in 30 seconds. Zero-downtime deployment.

**⚠️ Common Mistakes to Avoid**
- Don't use Free tier in production — no SLA, shared compute
- App Service Plan price ≠ App price — the Plan determines cost

---

### Q10. What are Azure Functions?

**🎯 Short Answer**
Serverless compute: write functions triggered by events (HTTP, timers, queues, blobs) and pay only per execution. No server management.

**💬 Detailed Answer**

```python
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name', 'World')
    return func.HttpResponse(f"Hello, {name}!")
```

**Hosting Plans:**
| Plan | Billing | Cold Start | Max Duration |
|------|---------|------------|--------------|
| Consumption | Per execution | Yes | 10 min |
| Premium | Per vCPU/hr | No (pre-warmed) | Unlimited |
| Dedicated | Per hour | No | Unlimited |

**🌍 Real-World Example**
E-commerce site resizes product images on Blob Storage upload. Function triggers automatically — handles thousands/minute at near-zero cost.

**⚠️ Common Mistakes to Avoid**
- Consumption plan: 10-minute max execution — use Premium for long tasks
- Functions are stateless — no session storage

---

### Q11. What is Azure Blob Storage?

**🎯 Short Answer**
Object storage for unstructured data — files, images, videos, backups. Data stored as blobs in containers within a storage account.

**💬 Detailed Answer**

**Access Tiers:**
| Tier | Use Case |
|------|----------|
| Hot | Frequently accessed |
| Cool | Infrequently accessed (30+ days) |
| Cold | Rarely accessed (90+ days) |
| Archive | Long-term, slow retrieval (hours) |

**Hierarchy:**
```
Storage Account
└── Container
    ├── file1.jpg (Block Blob)
    ├── app.log  (Append Blob)
    └── vm.vhd   (Page Blob)
```

**🌍 Real-World Example**
Streaming service: Hot tier for new content, Cool for older titles, Archive for expired. Static assets served from Blob + CDN.

**⚠️ Common Mistakes to Avoid**
- Don't store secrets in Blob Storage — use Key Vault
- Archive blobs take hours to rehydrate before they can be read

---

### Q12. What is a Virtual Network (VNet)?

**🎯 Short Answer**
Private isolated network in Azure where resources communicate securely. Similar to a traditional on-premises network but in the cloud.

**💬 Detailed Answer**

```
VNet: 10.0.0.0/16
├── Subnet: WebTier    10.0.1.0/24  → Web servers
├── Subnet: AppTier    10.0.2.0/24  → API servers
├── Subnet: DataTier   10.0.3.0/24  → Databases
└── GatewaySubnet      10.0.4.0/27  → VPN/ExpressRoute
```

**Key Features:** VNet Peering | Service Endpoints | Private Endpoints | VPN Gateway

**🌍 Real-World Example**
3-tier app: web servers in public subnet, API servers in private subnet, DB in data subnet with no internet access. NSGs control all traffic flow.

**⚠️ Common Mistakes to Avoid**
- Overlapping address spaces = VNets can't peer
- Don't put databases in public subnets

---

### Q13. What is an NSG (Network Security Group)?

**🎯 Short Answer**
Firewall controlling inbound/outbound traffic using rules based on IP, port, and protocol. Applied at subnet or NIC level.

**💬 Detailed Answer**

**Rule Properties:** Priority (100–4096) | Source | Destination | Port | Protocol | Allow/Deny

**Default Rules (undeletable):**
```
Inbound:
  65000: AllowVNetInBound
  65500: DenyAllInBound

Outbound:
  65000: AllowVNetOutBound
  65001: AllowInternetOutBound
  65500: DenyAllOutBound
```

**🌍 Real-World Example**
Database subnet NSG: only allow port 1433 from app subnet IP range. All other traffic denied including internet.

**⚠️ Common Mistakes to Avoid**
- Lower priority number = higher precedence (100 beats 200)
- NSG rules are stateful — inbound allow = return traffic auto-allowed

---

### Q14. What is Azure SQL Database?

**🎯 Short Answer**
Fully managed relational PaaS database based on SQL Server. Microsoft handles backups, patching, HA, and scaling.

**💬 Detailed Answer**

**Deployment Options:**
| Option | Use Case |
|--------|----------|
| Single Database | Isolated DB with own resources |
| Elastic Pool | Multiple DBs sharing resources |
| Managed Instance | Full SQL Server + VNet integration |

**Tiers:** Basic → Standard → Premium → Hyperscale (100 TB) → Serverless (auto-pause)

**Built-in:** Automatic backups | Point-in-time restore | Geo-replication | Auto-tuning

**🌍 Real-World Example**
HR SaaS with 50 client databases uses Elastic Pool — shares DTU pool instead of 50 individual purchases → 60% cost savings.

**⚠️ Common Mistakes to Avoid**
- SQL Database (PaaS) ≠ SQL Server on VM (IaaS)
- DTU = blended CPU+memory+IO measure — consider vCore for predictable workloads

---

### Q15. What is Azure Active Directory (Azure AD / Entra ID)?

**🎯 Short Answer**
Microsoft's cloud-based identity and access management. Handles authentication (who you are) and authorization (what you can do) for Azure and Microsoft 365.

**💬 Detailed Answer**

**Key Concepts:**
- **Tenant** — dedicated Azure AD instance for your org
- **Service Principal** — identity for apps (robot account)
- **Managed Identity** — service principal managed by Azure

**Azure AD vs On-Prem AD:**
| Feature | Azure AD | On-Prem AD |
|---------|----------|-----------|
| Protocol | OAuth2, OIDC, SAML | Kerberos, LDAP |
| MFA | Built-in | Requires ADFS |

**🌍 Real-World Example**
Company uses Azure AD SSO. One login → access Azure Portal, Microsoft 365, Salesforce, internal apps.

**⚠️ Common Mistakes to Avoid**
- Azure AD ≠ Active Directory Domain Services — different protocols
- Don't use single Global Admin — distribute with RBAC

---

### Q16. What is RBAC in Azure?

**🎯 Short Answer**
Role-Based Access Control — controls who has access to Azure resources, what they can do, and at what scope.

**💬 Detailed Answer**

**Assignment = Principal + Role + Scope**

```
Role Assignment:
  Who:   Alice (user)
  Role:  Contributor
  Scope: /resourceGroups/ecommerce-prod-rg
→ Alice can create/modify/delete resources in that RG
  but cannot manage access (Owner only)
```

**Built-in Roles:**
| Role | Capabilities |
|------|-------------|
| Owner | Full access + manage access |
| Contributor | Full access, no access management |
| Reader | View only |

**🌍 Real-World Example**
5 devs get Contributor on `dev-rg`. DevOps lead gets Owner on `prod-rg`. Monitoring tool gets Reader on all RGs.

**⚠️ Common Mistakes to Avoid**
- RBAC = access control. Azure Policy = governance. They're complementary, not alternatives
- Always least-privilege — don't give Owner when Reader works

---

### Q17. What is Azure Key Vault?

**🎯 Short Answer**
Secure cloud service for storing secrets (passwords), keys (encryption), and certificates. Apps retrieve secrets at runtime — no hardcoding.

**💬 Detailed Answer**

```python
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
client = SecretClient("https://my-keyvault.vault.azure.net/", credential)

db_password = client.get_secret("database-password").value
# No password in code! ✅
```

**🌍 Real-World Example**
CI/CD pipeline stores DB passwords, API keys, SSL certs in Key Vault. App Service retrieves via Managed Identity — nothing in env vars or code.

**⚠️ Common Mistakes to Avoid**
- Never hardcode secrets — always Key Vault
- Enable soft-delete + purge protection in production

---

### Q18. What is Cosmos DB?

**🎯 Short Answer**
Globally distributed multi-model NoSQL database. Single-digit millisecond latency, 99.999% SLA, supports JSON docs, key-value, graph, and column-family.

**💬 Detailed Answer**

**APIs:** NoSQL | MongoDB | Cassandra | Gremlin | Table

**Consistency Levels:**
```
Strong ←→ Bounded Staleness ←→ Session ←→ Consistent Prefix ←→ Eventual
(most consistent)                              (most available/performant)
```

**Key:** Throughput measured in Request Units (RUs). Partition key selection is critical.

**🌍 Real-World Example**
Gaming leaderboard: Session consistency, 5-region distribution. Asia players write to Asia, EU players to EU — both get sub-10ms latency.

**⚠️ Common Mistakes to Avoid**
- Strong consistency globally = poor performance — use Session for most cases
- Bad partition keys cause hot partitions and throttling

---

### Q19. What is Azure Load Balancer?

**🎯 Short Answer**
Distributes incoming TCP/UDP traffic across multiple backend VMs or services to prevent overload and ensure availability.

**💬 Detailed Answer**

**Azure Load Balancing Options:**
| Service | Layer | Use Case |
|---------|-------|----------|
| Load Balancer | L4 (TCP/UDP) | VMs, Scale Sets |
| Application Gateway | L7 (HTTP) | Web apps, URL routing, WAF |
| Traffic Manager | DNS | Multi-region routing |
| Azure Front Door | Global L7 | CDN + WAF + global routing |

> Always use **Standard SKU** in production — Basic has no SLA.

**🌍 Real-World Example**
API serving 10K req/min distributed across 5 VMs. VM-3 fails health probe → Load Balancer stops sending traffic to it in 30 seconds.

**⚠️ Common Mistakes to Avoid**
- Basic LB = no SLA — use Standard in production
- Don't confuse L4 LB with L7 Application Gateway

---

### Q20. What is Azure DevOps?

**🎯 Short Answer**
Developer services for planning, developing, testing, and deploying software. Includes Repos, Pipelines, Boards, Artifacts, and Test Plans.

**💬 Detailed Answer**

```yaml
# Azure Pipelines YAML
trigger:
  - main
pool:
  vmImage: 'ubuntu-latest'
stages:
- stage: Build
  jobs:
  - job: BuildApp
    steps:
    - script: pip install -r requirements.txt
    - script: pytest tests/
- stage: Deploy
  dependsOn: Build
  jobs:
  - job: DeployToAzure
    steps:
    - task: AzureWebApp@1
      inputs:
        azureSubscription: 'my-service-connection'
        appName: 'my-fastapi-app'
```

**🌍 Real-World Example**
Team commits → Pipelines builds, tests, creates Docker image, pushes to ACR, deploys to AKS — all in under 10 minutes.

**⚠️ Common Mistakes to Avoid**
- Mark secrets as secret in pipeline variables
- Use YAML pipelines (not Classic) — version-controlled and auditable

---

### Q21. What is Managed Identity?

**🎯 Short Answer**
Provides Azure services with an auto-managed identity in Azure AD. Apps authenticate to other Azure services without storing credentials anywhere.

**💬 Detailed Answer**

```
App Service (with Managed Identity)
    │
    ↓ "Who are you?" → Azure AD issues short-lived token
    ↓
Key Vault / Storage / SQL → checks RBAC → Returns data
```

**Types:**
- **System-assigned** — tied to one resource, deleted with it
- **User-assigned** — independent, shareable across resources

```python
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
# Automatically uses Managed Identity in Azure, CLI locally ✅
```

**🌍 Real-World Example**
Azure Function uses Managed Identity → reads Key Vault secrets, writes to Blob, queries SQL. Zero credentials stored anywhere.

**⚠️ Common Mistakes to Avoid**
- Never store passwords in code or env vars — use Managed Identity
- User-assigned identity must be manually cleaned up

---

### Q22. What is Azure Monitor?

**🎯 Short Answer**
Centralized monitoring platform collecting metrics, logs, and traces from all Azure resources. Enables alerting, dashboards, and diagnostics.

**💬 Detailed Answer**

```
Azure Resources → Azure Monitor
                  ├── Metrics Explorer (real-time charts)
                  ├── Log Analytics (KQL query logs)
                  ├── Alerts (email/SMS/webhook)
                  ├── Application Insights (APM)
                  └── Workbooks (interactive reports)
```

**KQL Example:**
```kql
requests
| where timestamp > ago(1h)
| where success == false
| summarize count() by resultCode
| order by count_ desc
```

**🌍 Real-World Example**
Alert rule: "HTTP 5xx errors > 10/minute for 5 min → email on-call engineer + PagerDuty." Zero manual monitoring.

**⚠️ Common Mistakes to Avoid**
- Metrics alone aren't enough — logs give context
- Set up alerts BEFORE going to production

---

### Q23. What is Application Insights?

**🎯 Short Answer**
APM service within Azure Monitor. Tracks request rates, response times, failures, dependency calls, exceptions, and user behavior in real time.

**💬 Detailed Answer**

**Tracks:** Request rate/latency | Dependency calls (DB, APIs) | Exceptions | Custom events | Live metrics

```python
from applicationinsights import TelemetryClient
tc = TelemetryClient('INSTRUMENTATION_KEY')

tc.track_event('OrderPlaced', {'orderId': '12345', 'amount': 99.99})
try:
    process_order()
except Exception:
    tc.track_exception()
tc.flush()
```

**Application Map:** Visual diagram of app components, dependency calls, failure rates, response times.

**🌍 Real-World Example**
App Insights detects 15% of `/api/checkout` calls taking >5 seconds. Traces reveal slow SQL query. Add index → 200ms. Found without raw log digging.

**⚠️ Common Mistakes to Avoid**
- Don't ignore it after setup — review Application Map and Failure reports regularly
- Enable adaptive sampling for high-traffic apps to control ingestion costs

---

### Q24. What is AKS (Azure Kubernetes Service)?

**🎯 Short Answer**
Managed Kubernetes service — Azure handles the control plane (free). You manage and pay for worker nodes only.

**💬 Detailed Answer**

```
Azure AKS Cluster
├── Control Plane (managed by Azure, free)
│   ├── API Server
│   ├── etcd
│   └── Scheduler / Controller Manager
└── Node Pools (you pay for these VMs)
    ├── System Pool (kube-system pods)
    └── User Pool (your app pods)
```

**Features:** Cluster Autoscaler | HPA | Azure AD auth | Key Vault integration | ACR integration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-api
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: my-api
        image: myacr.azurecr.io/my-api:v1
        ports:
        - containerPort: 8080
```

**🌍 Real-World Example**
15 microservices on AKS. Business hours: 20 nodes. Overnight: 5 nodes. 75% compute savings.

**⚠️ Common Mistakes to Avoid**
- AKS control plane is free but nodes are not — right-size pools
- Always run 2+ nodes in production

---

### Q25. What is Microsoft Defender for Cloud?

**🎯 Short Answer**
Unified cloud security management: security posture assessment (CSPM), threat protection (CWP), and compliance monitoring across Azure, on-premises, and multi-cloud.

**💬 Detailed Answer**

**Secure Score:**
```
Secure Score: 72%
├── Enable MFA for all users [High]
├── Enable disk encryption on VMs [Medium]
└── Remove unused admin credentials [High]
Fix recommendations → score improves
```

**Detects:** Suspicious VM processes | Brute force RDP/SSH | SQL injection | Unusual data exfiltration

**🌍 Real-World Example**
Defender alerts: VM communicating with known malicious C2 server. Alert fires in minutes → team isolates VM → data exfiltration prevented.

**⚠️ Common Mistakes to Avoid**
- Don't ignore Secure Score — each recommendation = real risk
- Enable paid Defender plans (not just free CSPM) for production

---

## 🔵 Intermediate Level: Top 25 Questions (2–5 Years)

---

### Q26. Explain Azure VNet Peering vs VPN Gateway

**🎯 Short Answer**
VNet Peering: private, low-latency, no gateway, Microsoft backbone. VPN Gateway: encrypted tunnel over public internet, supports on-premises connectivity.

**💬 Detailed Answer**

| Feature | VNet Peering | VPN Gateway |
|---------|-------------|-------------|
| Latency | <1ms (same region) | 5–30ms |
| Bandwidth | No limits | Up to 10 Gbps |
| Encryption | No (private backbone) | Yes (IPSec/IKE) |
| On-premises | No | Yes (Site-to-Site) |
| Cost | Per GB | Per gateway hr + per GB |
| Setup | Minutes | Hours |
| Transitive | No | With hub-spoke |

```
Hub-Spoke with VNet Peering:
        Hub VNet (Firewall, Bastion, DNS)
           │           │           │
       Spoke-1      Spoke-2      Spoke-3

⚠️ Peering NOT transitive:
   Spoke-1 cannot reach Spoke-2 directly
   Must route through Hub Firewall
```

**🌍 Real-World Example**
Hub VNet with Azure Firewall + Bastion peered with 10 spoke VNets. All spoke-to-spoke traffic inspected by hub firewall.

**⚠️ Common Mistakes to Avoid**
- Peering is NOT transitive — plan routing carefully
- Address spaces must not overlap before peering

---

### Q27. CI/CD for a Microservices App on Azure

**🎯 Short Answer**
Each microservice has its own pipeline: build → test → Docker image → ACR → AKS deployment. Multiple pipelines in parallel; environments use approvals and gates.

**💬 Detailed Answer**

```
Feature branch push
  ↓
[CI Pipeline — on PR]
  ├── Unit tests
  ├── SAST security scan
  ├── Docker build
  └── Push to ACR (tagged with PR number)

Merge to main
  ↓
[CD Pipeline]
  ├── Stage 1: Dev → integration tests
  ├── Stage 2: Staging (requires approval) → smoke + perf tests
  └── Stage 3: Production (2 approvals + business hours gate)
      └── Rolling deploy → Monitor App Insights 15 min
          └── Auto-rollback if error rate > 1%
```

**🌍 Real-World Example**
Team of 8 manages 12 microservices. Shared pipeline template library → 80% code reuse, low maintenance overhead.

**⚠️ Common Mistakes to Avoid**
- Don't deploy directly to production without staging validation
- Use workload identity federation for service connections

---

### Q28. Azure Storage Account Types

**🎯 Short Answer**
Different account types (General Purpose v2, Block Blob Premium, Azure Files Premium) offer different performance tiers and services.

**💬 Detailed Answer**

| Type | Supported Services | Use Case |
|------|-------------------|----------|
| GPv2 | Blobs, Files, Queues, Tables | Default choice |
| Premium Block Blob | Block + Append Blobs | High transactions, IoT |
| Premium Files | File shares | SMB/NFS |

**Redundancy (cheapest → most resilient):**
```
LRS  → 3 copies, one data center
ZRS  → 3 copies, 3 AZs
GRS  → LRS + async copy to paired region
RA-GRS → GRS + read from secondary
GZRS → ZRS + async to paired region
RA-GZRS → GZRS + read from secondary (best)
```

**🌍 Real-World Example**
Media company: GPv2 + RA-GRS for video (global reads + DR), Premium Block Blob for IoT ingestion, Azure Files + ZRS for shared config.

**⚠️ Common Mistakes to Avoid**
- Don't use LRS for data that cannot be lost — use ZRS minimum
- Don't expose storage to internet — use private endpoints or firewall rules

---

### Q29. Azure Application Gateway vs Load Balancer

**🎯 Short Answer**
Load Balancer = Layer 4 (TCP/UDP), understands only IP/port. Application Gateway = Layer 7 (HTTP/HTTPS), understands URLs, headers, cookies — enables WAF, URL routing, SSL termination.

**💬 Detailed Answer**

```
Azure Load Balancer (Layer 4):
Client → LB:80 → VM1/VM2/VM3 (based on IP/port)

Application Gateway (Layer 7):
Client → AppGW:443
  ├── /api/*     → Backend Pool 1 (API servers)
  ├── /images/*  → Backend Pool 2 (Image servers)
  └── /admin/*   → Backend Pool 3 (Admin app)
  WAF inspects all for OWASP threats
```

**Features of App Gateway:** SSL termination | URL routing | Host routing | WAF | Cookie affinity | Autoscaling (v2)

**🌍 Real-World Example**
E-commerce: `/api/products` → Node.js, `/api/payments` → PCI servers, `/` → React frontend. WAF blocks SQL injection and XSS.

**⚠️ Common Mistakes to Avoid**
- App Gateway v1 is deprecated — use v2
- WAF in Detection mode only logs — switch to Prevention in production

---

### Q30. Azure Database Scaling Strategies

**🎯 Short Answer**
Vertical scaling (change tier/size) for quick wins. Horizontal scaling (read replicas, sharding, elastic pools) for long-term growth.

**💬 Detailed Answer**

**1. Vertical Scaling:** Change SQL tier or vCores | Change Cosmos DB RUs

**2. Read Replicas:**
```
Primary DB (read/write)
  ├── Replica 1 (East US) → reporting
  ├── Replica 2 (West US) → analytics
  └── Replica 3 (East Asia) → regional users
```

**3. Elastic Pools:**
```
Elastic Pool: 200 eDTUs shared
  DB1 (active: 150) + DB2 (idle: 10) = efficient
  vs 200 DTUs × 50 DBs = very expensive
```

**4. Cosmos DB Sharding:** Auto-shards on partition key — key selection is critical

**5. Azure SQL Hyperscale:** 100 TB, 5 readable replicas, instant PITR

**🌍 Real-World Example**
SaaS: Hyperscale for main transactional DB, 2 read replicas for analytics, 100 tenant DBs in 3 Elastic Pools.

**⚠️ Common Mistakes to Avoid**
- Scaling up is temporary — design for horizontal scale
- Elastic Pools: one DB maxing pool hurts others

---

### Q31. Managed Identity Implementation — Step by Step

**🎯 Short Answer**
Enable MI on resource → grant RBAC role on target service → use DefaultAzureCredential in code → Azure handles token management.

**💬 Detailed Answer**

```bash
# 1. Enable System-assigned MI on App Service
az webapp identity assign --name myapp --resource-group myapp-rg
# Returns: { "principalId": "abc-123-..." }

# 2. Grant RBAC (preferred over Access Policies)
az role assignment create \
  --role "Key Vault Secrets User" \
  --assignee abc-123-... \
  --scope /subscriptions/.../keyvaults/my-keyvault
```

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()
# Uses MI in Azure, CLI login locally, VS Code login in dev — same code!

kv_client = SecretClient("https://my-kv.vault.azure.net/", credential)
secret = kv_client.get_secret("db-password").value
```

**🌍 Real-World Example**
Azure Function: MI reads Key Vault config, queries Azure SQL (token-based auth), writes to Blob. Zero credentials anywhere. Auditable in Azure AD sign-in logs.

**⚠️ Common Mistakes to Avoid**
- Don't use MI for user-facing logins — it's service-to-service auth
- System-assigned deleted with resource — use user-assigned for shared scenarios

---

### Q32. Azure Service Bus vs Event Hub vs Storage Queue

**🎯 Short Answer**
Storage Queue: simple FIFO. Service Bus: enterprise messaging with ordering, dead-letter, sessions. Event Hub: high-throughput event streaming (millions/sec).

**💬 Detailed Answer**

| Feature | Storage Queue | Service Bus | Event Hub |
|---------|--------------|-------------|-----------|
| Max message | 64 KB | 256 KB–100 MB | 1 MB |
| Retention | 7 days | 14 days | 90 days |
| Ordering | Best effort | FIFO (sessions) | Partition-level |
| Dead letter | No | Yes | No |
| Throughput | High | Medium | Very High |
| Use case | Simple tasks | Business workflows | Streaming/telemetry |

```
When to use:
Storage Queue → Simple background jobs
Service Bus  → Payment/fulfillment workflows (ordered, exactly-once)
Event Hub    → IoT telemetry, clickstream, log aggregation (500K+ events/sec)
```

**🌍 Real-World Example**
IoT platform: Event Hub (1M events/sec from 50K devices), Service Bus (ordered payment workflow), Storage Queue (image resize tasks).

**⚠️ Common Mistakes to Avoid**
- Event Hub ≠ Service Bus replacement — different purposes
- Storage Queue: no ordering/dead-letter — don't use for financial workflows

---

### Q33. AKS Autoscaling — HPA, Cluster Autoscaler, KEDA

**🎯 Short Answer**
HPA scales pod replicas based on CPU/memory. Cluster Autoscaler adds/removes nodes. KEDA scales pods based on event sources (queues, topics, custom metrics).

**💬 Detailed Answer**

**HPA:**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
spec:
  scaleTargetRef:
    name: my-api
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

**KEDA (scale from Service Bus queue):**
```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
spec:
  scaleTargetRef:
    name: order-processor
  triggers:
  - type: azure-servicebus
    metadata:
      queueName: orders
      messageCount: "5"   # 1 pod per 5 messages
```

**Scaling Flow:**
```
500 messages in queue
  → KEDA: 500/5 = 100 pods needed
  → HPA: creates 100 pods
  → Cluster Autoscaler: adds 5 nodes
  → Messages processed
  → KEDA: scales to 0 pods
  → Autoscaler: removes empty nodes after 10 min
```

**⚠️ Common Mistakes to Avoid**
- Don't set minReplicas=0 for always-available services
- Cluster Autoscaler has 10-min scale-down delay — plan for bursts

---

### Q34. Azure ExpressRoute

**🎯 Short Answer**
Dedicated private circuit from on-premises to Azure, bypassing the internet. Up to 100 Gbps, consistent latency, higher security — ideal for regulated industries.

**💬 Detailed Answer**

| Feature | ExpressRoute | VPN Gateway |
|---------|-------------|-------------|
| Path | Private circuit (ISP) | Encrypted internet |
| Bandwidth | 50 Mbps – 100 Gbps | Up to 10 Gbps |
| Latency | Consistent | Variable |
| SLA | 99.95% | 99.9% |
| Setup | Weeks | Hours |
| Cost | High | Lower |

**Peering Types:**
- **Azure Private Peering** — connect to VNets
- **Microsoft Peering** — connect to Microsoft 365, Dynamics

**🌍 Real-World Example**
Financial firm transfers 10TB trading data daily. ExpressRoute 10 Gbps: 2 hours. VPN: 22+ hours with variable latency.

**⚠️ Common Mistakes to Avoid**
- ExpressRoute doesn't encrypt by default — encrypt at application layer
- Always provision two circuits for redundancy

---

### Q35. Designing for High Availability in Azure

**🎯 Short Answer**
Eliminate single points of failure: deploy across Availability Zones, use Standard Load Balancer, zone-redundant databases, geo-replicated storage, and Traffic Manager for multi-region failover.

**💬 Detailed Answer**

**HA Checklist:**
```
✅ VMs across 3 Availability Zones
✅ Standard Load Balancer / Application Gateway
✅ Zone-redundant Azure SQL + read replicas
✅ ZRS or GRS storage
✅ Redis Cache with replica
✅ Traffic Manager for DNS failover
✅ Automated alerts on availability metrics
✅ Tested restore runbook
```

**Composite SLA Calculation:**
```
App Service: 99.95%
Azure SQL:   99.99%
Redis:       99.9%

Composite = 99.95% × 99.99% × 99.9% = 99.84%
≈ 14 hours downtime/year
```

**Multi-Region Active-Passive:**
```
Primary (East US)               Secondary (West US)
  App Gateway                     App Gateway
  VM Scale Set (active)   →       VM Scale Set (standby)
  Azure SQL (primary)   →GRS→    Azure SQL (readable secondary)
         ↑                              ↑
         └─── Traffic Manager ──────────┘
              DNS failover if primary unhealthy
```

**⚠️ Common Mistakes to Avoid**
- Availability Sets ≠ Availability Zones (Sets = same data center)
- Composite SLAs are always lower than individual service SLAs

---

### Q36. Azure Private Endpoint vs Service Endpoint

**🎯 Short Answer**
Service Endpoint: extends VNet identity to Azure service (still public IP). Private Endpoint: creates private IP in your VNet — service becomes fully private, public access can be disabled.

**💬 Detailed Answer**

```
Service Endpoint:
VNet → Azure backbone → Azure SQL PUBLIC endpoint
(VNet identity used, but public endpoint still exists)

Private Endpoint:
VNet → Private IP (10.0.1.10) → Azure SQL
(SQL gets a NIC in YOUR subnet — fully private)
```

| Feature | Service Endpoint | Private Endpoint |
|---------|-----------------|-----------------|
| Private IP in VNet | No | Yes |
| Public endpoint disabled | No | Yes |
| DNS changes | No | Yes (private DNS zone) |
| Cost | Free | ~$7/month |
| Security | Better | Best |

**⚠️ Common Mistakes to Avoid**
- Forgetting to create Private DNS Zone — endpoint won't resolve correctly
- Service Endpoint doesn't disable public endpoint — use Private Endpoint for truly private access

---

### Q37. Zero Trust Security in Azure

**🎯 Short Answer**
"Never trust, always verify" — regardless of network location. Implement with Conditional Access, Managed Identity, Private Endpoints, JIT VM access, RBAC least privilege, and network micro-segmentation.

**💬 Detailed Answer**

```
Identity Layer:
  ├── Azure AD + MFA enforced
  ├── Conditional Access (block risky sign-ins)
  ├── PIM (JIT admin access — time-limited)
  └── Managed Identity (service-to-service)

Network Layer:
  ├── Private Endpoints
  ├── NSG micro-segmentation
  ├── Azure Firewall (east-west inspection)
  └── JIT VM Access (open RDP only when needed)

Data Layer:
  ├── Encryption at rest + in transit (TLS 1.2+)
  └── Key Vault key management

Application Layer:
  ├── App Gateway WAF
  └── API Management with OAuth2
```

**PIM (Privileged Identity Management):**
```
Instead of: User always has Owner role (risky!)
Use PIM:
  1. User requests "Owner" for 2 hours
  2. Manager approves via email
  3. Auto-revoked after 2 hours
  4. Full audit trail
```

**🌍 Real-World Example**
No developer has permanent production access. JIT via PIM (approved in 2 min), expires in 4 hours. Access only via Azure Bastion — no direct RDP/SSH.

**⚠️ Common Mistakes to Avoid**
- Zero Trust ≠ "internal network is safe"
- Don't give permanent privileged access — always use PIM

---

### Q38. Azure Cost Optimization Strategies

**🎯 Short Answer**
Right-size resources, use Reserved Instances and Spot VMs, autoscale, storage lifecycle policies, Azure Hybrid Benefit, and review Azure Advisor recommendations regularly.

**💬 Detailed Answer**

**1. Right-Sizing** (biggest savings):
```bash
az advisor recommendation list --category Cost
# VM using 5% CPU → downsize from D4s to B2s → ~70% savings
```

**2. Reserved Instances:**
```
Pay-as-you-go: Standard_D4s = $0.19/hr = $1,664/yr
1-Year RI:                     $0.12/hr = $1,051/yr (37% off)
3-Year RI:                     $0.08/hr = $701/yr (58% off)
```

**3. Spot VMs:** Up to 90% off (can be evicted) — batch jobs, CI/CD agents

**4. Storage Lifecycle Policy:**
```json
{
  "rules": [{
    "actions": {
      "baseBlob": {
        "tierToCool": { "daysAfterLastModifiedGreaterThan": 30 },
        "tierToArchive": { "daysAfterLastModifiedGreaterThan": 90 },
        "delete": { "daysAfterLastModifiedGreaterThan": 365 }
      }
    }
  }]
}
```

**5. Azure Hybrid Benefit:** Existing Windows Server licenses → 40% VM savings

**🌍 Real-World Example**
Company reduces spend from $50K to $22K/month: right-sizing (-$8K), Reserved Instances (-$6K), lifecycle policies (-$4K), zombie cleanup (-$3K), Spot for CI/CD (-$4K), dev VM shutdown (-$3K).

**⚠️ Common Mistakes to Avoid**
- Spot VMs can be evicted — never use for stateful production workloads
- Don't buy RIs without 30+ days usage data

---

### Q39. Disaster Recovery (DR) in Azure

**🎯 Short Answer**
DR is defined by RTO (recovery time) and RPO (data loss). Implement with Azure Site Recovery for VMs, geo-replication for databases, RA-GRS for storage, Traffic Manager for DNS failover, and tested runbooks.

**💬 Detailed Answer**

**DR Tiers:**
| Tier | Strategy | RTO | RPO | Cost |
|------|----------|-----|-----|------|
| 1 | Backup & Restore | Hours–Days | 24 hours | Low |
| 2 | Pilot Light | 1–2 hours | Minutes | Medium |
| 3 | Warm Standby | Minutes | Seconds | High |
| 4 | Active/Active | Near-zero | Near-zero | Highest |

**Azure SQL Auto-Failover Groups:**
```
Primary: East US (read/write)
Secondary: West US (async replica)
→ Failover time: < 30 seconds
→ Connection string stays the same (CNAME auto-updates)
```

**🌍 Real-World Example**
Retail company DR test:
1. Traffic Manager detects primary failure
2. SQL auto-failover group triggers (30 sec)
3. Traffic Manager DNS updates (60 sec TTL)
4. Site Recovery VMs ready (pilot light pre-warmed)
5. Total RTO: < 5 minutes ✅

**⚠️ Common Mistakes to Avoid**
- Never assume DR works — test quarterly
- Backup ≠ DR — restore from backup can take hours to days

---

### Q40. Securing an AKS Cluster

**🎯 Short Answer**
Secure AKS with Azure AD integration, RBAC, private cluster mode, image scanning, Workload Identity (no stored creds), network policies, and Defender for Containers.

**💬 Detailed Answer**

```
Layer 1: Cluster Access
  ├── Azure AD integration
  ├── Kubernetes RBAC (ClusterRoles/RoleBindings)
  └── Private cluster (API server not internet-facing)

Layer 2: Node Security
  ├── Auto OS patching
  └── CIS-hardened images

Layer 3: Container Security
  ├── Image scanning (Defender / Trivy)
  ├── Non-root containers
  └── Read-only root filesystem

Layer 4: Network Security
  ├── Network Policies (deny by default)
  └── Private Endpoints for Azure services

Layer 5: Secrets
  └── Key Vault CSI Driver + Workload Identity
```

**Network Policy (deny-by-default):**
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
spec:
  podSelector:
    matchLabels:
      app: backend
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - port: 8080
```

**🌍 Real-World Example**
Fintech AKS: private API server, Azure AD RBAC, all images scanned before deploy, network policies blocking pod-to-pod by default, Key Vault CSI for secrets. Passed PCI-DSS audit first attempt.

**⚠️ Common Mistakes to Avoid**
- Don't run containers as root — set `runAsNonRoot: true`
- Don't use Kubernetes Secrets without encryption at rest — use Key Vault CSI Driver

---

### Q41–Q50: Quick Reference

**Q41. Azure Traffic Manager** — DNS-based global routing. Methods: Priority (active-passive), Weighted (A/B), Performance (nearest), Geographic (data residency). Failover time = DNS TTL.

**Q42. Azure Cache for Redis** — Managed Redis for caching, sessions, pub/sub. Tiers: Basic → Standard (replica) → Premium (clustering + VNet). Response time: 800ms DB → 2ms Redis hit.

**Q43. Azure API Management (APIM)** — Publish, secure, document, and monitor APIs. Policies for rate limiting, JWT auth, CORS transformation. Products + subscription keys for developer access.

**Q44. Azure Logic Apps** — Low-code workflow automation with 400+ connectors. Trigger on email, HTTP, schedule → transform → write to SQL/Blob → notify Teams. Zero code needed.

**Q45. Azure Bicep** — DSL that simplifies ARM Templates. 50–70% less code, native VS Code intellisense, compiles to ARM JSON, modular (reusable modules). Preferred over raw ARM for new projects.

**Q46. Azure Policy vs RBAC** — RBAC: WHO can do what. Policy: WHAT can be configured (governance). Policies: "all resources must have CostCenter tag", "only allow East US region", "VMs must use managed disks".

**Q47. Azure Container Registry (ACR)** — Private Docker registry integrated with AKS, App Service, Azure Pipelines. SKUs: Basic/Standard/Premium (geo-replication). Image scanning with Defender for Containers. Use AcrPull role with Managed Identity.

**Q48. Azure Data Factory (ADF)** — ETL/ELT pipeline service. 90+ connectors. Activities: Copy, Data Flow, Execute Pipeline. Integration Runtimes for cloud, on-premises, SSIS. Alternative: Synapse Analytics (integrated ADF + SQL + Spark).

**Q49. Defender for Containers** — Scans ACR images for CVEs on push. Runtime threat detection in AKS (crypto mining, privilege escalation). Kubernetes hardening recommendations (CIS benchmark). Integrates with Microsoft Sentinel.

**Q50. Log Analytics Workspace** — Central log store for Azure Monitor. Query with KQL. Default 30-day retention (configurable to 2 years). Sources: Azure resources, agents (AMA), App Insights.

---

## 🟠 Scenario-Based Questions (10)

---

### Scenario 1: Your web app is slow — troubleshoot it

```
Step 1: Application Insights
  → Live Metrics: is app under load?
  → Failures: exceptions or failed requests?
  → Performance: which endpoints are slowest?

Step 2: Identify bottleneck
  → Slow DB query → check App Insights dependency traces
  → High CPU → Azure Monitor metrics
  → Cache miss → Redis hit rate

Step 3: Check dependencies
  → Redis cache hit rate low?
  → External API timeouts?
  → Service Bus message backlog?

Step 4: Scale
  → Horizontal: more App Service instances
  → Vertical: scale up tier
  → DB: add read replicas or increase DTUs

Step 5: Long-term
  → Add Redis caching
  → Optimize slow queries
  → Async processing for heavy operations
```

---

### Scenario 2: Design a highly available 3-tier web app

```
Architecture:

Internet
   ↓
Azure Front Door (global WAF + CDN + routing)
   ↓
Application Gateway + WAF (regional, SSL termination)
   ↓
App Service (Standard, 3 instances, zone-redundant)
   ↓
Azure Cache for Redis (Standard, replicated)
   ↓
Azure SQL (Business Critical, zone-redundant)
   + Active Geo-Replication to West US

Supporting:
- Azure AD: authentication
- Key Vault: secrets
- Application Insights: APM
- Azure Backup: daily, 35-day retention
- Traffic Manager: multi-region DNS failover

Achieved SLA: 99.99%+
```

---

### Scenario 3: Migrate on-premises app to Azure

```
Phase 1: Assessment
  → Azure Migrate: discover VMs, databases, web apps
  → Assess dependencies, sizes, TCO

Phase 2: Lift-and-Shift
  → Azure Site Recovery: replicate VMs
  → Azure Database Migration Service: migrate SQL
  → Test failover to validate

Phase 3: Go-Live
  → Cut over DNS
  → Monitor with Azure Monitor + App Insights

Phase 4: Optimize (Post-Migration)
  → Containerize → AKS
  → Move to PaaS (App Service vs IaaS VMs)
  → Autoscaling, Reserved Instances
  → Key Vault, Defender, Managed Identity
```

---

### Scenario 4: VM running out of disk space

```
Immediate:
  1. SSH in: df -h, du -sh /* → find what's consuming space
  2. Clear logs/temp/old backups if safe
  3. Expand OS disk: Portal → VM → Disks → Resize (no reboot needed)

Medium-term:
  4. Add new data disk for app data
  5. Move logs to Blob Storage

Long-term:
  6. Azure Monitor alert: disk < 20% → email alert
  7. Log rotation policy
  8. Move stateful data off VM to managed services
```

---

### Scenario 5: Blue-Green deployment on AKS

```
# Blue (current production)
Deployment: my-app-blue (v1.0, 3 replicas)
Service: my-app-svc → selector: version=blue

# Green (new version, no traffic)
Deployment: my-app-green (v1.1, 3 replicas)

# Validate green deployment
kubectl run smoke-test ...

# Switch traffic (zero-downtime, instant)
kubectl patch service my-app-svc \
  -p '{"spec":{"selector":{"version":"green"}}}'

# Keep blue for 1hr as rollback
# If issues: patch back to blue in seconds
# After validation: delete blue
```

---

### Scenario 6: Secret rotation in a running app

```
1. Store db-password → v1 in Key Vault
2. App uses Managed Identity to read (always latest version)
3. Rotate: create db-password → v2 in Key Vault
   + Update database with new password
4. App Service reference auto-picks up new version
5. Maintain both passwords briefly (rotation window)
6. After 24h: expire old version in Key Vault

Automated rotation with Event Grid:
  → Key Vault fires SecretNearExpiry 30 days before expiry
  → Azure Function rotates secret automatically
```

---

### Scenario 7: Cost spike 3x this month — investigate

```
Step 1: Azure Cost Management
  → Cost analysis by resource/RG/service
  → Compare this month vs last
  → Find which resource spiked and on which day

Step 2: Common culprits
  → Large data egress? → Check networking costs
  → VM left running? → Check compute costs
  → Dev resources in prod subscription?
  → Someone deployed expensive resource?

Step 3: Prevent future spikes
  → Budget alerts: email at 80% and 100% of budget
  → Anomaly detection: daily spend > 3x average

Step 4: Optimize
  → Delete zombie resources (Advisor)
  → Right-size oversized VMs
  → Storage lifecycle policies
  → Reserved Instances for stable workloads
```

---

### Scenario 8: Azure DevOps pipeline failing intermittently

```
Step 1: Check logs
  → Which step fails? Flaky or consistent?
  → Retry job — is it infrastructure flakiness?

Step 2: Common causes
  → Rate limiting on external registries (npm, pip) → use Azure Artifacts cache
  → Build agent resource exhaustion → increase agent size
  → Network timeout → add retry logic
  → Race condition in parallel stages → add dependencies
  → Expired service connection → renew

Step 3: Improve reliability
  → Add retry tasks for flaky steps
  → Use private agents with stable network
  → Cache dependencies (npm cache, pip cache)
  → Pin dependency versions (no floating "latest")

Step 4: Monitor
  → Pipeline analytics → which stages fail most
  → Notifications for failed deployments
```

---

### Scenario 9: Multi-tenant isolation in Azure SaaS

```
Option 1: Subscription per tenant (highest isolation)
  → Complete resource, network, cost isolation
  → Best for enterprise + compliance needs
  → Complex to manage at scale

Option 2: Resource Group per tenant
  → Same subscription, separate RGs
  → RBAC isolation per tenant
  → Good for SMB tenants

Option 3: Application-level isolation (most common)
  → Shared infrastructure, tenant_id in all tables
  → Azure AD B2C for customer auth
  → Row-Level Security in Azure SQL
  → API layer enforces tenant_id on all queries

Compliance:
  → Know where each tenant's data resides
  → Data residency: EU tenants' data stays in EU?
  → Can you restore a single tenant independently?
```

---

### Scenario 10: Event-driven order processing system on Azure

```
Customer places order
    ↓
API Management (auth, rate limiting)
    ↓
Order Service (App Service / AKS)
    ↓
Service Bus Topic (orders)
    ├── Subscription: Payment Processor
    │     → Publishes: PaymentComplete event
    ├── Subscription: Inventory Service
    │     → Publishes: InventoryReserved event
    └── Subscription: Notification Service
          → Sends confirmation email (SendGrid)

All events → Cosmos DB (order status updates)
           → SignalR → real-time UI status

Dead Letter Queues:
  → Failed messages → DLQ → Alert → Manual review

Monitoring:
  → Service Bus queue depth alert > 1000
  → App Insights E2E order trace
  → Alert on payment failures > 1%
```

---

## ⚡ Rapid Fire Questions (20)

| # | Question | Answer |
|---|----------|--------|
| 1 | What protocol does Azure AD use? | OAuth 2.0, OpenID Connect, SAML 2.0 |
| 2 | Default port for RDP? | 3389 |
| 3 | Max block blob size? | 4.75 TB |
| 4 | Tool to estimate Azure costs? | Azure Pricing Calculator |
| 5 | What does SLA stand for? | Service Level Agreement |
| 6 | Azure CLI login command? | `az login` |
| 7 | Rate limiting HTTP status code? | 429 Too Many Requests |
| 8 | What is Kubernetes used for? | Orchestrating containerized workloads |
| 9 | Default Log Analytics retention? | 30 days |
| 10 | What is Azure Bastion? | Browser-based RDP/SSH to VMs without public IP |
| 11 | What does ARM stand for? | Azure Resource Manager |
| 12 | What does AKS stand for? | Azure Kubernetes Service |
| 13 | What is a Managed Disk? | Azure-managed virtual disk for VMs |
| 14 | Minimum AKS system pool nodes? | 1 (3 recommended for HA) |
| 15 | What does TTL mean in DNS? | Time To Live |
| 16 | Free App Service tier name? | F1 (Free) |
| 17 | HTTPS port? | 443 |
| 18 | What is KEDA? | Kubernetes Event-Driven Autoscaling |
| 19 | ARM Template format? | JSON |
| 20 | What does GPv2 stand for? | General Purpose v2 (Storage Account type) |

---

## 📌 Mini Cheat Sheet for Last-Minute Revision

---

### Core Concepts
```
Resource Group    → Logical container for resources
Subscription      → Billing + access boundary
Management Group  → Container for multiple subscriptions
Tenant            → Azure AD instance for your org

Availability Set  → HA within one data center (fault/update domains)
Availability Zone → HA across 3 separate data centers
Region Pair       → DR across geographically distant regions
```

---

### Compute Quick Reference

| Service | Type | When to Use |
|---------|------|-------------|
| Virtual Machine | IaaS | Full control, lift-and-shift |
| VM Scale Sets | IaaS | Auto-scaling identical VMs |
| App Service | PaaS | Web apps, APIs |
| Azure Functions | Serverless | Event-driven, short tasks |
| Container Instances (ACI) | PaaS | Quick containers, no K8s |
| AKS | PaaS+IaaS | Microservices, containerized apps |

---

### Storage Quick Reference

| Service | Use Case |
|---------|----------|
| Blob (Block) | Files, images, videos |
| Blob (Append) | Log files |
| Azure Files | SMB/NFS shared drives |
| Disk (Managed) | VM OS and data disks |
| Table Storage | Key-value NoSQL |
| Queue Storage | Simple messaging |

**Access Tiers:** Hot → Cool → Cold → Archive (freq. vs price)
**Redundancy:** LRS → ZRS → GRS → RA-GRS → GZRS → RA-GZRS

---

### Networking Quick Reference
```
VNet           → Private network (like AWS VPC)
Subnet         → Subdivision of VNet
NSG            → Firewall at subnet/NIC (Layer 4)
VNet Peering   → Connect VNets (Microsoft backbone)
VPN Gateway    → Encrypted tunnel to on-premises
ExpressRoute   → Private circuit to on-premises
Azure Firewall → Managed stateful firewall (L4+L7)

Load Balancer  → L4, TCP/UDP
App Gateway    → L7, HTTP/HTTPS, WAF
Traffic Manager→ DNS-level global routing
Azure Front Door → Global WAF + CDN + L7
```

---

### Database Quick Reference

| Service | Type | Best For |
|---------|------|----------|
| Azure SQL Database | Relational PaaS | OLTP |
| SQL Managed Instance | Relational PaaS | SQL Server migration |
| Azure Database for PostgreSQL | Relational PaaS | Open-source SQL |
| Cosmos DB | Multi-model NoSQL | Global, low latency |
| Redis Cache | In-memory | Caching, sessions |
| Azure Synapse | Analytics | DWH, big data |

---

### Security Quick Reference
```
Azure AD (Entra ID)  → Identity (SSO, MFA, Conditional Access)
RBAC                 → Who can do what
Managed Identity     → Service identity without credentials
Key Vault            → Secrets, keys, certificates
Azure Policy         → Governance/compliance enforcement
PIM                  → Just-in-time privileged access
Defender for Cloud   → Security posture + threat protection
Microsoft Sentinel   → SIEM + SOAR
```

---

### Key Differences to Remember

| Topic | A | B |
|-------|---|---|
| Stopped vs Deallocated | Still billed | Not billed |
| IaaS vs PaaS | You manage OS | MS manages OS |
| Auth vs Authz | Who you are | What you can do |
| RBAC vs Policy | Access control | Governance |
| VNet Peering vs VPN | MS backbone | Internet tunnel |
| Service Endpoint vs Private Endpoint | Public IP still | Private IP in VNet |
| Availability Set vs Zone | Same data center | Separate data centers |
| Azure LB vs App Gateway | Layer 4 (TCP) | Layer 7 (HTTP) |
| Event Hub vs Service Bus | Streaming | Enterprise messaging |
| ARM vs Bicep | JSON verbose | DSL clean, compiles to ARM |

---

### Common Azure CLI Commands
```bash
az login                                          # Login
az account set --subscription "my-sub"           # Set subscription
az group create --name myRG --location eastus     # Create RG
az vm create --resource-group myRG --name myVM \  # Create VM
  --image Ubuntu2204 --size Standard_B2s
az deployment group create --resource-group myRG \ # Deploy Bicep
  --template-file main.bicep
az aks get-credentials --resource-group myRG \   # Get AKS kubeconfig
  --name myAKS
az webapp log tail --name myApp --resource-group myRG  # Stream logs
az resource list --resource-group myRG -o table  # List resources
az advisor recommendation list --category Cost   # Cost recommendations
```

---

### Important Azure SLAs

| Service | SLA |
|---------|-----|
| Azure VM (premium SSD, single) | 99.9% |
| Azure VM (across AZs) | 99.99% |
| Azure SQL (Business Critical) | 99.995% |
| Azure App Service (Standard+) | 99.95% |
| Azure Blob (RA-GRS) | 99.99% |
| Cosmos DB | 99.999% |
| Azure Front Door | 99.99% |
| AKS Control Plane | 99.95% |

---

> 💡 **Interview Tips:**
> - Structure every answer: **Definition → How it works → Real example → Trade-offs**
> - Always mention cost implications — interviewers love cost-aware candidates
> - Draw text diagrams when explaining designs
> - Know at least one AWS equivalent for every service
> - Admit what you don't know: "I haven't used that but here's how I'd approach it"

---

*Guide prepared by Senior Cloud Architect | June 2026*
*Target Role: Azure Developer · Cloud Engineer · Full Stack Developer with Azure*
