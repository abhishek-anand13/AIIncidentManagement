# Incident ID
INC006

# Title
API Gateway 502

# Severity
High

# Symptoms
- The API gateway returned HTTP 502 responses to client requests
- External API traffic failed intermittently during the incident window
- Users experienced disrupted workflows and failed requests
- Monitoring showed a sharp increase in gateway error rates
- Retry storms increased backend load during recovery

# Root Cause
An upstream service became unavailable for a brief period and the API gateway could not successfully proxy requests to it. The dependency failure propagated to the edge layer, resulting in elevated 502 responses.

# Resolution
1. Restored the affected upstream service
2. Reduced request concurrency to prevent overload on the gateway
3. Verified gateway health and confirmed the error rate returned to baseline
4. Monitored client traffic for sustained recovery

# Lessons Learned
- Upstream dependency health should be monitored with explicit alerting
- Circuit breakers and backoff retries reduce blast radius during dependency failures
- Gateway error trends should be tracked as part of service health monitoring

# Keywords
api gateway, http 502, upstream dependency, proxy failure, edge service, retry storm, load management, production incident
