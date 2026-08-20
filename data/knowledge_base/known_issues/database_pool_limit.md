# Known Issue
Database Pool Limit

# Issue ID
KI-DB-001

# Description
The application repeatedly hit the configured database connection pool limit during peak traffic, causing connection contention and request timeouts.

# Symptoms
- Database timeouts increased under load
- Requests queued longer than expected
- Error rates rose during peak traffic periods
- Connection pool saturation alerts fired repeatedly
- Application latency increased as database access became throttled

# Root Cause
The connection pool size was too small for the current request volume and burst traffic. In addition, a small number of slow-running queries held connections longer than expected, which amplified contention across the application.

# Workaround
1. Reduce traffic burst pressure temporarily
2. Increase the database connection pool size
3. Identify and optimize slow-running queries
4. Monitor connection usage until the system stabilizes

# Permanent Fix
The engineering team increased the pool capacity to match expected workload and tuned the most expensive database queries to release connections sooner. Operational monitoring was also improved to alert before saturation became critical.

# Related Runbook
database_timeout.md

# Keywords
database, connection pool, query latency, timeout, connection saturation, transaction processing, pool tuning, production issue
