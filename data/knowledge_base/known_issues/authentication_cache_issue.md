# Known Issue
Authentication Cache Issue

# Issue ID
KI-AUTH-001

# Description
A cache inconsistency caused authentication failures for some users after credential updates, resulting in stale token behavior and login disruption.

# Symptoms
- Some users could not log in after password changes
- Tokens appeared stale or invalid
- Authentication failures increased after credential updates
- Support requests increased around identity-related changes
- Monitoring showed elevated authentication error rates

# Root Cause
The authentication cache was not invalidated correctly after user credential changes. As a result, some requests continued to use stale identity data until the cache was manually cleared or refreshed.

# Workaround
1. Clear the stale authentication cache entries
2. Force token refresh for affected users
3. Revalidate authentication flows after cache reset
4. Monitor for recurring invalidation failures

# Permanent Fix
The engineering team updated the cache invalidation logic so credential changes immediately invalidate stale authentication state. The fix was then validated through identity-related test cases to ensure the cache stays consistent.

# Related Runbook
authentication_failure.md

# Keywords
authentication, cache invalidation, token refresh, credential update, identity service, stale session, login failure, security incident
