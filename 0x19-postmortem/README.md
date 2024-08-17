# Postmortem Report:
## Web Application Outage

<p align="center">
<img src="https://raw.githubusercontent.com/MitaliSengupta/holberton-system_engineering-devops/master/0x19-postmortem/image.gif" width=100% height=100% />
</p>

## Issue Summary

- **Duration** : August 15, 2024, 14:15 - 16:45 UTC

- **Impact** : The main user-facing web application experienced a significant slowdown, with page load times 
increasing from an average of 2 seconds to over 30 seconds. Approximately 70% of users were affected, with many reporting timeouts and inability to access the service.

- **Root Cause** : A misconfiguration in the load balancer caused a bottleneck, leading to server overload and degraded performance.

#### Timeline

- **14:15 UTC**  - The issue was detected by an automated monitoring alert indicating a spike in page load times.
- **14:20 UTC** - The DevOps team was notified of the issue through the monitoring system.
- **14:25 UTC** - Initial investigation began, focusing on the application servers, assuming a memory leak due to the gradual performance degradation.
- **14:45 UTC** - The database was checked for slow queries, but no anomalies were found.
- **15:00 UTC** - The network team was brought in to investigate potential networking issues, but this path was found to be a dead end.
- **15:30 UTC** - The issue was escalated to the cloud infrastructure team, who identified unusual traffic patterns in the load balancer logs.
- **15:50 UTC** - A misconfiguration in the load balancer’s routing rules was discovered, causing all traffic to be routed to a single server instead of being distributed evenly.
- **16:00 UTC** - The load balancer configuration was corrected, and traffic distribution returned to normal.
- **16:15 UTC** - Monitoring confirmed that page load times had returned to expected levels.
- **16:45 UTC** - The incident was declared resolved after an additional 30 minutes of stable performance.


#### Root Cause and Resolution

The root cause of the outage was traced to a recent update to the load balancer’s configuration, which introduced an error in the routing rules. Specifically, a wildcard character was incorrectly placed, causing all incoming traffic to be directed to a single server rather than being evenly distributed across the server pool. This led to the overloaded server handling more requests than it could manage, resulting in significant performance degradation for the majority of users.

The issue was resolved by correcting the load balancer configuration to ensure proper traffic distribution. Once the fix was applied, the system quickly returned to normal operation, as confirmed by monitoring tools.

#### Corrective and Preventative Measures

To prevent a recurrence of this issue, the following actions will be taken:

1. **Configuration Review Process**: Implement a mandatory peer-review process for all configuration changes to critical infrastructure components, such as load balancers.

2. **Automated Configuration Validation**: Develop and integrate automated tools to validate configuration changes before they are applied, specifically checking for common errors like improper use of wildcards.

3. **Enhanced Monitoring**: Add specific monitoring for traffic distribution across servers to detect and alert on imbalances that could indicate configuration issues.

4. **Load Balancer Redundancy**: Investigate and implement additional redundancy in the load balancing setup to ensure that misconfigurations do not lead to a single point of failure.

#### Tasks to Address the Issue:

-  Review and update load balancer configuration.

-  Implement automated configuration validation tools.

-  Update monitoring systems to include traffic distribution alerts.

-  Conduct training sessions for the DevOps team on best practices for load balancer configurations.

This postmortem highlights the importance of rigorous change management processes and the need for proactive 
monitoring to detect and address issues before they impact users.
