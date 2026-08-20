# Runbook
Network Timeout

# Purpose
Use this runbook when service-to-service communication experiences intermittent or sustained timeouts caused by network instability.

# Preconditions
- Verify the issue is affecting production traffic or a critical service path
- Confirm elevated latency, packet loss, or timeout alerts in monitoring
- Ensure access to network telemetry, host logs, and routing data
- Review recent infrastructure or firewall changes that could impact connectivity

# Resolution Steps
1. Confirm the scope of the networking issue across affected services and regions
2. Review routing, packet loss, and latency metrics for the impacted path
3. Inspect host and network logs for evidence of drops or congestion
4. Reroute traffic to a healthy path if failover is available
5. Restart or reconnect affected services if they remain unhealthy after path correction
6. Apply the underlying network fix or rollback recent infrastructure changes
7. Monitor request success rates and end-to-end connectivity until the issue is resolved

# Verification
Confirm the incident is resolved when service-to-service calls succeed consistently, timeout rates return to baseline, and network metrics stabilize.

# Rollback
If the mitigation fails, revert recent routing or infrastructure changes, restore the previous network path, and engage the platform team.

# Escalation
Escalate to the network or platform engineering team if the issue persists after rerouting, service recovery, and infrastructure review.

# Keywords
network, timeout, routing, packet loss, latency, connectivity, failover, infrastructure operations, service communication
