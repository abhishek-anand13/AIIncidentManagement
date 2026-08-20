# Incident ID
INC009

# Title
Message Queue Backlog

# Severity
Medium

# Symptoms
- Message queue depth increased beyond normal levels
- Background processing jobs were delayed significantly
- Consumer lag metrics exceeded the acceptable threshold
- Queue age increased as messages accumulated
- Operators observed reduced throughput for asynchronous workloads

# Root Cause
One consumer instance slowed down after a dependency outage, causing processing delays and backlog growth in the message queue. The slowdown reduced throughput and allowed pending messages to accumulate.

# Resolution
1. Restored the affected dependency and recovered the consumer
2. Scaled out consumer capacity temporarily
3. Cleared the backlog gradually to avoid overloading downstream systems
4. Verified processing rates returned to normal

# Lessons Learned
- Queue depth and consumer lag should be monitored together
- Consumer autoscaling should respond to queue pressure
- Recovery workflows for dependency failures should be tested regularly

# Keywords
message queue, backlog, consumer lag, asynchronous processing, queue depth, dependency outage, throughput, event processing
