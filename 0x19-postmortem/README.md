# ABC Web Service Outage Postmortem

## Issue Summary

- **Duration of Outage:** 4 hours
  - Start: 13th October 2023, 15:00 UTC
  - End: 13th October 2023, 19:00 UTC
- **Impact:** The ABC Web Service experienced a complete outage during the specified duration, with a 100% user impact.
- **Root Cause:** The outage was caused by a misconfiguration of the load balancer settings.

## Postmortem Report

### Timeline

- **Issue Detected:** 13th October 2023, 15:00 UTC
- **Detection Method:** A monitoring alert was triggered due to increased server response times and HTTP 503 errors.
- **Actions Taken:**
  - Engineers initially investigated server logs and database performance, assuming a backend issue.
  - Due to misleading logs, database query optimization was attempted.
  - Incident was escalated to the DevOps team for further investigation.

### Misleading Investigation/Debugging Paths

- Focusing on server and database logs, which did not reveal the issue.
- Database query optimization was pursued, even though database performance was not the root cause.

### Escalation

The incident was escalated to the DevOps team after the initial investigation by the development team.

### Resolution

- DevOps team discovered the misconfiguration in load balancer settings.
- Corrected the load balancer settings, restoring proper traffic distribution.
- Service was gradually restored, with full recovery at 19:00 UTC.

### Root Cause and Resolution

- **Root Cause:** The root cause of the outage was a misconfiguration in the load balancer settings. The load balancer was not evenly distributing traffic among the application servers, causing some servers to be overwhelmed with requests, while others were underutilized.
- **Resolution:** The DevOps team reconfigured the load balancer settings to evenly distribute incoming traffic among the application servers. This alleviated the overloading of certain servers, ensuring a balanced distribution of user requests.

### Corrective and Preventative Measures

- **Things to Improve/Fix:**
  1. Implement automated monitoring of load balancer settings to detect misconfigurations in real-time.
  2. Develop a runbook for load balancer configuration checks and updates to prevent similar incidents in the future.
  3. Establish a clear incident escalation protocol, ensuring swift handover to the appropriate teams for investigation and resolution.
- **List of Tasks:**
  - Implement automated load balancer configuration checks and alerts.
  - Develop and maintain a runbook for load balancer configuration updates.
  - Conduct a post-incident review to identify improvements in incident response and detection.
  - Train team members on the incident escalation process to ensure efficient issue resolution.

This outage served as a valuable learning experience, highlighting the importance of monitoring, clear escalation procedures, and thorough investigation of issues. By implementing the corrective and preventative measures outlined above, we aim to bolster our system's resilience and minimize the risk of future service interruptions.

