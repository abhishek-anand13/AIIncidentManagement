# Incident ID
INC002

# Title
High CPU

# Severity
High

# Symptoms
- CPU utilization rose above acceptable thresholds across application instances
- Service response times increased significantly during the incident window
- Performance dashboards showed abnormal processing spikes
- Background jobs consumed excessive compute resources
- Operators observed degraded service quality under load

# Root Cause
A faulty background job repeatedly recomputed the same dataset without caching, which caused excessive CPU consumption. The workload amplified over time and affected multiple instances until the process was identified and contained.

# Resolution
1. Identified the runaway background job causing the spike
2. Temporarily disabled the faulty workload
3. Implemented caching for repeated computations
4. Rebalanced workload across instances and monitored CPU recovery

# Lessons Learned
- Background jobs should include execution safeguards and rate limits
- Expensive recomputation paths should be cached where possible
- CPU hot spots should be monitored by service and endpoint

# Keywords
cpu, performance degradation, background job, caching, compute saturation, workload balancing, application latency, production incident
