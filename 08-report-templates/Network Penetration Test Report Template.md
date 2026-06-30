# Network Penetration Test Report Template

> **Use Case:** Authorized network penetration testing reports, internal assessments, external assessments, assumed-breach assessments, segmentation tests, Active Directory assessments, wireless/VPN assessments, and infrastructure security reviews.
> **Scope Boundary:** This report template is for ethical, contractual, and explicitly authorized assessments only. Do not use it to document unauthorized access, credential theft against third parties, stealth, persistence, destructive actions, malware deployment, or real-world misuse. Any exploitation or proof-of-concept content must be framed as safe validation within the approved engagement scope.

---

## 1. Cover Page

| Field                        | Value                                                                                                                |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Report Title                 | `Network Penetration Test Report`                                                                                    |
| Client / Organization        | `<client_name>`                                                                                                      |
| Engagement Name              | `<engagement_name>`                                                                                                  |
| Assessment Type              | `<external / internal / assumed-breach / segmentation / wireless / VPN / Active Directory / infrastructure / mixed>` |
| Assessment Dates             | `<assessment_start_date> to <assessment_end_date>`                                                                   |
| Report Date                  | `<YYYY-MM-DD>`                                                                                                       |
| Report Version               | `<report_version>`                                                                                                   |
| Classification / Sensitivity | `<public / internal / confidential / restricted>`                                                                    |
| Prepared By                  | `<tester_or_company_name>`                                                                                           |
| Reviewed By                  | `<reviewer_name>`                                                                                                    |
| Distribution List            | `<authorized_recipients>`                                                                                            |
| Evidence Root                | `<evidence_root_path>`                                                                                               |

### 1.1 Confidentiality Notice

```text
<Insert confidentiality notice, distribution restrictions, data handling requirements, and client-specific report handling instructions.>
```

---

## 2. Document Control

| Version        | Date           | Author     | Reviewer     | Change Summary     |
| -------------- | -------------- | ---------- | ------------ | ------------------ |
| `<0.1 Draft>`  | `<YYYY-MM-DD>` | `<author>` | `<reviewer>` | `<initial_draft>`  |
| `<1.0 Final>`  | `<YYYY-MM-DD>` | `<author>` | `<reviewer>` | `<final_report>`   |
| `<1.1 Retest>` | `<YYYY-MM-DD>` | `<author>` | `<reviewer>` | `<retest_updates>` |

### 2.1 Distribution Restrictions

```text
<Describe who may receive, store, copy, transmit, or reference this report. Include any client-specific restrictions.>
```

---

## 3. Legal Authorization and Scope Statement

### 3.1 Authorization Statement

```text
<Describe the written authorization for the assessment, including contract/SOW reference, letter of engagement reference, approved targets, approved testing dates, and legal boundaries.>
```

### 3.2 Scope Summary

| Scope Item                      | Value                               |
| ------------------------------- | ----------------------------------- |
| Contract / SOW Reference        | `<contract_or_sow_reference>`       |
| Letter of Engagement Reference  | `<letter_of_engagement_reference>`  |
| Approved Testing Dates          | `<approved_testing_dates>`          |
| Approved Testing Window         | `<testing_window>`                  |
| Authorized Targets              | `<targets>`                         |
| Excluded Targets                | `<excluded_targets>`                |
| Authorized Source IPs           | `<source_ips>`                      |
| Emergency Contact               | `<emergency_contact>`               |
| Escalation Contact              | `<escalation_contact>`              |
| Data Handling Requirements      | `<data_handling_requirements>`      |
| Evidence Retention Requirements | `<evidence_retention_requirements>` |

### 3.3 Prohibited Actions

* [ ] Testing outside the approved scope
* [ ] Attacking third-party infrastructure
* [ ] Denial-of-service testing unless explicitly authorized
* [ ] Destructive testing
* [ ] Persistence outside approved lab or test objectives
* [ ] Stealth or evasion against real monitoring systems
* [ ] Malware deployment
* [ ] Credential theft against third parties
* [ ] Accessing, copying, or exfiltrating sensitive data beyond approved proof requirements
* [ ] Modifying production data unless explicitly authorized

---

## 4. Executive Summary

### 4.1 Plain-Language Summary

```text
<Provide a concise, non-technical summary of the engagement, overall risk, primary attack paths, most important findings, business impact, and recommended next actions.>
```

### 4.2 Overall Metrics

| Metric                 | Value                              |
| ---------------------- | ---------------------------------- |
| Overall Risk           | `<Critical / High / Medium / Low>` |
| Critical Findings      | `<count>`                          |
| High Findings          | `<count>`                          |
| Medium Findings        | `<count>`                          |
| Low Findings           | `<count>`                          |
| Informational Findings | `<count>`                          |
| Total Findings         | `<count>`                          |
| Confirmed Attack Paths | `<count>`                          |
| Retest Recommended     | `<Yes / No>`                       |

### 4.3 Key Business Risks

| Risk              | Business Impact | Related Finding(s) | Recommended Action     |
| ----------------- | --------------- | ------------------ | ---------------------- |
| `<business_risk>` | `<impact>`      | `<finding_ids>`    | `<recommended_action>` |

### 4.4 Primary Attack Paths

| Attack Path ID | Summary                 | Business Impact     | Evidence         |
| -------------- | ----------------------- | ------------------- | ---------------- |
| `<AP-001>`     | `<attack_path_summary>` | `<business_impact>` | `<evidence_ids>` |

### 4.5 Most Critical Findings

| Finding ID     | Title             | Severity     | Affected Asset(s)   | Business Impact     |
| -------------- | ----------------- | ------------ | ------------------- | ------------------- |
| `<finding_id>` | `<finding_title>` | `<severity>` | `<affected_assets>` | `<business_impact>` |

### 4.6 Positive Security Observations

| Observation              | Evidence        | Security Value     |
| ------------------------ | --------------- | ------------------ |
| `<positive_observation>` | `<evidence_id>` | `<security_value>` |

### 4.7 Recommended Immediate Actions

* [ ] `<immediate_action_1>`
* [ ] `<immediate_action_2>`
* [ ] `<immediate_action_3>`

### 4.8 Strategic Remediation Themes

* [ ] `<strategic_theme_1>`
* [ ] `<strategic_theme_2>`
* [ ] `<strategic_theme_3>`

### 4.9 Residual Risk

```text
<Describe risk that may remain after immediate remediation, compensating controls, or accepted-risk decisions.>
```

---

## 5. Business Impact Summary

### 5.1 Impact Narrative

```text
<Explain the business impact of the confirmed findings and validated attack paths. Separate confirmed impact from potential impact.>
```

### 5.2 Business Impact Table

| Business Risk          | Impact                 | Evidence        | Recommended Action     |
| ---------------------- | ---------------------- | --------------- | ---------------------- |
| Confidentiality Impact | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Integrity Impact       | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Availability Impact    | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Operational Impact     | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Regulatory Impact      | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Financial Impact       | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Customer Impact        | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Third-Party Impact     | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Reputational Impact    | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |

---

## 6. Engagement Objectives

### 6.1 Primary Objectives

* [ ] Determine external attack surface exposure.
* [ ] Validate exploitability of network-facing services.
* [ ] Assess internal lateral movement risk.
* [ ] Identify privilege escalation paths.
* [ ] Evaluate segmentation controls.
* [ ] Assess Active Directory exposure.
* [ ] Validate security monitoring and response opportunities.
* [ ] Provide prioritized remediation guidance.

### 6.2 Secondary Objectives

* [ ] `<secondary_objective_1>`
* [ ] `<secondary_objective_2>`
* [ ] `<secondary_objective_3>`

### 6.3 Security Questions

| Question ID | Security Question     | Answer Summary     | Evidence         |
| ----------- | --------------------- | ------------------ | ---------------- |
| `<Q-001>`   | `<security_question>` | `<answer_summary>` | `<evidence_ids>` |

### 6.4 Success Criteria

| Criterion             | Status                            | Evidence        |
| --------------------- | --------------------------------- | --------------- |
| `<success_criterion>` | `<met / partially_met / not_met>` | `<evidence_id>` |

### 6.5 Deliverables

| Deliverable         | Status                                  | Notes     |
| ------------------- | --------------------------------------- | --------- |
| Executive report    | `<complete / pending / not_applicable>` | `<notes>` |
| Technical report    | `<complete / pending / not_applicable>` | `<notes>` |
| Findings register   | `<complete / pending / not_applicable>` | `<notes>` |
| Evidence package    | `<complete / pending / not_applicable>` | `<notes>` |
| Retest plan         | `<complete / pending / not_applicable>` | `<notes>` |
| Remediation roadmap | `<complete / pending / not_applicable>` | `<notes>` |

---

## 7. Assessment Methodology

### 7.1 Methodology Phases

| Phase                             | Objective     | Activities Performed | Evidence        |
| --------------------------------- | ------------- | -------------------- | --------------- |
| Pre-Engagement Review             | `<objective>` | `<activities>`       | `<evidence_id>` |
| Scope Validation                  | `<objective>` | `<activities>`       | `<evidence_id>` |
| Reconnaissance                    | `<objective>` | `<activities>`       | `<evidence_id>` |
| Host Discovery                    | `<objective>` | `<activities>`       | `<evidence_id>` |
| Port and Service Enumeration      | `<objective>` | `<activities>`       | `<evidence_id>` |
| Vulnerability Identification      | `<objective>` | `<activities>`       | `<evidence_id>` |
| Vulnerability Validation          | `<objective>` | `<activities>`       | `<evidence_id>` |
| Exploitation Validation           | `<objective>` | `<activities>`       | `<evidence_id>` |
| Privilege Escalation Validation   | `<objective>` | `<activities>`       | `<evidence_id>` |
| Lateral Movement Validation       | `<objective>` | `<activities>`       | `<evidence_id>` |
| Post-Exploitation Impact Analysis | `<objective>` | `<activities>`       | `<evidence_id>` |
| Cleanup                           | `<objective>` | `<activities>`       | `<evidence_id>` |
| Reporting                         | `<objective>` | `<activities>`       | `<evidence_id>` |
| Retest Planning                   | `<objective>` | `<activities>`       | `<evidence_id>` |

### 7.2 Methodology Flow

```text
[Pre-Engagement Review]
        |
        v
[Scope Validation]
        |
        v
[Reconnaissance]
        |
        v
[Discovery + Enumeration]
        |
        v
[Vulnerability Identification]
        |
        v
[Safe Validation]
        |
        v
[Attack Path Analysis]
        |
        v
[Impact Analysis]
        |
        v
[Cleanup]
        |
        v
[Reporting + Remediation Roadmap]
        |
        v
[Retest Planning]
```

---

## 8. Rules of Engagement

### 8.1 ROE Summary

| Rule Area                                  | Requirement                                  |
| ------------------------------------------ | -------------------------------------------- |
| Testing Windows                            | `<testing_windows>`                          |
| Rate Limits                                | `<rate_limits>`                              |
| Denial-of-Service Restrictions             | `<dos_restrictions>`                         |
| Credential Testing Limits                  | `<credential_testing_limits>`                |
| Password Spraying Restrictions             | `<password_spraying_restrictions>`           |
| Phishing / Social Engineering Restrictions | `<phishing_social_engineering_restrictions>` |
| Exploit Validation Limits                  | `<exploit_validation_limits>`                |
| Data Exfiltration Limits                   | `<data_exfiltration_limits>`                 |
| Production Safety Requirements             | `<production_safety_requirements>`           |
| Notification Requirements                  | `<notification_requirements>`                |
| Stop Conditions                            | `<stop_conditions>`                          |
| Cleanup Requirements                       | `<cleanup_requirements>`                     |

### 8.2 ROE Checklist

* [ ] Scope confirmed before testing
* [ ] Testing windows observed
* [ ] Source IPs approved
* [ ] Emergency contacts confirmed
* [ ] Rate limits followed
* [ ] Sensitive data access minimized
* [ ] Evidence redacted
* [ ] Production safety restrictions followed
* [ ] Client notified of critical findings
* [ ] Cleanup completed
* [ ] Final evidence package handled according to requirements

---

## 9. Environment and Tooling

### 9.1 Tester Environment

| Field                   | Value                     |
| ----------------------- | ------------------------- |
| Tester Workstation      | `<tester_workstation>`    |
| Operating System        | `<tester_os>`             |
| VPN / Jump Host         | `<vpn_or_jump_host>`      |
| Authorized Source IPs   | `<source_ips>`            |
| Working Directory       | `<working_directory>`     |
| Packet Capture Location | `<pcap_path>`             |
| Logging Configuration   | `<logging_configuration>` |

### 9.2 Tools Used

| Tool          | Version     | Purpose     | Output Path     |
| ------------- | ----------- | ----------- | --------------- |
| `<tool_name>` | `<version>` | `<purpose>` | `<output_path>` |

### 9.3 Wordlists

| Wordlist          | Path              | Purpose     |
| ----------------- | ----------------- | ----------- |
| `<wordlist_name>` | `<wordlist_path>` | `<purpose>` |

### 9.4 Scanner Policies

| Scanner     | Policy Name     | Authenticated? | Scope     | Notes     |
| ----------- | --------------- | -------------- | --------- | --------- |
| `<scanner>` | `<policy_name>` | `<Yes / No>`   | `<scope>` | `<notes>` |

### 9.5 Tool Version Commands

```bash
<tool_version_commands>
```

```text
<tool_version_output>
```

---

## 10. Scope Inventory

### 10.1 External Scope

| Asset     | Type                                                                   | IP / Hostname      | In Scope               | Notes     |
| --------- | ---------------------------------------------------------------------- | ------------------ | ---------------------- | --------- |
| `<asset>` | `<public_ip / hostname / application / cloud_edge / vpn / mail / dns>` | `<ip_or_hostname>` | `<Yes / No / Partial>` | `<notes>` |

### 10.2 Internal Scope

| Network Range     | VLAN / Segment      | Purpose     | In Scope               | Notes     |
| ----------------- | ------------------- | ----------- | ---------------------- | --------- |
| `<network_range>` | `<vlan_or_segment>` | `<purpose>` | `<Yes / No / Partial>` | `<notes>` |

### 10.3 Active Directory Scope

| Domain     | Domain Controller(s)   | Trusts     | In Scope               | Notes     |
| ---------- | ---------------------- | ---------- | ---------------------- | --------- |
| `<domain>` | `<domain_controllers>` | `<trusts>` | `<Yes / No / Partial>` | `<notes>` |

### 10.4 Wireless / VPN Scope

| Asset     | Type               | SSID / VPN Profile      | In Scope               | Notes     |
| --------- | ------------------ | ----------------------- | ---------------------- | --------- |
| `<asset>` | `<wireless / vpn>` | `<ssid_or_vpn_profile>` | `<Yes / No / Partial>` | `<notes>` |

---

## 11. Attack Surface Summary

### 11.1 Summary

```text
<Summarize discovered hosts, exposed services, remote access services, administrative interfaces, legacy protocols, high-value systems, and notable security control observations.>
```

### 11.2 Attack Surface Table

| Asset     | Open Ports     | Services     | Exposure                                              | Risk Notes     |
| --------- | -------------- | ------------ | ----------------------------------------------------- | -------------- |
| `<asset>` | `<open_ports>` | `<services>` | `<internet-facing / internal / restricted / unknown>` | `<risk_notes>` |

### 11.3 Notable Exposure Categories

| Category                      | Observed?    | Evidence        | Notes     |
| ----------------------------- | ------------ | --------------- | --------- |
| Internet-Facing Systems       | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Remote Access Services        | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Administrative Interfaces     | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Legacy Protocols              | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Cleartext Protocols           | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Exposed Databases             | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Exposed File Shares           | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Authentication Services       | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| High-Value Systems            | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Security Control Observations | `<Yes / No>` | `<evidence_id>` | `<notes>` |

---

## 12. Reconnaissance and Discovery Results

### 12.1 Passive Reconnaissance

```bash
<passive_recon_command>
```

```text
<passive_recon_output>
```

### 12.2 DNS Enumeration

```bash
<dns_enumeration_command>
```

```text
<dns_enumeration_output>
```

### 12.3 WHOIS / ASN Review

```bash
<whois_asn_command>
```

```text
<whois_asn_output>
```

### 12.4 Certificate Transparency Review

```bash
<certificate_transparency_command>
```

```text
<certificate_transparency_output>
```

### 12.5 Subdomain Discovery

```bash
<subdomain_discovery_command>
```

```text
<subdomain_discovery_output>
```

### 12.6 IP Range Discovery

```bash
<ip_range_discovery_command>
```

```text
<ip_range_discovery_output>
```

### 12.7 Host Discovery

```bash
<host_discovery_command>
```

```text
<host_discovery_output>
```

### 12.8 Reverse DNS

```bash
<reverse_dns_command>
```

```text
<reverse_dns_output>
```

### 12.9 Internal Discovery

```bash
<internal_discovery_command>
```

```text
<internal_discovery_output>
```

### 12.10 Network Path / Traceroute Observations

```bash
<network_path_command>
```

```text
<network_path_output>
```

### 12.11 Discovery Findings Table

| Discovery Area     | Key Observation     | Evidence ID     | Security Relevance     |
| ------------------ | ------------------- | --------------- | ---------------------- |
| `<discovery_area>` | `<key_observation>` | `<evidence_id>` | `<security_relevance>` |

---

## 13. Port and Service Enumeration

### 13.1 Enumeration Summary

```text
<Summarize open ports, exposed services, version information, high-risk protocols, and notable service-level observations.>
```

### 13.2 Port and Service Table

| Host     |     Port | Protocol      | Service     | Version     | Evidence        | Notes     |
| -------- | -------: | ------------- | ----------- | ----------- | --------------- | --------- |
| `<host>` | `<port>` | `<tcp / udp>` | `<service>` | `<version>` | `<evidence_id>` | `<notes>` |

### 13.3 TCP Services

```bash
<tcp_enumeration_command>
```

```text
<tcp_enumeration_output>
```

### 13.4 UDP Services

```bash
<udp_enumeration_command>
```

```text
<udp_enumeration_output>
```

### 13.5 IPv6 Services

```bash
<ipv6_enumeration_command>
```

```text
<ipv6_enumeration_output>
```

### 13.6 Remote Access Services

| Host     | Service     |     Port | Authentication Observed | Risk Notes     | Evidence        |
| -------- | ----------- | -------: | ----------------------- | -------------- | --------------- |
| `<host>` | `<service>` | `<port>` | `<auth_observed>`       | `<risk_notes>` | `<evidence_id>` |

### 13.7 Web Management Interfaces

| Host     | URL     | Product / Version   | Auth Required          | Risk Notes     | Evidence        |
| -------- | ------- | ------------------- | ---------------------- | -------------- | --------------- |
| `<host>` | `<url>` | `<product_version>` | `<Yes / No / Unknown>` | `<risk_notes>` | `<evidence_id>` |

### 13.8 File-Sharing Services

| Host     | Service                            | Shares / Exports      | Access Level     | Risk Notes     | Evidence        |
| -------- | ---------------------------------- | --------------------- | ---------------- | -------------- | --------------- |
| `<host>` | `<SMB / NFS / FTP / SFTP / other>` | `<shares_or_exports>` | `<access_level>` | `<risk_notes>` | `<evidence_id>` |

### 13.9 Directory Services

| Host     | Service                          |     Port | Signing / Encryption          | Risk Notes     | Evidence        |
| -------- | -------------------------------- | -------: | ----------------------------- | -------------- | --------------- |
| `<host>` | `<LDAP / Kerberos / GC / other>` | `<port>` | `<signing_encryption_status>` | `<risk_notes>` | `<evidence_id>` |

### 13.10 Database Services

| Host     | Service              |     Port | Exposure     | Risk Notes     | Evidence        |
| -------- | -------------------- | -------: | ------------ | -------------- | --------------- |
| `<host>` | `<database_service>` | `<port>` | `<exposure>` | `<risk_notes>` | `<evidence_id>` |

### 13.11 Email Services

| Host     | Service                          |     Port | Security Observations | Evidence        |
| -------- | -------------------------------- | -------: | --------------------- | --------------- |
| `<host>` | `<smtp / imap / pop3 / webmail>` | `<port>` | `<observations>`      | `<evidence_id>` |

### 13.12 Network Device Services

| Host     | Device Type                                                  | Management Service | Exposure     | Evidence        |
| -------- | ------------------------------------------------------------ | ------------------ | ------------ | --------------- |
| `<host>` | `<firewall / router / switch / load_balancer / vpn / other>` | `<service>`        | `<exposure>` | `<evidence_id>` |

### 13.13 Industrial / OT Services, If Applicable

| Host     | Protocol     |     Port | Asset Type     | Risk Notes     | Evidence        |
| -------- | ------------ | -------: | -------------- | -------------- | --------------- |
| `<host>` | `<protocol>` | `<port>` | `<asset_type>` | `<risk_notes>` | `<evidence_id>` |

---

## 14. Vulnerability Validation Summary

### 14.1 Summary

```text
<Summarize scanner findings, manual validation, false positives removed, confirmed vulnerabilities, unvalidated vulnerabilities, environmental constraints, and exploitability notes.>
```

### 14.2 Vulnerability Validation Table

| Vulnerability     | Asset     | Source                                              | Validation Method     | Status                                                  | Evidence        |
| ----------------- | --------- | --------------------------------------------------- | --------------------- | ------------------------------------------------------- | --------------- |
| `<vulnerability>` | `<asset>` | `<scanner / manual / config_review / service_enum>` | `<validation_method>` | `<confirmed / false_positive / unvalidated / accepted>` | `<evidence_id>` |

### 14.3 Scanner Findings

| Scanner Finding     | Asset     | Scanner Severity | Validation Status                            | Notes     |
| ------------------- | --------- | ---------------- | -------------------------------------------- | --------- |
| `<scanner_finding>` | `<asset>` | `<severity>`     | `<confirmed / false_positive / unvalidated>` | `<notes>` |

### 14.4 Manual Validation Notes

```text
<Describe how findings were safely validated without destructive actions or unauthorized access.>
```

### 14.5 False Positives Removed

| Finding     | Reason Removed | Evidence        |
| ----------- | -------------- | --------------- |
| `<finding>` | `<reason>`     | `<evidence_id>` |

### 14.6 Environmental Constraints

| Constraint     | Impact     | Notes     |
| -------------- | ---------- | --------- |
| `<constraint>` | `<impact>` | `<notes>` |

---

## 15. Attack Path Narrative

### 15.1 Attack Path Summary

```text
Attack Path <ID>:
<initial_access_condition>
  -> <validated_weakness>
  -> <privilege_or_access_gain>
  -> <business_impact>
```

### 15.2 Attack Path Table

| Step | Action     | Result     | Evidence        | Risk     |
| ---: | ---------- | ---------- | --------------- | -------- |
|  `1` | `<action>` | `<result>` | `<evidence_id>` | `<risk>` |
|  `2` | `<action>` | `<result>` | `<evidence_id>` | `<risk>` |
|  `3` | `<action>` | `<result>` | `<evidence_id>` | `<risk>` |

### 15.3 Attack Path Metadata

| Field                          | Value                              |
| ------------------------------ | ---------------------------------- |
| Attack Path ID                 | `<AP-001>`                         |
| Preconditions                  | `<preconditions>`                  |
| Initial Access Condition       | `<initial_access_condition>`       |
| Access Level Gained            | `<access_level_gained>`            |
| Lateral Movement Potential     | `<lateral_movement_potential>`     |
| Privilege Escalation Potential | `<privilege_escalation_potential>` |
| Sensitive Data Exposure Risk   | `<sensitive_data_exposure_risk>`   |
| Business Impact                | `<business_impact>`                |
| Detection Opportunities        | `<detection_opportunities>`        |
| Cleanup Performed              | `<Yes / No / Not Applicable>`      |

### 15.4 Attack Path Diagram

```text
<Initial Exposure>
        |
        v
<Weak Service / Misconfiguration / Vulnerability>
        |
        v
<Validated Access or Control>
        |
        v
<Privilege Increase or Expanded Reach>
        |
        v
<Business Impact>
```

---

## 16. Findings Summary

| ID             | Finding Title     | Severity                                           | Confidence              | Affected Asset(s)   | Status                                                                                         |
| -------------- | ----------------- | -------------------------------------------------- | ----------------------- | ------------------- | ---------------------------------------------------------------------------------------------- |
| `<finding_id>` | `<finding_title>` | `<Informational / Low / Medium / High / Critical>` | `<Low / Medium / High>` | `<affected_assets>` | `<Open / Fixed / Partially Fixed / Accepted Risk / False Positive / Duplicate / Needs Retest>` |

---

## 17. Detailed Finding Template

## Finding `<finding_id>`: `<finding_title>`

| Field               | Value                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| Severity            | `<Informational / Low / Medium / High / Critical>`                                             |
| Confidence          | `<Low / Medium / High>`                                                                        |
| Status              | `<Open / Fixed / Partially Fixed / Accepted Risk / False Positive / Duplicate / Needs Retest>` |
| Affected Asset(s)   | `<affected_assets>`                                                                            |
| Affected Service(s) | `<affected_services>`                                                                          |
| Affected Port(s)    | `<affected_ports>`                                                                             |
| CVSS                | `<vector_score>`                                                                               |
| CWE                 | `<CWE-ID>`                                                                                     |
| MITRE ATT&CK        | `<technique_id_if_applicable>`                                                                 |
| CIS Controls        | `<cis_control_mapping>`                                                                        |
| NIST CSF            | `<nist_csf_mapping>`                                                                           |
| Evidence IDs        | `<evidence_ids>`                                                                               |
| Related Attack Path | `<attack_path_id>`                                                                             |

### 17.1 Executive Description

```text
<Explain the issue in plain business language. Describe why it matters and what risk it creates.>
```

### 17.2 Technical Description

```text
<Explain the technical weakness, affected service, configuration, or vulnerability.>
```

### 17.3 Facts

| Fact ID      | Fact               | Evidence        | Confidence              |
| ------------ | ------------------ | --------------- | ----------------------- |
| `<FACT-001>` | `<confirmed_fact>` | `<evidence_id>` | `<Low / Medium / High>` |

### 17.4 Evidence

```text
<sanitized_evidence>
```

### 17.5 Safe Reproduction / Validation Steps

1. `<step_1>`
2. `<step_2>`
3. `<step_3>`

### 17.6 Validation Output

```text
<sanitized_validation_output>
```

### 17.7 Impact

```text
<Describe technical and business impact. Separate confirmed impact from potential impact.>
```

### 17.8 Likelihood

```text
<Describe exploitability, preconditions, exposure, required access, and attacker effort.>
```

### 17.9 Root Cause

```text
<Describe the underlying configuration, patching, design, process, or control failure.>
```

### 17.10 Remediation

```text
<Provide direct remediation steps, including tactical fix and strategic improvement.>
```

### 17.11 Detection Opportunities

```text
<Describe logs, telemetry, alert logic, or monitoring opportunities.>
```

### 17.12 Retest Procedure

```text
<Describe how to safely verify remediation.>
```

### 17.13 References

| Reference     | Description     |
| ------------- | --------------- |
| `<reference>` | `<description>` |

---

## 18. Active Directory Assessment Section, If Applicable

### 18.1 Domain Overview

| Field              | Value                  |
| ------------------ | ---------------------- |
| Domain             | `<domain>`             |
| Forest             | `<forest>`             |
| Domain Controllers | `<domain_controllers>` |
| Functional Level   | `<functional_level>`   |
| Trusts             | `<trusts>`             |
| Assessment Method  | `<method>`             |

### 18.2 Active Directory Finding Areas

| AD Finding Area                     | Observation     | Risk     | Evidence        | Recommendation     |
| ----------------------------------- | --------------- | -------- | --------------- | ------------------ |
| Domain Controllers                  | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Forest / Domain Trusts              | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Privileged Groups                   | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Kerberos Exposure                   | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| LDAP / SMB Signing                  | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Password Policy                     | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Account Lockout Policy              | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Local Administrator Exposure        | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Kerberoasting Risk                  | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| AS-REP Roasting Risk                | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Delegation Risk                     | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| GPO Weaknesses                      | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| ACL Abuse Paths                     | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Admin Session Exposure              | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Credential Exposure                 | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| BloodHound / Graph Analysis Summary | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |

---

## 19. Internal Network Assessment Section, If Applicable

### 19.1 Internal Network Summary

```text
<Summarize internal network posture, segmentation, reachable services, trust assumptions, and lateral movement risk.>
```

### 19.2 Internal Assessment Areas

| Area                                     | Observation     | Risk     | Evidence        | Recommendation     |
| ---------------------------------------- | --------------- | -------- | --------------- | ------------------ |
| Network Segmentation                     | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| VLAN / Segment Access                    | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Internal Trust Assumptions               | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Exposed Management Services              | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Lateral Movement Paths                   | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Cleartext Protocols                      | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Name Resolution Poisoning Risk           | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Patch Posture                            | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| File Share Exposure                      | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Local Privilege Escalation Opportunities | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Sensitive Data Exposure                  | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Excessive Permissions                    | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |

---

## 20. External Network Assessment Section, If Applicable

### 20.1 External Network Summary

```text
<Summarize internet-facing exposure, public services, remote access exposure, edge security posture, and critical risks.>
```

### 20.2 External Assessment Areas

| Area                            | Observation     | Risk     | Evidence        | Recommendation     |
| ------------------------------- | --------------- | -------- | --------------- | ------------------ |
| Public IP Exposure              | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Internet-Facing Services        | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Remote Access Exposure          | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| VPN Exposure                    | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| TLS Posture                     | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Email Security Posture          | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| DNS Posture                     | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Exposed Administrative Panels   | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Cloud Edge Exposure             | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Known Exploited Vulnerabilities | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Patch Posture                   | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |

---

## 21. Wireless / VPN Assessment Section, If Applicable

### 21.1 Wireless / VPN Summary

```text
<Summarize wireless or VPN security posture, authentication model, encryption, MFA, client isolation, monitoring, and access control observations.>
```

### 21.2 Wireless / VPN Assessment Areas

| Area                          | Observation     | Risk     | Evidence        | Recommendation     |
| ----------------------------- | --------------- | -------- | --------------- | ------------------ |
| SSIDs / VPN Profiles Reviewed | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Authentication Method         | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Encryption Method             | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Certificate Validation        | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Split Tunneling               | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| MFA Enforcement               | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Client Isolation              | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Rogue AP Observations         | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Signal Exposure               | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Access Control Observations   | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Logging and Monitoring        | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |

---

## 22. Security Control Observations

| Control                  | Observation     | Effectiveness                                                    | Recommendation     |
| ------------------------ | --------------- | ---------------------------------------------------------------- | ------------------ |
| Firewall                 | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| IDS / IPS                | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| EDR                      | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| SIEM / Logging           | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| WAF                      | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| NAC                      | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Network Segmentation     | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| MFA                      | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Patch Management         | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Vulnerability Management | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Backup / Recovery        | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |

---

## 23. Risk Rating Methodology

### 23.1 Severity Model

| Severity      | Definition     |
| ------------- | -------------- |
| Critical      | `<definition>` |
| High          | `<definition>` |
| Medium        | `<definition>` |
| Low           | `<definition>` |
| Informational | `<definition>` |

### 23.2 Confidence Model

| Confidence | Definition     |
| ---------- | -------------- |
| High       | `<definition>` |
| Medium     | `<definition>` |
| Low        | `<definition>` |

### 23.3 Likelihood Factors

| Factor                      | Description     |
| --------------------------- | --------------- |
| Exposure                    | `<description>` |
| Exploitability              | `<description>` |
| Required Access             | `<description>` |
| Attack Complexity           | `<description>` |
| Existing Controls           | `<description>` |
| Public Exploit Availability | `<description>` |
| Required User Interaction   | `<description>` |

### 23.4 Impact Factors

| Factor                 | Description     |
| ---------------------- | --------------- |
| Confidentiality        | `<description>` |
| Integrity              | `<description>` |
| Availability           | `<description>` |
| Business Criticality   | `<description>` |
| Regulatory Exposure    | `<description>` |
| Operational Disruption | `<description>` |

### 23.5 Environmental Modifiers

| Modifier               | Description     |
| ---------------------- | --------------- |
| Asset Criticality      | `<description>` |
| Compensating Controls  | `<description>` |
| Network Segmentation   | `<description>` |
| Monitoring Visibility  | `<description>` |
| Remediation Complexity | `<description>` |

---

## 24. Remediation Roadmap

### 24.1 Prioritized Roadmap

| Priority              | Finding ID     | Remediation     | Owner     | Effort                  | Target Date    | Risk Reduction     |
| --------------------- | -------------- | --------------- | --------- | ----------------------- | -------------- | ------------------ |
| `<P0 / P1 / P2 / P3>` | `<finding_id>` | `<remediation>` | `<owner>` | `<Low / Medium / High>` | `<YYYY-MM-DD>` | `<risk_reduction>` |

### 24.2 Immediate Actions

* [ ] `<immediate_action_1>`
* [ ] `<immediate_action_2>`
* [ ] `<immediate_action_3>`

### 24.3 30-Day Actions

* [ ] `<30_day_action_1>`
* [ ] `<30_day_action_2>`
* [ ] `<30_day_action_3>`

### 24.4 60-Day Actions

* [ ] `<60_day_action_1>`
* [ ] `<60_day_action_2>`
* [ ] `<60_day_action_3>`

### 24.5 90-Day Actions

* [ ] `<90_day_action_1>`
* [ ] `<90_day_action_2>`
* [ ] `<90_day_action_3>`

### 24.6 Strategic Improvements

* [ ] `<strategic_improvement_1>`
* [ ] `<strategic_improvement_2>`
* [ ] `<strategic_improvement_3>`

### 24.7 Process Improvements

* [ ] `<process_improvement_1>`
* [ ] `<process_improvement_2>`
* [ ] `<process_improvement_3>`

### 24.8 Long-Term Architecture Changes

* [ ] `<architecture_change_1>`
* [ ] `<architecture_change_2>`
* [ ] `<architecture_change_3>`

---

## 25. Detection and Monitoring Recommendations

### 25.1 Detection Opportunities

| Detection Opportunity     | Data Source     | Logic Summary     | Related Finding | Priority                |
| ------------------------- | --------------- | ----------------- | --------------- | ----------------------- |
| `<detection_opportunity>` | `<data_source>` | `<logic_summary>` | `<finding_id>`  | `<High / Medium / Low>` |

### 25.2 Monitoring Areas

* [ ] Authentication anomalies
* [ ] Privileged group changes
* [ ] Suspicious service access
* [ ] Lateral movement indicators
* [ ] Password spraying indicators
* [ ] Kerberos abuse indicators
* [ ] SMB / LDAP / RPC anomalies
* [ ] Remote administration activity
* [ ] Vulnerability exploitation attempts
* [ ] Data access anomalies
* [ ] New service creation
* [ ] Unusual network connections
* [ ] Administrative interface access
* [ ] Cloud audit events
* [ ] VPN anomalies

### 25.3 Detection Pseudocode Placeholder

```text
<insert vendor-neutral detection logic or SIEM rule placeholder>
```

---

## 26. Cleanup and Data Handling

### 26.1 Cleanup Summary

```text
<Describe cleanup actions performed after testing, including accounts, files, tools, temporary changes, sessions, credentials, and evidence handling.>
```

### 26.2 Cleanup Table

| Item                       | Location     | Action Taken     | Evidence        | Status                                  |
| -------------------------- | ------------ | ---------------- | --------------- | --------------------------------------- |
| Accounts Created           | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Files Uploaded             | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Tools Staged               | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Temporary Firewall Changes | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Test Data Created          | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Sessions Terminated        | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Credentials Handled        | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Sensitive Data Observed    | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Evidence Redaction         | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Evidence Storage           | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Evidence Deletion Schedule | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |

### 26.3 Evidence Redaction Guidance

* [ ] Redact passwords, tokens, API keys, private keys, and session identifiers.
* [ ] Redact personal data unless explicitly required for proof.
* [ ] Redact customer data and regulated data.
* [ ] Preserve enough context for validation.
* [ ] Store raw evidence only in approved restricted locations.
* [ ] Reference raw evidence by evidence ID when direct inclusion is inappropriate.

---

## 27. Retest Plan

### 27.1 Retest Scope

```text
<Describe which findings, assets, services, attack paths, or controls should be retested.>
```

### 27.2 Retest Table

| Finding ID     | Retest Step     | Expected Result     | Status                                      | Evidence        |
| -------------- | --------------- | ------------------- | ------------------------------------------- | --------------- |
| `<finding_id>` | `<retest_step>` | `<expected_result>` | `<not_started / passed / failed / partial>` | `<evidence_id>` |

### 27.3 Retest Methodology

```text
<Describe safe retest methodology, required access, test environment, validation criteria, and evidence requirements.>
```

### 27.4 Responsible Parties

| Role              | Name / Team  | Responsibility     |
| ----------------- | ------------ | ------------------ |
| Client Owner      | `<owner>`    | `<responsibility>` |
| Technical Owner   | `<owner>`    | `<responsibility>` |
| Retest Tester     | `<tester>`   | `<responsibility>` |
| Security Reviewer | `<reviewer>` | `<responsibility>` |

---

## 28. Evidence Index

| Evidence ID     | Description     | Type                                                                                                                                                                                               | Path / Link      | Timestamp     | Related Finding |
| --------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------- | --------------- |
| `<evidence_id>` | `<description>` | `<screenshot / terminal_output / scanner_output / packet_capture / HTTP_request_response / log_entry / configuration_snippet / exploit_validation_output / AD_graph_output / client_confirmation>` | `<path_or_link>` | `<timestamp>` | `<finding_id>`  |

### 28.1 Evidence Storage Layout

```text
<evidence_root>/
├── 00_scope/
├── 01_recon/
├── 02_discovery/
├── 03_enumeration/
├── 04_vulnerability_validation/
├── 05_attack_paths/
├── 06_findings/
├── 07_screenshots/
├── 08_tool_output/
├── 09_packet_captures/
├── 10_cleanup/
├── 11_retest/
└── 12_report/
```

---

## 29. Screenshot Index

| Screenshot ID     | Description     | Path                | Related Finding |
| ----------------- | --------------- | ------------------- | --------------- |
| `<screenshot_id>` | `<description>` | `<screenshot_path>` | `<finding_id>`  |

### 29.1 Screenshot Placeholder

```markdown
![<description>](<screenshot_path>)
```

---

## 30. Tool Output Appendix

### 30.1 Nmap Output

```text
<sanitized_nmap_output>
```

### 30.2 Vulnerability Scanner Output Summary

```text
<sanitized_nessus_openvas_qualys_output_summary>
```

### 30.3 SMB Enumeration Output

```text
<sanitized_smb_enumeration_output>
```

### 30.4 LDAP Enumeration Output

```text
<sanitized_ldap_enumeration_output>
```

### 30.5 DNS Enumeration Output

```text
<sanitized_dns_enumeration_output>
```

### 30.6 Active Directory Enumeration Output

```text
<sanitized_ad_enumeration_output>
```

### 30.7 Packet Capture References

| PCAP ID     | Description     | Path          | Related Finding |
| ----------- | --------------- | ------------- | --------------- |
| `<pcap_id>` | `<description>` | `<pcap_path>` | `<finding_id>`  |

### 30.8 Manual Validation Logs

```text
<sanitized_manual_validation_logs>
```

---

## 31. Limitations

### 31.1 Assessment Limitations

| Limitation                     | Impact     | Notes     |
| ------------------------------ | ---------- | --------- |
| Scope Limitations              | `<impact>` | `<notes>` |
| Time Limitations               | `<impact>` | `<notes>` |
| Credential Limitations         | `<impact>` | `<notes>` |
| Testing Window Limitations     | `<impact>` | `<notes>` |
| Production Safety Restrictions | `<impact>` | `<notes>` |
| Network Filtering Constraints  | `<impact>` | `<notes>` |
| Unreachable Targets            | `<impact>` | `<notes>` |
| Unvalidated Findings           | `<impact>` | `<notes>` |
| Assumptions                    | `<impact>` | `<notes>` |

### 31.2 Unreachable or Untested Assets

| Asset     | Reason Not Tested | Risk     | Recommendation     |
| --------- | ----------------- | -------- | ------------------ |
| `<asset>` | `<reason>`        | `<risk>` | `<recommendation>` |

---

## 32. Appendix: Terms and Definitions

| Term                 | Definition     |
| -------------------- | -------------- |
| Exploitability       | `<definition>` |
| Exposure             | `<definition>` |
| Attack Path          | `<definition>` |
| Vulnerability        | `<definition>` |
| Risk                 | `<definition>` |
| Threat               | `<definition>` |
| Impact               | `<definition>` |
| Likelihood           | `<definition>` |
| Compensating Control | `<definition>` |
| False Positive       | `<definition>` |
| Accepted Risk        | `<definition>` |
| Residual Risk        | `<definition>` |
| Privilege Escalation | `<definition>` |
| Lateral Movement     | `<definition>` |
| Segmentation         | `<definition>` |

---

## 33. Appendix: References

| Reference Type     | Reference                     | Notes     |
| ------------------ | ----------------------------- | --------- |
| Vendor Advisory    | `<vendor_advisory>`           | `<notes>` |
| CVE Reference      | `<cve_reference>`             | `<notes>` |
| CWE Reference      | `<cwe_reference>`             | `<notes>` |
| CVSS Calculator    | `<cvss_calculator_reference>` | `<notes>` |
| MITRE ATT&CK       | `<mitre_attack_reference>`    | `<notes>` |
| CIS Controls       | `<cis_controls_reference>`    | `<notes>` |
| NIST Guidance      | `<nist_guidance_reference>`   | `<notes>` |
| Tool Documentation | `<tool_documentation>`        | `<notes>` |
| Client Standard    | `<client_standard>`           | `<notes>` |
| Internal Policy    | `<internal_policy>`           | `<notes>` |

---

## 34. Appendix: Report Review Checklist

* [ ] Cover page complete
* [ ] Document control complete
* [ ] Authorization and scope documented
* [ ] Executive summary written for non-technical stakeholders
* [ ] Business impact documented
* [ ] Methodology documented
* [ ] Rules of engagement documented
* [ ] Environment and tooling documented
* [ ] Scope inventory complete
* [ ] Attack surface summarized
* [ ] Reconnaissance results documented
* [ ] Port and service enumeration documented
* [ ] Vulnerability validation documented
* [ ] Attack path narrative included where applicable
* [ ] Findings summary complete
* [ ] Detailed findings include evidence
* [ ] Detailed findings include severity and confidence
* [ ] Detailed findings include CVSS and mappings where relevant
* [ ] Remediation roadmap included
* [ ] Detection recommendations included
* [ ] Cleanup and data handling documented
* [ ] Retest plan included
* [ ] Evidence index complete
* [ ] Screenshot index complete
* [ ] Tool output sanitized
* [ ] Limitations documented
* [ ] References included
* [ ] Weaponized exploitation instructions excluded
* [ ] Sensitive evidence redacted
* [ ] Final report reviewed and approved

