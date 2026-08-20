# Runbook
Restart Application

# Purpose
Use this runbook when a service is unhealthy and a controlled restart is the safest immediate mitigation step.

# Preconditions
- Verify the service is unhealthy or failing health checks
- Review recent logs and deployment activity for obvious errors
- Confirm the restart will not disrupt critical business workflows unexpectedly
- Ensure access to the deployment platform or host management tools

# Resolution Steps
1. Confirm the service is failing and that a restart is appropriate for the current incident
2. Review recent application logs, deployment history, and resource metrics
3. Restart the affected application instance, pod, or service process
4. Observe startup behavior and health checks after the restart
5. Validate application logs for recovery and absence of fatal errors
6. Monitor service metrics and client traffic until normal behavior is observed

# Verification
Confirm the incident is resolved when the service returns to healthy status, health checks pass, and error rates are back to normal.

# Rollback
If the restart does not recover the service or causes additional instability, revert the last deployment or restore the prior instance configuration and investigate further.

# Escalation
Escalate to the application engineering team if the service remains unhealthy after a controlled restart or if the restart reveals a recurring defect.

# Keywords
application restart, service recovery, health check failure, deployment rollback, application logs, container restart, incident mitigation, production operations
