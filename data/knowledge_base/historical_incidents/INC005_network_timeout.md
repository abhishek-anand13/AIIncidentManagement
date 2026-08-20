# Incident ID
INC005

# Title
Network Timeout

# Severity
High

# Symptoms
- Service-to-service calls began timing out intermittently
- API response times increased and became unstable
- Retry volume rose sharply across dependent services
- Network latency alerts triggered repeatedly
- Operators observed degraded communication between internal components

# Root Cause
A transient routing issue in the internal network caused packet loss and elevated latency on several paths. The instability affected service-to-service communication within the same region and increased retry traffic across the platform.

# Resolution
1. Identified the impacted network paths and routing issue
2. Rerouted traffic to healthy paths
3. Coordinated with the infrastructure team to stabilize routing
4. Verified connectivity and restored normal traffic flow

# Lessons Learned
- Critical network paths should have redundancy and failover coverage
- Route health and packet loss metrics should be monitored continuously
- Failover procedures should be tested under realistic conditions

# Keywords
network, timeout, routing, packet loss, latency, service mesh, internal connectivity, infrastructure incident
