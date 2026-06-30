# Detection Template

> **Use Case:** Authorized defensive security, detection engineering, threat hunting, SOC alerting, incident response, purple-team validation, and detection-as-code workflows.
> **Scope Boundary:** Do not use this template to support unauthorized access, stealth, evasion, persistence, malware deployment, credential theft, or real-world attacker operations. Validation must use approved, controlled systems and authorized test data.

---

## 1. Detection Metadata

| Field                           | Value                                                                                                          |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Detection Name                  | `<detection_name>`                                                                                             |
| Detection ID                    | `<detection_id>`                                                                                               |
| Rule ID                         | `<rule_id>`                                                                                                    |
| Status                          | `<Draft / Testing / Production / Tuning / Deprecated / Disabled>`                                              |
| Author                          | `<author_name>`                                                                                                |
| Reviewer                        | `<reviewer_name>`                                                                                              |
| Detection Owner                 | `<detection_owner>`                                                                                            |
| Created Date                    | `<YYYY-MM-DD>`                                                                                                 |
| Last Modified Date              | `<YYYY-MM-DD>`                                                                                                 |
| Last Tested Date                | `<YYYY-MM-DD>`                                                                                                 |
| Next Review Date                | `<YYYY-MM-DD>`                                                                                                 |
| Business Unit / Environment     | `<business_unit_or_environment>`                                                                               |
| Platform                        | `<Windows / Linux / macOS / Cloud / Identity / Network / Application / Container / Kubernetes / SaaS / Other>` |
| Log Source                      | `<log_source>`                                                                                                 |
| SIEM / EDR / XDR / NDR Tool     | `<security_tool>`                                                                                              |
| Query Language                  | `<query_language>`                                                                                             |
| Repository Path                 | `<repository_path>`                                                                                            |
| Rule File Path                  | `<rule_file_path>`                                                                                             |
| Related Ticket / Change Request | `<ticket_or_change_request>`                                                                                   |
| Related Incident IDs            | `<incident_ids>`                                                                                               |
| Related Detection IDs           | `<related_detection_ids>`                                                                                      |
| Related Runbook                 | `<runbook_link>`                                                                                               |
| Dashboard Link                  | `<dashboard_link>`                                                                                             |
| Evidence Root                   | `<evidence_path>`                                                                                              |

### 1.1 Detection Status Definitions

| Status     | Meaning                                                                   |
| ---------- | ------------------------------------------------------------------------- |
| Draft      | Detection is being designed and has not been validated.                   |
| Testing    | Detection is under lab or controlled validation.                          |
| Production | Detection is active and routed according to SOC workflow.                 |
| Tuning     | Detection is active but undergoing false-positive or fidelity refinement. |
| Deprecated | Detection is obsolete but retained for historical reference.              |
| Disabled   | Detection is intentionally turned off.                                    |

---

## 2. Executive Summary

### 2.1 Plain-Language Summary

```text
<Explain what this detection identifies, why the behavior matters, what security value it provides, and who should respond.>
```

### 2.2 Threat Behavior Detected

```text
<Describe the suspicious, malicious, or policy-relevant behavior this detection is intended to identify.>
```

### 2.3 Security Value

| Field                      | Value                                                                                                                                                      |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Expected Security Value    | `<early_detection / containment_support / lateral_movement_visibility / cloud_control_visibility / identity_risk_visibility / policy_enforcement / other>` |
| Severity                   | `<Informational / Low / Medium / High / Critical>`                                                                                                         |
| Confidence                 | `<Low / Medium / High>`                                                                                                                                    |
| Operational Priority       | `<P0 / P1 / P2 / P3>`                                                                                                                                      |
| Recommended Response Owner | `<SOC / IR / IAM / Cloud Security / Endpoint Team / Network Team / AppSec / Platform Team>`                                                                |
| Primary Assets Protected   | `<asset_list>`                                                                                                                                             |
| Business Impact if Missed  | `<business_impact>`                                                                                                                                        |

---

## 3. Detection Objective

### 3.1 Primary Goal

```text
<Describe the primary detection goal.>
```

### 3.2 Secondary Goals

* [ ] `<secondary_goal_1>`
* [ ] `<secondary_goal_2>`
* [ ] `<secondary_goal_3>`

### 3.3 Behavior Being Detected

```text
<Describe the observable behavior, not just the tool, hash, filename, or indicator.>
```

### 3.4 Detection Type

| Type                      | Applies?   | Notes     |
| ------------------------- | ---------- | --------- |
| Signature-based           | `<Yes/No>` | `<notes>` |
| Behavior-based            | `<Yes/No>` | `<notes>` |
| Anomaly-based             | `<Yes/No>` | `<notes>` |
| Correlation-based         | `<Yes/No>` | `<notes>` |
| Threshold-based           | `<Yes/No>` | `<notes>` |
| Risk-based                | `<Yes/No>` | `<notes>` |
| Indicator-based           | `<Yes/No>` | `<notes>` |
| Machine-learning-assisted | `<Yes/No>` | `<notes>` |

### 3.5 Detection Maturity

| Maturity              | Selected   | Notes     |
| --------------------- | ---------- | --------- |
| Experimental          | `<Yes/No>` | `<notes>` |
| Initial               | `<Yes/No>` | `<notes>` |
| Tuned                 | `<Yes/No>` | `<notes>` |
| High fidelity         | `<Yes/No>` | `<notes>` |
| Legacy / Needs Review | `<Yes/No>` | `<notes>` |

---

## 4. Threat Context

### 4.1 Threat Summary

```text
<Describe the threat behavior, intrusion phase, affected technologies, and why defenders care about detecting this activity.>
```

### 4.2 Threat Context Table

| Field                        | Value                                                                                                                                                                                                                |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Relevant Intrusion Phase     | `<reconnaissance / initial_access / execution / persistence / privilege_escalation / defense_evasion / credential_access / discovery / lateral_movement / collection / command_and_control / exfiltration / impact>` |
| Known Adversary Use          | `<known_adversary_use_if_applicable>`                                                                                                                                                                                |
| Relevant Malware / Tooling   | `<malware_or_tooling_if_applicable>`                                                                                                                                                                                 |
| Relevant Vulnerability / CVE | `<cve_or_vulnerability_if_applicable>`                                                                                                                                                                               |
| Business Impact              | `<business_impact>`                                                                                                                                                                                                  |
| Assets at Risk               | `<assets_at_risk>`                                                                                                                                                                                                   |
| Preconditions                | `<preconditions>`                                                                                                                                                                                                    |
| Expected Attacker Objective  | `<attacker_objective>`                                                                                                                                                                                               |
| Defensive Hypothesis         | `<defensive_hypothesis_summary>`                                                                                                                                                                                     |

### 4.3 Detection Hypothesis

```text
Hypothesis:
<If an adversary performs [behavior] against [asset/user/system], then [telemetry pattern] should be observable in [data source] within [time window].>
```

### 4.4 Facts

| ID           | Fact               | Evidence                | Confidence              |
| ------------ | ------------------ | ----------------------- | ----------------------- |
| `<FACT-001>` | `<confirmed_fact>` | `<evidence_path_or_id>` | `<Low / Medium / High>` |

### 4.5 Hypotheses

| ID          | Hypothesis     | Supporting Evidence     | Validation Method          | Status                                    | Confidence              |
| ----------- | -------------- | ----------------------- | -------------------------- | ----------------------------------------- | ----------------------- |
| `<HYP-001>` | `<hypothesis>` | `<evidence_path_or_id>` | `<safe_validation_method>` | `<Open / Testing / Confirmed / Rejected>` | `<Low / Medium / High>` |

---

## 5. MITRE ATT&CK Mapping

| Tactic     | Technique     | Sub-Technique     | ATT&CK ID              | Data Source     | Data Component     | Notes     |
| ---------- | ------------- | ----------------- | ---------------------- | --------------- | ------------------ | --------- |
| `<tactic>` | `<technique>` | `<sub_technique>` | `<mitre_technique_id>` | `<data_source>` | `<data_component>` | `<notes>` |

### 5.1 ATT&CK Coverage Rationale

```text
<Explain why this detection maps to the selected ATT&CK technique or sub-technique. Describe the behavior being detected and how the telemetry supports the mapping.>
```

### 5.2 Related Techniques

| Relationship        | Technique     | ATT&CK ID     | Notes     |
| ------------------- | ------------- | ------------- | --------- |
| Upstream Behavior   | `<technique>` | `<attack_id>` | `<notes>` |
| Downstream Behavior | `<technique>` | `<attack_id>` | `<notes>` |
| Related Behavior    | `<technique>` | `<attack_id>` | `<notes>` |

### 5.3 ATT&CK Coverage Gaps

| Gap              | Impact     | Required Telemetry / Logic      | Recommendation     |
| ---------------- | ---------- | ------------------------------- | ------------------ |
| `<coverage_gap>` | `<impact>` | `<required_telemetry_or_logic>` | `<recommendation>` |

---

## 6. Data Source and Telemetry Requirements

### 6.1 Telemetry Requirements Table

| Requirement     | Field / Event      | Source          | Required   | Example Value     | Notes     |
| --------------- | ------------------ | --------------- | ---------- | ----------------- | --------- |
| `<requirement>` | `<field_or_event>` | `<data_source>` | `<Yes/No>` | `<example_value>` | `<notes>` |

### 6.2 Required Data Sources

* [ ] `<required_data_source_1>`
* [ ] `<required_data_source_2>`
* [ ] `<required_data_source_3>`

### 6.3 Optional Enrichment Sources

* [ ] Asset inventory
* [ ] Identity directory
* [ ] Privileged user list
* [ ] CMDB
* [ ] Vulnerability data
* [ ] Threat intelligence
* [ ] GeoIP
* [ ] ASN enrichment
* [ ] Endpoint inventory
* [ ] Cloud account metadata
* [ ] Change management records

### 6.4 Required Fields

| Logical Field         | Required   | Source Field     | Notes     |
| --------------------- | ---------- | ---------------- | --------- |
| Timestamp             | `<Yes/No>` | `<source_field>` | `<notes>` |
| Hostname              | `<Yes/No>` | `<source_field>` | `<notes>` |
| User                  | `<Yes/No>` | `<source_field>` | `<notes>` |
| Source IP             | `<Yes/No>` | `<source_field>` | `<notes>` |
| Destination IP        | `<Yes/No>` | `<source_field>` | `<notes>` |
| Process Name          | `<Yes/No>` | `<source_field>` | `<notes>` |
| Process Path          | `<Yes/No>` | `<source_field>` | `<notes>` |
| Process Command Line  | `<Yes/No>` | `<source_field>` | `<notes>` |
| Parent Process        | `<Yes/No>` | `<source_field>` | `<notes>` |
| File Path             | `<Yes/No>` | `<source_field>` | `<notes>` |
| Hash                  | `<Yes/No>` | `<source_field>` | `<notes>` |
| Registry Path         | `<Yes/No>` | `<source_field>` | `<notes>` |
| Authentication Result | `<Yes/No>` | `<source_field>` | `<notes>` |
| Cloud Principal       | `<Yes/No>` | `<source_field>` | `<notes>` |
| API Action            | `<Yes/No>` | `<source_field>` | `<notes>` |
| User Agent            | `<Yes/No>` | `<source_field>` | `<notes>` |
| Event ID              | `<Yes/No>` | `<source_field>` | `<notes>` |

### 6.5 Event Types

| Event Category                | Events Required                    | Notes     |
| ----------------------------- | ---------------------------------- | --------- |
| Endpoint Events               | `<endpoint_event_types>`           | `<notes>` |
| Identity Events               | `<identity_event_types>`           | `<notes>` |
| Network Events                | `<network_event_types>`            | `<notes>` |
| Cloud Audit Events            | `<cloud_audit_events>`             | `<notes>` |
| Application Logs              | `<application_log_events>`         | `<notes>` |
| DNS Events                    | `<dns_events>`                     | `<notes>` |
| Proxy Events                  | `<proxy_events>`                   | `<notes>` |
| Email Events                  | `<email_events>`                   | `<notes>` |
| Container / Kubernetes Events | `<container_or_kubernetes_events>` | `<notes>` |

### 6.6 Retention and Collection

| Field                                | Value                                                                         |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| Required Retention Period            | `<retention_period>`                                                          |
| Collection Method                    | `<agent / API / forwarder / syslog / event_hub / streaming_pipeline / other>` |
| Sensor / Control Producing Telemetry | `<sensor_or_control>`                                                         |
| Parsing / Normalization Required     | `<Yes/No>`                                                                    |
| Time Synchronization Requirement     | `<time_sync_requirement>`                                                     |
| Known Blind Spots                    | `<known_blind_spots>`                                                         |

---

## 7. Detection Logic

### 7.1 Logic Summary

```text
Detection Logic Summary:
<Describe the behavior and why the selected events indicate suspicious or malicious activity.>

Trigger:
<Describe the exact condition that should generate an alert.>

Correlation:
<Describe how events are related across host/user/process/IP/session/time.>

Time Window:
<Example: 5 minutes, 1 hour, 24 hours>

Suppression:
<When alerts should be suppressed, grouped, or deduplicated.>
```

### 7.2 Logic Details

| Field                   | Value                       |
| ----------------------- | --------------------------- |
| Trigger Condition       | `<trigger_condition>`       |
| Correlation Logic       | `<correlation_logic>`       |
| Time Window             | `<time_window>`             |
| Thresholds              | `<thresholds>`              |
| Required Event Sequence | `<required_event_sequence>` |
| Field Joins             | `<field_joins>`             |
| Suppression Logic       | `<suppression_logic>`       |
| Exclusions              | `<exclusions>`              |
| Enrichment              | `<enrichment>`              |
| Risk Scoring            | `<risk_scoring>`            |
| Alert Grouping          | `<alert_grouping>`          |
| Deduplication Logic     | `<deduplication_logic>`     |

### 7.3 Detection Logic Classification

| Logic Element     | Behavior-Based? | Indicator-Based? | Notes     |
| ----------------- | --------------- | ---------------- | --------- |
| `<logic_element>` | `<Yes/No>`      | `<Yes/No>`       | `<notes>` |

### 7.4 Detection Logic Pseudocode

```text
<insert vendor-neutral detection pseudocode here>
```

---

## 8. Query / Rule Implementation

### 8.1 Sigma

```yaml
<insert Sigma rule here>
```

### 8.2 Splunk SPL

```spl
<insert Splunk SPL query here>
```

### 8.3 Microsoft Sentinel / KQL

```kql
<insert KQL query here>
```

### 8.4 Elastic EQL / KQL

```text
<insert Elastic query here>
```

### 8.5 CrowdStrike / EDR Query

```text
<insert EDR query here>
```

### 8.6 YARA

```yara
<insert YARA rule here>
```

### 8.7 Suricata / Network Rule

```text
<insert network detection rule here>
```

### 8.8 Custom Pseudocode

```text
<insert vendor-neutral detection pseudocode here>
```

### 8.9 Rule Parameters

| Parameter     | Value     | Rationale     | Notes     |
| ------------- | --------- | ------------- | --------- |
| `<parameter>` | `<value>` | `<rationale>` | `<notes>` |

---

## 9. Field Mapping and Normalization

| Logical Field         | Source Field               | Normalized Field                     | Type               | Required   | Notes     |
| --------------------- | -------------------------- | ------------------------------------ | ------------------ | ---------- | --------- |
| Timestamp             | `<source_timestamp_field>` | `<normalized_timestamp_field>`       | `<datetime>`       | `<Yes/No>` | `<notes>` |
| Hostname              | `<source_hostname_field>`  | `<normalized_hostname_field>`        | `<string>`         | `<Yes/No>` | `<notes>` |
| User                  | `<source_user_field>`      | `<normalized_user_field>`            | `<string>`         | `<Yes/No>` | `<notes>` |
| Source IP             | `<source_ip_field>`        | `<normalized_source_ip_field>`       | `<ip>`             | `<Yes/No>` | `<notes>` |
| Destination IP        | `<destination_ip_field>`   | `<normalized_destination_ip_field>`  | `<ip>`             | `<Yes/No>` | `<notes>` |
| Process Name          | `<process_name_field>`     | `<normalized_process_name_field>`    | `<string>`         | `<Yes/No>` | `<notes>` |
| Process Path          | `<process_path_field>`     | `<normalized_process_path_field>`    | `<string>`         | `<Yes/No>` | `<notes>` |
| Process Command Line  | `<command_line_field>`     | `<normalized_command_line_field>`    | `<string>`         | `<Yes/No>` | `<notes>` |
| Parent Process        | `<parent_process_field>`   | `<normalized_parent_process_field>`  | `<string>`         | `<Yes/No>` | `<notes>` |
| File Path             | `<file_path_field>`        | `<normalized_file_path_field>`       | `<string>`         | `<Yes/No>` | `<notes>` |
| Hash                  | `<hash_field>`             | `<normalized_hash_field>`            | `<string>`         | `<Yes/No>` | `<notes>` |
| Registry Path         | `<registry_path_field>`    | `<normalized_registry_path_field>`   | `<string>`         | `<Yes/No>` | `<notes>` |
| Authentication Result | `<auth_result_field>`      | `<normalized_auth_result_field>`     | `<string>`         | `<Yes/No>` | `<notes>` |
| Cloud Principal       | `<cloud_principal_field>`  | `<normalized_cloud_principal_field>` | `<string>`         | `<Yes/No>` | `<notes>` |
| API Action            | `<api_action_field>`       | `<normalized_api_action_field>`      | `<string>`         | `<Yes/No>` | `<notes>` |
| User Agent            | `<user_agent_field>`       | `<normalized_user_agent_field>`      | `<string>`         | `<Yes/No>` | `<notes>` |
| Event ID              | `<event_id_field>`         | `<normalized_event_id_field>`        | `<string/integer>` | `<Yes/No>` | `<notes>` |

### 9.1 Normalization Requirements

```text
<Describe parsing, transformation, enrichment, lookup, schema mapping, or timestamp normalization required before the detection can operate reliably.>
```

---

## 10. Alert Severity and Confidence

### 10.1 Severity and Confidence Summary

| Field                | Value                                              |
| -------------------- | -------------------------------------------------- |
| Severity             | `<Informational / Low / Medium / High / Critical>` |
| Confidence           | `<Low / Medium / High>`                            |
| Risk Score           | `<risk_score>`                                     |
| Severity Rationale   | `<severity_rationale>`                             |
| Confidence Rationale | `<confidence_rationale>`                           |

### 10.2 Scoring Table

| Factor                   | Value                                 | Score / Impact        | Notes     |
| ------------------------ | ------------------------------------- | --------------------- | --------- |
| Asset Criticality        | `<low/medium/high/critical>`          | `<score_or_modifier>` | `<notes>` |
| User Privilege           | `<standard/privileged/service/admin>` | `<score_or_modifier>` | `<notes>` |
| Internet Exposure        | `<none/internal/external>`            | `<score_or_modifier>` | `<notes>` |
| Repeat Activity          | `<single/repeated/widespread>`        | `<score_or_modifier>` | `<notes>` |
| Known Threat Association | `<none/suspected/confirmed>`          | `<score_or_modifier>` | `<notes>` |
| Detection Fidelity       | `<low/medium/high>`                   | `<score_or_modifier>` | `<notes>` |
| Business Impact          | `<low/medium/high/critical>`          | `<score_or_modifier>` | `<notes>` |

### 10.3 Severity Adjustment Rules

```text
<Describe when severity should be raised or lowered based on asset criticality, user privilege, exposure, repeated activity, confirmed compromise indicators, or business context.>
```

---

## 11. False Positives

### 11.1 Expected Benign Causes

| False Positive Scenario     | How to Identify     | Recommended Tuning     | Risk of Exclusion     |
| --------------------------- | ------------------- | ---------------------- | --------------------- |
| `<false_positive_scenario>` | `<how_to_identify>` | `<recommended_tuning>` | `<risk_of_exclusion>` |

### 11.2 False Positive Sources

* [ ] Known administrative tools
* [ ] Known security tooling
* [ ] Backup software
* [ ] Software deployment tools
* [ ] Developer workflows
* [ ] Maintenance windows
* [ ] Approved automation
* [ ] Vulnerability scanners
* [ ] IT support tooling
* [ ] Monitoring agents
* [ ] Cloud automation
* [ ] CI/CD jobs
* [ ] Environmental exceptions

### 11.3 Tuning Recommendations

```text
<Describe approved tuning methods, allowlists, suppression windows, asset/user exclusions, threshold adjustments, enrichment requirements, and review requirements before exclusion.>
```

### 11.4 False Positive Evidence

```text
<insert sample benign logs, query output, analyst notes, or validation evidence here>
```

---

## 12. False Negatives and Limitations

### 12.1 Limitations Table

| Limitation     | Impact     | Compensating Control     | Follow-Up Action     |
| -------------- | ---------- | ------------------------ | -------------------- |
| `<limitation>` | `<impact>` | `<compensating_control>` | `<follow_up_action>` |

### 12.2 False Negative Conditions

* [ ] Required telemetry missing
* [ ] Required fields not populated
* [ ] Sensor disabled or unhealthy
* [ ] Events delayed beyond correlation window
* [ ] Logs not normalized correctly
* [ ] Activity occurs outside monitored environment
* [ ] Activity uses unsupported platform
* [ ] Activity is below configured threshold
* [ ] Logic only detects known pattern subset
* [ ] Environmental baseline is incomplete
* [ ] Enrichment data unavailable or stale

### 12.3 Defensive Evasion-Resistance Limitations

```text
<Describe high-level classes of ways this detection could fail without providing operational evasion instructions. Focus on telemetry gaps, control limitations, and compensating detections.>
```

### 12.4 Compensating Detections

| Detection ID     | Detection Name     | Coverage Relationship                               | Notes     |
| ---------------- | ------------------ | --------------------------------------------------- | --------- |
| `<detection_id>` | `<detection_name>` | `<overlap / upstream / downstream / complementary>` | `<notes>` |

---

## 13. Test and Validation Plan

### 13.1 Validation Scope

| Field                     | Value                         |
| ------------------------- | ----------------------------- |
| Test Objective            | `<test_objective>`            |
| Test Environment          | `<test_environment>`          |
| Test Data                 | `<test_data_description>`     |
| Approved Emulation Method | `<approved_emulation_method>` |
| Validation Owner          | `<validation_owner>`          |
| Validation Date           | `<YYYY-MM-DD>`                |
| Expected Telemetry        | `<expected_telemetry>`        |
| Expected Alert            | `<expected_alert>`            |
| Negative Test Cases       | `<negative_test_cases>`       |
| Regression Test Cases     | `<regression_test_cases>`     |

### 13.2 Safe Validation Rules

* [ ] Use controlled lab systems.
* [ ] Use approved test accounts.
* [ ] Use non-destructive simulations.
* [ ] Do not run destructive payloads.
* [ ] Do not test against production without written authorization.
* [ ] Do not use unauthorized credentials, targets, or data.
* [ ] Capture evidence for both matching and non-matching cases.
* [ ] Record expected and actual results.
* [ ] Clean up test artifacts.

### 13.3 Validation Test Matrix

| Test ID      | Test Type                                    | Procedure     | Expected Result     | Actual Result     | Pass / Fail   | Evidence          |
| ------------ | -------------------------------------------- | ------------- | ------------------- | ----------------- | ------------- | ----------------- |
| `<TEST-001>` | `<positive/negative/regression/performance>` | `<procedure>` | `<expected_result>` | `<actual_result>` | `<Pass/Fail>` | `<evidence_path>` |

### 13.4 Validation Procedure

```text
<Describe controlled, authorized, non-destructive validation steps. Use placeholders for test commands and generated telemetry.>
```

### 13.5 Test Commands

```bash
<insert safe test command or controlled simulation command here>
```

### 13.6 Validation Output

```text
<insert validation output here>
```

### 13.7 Alert Validation Evidence

```json
<insert generated alert evidence here>
```

---

## 14. Sample Events

### 14.1 Positive Match Event

```json
<insert sanitized event that should match>
```

### 14.2 Negative Match Event

```json
<insert sanitized event that should not match>
```

### 14.3 Alert Example

```json
<insert sample alert payload>
```

### 14.4 Field-Level Explanation

| Field     | Positive Match Value | Negative Match Value | Why It Matters  |
| --------- | -------------------- | -------------------- | --------------- |
| `<field>` | `<positive_value>`   | `<negative_value>`   | `<explanation>` |

---

## 15. Triage Workflow

### 15.1 Analyst Triage Steps

1. Confirm alert context.
2. Validate user, host, process, identity, or cloud principal.
3. Review related events before and after the alert.
4. Check asset criticality.
5. Check user privilege level.
6. Check known false positive scenarios.
7. Determine whether the activity is authorized.
8. Identify related alerts in the same time window.
9. Collect evidence.
10. Escalate if suspicious or confirmed malicious.
11. Document disposition.

### 15.2 Triage Table

| Step | Analyst Action                 | Tool / Data Source                         | Expected Evidence                     |
| ---- | ------------------------------ | ------------------------------------------ | ------------------------------------- |
| `1`  | Confirm alert metadata         | `<SIEM_or_alert_console>`                  | `<alert_id_timestamp_rule_name>`      |
| `2`  | Validate involved entity       | `<EDR/IAM/CMDB/cloud_console>`             | `<host_user_asset_identity_context>`  |
| `3`  | Review surrounding activity    | `<SIEM/EDR/XDR>`                           | `<events_before_after_alert>`         |
| `4`  | Check false positive scenarios | `<change_management/allowlist/admin_logs>` | `<approved_activity_or_no_match>`     |
| `5`  | Assess severity                | `<asset_inventory/IAM/threat_intel>`       | `<risk_context>`                      |
| `6`  | Collect evidence               | `<SIEM/EDR/case_management>`               | `<logs_process_tree_network_context>` |
| `7`  | Escalate or close              | `<case_management>`                        | `<disposition_and_notes>`             |

### 15.3 Disposition Values

| Disposition                | Definition                                                                     |
| -------------------------- | ------------------------------------------------------------------------------ |
| True Positive — Malicious  | Confirmed unauthorized or malicious activity.                                  |
| True Positive — Authorized | Detection correctly matched suspicious behavior that was approved or expected. |
| False Positive             | Detection matched benign activity that should not alert in the future.         |
| Benign Positive            | Detection matched expected but security-relevant behavior worth recording.     |
| Inconclusive               | Insufficient evidence to confirm benign or malicious.                          |
| Duplicate                  | Alert duplicates an existing case or incident.                                 |

---

## 16. Investigation Questions

* Which user, service account, workload identity, or cloud principal triggered the alert?
* What host, workload, container, application, or cloud resource was involved?
* Was the activity interactive, automated, scheduled, or service-driven?
* What parent process, upstream event, or prior authentication event preceded the alert?
* Was the activity seen on multiple hosts, accounts, regions, tenants, or applications?
* Is this activity normal for the user, system, service, or application?
* Was privileged access involved?
* Was sensitive data, credential material, administrative access, or production infrastructure involved?
* Are there related alerts in the same time window?
* Does the activity map to a known incident, maintenance window, deployment, or change request?
* Was the activity blocked, allowed, quarantined, or only observed?
* Are there signs of follow-on behavior?
* Are required logs complete and trustworthy?
* Is additional containment required?

---

## 17. Response Guidance

### 17.1 Initial Handling

| Severity      | Initial Handling                    | Target Response Time | Owner     |
| ------------- | ----------------------------------- | -------------------- | --------- |
| Critical      | `<critical_response_guidance>`      | `<timeframe>`        | `<owner>` |
| High          | `<high_response_guidance>`          | `<timeframe>`        | `<owner>` |
| Medium        | `<medium_response_guidance>`        | `<timeframe>`        | `<owner>` |
| Low           | `<low_response_guidance>`           | `<timeframe>`        | `<owner>` |
| Informational | `<informational_response_guidance>` | `<timeframe>`        | `<owner>` |

### 17.2 Response Actions

| Action                        | When to Consider | Owner     | Evidence Required | Notes     |
| ----------------------------- | ---------------- | --------- | ----------------- | --------- |
| Evidence preservation         | `<criteria>`     | `<owner>` | `<evidence>`      | `<notes>` |
| Host isolation                | `<criteria>`     | `<owner>` | `<evidence>`      | `<notes>` |
| Account disable/reset         | `<criteria>`     | `<owner>` | `<evidence>`      | `<notes>` |
| Cloud key/session revocation  | `<criteria>`     | `<owner>` | `<evidence>`      | `<notes>` |
| Firewall/blocklist update     | `<criteria>`     | `<owner>` | `<evidence>`      | `<notes>` |
| Malware/file collection       | `<criteria>`     | `<owner>` | `<evidence>`      | `<notes>` |
| Incident response handoff     | `<criteria>`     | `<owner>` | `<evidence>`      | `<notes>` |
| Legal/compliance notification | `<criteria>`     | `<owner>` | `<evidence>`      | `<notes>` |

### 17.3 Escalation Criteria

```text
<Escalate when [conditions]. Include affected assets, privilege level, confirmed malicious indicators, repeated activity, regulatory impact, or active incident correlation.>
```

### 17.4 Evidence Preservation Guidance

```text
<Describe what logs, artifacts, case notes, screenshots, event exports, packet captures, endpoint timelines, or cloud audit events should be preserved.>
```

---

## 18. Deployment Plan

### 18.1 Deployment Details

| Field                       | Value                                                      |
| --------------------------- | ---------------------------------------------------------- |
| Deployment Environment      | `<dev/test/staging/production>`                            |
| Detection Mode              | `<Silent / Monitor only / Alerting / Blocking/prevention>` |
| Rollout Phase               | `<phase>`                                                  |
| Backout Plan                | `<backout_plan>`                                           |
| Change Control              | `<change_request>`                                         |
| Alert Routing               | `<queue_or_channel>`                                       |
| Case Management Integration | `<case_management_tool>`                                   |
| Notification Channels       | `<notification_channels>`                                  |
| Runbook Link                | `<runbook_link>`                                           |
| Dashboard Link              | `<dashboard_link>`                                         |

### 18.2 Rollout Phases

| Phase                      | Description     | Success Criteria     | Exit Criteria     |
| -------------------------- | --------------- | -------------------- | ----------------- |
| Phase 1 — Lab              | `<description>` | `<success_criteria>` | `<exit_criteria>` |
| Phase 2 — Silent / Monitor | `<description>` | `<success_criteria>` | `<exit_criteria>` |
| Phase 3 — Alerting         | `<description>` | `<success_criteria>` | `<exit_criteria>` |
| Phase 4 — Tuning           | `<description>` | `<success_criteria>` | `<exit_criteria>` |
| Phase 5 — Production       | `<description>` | `<success_criteria>` | `<exit_criteria>` |

### 18.3 Backout Plan

```text
<Describe how to disable, roll back, or revert the detection if it creates excessive volume, performance issues, or incorrect blocking/prevention behavior.>
```

---

## 19. Performance and Cost Considerations

### 19.1 Query and Platform Impact

| Factor               | Current Estimate         | Risk                | Notes     |
| -------------------- | ------------------------ | ------------------- | --------- |
| Query Cost           | `<cost_estimate>`        | `<Low/Medium/High>` | `<notes>` |
| Event Volume         | `<event_volume>`         | `<Low/Medium/High>` | `<notes>` |
| Cardinality Concerns | `<cardinality_concerns>` | `<Low/Medium/High>` | `<notes>` |
| Index Impact         | `<index_impact>`         | `<Low/Medium/High>` | `<notes>` |
| Runtime Impact       | `<runtime_impact>`       | `<Low/Medium/High>` | `<notes>` |
| Alert Volume         | `<alert_volume>`         | `<Low/Medium/High>` | `<notes>` |
| Storage Impact       | `<storage_impact>`       | `<Low/Medium/High>` | `<notes>` |

### 19.2 Optimization Notes

```text
<Describe query optimizations, index constraints, field selection, pre-filtering, summary tables, lookup use, suppression strategy, or alert grouping improvements.>
```

### 19.3 Suppression Strategy

```text
<Describe how repeat alerts are grouped, deduplicated, throttled, suppressed, or escalated.>
```

---

## 20. Detection Review Checklist

* [ ] Detection has a clear hypothesis.
* [ ] Required data sources exist.
* [ ] Required fields are populated.
* [ ] Logic maps to documented threat behavior.
* [ ] ATT&CK mapping is accurate.
* [ ] Data source and data component mappings are documented.
* [ ] Detection logic is documented in vendor-neutral language.
* [ ] Query or rule syntax is stored in fenced code blocks.
* [ ] Field mappings are documented.
* [ ] Severity rationale is documented.
* [ ] Confidence rationale is documented.
* [ ] False positives are documented.
* [ ] False negatives are documented.
* [ ] Telemetry gaps are documented.
* [ ] Query was tested against positive data.
* [ ] Query was tested against negative data.
* [ ] Regression test cases are documented.
* [ ] Alert includes enough context for triage.
* [ ] Triage workflow is documented.
* [ ] Response guidance is documented.
* [ ] Owner and review date are assigned.
* [ ] Detection is version controlled.
* [ ] Deployment plan is documented.
* [ ] Rollback guidance is documented.
* [ ] Maintenance plan is documented.

---

## 21. Coverage and Gap Analysis

### 21.1 Coverage Table

| Behavior     | Covered?           | Detection ID     | Data Source     | Gap     | Recommendation     |
| ------------ | ------------------ | ---------------- | --------------- | ------- | ------------------ |
| `<behavior>` | `<Yes/No/Partial>` | `<detection_id>` | `<data_source>` | `<gap>` | `<recommendation>` |

### 21.2 Related Detections

| Detection ID     | Detection Name     | Relationship                                           | Notes     |
| ---------------- | ------------------ | ------------------------------------------------------ | --------- |
| `<detection_id>` | `<detection_name>` | `<overlapping / upstream / downstream / compensating>` | `<notes>` |

### 21.3 Missing Detections

| Missing Behavior     | Required Data Source     | Priority            | Recommendation     |
| -------------------- | ------------------------ | ------------------- | ------------------ |
| `<missing_behavior>` | `<required_data_source>` | `<High/Medium/Low>` | `<recommendation>` |

### 21.4 Telemetry Improvements

| Improvement               | Required Owner | Priority            | Expected Benefit     |
| ------------------------- | -------------- | ------------------- | -------------------- |
| `<telemetry_improvement>` | `<owner>`      | `<High/Medium/Low>` | `<expected_benefit>` |

### 21.5 Engineering Backlog Items

| Backlog Item     | Owner     | Priority            | Status     | Notes     |
| ---------------- | --------- | ------------------- | ---------- | --------- |
| `<backlog_item>` | `<owner>` | `<High/Medium/Low>` | `<status>` | `<notes>` |

---

## 22. Maintenance Plan

### 22.1 Maintenance Details

| Field                     | Value                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------- |
| Review Cadence            | `<monthly / quarterly / semiannual / annual / after_incident / after_platform_change>` |
| Owner                     | `<owner>`                                                                              |
| Next Review Date          | `<YYYY-MM-DD>`                                                                         |
| Review Trigger            | `<trigger>`                                                                            |
| Deprecation Criteria      | `<deprecation_criteria>`                                                               |
| Required Retest Frequency | `<retest_frequency>`                                                                   |

### 22.2 Review Triggers

* [ ] High false-positive volume
* [ ] Confirmed false negative
* [ ] Data source schema change
* [ ] Sensor or platform change
* [ ] ATT&CK technique update
* [ ] New threat intelligence
* [ ] Incident feedback
* [ ] Business process change
* [ ] Asset criticality change
* [ ] Detection ownership change
* [ ] Query performance degradation

### 22.3 Rule Tuning History

| Date           | Change     | Reason     | Author     | Reviewer     |
| -------------- | ---------- | ---------- | ---------- | ------------ |
| `<YYYY-MM-DD>` | `<change>` | `<reason>` | `<author>` | `<reviewer>` |

### 22.4 Data Source Changes

| Date           | Data Source     | Change     | Impact     | Action Taken     |
| -------------- | --------------- | ---------- | ---------- | ---------------- |
| `<YYYY-MM-DD>` | `<data_source>` | `<change>` | `<impact>` | `<action_taken>` |

### 22.5 Incident Feedback Loop

```text
<Describe how incident findings, analyst feedback, false-positive analysis, and missed detections are fed back into rule tuning and coverage planning.>
```

---

## 23. Evidence Index

| Evidence ID  | Description     | Source     | Path / Link       | Timestamp     | Notes     |
| ------------ | --------------- | ---------- | ----------------- | ------------- | --------- |
| `<EVID-001>` | `<description>` | `<source>` | `<evidence_path>` | `<timestamp>` | `<notes>` |

### 23.1 Evidence Storage Layout

```text
<evidence_root>/
├── metadata/
├── threat_context/
├── telemetry_samples/
├── queries/
├── validation/
├── alerts/
├── false_positives/
├── false_negatives/
├── tuning/
├── deployment/
├── screenshots/
└── review_notes/
```

### 23.2 Evidence Handling Notes

```text
<Describe evidence integrity, sensitive data handling, redaction requirements, retention expectations, and access controls.>
```

---

## 24. Open Questions and Follow-Up Tasks

### 24.1 Open Assumptions

| ID          | Assumption     | Risk if Wrong     | Owner     | Status                                     |
| ----------- | -------------- | ----------------- | --------- | ------------------------------------------ |
| `<ASM-001>` | `<assumption>` | `<risk_if_wrong>` | `<owner>` | `<Open / Confirmed / Rejected / Deferred>` |

### 24.2 Missing Logs

| Missing Log / Field      | Impact     | Required Owner | Follow-Up Action     | Priority            |
| ------------------------ | ---------- | -------------- | -------------------- | ------------------- |
| `<missing_log_or_field>` | `<impact>` | `<owner>`      | `<follow_up_action>` | `<High/Medium/Low>` |

### 24.3 Required Engineering Changes

| Change                 | Reason     | Owner     | Priority            | Status     |
| ---------------------- | ---------- | --------- | ------------------- | ---------- |
| `<engineering_change>` | `<reason>` | `<owner>` | `<High/Medium/Low>` | `<status>` |

### 24.4 Required Threat Intelligence

| Intelligence Need | Reason     | Source     | Owner     | Status     |
| ----------------- | ---------- | ---------- | --------- | ---------- |
| `<intel_need>`    | `<reason>` | `<source>` | `<owner>` | `<status>` |

### 24.5 Required Purple-Team Tests

| Test                 | Objective     | Environment     | Owner     | Status     |
| -------------------- | ------------- | --------------- | --------- | ---------- |
| `<purple_team_test>` | `<objective>` | `<environment>` | `<owner>` | `<status>` |

### 24.6 Analyst Feedback Needed

| Feedback Area     | Question     | Requested From      | Status     |
| ----------------- | ------------ | ------------------- | ---------- |
| `<feedback_area>` | `<question>` | `<analyst_or_team>` | `<status>` |

### 24.7 Detection Backlog Items

| Backlog ID      | Task     | Priority            | Owner     | Due Date       | Status                                       |
| --------------- | -------- | ------------------- | --------- | -------------- | -------------------------------------------- |
| `<BACKLOG-001>` | `<task>` | `<High/Medium/Low>` | `<owner>` | `<YYYY-MM-DD>` | `<Open / In Progress / Complete / Deferred>` |

### 24.8 Final Notes

```text
<Freeform notes, caveats, lessons learned, reviewer comments, and remaining questions.>
```
