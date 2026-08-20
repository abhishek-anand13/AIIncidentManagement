# Runbook
High CPU

# Purpose
Use this runbook when application services show sustained high CPU usage that causes latency, reduced throughput, or instability.

# Preconditions
- Verify the CPU issue is occurring in production or a critical non-production environment
- Confirm alerting data for CPU saturation and service latency
- Ensure access to host, container, or process monitoring tools
- Identify whether the load is caused by a deployment, batch job, or traffic increase

# Resolution Steps
1. Validate the CPU spike using monitoring dashboards and node or container metrics
2. Identify the top CPU-consuming processes, services, or endpoints
3. Review recent deployments, batch jobs, and traffic patterns for correlation
4. Disable or rate-limit the offending background workload if it is non-essential
5. Optimize the hot path, query, or loop causing excessive processing
6. Scale out capacity if the load is legitimate and expected
7. Rebalance traffic or workload distribution if one instance is overloaded
8. Monitor CPU trends until the service returns to normal operating levels

# Verification
Confirm the incident is resolved when CPU utilization returns to an acceptable range, application latency normalizes, and no new alerts or throttling events are triggered.

# Rollback
If the mitigation worsens the issue, restore the previous workload configuration, re-enable the last stable deployment, and reassess the traffic or code change.

# Escalation
Escalate to the application engineering or infrastructure team if CPU remains elevated after workload reduction, optimization, and capacity scaling steps.

# Keywords
cpu, performance degradation, processor saturation, workload tuning, background job, scaling, container monitoring, production operations
