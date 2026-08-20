# Known Issue
Deployment Bug

# Issue ID
KI-DEP-001

# Description
A deployment introduced a configuration regression that caused services to fail during startup and remain unhealthy until the issue was corrected.

# Symptoms
- Pods remained in a crash loop after deployment
- Health checks failed repeatedly during startup
- New deployments were marked unhealthy by readiness probes
- Application logs reported missing configuration values
- Service availability was reduced until the deployment was corrected

# Root Cause
The deployment manifest omitted a required environment variable. Because the application depended on that variable during initialization, the service could not complete startup and repeatedly restarted.

# Workaround
1. Revert the deployment to the last known good configuration
2. Add the missing environment variable to the manifest
3. Redeploy the service and verify readiness probes
4. Monitor startup logs for successful initialization

# Permanent Fix
The engineering team corrected the deployment configuration by adding the missing environment variable and validated the manifest in pre-production before rollout. Deployment checks were also strengthened to catch missing configuration values earlier.

# Related Runbook
restart_application.md

# Keywords
deployment, configuration regression, environment variable, crash loop, readiness probe, startup failure, kubernetes, rollout
