# Incident ID
INC010

# Title
SSL Certificate Expired

# Severity
Medium

# Symptoms
- HTTPS connections failed for browsers and clients
- Users encountered certificate warnings and access failures
- Monitoring reported TLS validation errors
- Support teams saw an increase in secure-access complaints
- External health checks detected certificate trust issues

# Root Cause
The TLS certificate was not renewed before its expiration date. Once the certificate expired, secure connections could no longer be validated and clients rejected the application’s HTTPS endpoints.

# Resolution
1. Replaced the expired certificate with a renewed one
2. Restarted services so they would load the new certificate
3. Verified HTTPS endpoints were accessible again
4. Confirmed certificate validity through external checks

# Lessons Learned
- Certificate renewal should be automated and monitored well in advance
- TLS validation should be included in deployment and health checks
- Expiration dates should be tracked centrally for all production certificates

# Keywords
ssl, tls, certificate expiration, https, certificate renewal, trust chain, secure transport, web security
