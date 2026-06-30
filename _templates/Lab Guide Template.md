# Lab Writeup Template

> **Use Case:** Authorized offensive-security labs, CTF-style challenges, cyber ranges, penetration-testing exercises, exploit-development labs, reverse-engineering labs, web/API security labs, Active Directory labs, cloud labs, and vulnerability-research exercises.
> **Scope Boundary:** This template is for controlled, ethical, educational, defensive, or explicitly authorized lab environments only. Do not use it to document unauthorized access, real-world exploitation, credential theft against third parties, persistence, stealth, evasion, or misuse outside the approved lab scope.

---

## 1. Lab Metadata

| Field                      | Value                                                                                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lab Name                   | `<lab_name>`                                                                                                                                                                              |
| Platform                   | `<platform_name>`                                                                                                                                                                         |
| Lab Type                   | `<network_penetration_testing / web_application / API / Active_Directory / reverse_engineering / exploit_development / malware_analysis / cloud / wireless / mobile / mixed_environment>` |
| Difficulty                 | `<easy / medium / hard / expert / unknown>`                                                                                                                                               |
| Author / Instructor        | `<author_name>`                                                                                                                                                                           |
| Analyst / Student          | `<analyst_or_student_name>`                                                                                                                                                               |
| Date Started               | `<YYYY-MM-DD>`                                                                                                                                                                            |
| Date Completed             | `<YYYY-MM-DD>`                                                                                                                                                                            |
| Time Spent                 | `<time_spent>`                                                                                                                                                                            |
| Target IP / Hostname       | `<target_ip_or_hostname>`                                                                                                                                                                 |
| Target Operating System(s) | `<target_operating_systems>`                                                                                                                                                              |
| Attacker Machine           | `<attacker_machine>`                                                                                                                                                                      |
| Tools Used                 | `<tools_used>`                                                                                                                                                                            |
| Lab URL / Source           | `<lab_url_or_source>`                                                                                                                                                                     |
| Report Version             | `<report_version>`                                                                                                                                                                        |
| Evidence Root              | `<evidence_root_path>`                                                                                                                                                                    |
| Screenshot Root            | `<screenshot_root_path>`                                                                                                                                                                  |
| Notes Path                 | `<notes_path>`                                                                                                                                                                            |

### 1.1 Authorization / Scope Statement

```text
<Describe the authorized lab scope, target systems, approved activities, and boundaries. Confirm that all testing was performed in a controlled lab or explicitly authorized environment.>
```

### 1.2 Out-of-Scope Actions

* [ ] Attacking real systems
* [ ] Targeting third-party infrastructure
* [ ] Credential theft outside the lab
* [ ] Persistence outside the lab objective
* [ ] Stealth or evasion against real monitoring systems
* [ ] Destructive testing not required by the lab
* [ ] Exfiltration of non-lab data
* [ ] Testing outside assigned IP ranges, hostnames, accounts, or cloud resources

### 1.3 Reset / Snapshot Notes

```text
<Describe how the lab can be reset, restored, reverted, or snapshotted. Include VM snapshot names, cloud teardown steps, container reset commands, or platform reset instructions.>
```

---

## 2. Executive Summary

### 2.1 Summary

```text
<One-paragraph summary of the lab, target, methodology, primary weakness, final outcome, and security lesson. Write this so a non-technical stakeholder can understand the main result.>
```

### 2.2 Key Results

| Field                         | Value                                               |
| ----------------------------- | --------------------------------------------------- |
| Primary Objective             | `<primary_objective>`                               |
| Final Outcome                 | `<completed / partially_completed / not_completed>` |
| Key Attack Path               | `<high_level_attack_path>`                          |
| Main Vulnerability / Weakness | `<main_vulnerability_or_weakness>`                  |
| Impact Summary                | `<impact_summary>`                                  |
| Remediation Summary           | `<remediation_summary>`                             |
| Confidence Level              | `<Low / Medium / High>`                             |

### 2.3 Key Findings

| Finding ID   | Title             | Severity                                           | Confidence              | Affected Asset     | Status                                             |
| ------------ | ----------------- | -------------------------------------------------- | ----------------------- | ------------------ | -------------------------------------------------- |
| `<FIND-001>` | `<finding_title>` | `<Informational / Low / Medium / High / Critical>` | `<Low / Medium / High>` | `<affected_asset>` | `<Open / Validated / Remediated / Not Applicable>` |

---

## 3. Scope and Rules of Engagement

### 3.1 Authorized Targets

| Target          | Type                                                                                  | IP / Hostname / URL   | In Scope     | Notes     |
| --------------- | ------------------------------------------------------------------------------------- | --------------------- | ------------ | --------- |
| `<target_name>` | `<host / web_app / API / AD_domain / cloud_account / binary / firmware / mobile_app>` | `<target_identifier>` | `<Yes / No>` | `<notes>` |

### 3.2 Excluded Targets

| Target              | Reason Excluded | Notes     |
| ------------------- | --------------- | --------- |
| `<excluded_target>` | `<reason>`      | `<notes>` |

### 3.3 Allowed Techniques

* [ ] Passive reconnaissance
* [ ] Active reconnaissance
* [ ] Port scanning
* [ ] Service enumeration
* [ ] Web/API enumeration
* [ ] Directory/content discovery
* [ ] Source review
* [ ] Reverse engineering
* [ ] Debugging
* [ ] Fuzzing in lab
* [ ] Safe proof-of-concept validation
* [ ] Privilege escalation within lab scope
* [ ] Post-exploitation enumeration within lab scope
* [ ] Evidence collection
* [ ] Reporting and remediation mapping

### 3.4 Prohibited Techniques

* [ ] Testing outside assigned scope
* [ ] Attacking third-party systems
* [ ] Destructive actions not required by the lab
* [ ] Real-world credential theft
* [ ] Persistence outside the lab objective
* [ ] Stealth or evasion against real systems
* [ ] Data exfiltration outside lab proof requirements
* [ ] Denial-of-service unless explicitly authorized
* [ ] Malware deployment outside controlled malware-analysis labs

### 3.5 Operational Constraints

| Constraint                       | Value / Rule                         | Notes     |
| -------------------------------- | ------------------------------------ | --------- |
| Rate Limits                      | `<rate_limit_rules>`                 | `<notes>` |
| Credential Usage Rules           | `<credential_rules>`                 | `<notes>` |
| Destructive Testing Restrictions | `<destructive_testing_restrictions>` | `<notes>` |
| Data Handling Rules              | `<data_handling_rules>`              | `<notes>` |
| Cleanup Expectations             | `<cleanup_expectations>`             | `<notes>` |
| Reporting Requirements           | `<reporting_requirements>`           | `<notes>` |

---

## 4. Lab Objectives

### 4.1 Objective Summary

```text
<Describe the intended learning outcome, technical objective, and expected final proof.>
```

### 4.2 Objectives Table

| Objective ID | Objective     | Evidence Required     | Status                                             |
| ------------ | ------------- | --------------------- | -------------------------------------------------- |
| `<OBJ-001>`  | `<objective>` | `<evidence_required>` | `<Not Started / In Progress / Complete / Blocked>` |

### 4.3 Flags or Proof Requirements

| Proof ID     | Description                   | Location / Source | Captured?    | Evidence        |
| ------------ | ----------------------------- | ----------------- | ------------ | --------------- |
| `<FLAG-001>` | `<flag_or_proof_description>` | `<location>`      | `<Yes / No>` | `<evidence_id>` |

### 4.4 Success Criteria

* [ ] Primary objective completed
* [ ] Evidence captured
* [ ] Commands and outputs documented
* [ ] Root cause explained
* [ ] Impact explained
* [ ] Remediation documented
* [ ] Detection opportunities documented
* [ ] Lessons learned recorded
* [ ] Reproducibility verified

### 4.5 Expected Deliverables

| Deliverable       | Required     | Status     | Notes     |
| ----------------- | ------------ | ---------- | --------- |
| Lab writeup       | `<Yes / No>` | `<status>` | `<notes>` |
| Evidence archive  | `<Yes / No>` | `<status>` | `<notes>` |
| Screenshots       | `<Yes / No>` | `<status>` | `<notes>` |
| Safe PoC          | `<Yes / No>` | `<status>` | `<notes>` |
| Remediation notes | `<Yes / No>` | `<status>` | `<notes>` |
| Detection mapping | `<Yes / No>` | `<status>` | `<notes>` |

---

## 5. Environment Setup

### 5.1 Attacker Machine

| Field             | Value                                     |
| ----------------- | ----------------------------------------- |
| OS                | `<attacker_os>`                           |
| Hostname          | `<attacker_hostname>`                     |
| IP Address        | `<attacker_ip>`                           |
| VPN Interface     | `<vpn_interface>`                         |
| Working Directory | `<working_directory>`                     |
| Shell             | `<bash / zsh / PowerShell / cmd / other>` |

### 5.2 Target Machine(s)

| Target          | IP / Hostname             | OS            | Role     | Notes     |
| --------------- | ------------------------- | ------------- | -------- | --------- |
| `<target_name>` | `<target_ip_or_hostname>` | `<target_os>` | `<role>` | `<notes>` |

### 5.3 Network Configuration

| Field              | Value             |
| ------------------ | ----------------- |
| Network Range      | `<network_range>` |
| VPN Required       | `<Yes / No>`      |
| VPN Profile        | `<vpn_profile>`   |
| DNS Server         | `<dns_server>`    |
| Proxy Required     | `<Yes / No>`      |
| Proxy Address      | `<proxy_address>` |
| Hosts File Entries | `<hosts_entries>` |

### 5.4 VPN Configuration

```bash
<vpn_connection_command>
```

### 5.5 DNS / Hosts Entries

```text
<target_ip> <hostname>
<target_ip> <fqdn>
```

### 5.6 Browser / Proxy Setup

| Setting                  | Value                       |
| ------------------------ | --------------------------- |
| Browser                  | `<browser>`                 |
| Proxy                    | `<proxy_host>:<proxy_port>` |
| CA Certificate Installed | `<Yes / No>`                |
| Intercept Enabled        | `<Yes / No>`                |
| Scope Configured         | `<Yes / No>`                |

### 5.7 Debugger Setup

| Field          | Value                                                   |
| -------------- | ------------------------------------------------------- |
| Debugger       | `<gdb / lldb / x64dbg / WinDbg / Ghidra / IDA / other>` |
| Symbols Loaded | `<Yes / No / Partial>`                                  |
| Target Binary  | `<binary_path>`                                         |
| Breakpoints    | `<breakpoint_summary>`                                  |
| Snapshot       | `<snapshot_name>`                                       |

### 5.8 Wordlists

| Wordlist          | Path              | Purpose     |
| ----------------- | ----------------- | ----------- |
| `<wordlist_name>` | `<wordlist_path>` | `<purpose>` |

### 5.9 Tool Versions

```bash
<tool_version_commands>
```

### 5.10 Setup Commands

```bash
<setup_commands>
```

### 5.11 Setup Verification Output

```text
<setup_verification_output>
```

---

## 6. Initial Assumptions and Hypotheses

| ID          | Assumption / Hypothesis      | Basis     | Validation Method     | Result                                  |
| ----------- | ---------------------------- | --------- | --------------------- | --------------------------------------- |
| `<HYP-001>` | `<assumption_or_hypothesis>` | `<basis>` | `<validation_method>` | `<validated / rejected / inconclusive>` |

### 6.1 Facts

| Fact ID      | Fact               | Evidence        | Confidence              |
| ------------ | ------------------ | --------------- | ----------------------- |
| `<FACT-001>` | `<confirmed_fact>` | `<evidence_id>` | `<Low / Medium / High>` |

### 6.2 Evidence

| Evidence ID  | Description     | Source             | Path              | Notes     |
| ------------ | --------------- | ------------------ | ----------------- | --------- |
| `<EVID-001>` | `<description>` | `<tool_or_source>` | `<evidence_path>` | `<notes>` |

### 6.3 Hypotheses

| Hypothesis ID | Hypothesis     | Supporting Evidence | Test Method          | Status                                    |
| ------------- | -------------- | ------------------- | -------------------- | ----------------------------------------- |
| `<HYP-001>`   | `<hypothesis>` | `<evidence_id>`     | `<safe_test_method>` | `<Open / Testing / Confirmed / Rejected>` |

---

## 7. Methodology Overview

### 7.1 Methodology Flow

1. Reconnaissance
2. Enumeration
3. Vulnerability discovery
4. Vulnerability validation
5. Exploitation in lab
6. Privilege escalation, if applicable
7. Post-exploitation enumeration, if applicable
8. Evidence collection
9. Root-cause analysis
10. Remediation and detection mapping
11. Lessons learned

### 7.2 Methodology Diagram

```text
[Scope Review]
      |
      v
[Reconnaissance]
      |
      v
[Enumeration]
      |
      v
[Vulnerability Discovery]
      |
      v
[Safe Validation]
      |
      v
[Lab Exploitation, if authorized]
      |
      v
[Privilege Escalation, if applicable]
      |
      v
[Evidence + Root Cause]
      |
      v
[Remediation + Detection Mapping]
      |
      v
[Lessons Learned]
```

### 7.3 Decision Points

| Decision Point         | Criteria     | Decision     | Rationale     |
| ---------------------- | ------------ | ------------ | ------------- |
| Continue recon         | `<criteria>` | `<decision>` | `<rationale>` |
| Expand enumeration     | `<criteria>` | `<decision>` | `<rationale>` |
| Validate vulnerability | `<criteria>` | `<decision>` | `<rationale>` |
| Stop testing           | `<criteria>` | `<decision>` | `<rationale>` |
| Escalate privileges    | `<criteria>` | `<decision>` | `<rationale>` |
| Collect more evidence  | `<criteria>` | `<decision>` | `<rationale>` |

---

## 8. Reconnaissance

### 8.1 Recon Summary

```text
<Summarize what was discovered during reconnaissance and how it shaped the next steps.>
```

### 8.2 Passive Recon

| Item                   | Result     | Evidence        |
| ---------------------- | ---------- | --------------- |
| `<passive_recon_item>` | `<result>` | `<evidence_id>` |

```bash
<passive_recon_command>
```

```text
<command_output>
```

### 8.3 Active Recon

| Item                  | Result     | Evidence        |
| --------------------- | ---------- | --------------- |
| `<active_recon_item>` | `<result>` | `<evidence_id>` |

```bash
<active_recon_command>
```

```text
<command_output>
```

### 8.4 Host Discovery

```bash
<host_discovery_command>
```

```text
<host_discovery_output>
```

| Host         | IP             | Status                   | Notes     |
| ------------ | -------------- | ------------------------ | --------- |
| `<hostname>` | `<ip_address>` | `<up / down / filtered>` | `<notes>` |

### 8.5 Port Scanning

```bash
<port_scan_command>
```

```text
<port_scan_output>
```

|     Port | Protocol      | State                        | Service     | Version     | Notes     |
| -------: | ------------- | ---------------------------- | ----------- | ----------- | --------- |
| `<port>` | `<tcp / udp>` | `<open / closed / filtered>` | `<service>` | `<version>` | `<notes>` |

### 8.6 Service Discovery

```bash
<service_discovery_command>
```

```text
<service_discovery_output>
```

| Service     | Endpoint     | Version     | Authentication Required | Notes     |
| ----------- | ------------ | ----------- | ----------------------- | --------- |
| `<service>` | `<endpoint>` | `<version>` | `<Yes / No / Unknown>`  | `<notes>` |

### 8.7 Technology Fingerprinting

```bash
<technology_fingerprinting_command>
```

```text
<technology_fingerprinting_output>
```

| Technology     | Version     | Source               | Confidence              | Notes     |
| -------------- | ----------- | -------------------- | ----------------------- | --------- |
| `<technology>` | `<version>` | `<tool_or_evidence>` | `<Low / Medium / High>` | `<notes>` |

### 8.8 Application Mapping

| Path / Route | Method                                | Status          | Auth Required          | Notes     |
| ------------ | ------------------------------------- | --------------- | ---------------------- | --------- |
| `<path>`     | `<GET / POST / PUT / DELETE / PATCH>` | `<status_code>` | `<Yes / No / Unknown>` | `<notes>` |

```http
<http_request>
```

```http
<http_response>
```

### 8.9 Directory / Content Discovery

```bash
<content_discovery_command>
```

```text
<content_discovery_output>
```

| Path     |          Status |     Size | Interesting? | Notes     |
| -------- | --------------: | -------: | ------------ | --------- |
| `<path>` | `<status_code>` | `<size>` | `<Yes / No>` | `<notes>` |

### 8.10 API Discovery

| Endpoint         | Method     | Parameters     | Auth Required          | Notes     |
| ---------------- | ---------- | -------------- | ---------------------- | --------- |
| `<api_endpoint>` | `<method>` | `<parameters>` | `<Yes / No / Unknown>` | `<notes>` |

```http
<api_request>
```

```http
<api_response>
```

### 8.11 Source / Code Artifact Discovery

| Artifact          | Location     | Type                                                          | Relevance     | Evidence        |
| ----------------- | ------------ | ------------------------------------------------------------- | ------------- | --------------- |
| `<artifact_name>` | `<location>` | `<source / backup / config / binary / map_file / debug_file>` | `<relevance>` | `<evidence_id>` |

---

## 9. Enumeration

### 9.1 Enumeration Summary

```text
<Summarize what enumeration revealed, including accounts, services, endpoints, permissions, versions, shares, domains, APIs, or binaries.>
```

### 9.2 Service Enumeration

| Service     | Enumeration Method | Findings     | Evidence        |
| ----------- | ------------------ | ------------ | --------------- |
| `<service>` | `<method>`         | `<findings>` | `<evidence_id>` |

```bash
<service_enumeration_command>
```

```text
<service_enumeration_output>
```

### 9.3 Web Enumeration

| Area              | Result     | Evidence        |
| ----------------- | ---------- | --------------- |
| Authentication    | `<result>` | `<evidence_id>` |
| Session Handling  | `<result>` | `<evidence_id>` |
| Input Points      | `<result>` | `<evidence_id>` |
| Uploads           | `<result>` | `<evidence_id>` |
| Admin Areas       | `<result>` | `<evidence_id>` |
| Client-Side Files | `<result>` | `<evidence_id>` |

### 9.4 API Enumeration

| Endpoint     | Method     | Parameters     | Response Behavior     | Notes     |
| ------------ | ---------- | -------------- | --------------------- | --------- |
| `<endpoint>` | `<method>` | `<parameters>` | `<response_behavior>` | `<notes>` |

### 9.5 Active Directory Enumeration

| Item                  | Result                    | Evidence        |
| --------------------- | ------------------------- | --------------- |
| Domain                | `<domain>`                | `<evidence_id>` |
| Users                 | `<user_summary>`          | `<evidence_id>` |
| Groups                | `<group_summary>`         | `<evidence_id>` |
| Computers             | `<computer_summary>`      | `<evidence_id>` |
| Shares                | `<share_summary>`         | `<evidence_id>` |
| Privileged Principals | `<privileged_principals>` | `<evidence_id>` |
| Trusts                | `<trust_summary>`         | `<evidence_id>` |

```bash
<ad_enumeration_command>
```

```text
<ad_enumeration_output>
```

### 9.6 Cloud Enumeration

| Resource          | Type              | Permissions     | Exposure                        | Evidence        |
| ----------------- | ----------------- | --------------- | ------------------------------- | --------------- |
| `<resource_name>` | `<resource_type>` | `<permissions>` | `<public / internal / private>` | `<evidence_id>` |

```bash
<cloud_enumeration_command>
```

```text
<cloud_enumeration_output>
```

### 9.7 Reverse Engineering / Binary Enumeration

| Artifact          | Type                                     | Architecture     | Interesting Functions | Evidence        |
| ----------------- | ---------------------------------------- | ---------------- | --------------------- | --------------- |
| `<artifact_name>` | `<binary / firmware / library / driver>` | `<architecture>` | `<functions>`         | `<evidence_id>` |

```bash
<binary_triage_command>
```

```text
<binary_triage_output>
```

---

## 10. Vulnerability Discovery

### 10.1 Discovery Summary

```text
<Summarize vulnerabilities, weaknesses, misconfigurations, suspicious behaviors, or attack paths identified during analysis.>
```

### 10.2 Candidate Vulnerabilities

| Candidate ID | Vulnerability / Weakness | Evidence        | Hypothesis     | Status                                    | Confidence              |
| ------------ | ------------------------ | --------------- | -------------- | ----------------------------------------- | ----------------------- |
| `<CAND-001>` | `<weakness>`             | `<evidence_id>` | `<hypothesis>` | `<Open / Testing / Confirmed / Rejected>` | `<Low / Medium / High>` |

### 10.3 Vulnerability Categories Reviewed

| Category                    | Reviewed     | Result     | Notes     |
| --------------------------- | ------------ | ---------- | --------- |
| Authentication bypass       | `<Yes / No>` | `<result>` | `<notes>` |
| Authorization bypass / IDOR | `<Yes / No>` | `<result>` | `<notes>` |
| Injection                   | `<Yes / No>` | `<result>` | `<notes>` |
| XSS / client-side injection | `<Yes / No>` | `<result>` | `<notes>` |
| SSRF                        | `<Yes / No>` | `<result>` | `<notes>` |
| XXE                         | `<Yes / No>` | `<result>` | `<notes>` |
| File upload abuse           | `<Yes / No>` | `<result>` | `<notes>` |
| Path traversal              | `<Yes / No>` | `<result>` | `<notes>` |
| Insecure deserialization    | `<Yes / No>` | `<result>` | `<notes>` |
| Command injection           | `<Yes / No>` | `<result>` | `<notes>` |
| Weak cryptography           | `<Yes / No>` | `<result>` | `<notes>` |
| Secrets exposure            | `<Yes / No>` | `<result>` | `<notes>` |
| Dependency vulnerability    | `<Yes / No>` | `<result>` | `<notes>` |
| Misconfiguration            | `<Yes / No>` | `<result>` | `<notes>` |
| Privilege escalation        | `<Yes / No>` | `<result>` | `<notes>` |
| Memory corruption           | `<Yes / No>` | `<result>` | `<notes>` |
| Logic flaw                  | `<Yes / No>` | `<result>` | `<notes>` |

### 10.4 Source-to-Sink or Path-to-Impact Notes

```text
<Describe how input, access, configuration, code behavior, or protocol behavior leads to the observed weakness or candidate finding.>
```

### 10.5 Evidence Snippet

```text
<code_snippet_or_tool_output>
```

---

## 11. Safe Vulnerability Validation

### 11.1 Validation Scope

```text
<Confirm that validation was performed only inside the authorized lab, using lab assets, lab accounts, lab data, and non-destructive proof methods.>
```

### 11.2 Validation Plan

| Validation ID | Candidate Finding | Method                     | Expected Result     | Actual Result     | Status                         |
| ------------- | ----------------- | -------------------------- | ------------------- | ----------------- | ------------------------------ |
| `<VAL-001>`   | `<candidate_id>`  | `<safe_validation_method>` | `<expected_result>` | `<actual_result>` | `<Pass / Fail / Inconclusive>` |

### 11.3 Validation Commands

```bash
<safe_validation_command>
```

### 11.4 Validation Output

```text
<validation_output>
```

### 11.5 HTTP Validation Evidence

```http
<safe_http_request>
```

```http
<safe_http_response>
```

### 11.6 Debugger / Runtime Validation Evidence

```text
<debugger_or_runtime_output>
```

### 11.7 What This Proves

```text
<Describe the specific security condition proven by the validation.>
```

### 11.8 What This Does Not Prove

```text
<Describe limitations, untested cases, environmental assumptions, and why the validation should not be interpreted beyond the lab scope.>
```

---

## 12. Exploitation Validation in Lab

> This section is limited to controlled, authorized lab validation. Do not include weaponized payloads, persistence, stealth, real-world target details, or instructions for misuse.

### 12.1 Exploitation Objective

```text
<Describe the lab-only objective, such as proving impact, reaching a training flag, triggering a controlled crash, or demonstrating access under approved lab conditions.>
```

### 12.2 Preconditions

| Precondition           | Required?    | Evidence        | Notes     |
| ---------------------- | ------------ | --------------- | --------- |
| Network access         | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Valid lab credentials  | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Specific role          | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| User interaction       | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Vulnerable version     | `<Yes / No>` | `<evidence_id>` | `<notes>` |
| Specific configuration | `<Yes / No>` | `<evidence_id>` | `<notes>` |

### 12.3 Safe Lab Proof Steps

```text
<Step 1: Describe controlled setup>
<Step 2: Describe benign trigger or lab-only action>
<Step 3: Describe expected proof>
<Step 4: Describe cleanup>
```

### 12.4 Commands / Requests

```bash
<lab_only_command>
```

```http
<lab_only_http_request>
```

### 12.5 Output / Proof

```text
<command_output_or_lab_proof>
```

### 12.6 Exploitation Result

| Field             | Value                                                         |
| ----------------- | ------------------------------------------------------------- |
| Result            | `<successful / partially_successful / failed / inconclusive>` |
| Proof Captured    | `<Yes / No>`                                                  |
| Evidence ID       | `<evidence_id>`                                               |
| Screenshot ID     | `<screenshot_id>`                                             |
| Reliability       | `<single_success / repeatable / intermittent / unknown>`      |
| Cleanup Completed | `<Yes / No / Not Applicable>`                                 |

---

## 13. Privilege Escalation, If Applicable

### 13.1 Privilege Escalation Summary

```text
<Describe the privilege escalation path inside the lab. Include the starting privilege, target privilege, weakness used, and final proof.>
```

### 13.2 Starting Context

| Field            | Value                         |
| ---------------- | ----------------------------- |
| User / Principal | `<current_user_or_principal>` |
| Groups / Roles   | `<groups_or_roles>`           |
| Host             | `<host>`                      |
| Privilege Level  | `<privilege_level>`           |
| Evidence         | `<evidence_id>`               |

```bash
<current_context_command>
```

```text
<current_context_output>
```

### 13.3 Enumeration for Escalation

| Area                     | Finding     | Evidence        |
| ------------------------ | ----------- | --------------- |
| OS / kernel              | `<finding>` | `<evidence_id>` |
| Services                 | `<finding>` | `<evidence_id>` |
| Scheduled tasks / cron   | `<finding>` | `<evidence_id>` |
| SUID / permissions       | `<finding>` | `<evidence_id>` |
| Credentials in lab scope | `<finding>` | `<evidence_id>` |
| Misconfigured ACLs       | `<finding>` | `<evidence_id>` |
| AD rights / delegation   | `<finding>` | `<evidence_id>` |
| Cloud IAM permissions    | `<finding>` | `<evidence_id>` |

### 13.4 Privilege Escalation Validation

```bash
<safe_lab_privilege_escalation_validation_command>
```

```text
<validation_output>
```

### 13.5 Final Context

| Field            | Value                       |
| ---------------- | --------------------------- |
| User / Principal | `<final_user_or_principal>` |
| Groups / Roles   | `<final_groups_or_roles>`   |
| Privilege Level  | `<final_privilege_level>`   |
| Proof            | `<proof>`                   |
| Evidence         | `<evidence_id>`             |

---

## 14. Post-Exploitation Observations, If Applicable

> This section is for controlled lab observation only. Avoid persistence, stealth, unauthorized lateral movement, or non-lab data access.

### 14.1 Post-Exploitation Purpose

```text
<Explain why post-exploitation enumeration was necessary for the lab objective, such as proving impact, finding a flag, mapping risk, or identifying root cause.>
```

### 14.2 Observations

| Observation ID | Observation     | Evidence        | Security Relevance     |
| -------------- | --------------- | --------------- | ---------------------- |
| `<POST-001>`   | `<observation>` | `<evidence_id>` | `<security_relevance>` |

### 14.3 Lab Data Accessed

| Data / File / Resource | Purpose     | Sensitive?   | Evidence        | Notes     |
| ---------------------- | ----------- | ------------ | --------------- | --------- |
| `<resource>`           | `<purpose>` | `<Yes / No>` | `<evidence_id>` | `<notes>` |

### 14.4 Cleanup

```bash
<cleanup_command>
```

```text
<cleanup_output>
```

---

## 15. Attack Path / Solution Chain

### 15.1 High-Level Attack Path

```text
<Initial Access Vector>
        |
        v
<Enumeration Finding>
        |
        v
<Vulnerability / Weakness>
        |
        v
<Safe Lab Validation>
        |
        v
<Privilege Escalation, if applicable>
        |
        v
<Objective / Flag / Proof>
```

### 15.2 Step-by-Step Chain

| Step | Action     | Evidence        | Decision / Rationale |
| ---: | ---------- | --------------- | -------------------- |
|  `1` | `<action>` | `<evidence_id>` | `<rationale>`        |
|  `2` | `<action>` | `<evidence_id>` | `<rationale>`        |
|  `3` | `<action>` | `<evidence_id>` | `<rationale>`        |

### 15.3 Critical Decision Points

| Decision     | Options Considered | Selected Path     | Why           |
| ------------ | ------------------ | ----------------- | ------------- |
| `<decision>` | `<options>`        | `<selected_path>` | `<rationale>` |

---

## 16. Findings

### 16.1 Findings Register

| Finding ID   | Title             | Severity                                           | Confidence              | CWE        | CVSS                     | Affected Asset     | Status                                                            |
| ------------ | ----------------- | -------------------------------------------------- | ----------------------- | ---------- | ------------------------ | ------------------ | ----------------------------------------------------------------- |
| `<FIND-001>` | `<finding_title>` | `<Informational / Low / Medium / High / Critical>` | `<Low / Medium / High>` | `<CWE-ID>` | `<CVSS_vector_or_score>` | `<affected_asset>` | `<Open / Validated / Remediated / Retest Passed / Retest Failed>` |

---

## 17. Finding Detail Template

Copy this section for each finding.

### `<finding_id>` — `<finding_title>`

| Field                        | Value                                                              |
| ---------------------------- | ------------------------------------------------------------------ |
| Finding ID                   | `<finding_id>`                                                     |
| Title                        | `<finding_title>`                                                  |
| Severity                     | `<Informational / Low / Medium / High / Critical>`                 |
| Confidence                   | `<Low / Medium / High>`                                            |
| CWE                          | `<CWE-ID: CWE Name>`                                               |
| CVSS Vector                  | `<CVSS_vector>`                                                    |
| CVSS Score                   | `<CVSS_score>`                                                     |
| Affected Asset               | `<affected_asset>`                                                 |
| Affected Component           | `<affected_component>`                                             |
| Affected Endpoint / Function | `<affected_endpoint_or_function>`                                  |
| Affected Role / User         | `<affected_role_or_user>`                                          |
| Preconditions                | `<preconditions>`                                                  |
| Business Impact              | `<business_impact>`                                                |
| Technical Impact             | `<technical_impact>`                                               |
| Status                       | `<Open / Validated / Remediated / Accepted Risk / Not Applicable>` |

### 17.1 Finding Summary

```text
<Concise explanation of the issue, why it exists, and why it matters.>
```

### 17.2 Facts

| Fact ID      | Fact     | Evidence        | Confidence              |
| ------------ | -------- | --------------- | ----------------------- |
| `<FACT-001>` | `<fact>` | `<evidence_id>` | `<Low / Medium / High>` |

### 17.3 Evidence

| Evidence ID  | Description     | Path              | Notes     |
| ------------ | --------------- | ----------------- | --------- |
| `<EVID-001>` | `<description>` | `<evidence_path>` | `<notes>` |

### 17.4 Technical Details

```text
<Describe the vulnerable behavior, affected logic, misconfiguration, weak control, or insecure pattern.>
```

### 17.5 Safe Validation Evidence

```bash
<safe_lab_validation_command>
```

```text
<command_output>
```

```http
<http_request_or_response>
```

### 17.6 Impact

```text
<Describe realistic impact in the lab and what analogous risk would mean in a real organization. Clearly separate confirmed lab impact from hypothetical real-world impact.>
```

### 17.7 Root Cause

```text
<Describe the underlying design, implementation, configuration, operational, or process failure that caused the issue.>
```

### 17.8 Remediation

```text
<Describe specific remediation steps. Include secure configuration, code-level fixes, permission changes, patching, hardening, monitoring, or workflow changes as applicable.>
```

### 17.9 Verification / Retest

```text
<Describe how to safely verify the fix in a controlled environment.>
```

| Retest Date    | Retested By       | Result                                       | Evidence        | Notes     |
| -------------- | ----------------- | -------------------------------------------- | --------------- | --------- |
| `<YYYY-MM-DD>` | `<reviewer_name>` | `<Passed / Failed / Partial / Not Retested>` | `<evidence_id>` | `<notes>` |

---

## 18. Root Cause Analysis

### 18.1 Root Cause Summary

```text
<Explain the root cause of the successful attack path or primary weakness.>
```

### 18.2 Root Cause Table

| Weakness     | Root Cause     | Control Failure    | Evidence        | Remediation Theme     |
| ------------ | -------------- | ------------------ | --------------- | --------------------- |
| `<weakness>` | `<root_cause>` | `<failed_control>` | `<evidence_id>` | `<remediation_theme>` |

### 18.3 Contributing Factors

* [ ] Weak authentication
* [ ] Missing authorization
* [ ] Excessive permissions
* [ ] Insecure default configuration
* [ ] Missing patch
* [ ] Exposed sensitive file
* [ ] Weak secrets handling
* [ ] Insufficient input validation
* [ ] Unsafe parsing
* [ ] Insecure service configuration
* [ ] Lack of network segmentation
* [ ] Poor monitoring visibility
* [ ] Business logic flaw
* [ ] Memory safety issue
* [ ] Dependency or supply-chain weakness

---

## 19. Impact Analysis

### 19.1 Confirmed Lab Impact

```text
<Describe what was actually achieved or observed in the lab.>
```

### 19.2 Potential Real-World Impact

```text
<Describe what this class of weakness could mean in a real environment, without overstating beyond available evidence.>
```

### 19.3 Impact Table

| Impact Area             | Confirmed in Lab      | Potential Real-World Relevance | Notes     |
| ----------------------- | --------------------- | ------------------------------ | --------- |
| Confidentiality         | `<None / Low / High>` | `<description>`                | `<notes>` |
| Integrity               | `<None / Low / High>` | `<description>`                | `<notes>` |
| Availability            | `<None / Low / High>` | `<description>`                | `<notes>` |
| Privilege Escalation    | `<Yes / No>`          | `<description>`                | `<notes>` |
| Lateral Movement        | `<Yes / No>`          | `<description>`                | `<notes>` |
| Business Process Impact | `<Yes / No>`          | `<description>`                | `<notes>` |

---

## 20. Remediation and Hardening

### 20.1 Remediation Summary

```text
<Summarize the recommended fixes for the primary weakness and related control gaps.>
```

### 20.2 Remediation Plan

| Priority              | Recommendation     | Owner     | Related Finding | Verification Method     |
| --------------------- | ------------------ | --------- | --------------- | ----------------------- |
| `<P0 / P1 / P2 / P3>` | `<recommendation>` | `<owner>` | `<finding_id>`  | `<verification_method>` |

### 20.3 Hardening Checklist

* [ ] Apply relevant patches
* [ ] Remove exposed sensitive files
* [ ] Enforce least privilege
* [ ] Harden service configuration
* [ ] Disable unnecessary services
* [ ] Restrict administrative interfaces
* [ ] Improve input validation
* [ ] Add server-side authorization checks
* [ ] Rotate exposed lab credentials
* [ ] Improve secrets storage
* [ ] Enforce secure session/token settings
* [ ] Add logging for critical events
* [ ] Add detection logic
* [ ] Add regression tests
* [ ] Document secure deployment baseline

### 20.4 Verification Commands

```bash
<safe_fix_verification_command>
```

```text
<verification_output>
```

---

## 21. Detection Opportunities

### 21.1 Detection Summary

```text
<Describe telemetry, logs, events, or behavioral patterns that defenders could monitor to detect this activity in an enterprise environment.>
```

### 21.2 Detection Mapping

| Detection ID | Behavior     | Data Source     | Detection Logic Summary | ATT&CK Mapping         | Notes     |
| ------------ | ------------ | --------------- | ----------------------- | ---------------------- | --------- |
| `<DET-001>`  | `<behavior>` | `<data_source>` | `<logic_summary>`       | `<tactic / technique>` | `<notes>` |

### 21.3 Useful Telemetry

| Telemetry     | Source     | Why It Matters | Example Evidence |
| ------------- | ---------- | -------------- | ---------------- |
| `<telemetry>` | `<source>` | `<reason>`     | `<evidence_id>`  |

### 21.4 Example Detection Pseudocode

```text
<vendor-neutral detection pseudocode or placeholder>
```

### 21.5 Logging Improvements

* [ ] Authentication events
* [ ] Authorization failures
* [ ] Administrative actions
* [ ] File access events
* [ ] Process execution
* [ ] Service changes
* [ ] Network connections
* [ ] DNS queries
* [ ] API calls
* [ ] Cloud audit events
* [ ] Privilege changes
* [ ] Security control failures

---

## 22. Evidence Index

| Evidence ID  | Description     | Type                                                                          | Tool / Source      | Path              | Timestamp     | Notes     |
| ------------ | --------------- | ----------------------------------------------------------------------------- | ------------------ | ----------------- | ------------- | --------- |
| `<EVID-001>` | `<description>` | `<terminal_output / screenshot / http / log / pcap / code / debugger / note>` | `<tool_or_source>` | `<evidence_path>` | `<timestamp>` | `<notes>` |

### 22.1 Evidence Storage Layout

```text
<evidence_root>/
├── 00_scope/
├── 01_setup/
├── 02_recon/
├── 03_enumeration/
├── 04_validation/
├── 05_exploitation_lab/
├── 06_privesc/
├── 07_post_exploitation/
├── 08_findings/
├── 09_screenshots/
├── 10_logs/
├── 11_scripts/
├── 12_reports/
└── 13_retest/
```

### 22.2 Evidence Handling Notes

```text
<Describe evidence integrity, sensitive data handling, redaction requirements, storage location, and retention expectations.>
```

---

## 23. Screenshot Index

| Screenshot ID | Description     | Path                | Related Section | Notes     |
| ------------- | --------------- | ------------------- | --------------- | --------- |
| `<SS-001>`    | `<description>` | `<screenshot_path>` | `<section>`     | `<notes>` |

### 23.1 Screenshot Placeholder

```text
![<screenshot_description>](<screenshot_path>)
```

---

## 24. Commands and Outputs Log

| Command ID  | Purpose     | Tool     | Related Evidence | Notes     |
| ----------- | ----------- | -------- | ---------------- | --------- |
| `<CMD-001>` | `<purpose>` | `<tool>` | `<evidence_id>`  | `<notes>` |

### 24.1 Command

```bash
<command>
```

### 24.2 Output

```text
<command_output>
```

### 24.3 Interpretation

```text
<Explain what the output means and how it affected the next decision.>
```

---

## 25. Scripts, Payloads, and Configuration Snippets

> Only include lab-safe, non-destructive, authorized test inputs or proof snippets. Do not include weaponized payloads intended for real-world misuse.

### 25.1 Script / Snippet Metadata

| Field           | Value              |
| --------------- | ------------------ |
| Script ID       | `<SCRIPT-001>`     |
| Purpose         | `<purpose>`        |
| Scope           | `<lab_only_scope>` |
| Path            | `<script_path>`    |
| Related Finding | `<finding_id>`     |
| Safety Notes    | `<safety_notes>`   |

### 25.2 Script / Snippet

```text
<safe_lab_script_or_configuration_snippet>
```

### 25.3 Expected Output

```text
<expected_output>
```

---

## 26. Troubleshooting Notes

### 26.1 Issues Encountered

| Issue ID      | Issue     | Cause     | Resolution     | Evidence        |
| ------------- | --------- | --------- | -------------- | --------------- |
| `<ISSUE-001>` | `<issue>` | `<cause>` | `<resolution>` | `<evidence_id>` |

### 26.2 Common Failure Modes

| Failure Mode     | Symptom     | Likely Cause     | Fix     |
| ---------------- | ----------- | ---------------- | ------- |
| `<failure_mode>` | `<symptom>` | `<likely_cause>` | `<fix>` |

### 26.3 Troubleshooting Commands

```bash
<troubleshooting_command>
```

```text
<troubleshooting_output>
```

---

## 27. Reproducibility

### 27.1 Reproducibility Summary

```text
<Describe whether the lab solution was repeatable and what conditions are required to reproduce it.>
```

### 27.2 Reproducibility Checklist

* [ ] Lab scope confirmed
* [ ] Target reset to known-good snapshot
* [ ] Attacker machine prepared
* [ ] VPN connected, if required
* [ ] DNS/hosts entries configured
* [ ] Tool versions recorded
* [ ] Commands copied exactly from fenced code blocks
* [ ] Required files present
* [ ] Required credentials available within lab scope
* [ ] Expected ports/services available
* [ ] Evidence paths created
* [ ] Screenshots captured
* [ ] Cleanup completed
* [ ] Final result reproduced

### 27.3 Reproduction Steps

| Step | Action     | Command / Evidence            | Expected Result     |
| ---: | ---------- | ----------------------------- | ------------------- |
|  `1` | `<action>` | `<command_id_or_evidence_id>` | `<expected_result>` |
|  `2` | `<action>` | `<command_id_or_evidence_id>` | `<expected_result>` |
|  `3` | `<action>` | `<command_id_or_evidence_id>` | `<expected_result>` |

### 27.4 Full Reproduction Command Sequence

```bash
<reproduction_commands>
```

### 27.5 Expected Final Output

```text
<expected_final_output>
```

---

## 28. Instructor KSAT Extraction

### 28.1 Knowledge, Skills, Abilities, and Tasks

| KSAT Type | KSAT               | Where Demonstrated | Evidence        | Notes     |
| --------- | ------------------ | ------------------ | --------------- | --------- |
| Knowledge | `<knowledge_item>` | `<section>`        | `<evidence_id>` | `<notes>` |
| Skill     | `<skill_item>`     | `<section>`        | `<evidence_id>` | `<notes>` |
| Ability   | `<ability_item>`   | `<section>`        | `<evidence_id>` | `<notes>` |
| Task      | `<task_item>`      | `<section>`        | `<evidence_id>` | `<notes>` |

### 28.2 Prerequisite Knowledge

* [ ] Networking fundamentals
* [ ] Linux command line
* [ ] Windows command line
* [ ] Web protocols
* [ ] HTTP requests/responses
* [ ] Authentication and authorization concepts
* [ ] Active Directory basics
* [ ] Cloud IAM basics
* [ ] Binary analysis basics
* [ ] Debugging basics
* [ ] Scripting basics
* [ ] Vulnerability classes
* [ ] Secure remediation concepts
* [ ] Evidence handling

### 28.3 Required Tools and Techniques

| Tool / Technique      | Purpose     | Required Proficiency                   |
| --------------------- | ----------- | -------------------------------------- |
| `<tool_or_technique>` | `<purpose>` | `<beginner / intermediate / advanced>` |

### 28.4 Learning Objectives Mapped to Lab Steps

| Learning Objective     | Lab Step     | Observable Student Behavior | Assessment Method     |
| ---------------------- | ------------ | --------------------------- | --------------------- |
| `<learning_objective>` | `<lab_step>` | `<observable_behavior>`     | `<assessment_method>` |

### 28.5 Instructor Notes

```text
<Instructor-focused explanation of how to teach the lab, common student mistakes, hints to provide, and assessment criteria.>
```

---

## 29. Student Reflection

### 29.1 Reflection Questions

| Question                                  | Response             |
| ----------------------------------------- | -------------------- |
| What was the first useful clue?           | `<student_response>` |
| What assumption was wrong?                | `<student_response>` |
| What was the key decision point?          | `<student_response>` |
| What concept was hardest?                 | `<student_response>` |
| What would you do differently next time?  | `<student_response>` |
| What evidence best supports the finding?  | `<student_response>` |
| How would this weakness be remediated?    | `<student_response>` |
| How could defenders detect this behavior? | `<student_response>` |

### 29.2 Student Lessons Learned

| Lesson ID      | Lesson Learned     | Supporting Evidence | Future Application     |
| -------------- | ------------------ | ------------------- | ---------------------- |
| `<LESSON-001>` | `<lesson_learned>` | `<evidence_id>`     | `<future_application>` |

### 29.3 Confidence Self-Assessment

| Area                    | Confidence Before       | Confidence After        | Notes     |
| ----------------------- | ----------------------- | ----------------------- | --------- |
| Reconnaissance          | `<Low / Medium / High>` | `<Low / Medium / High>` | `<notes>` |
| Enumeration             | `<Low / Medium / High>` | `<Low / Medium / High>` | `<notes>` |
| Vulnerability Discovery | `<Low / Medium / High>` | `<Low / Medium / High>` | `<notes>` |
| Exploitation Validation | `<Low / Medium / High>` | `<Low / Medium / High>` | `<notes>` |
| Privilege Escalation    | `<Low / Medium / High>` | `<Low / Medium / High>` | `<notes>` |
| Reporting               | `<Low / Medium / High>` | `<Low / Medium / High>` | `<notes>` |

---

## 30. Lessons Learned

### 30.1 Technical Lessons

| Lesson ID      | Lesson               | Evidence        | Notes     |
| -------------- | -------------------- | --------------- | --------- |
| `<LESSON-001>` | `<technical_lesson>` | `<evidence_id>` | `<notes>` |

### 30.2 Methodology Lessons

| Lesson ID    | Lesson                 | Where It Applied | Notes     |
| ------------ | ---------------------- | ---------------- | --------- |
| `<METH-001>` | `<methodology_lesson>` | `<section>`      | `<notes>` |

### 30.3 Defensive Lessons

| Lesson ID   | Lesson               | Detection / Remediation Relevance | Notes     |
| ----------- | -------------------- | --------------------------------- | --------- |
| `<DEF-001>` | `<defensive_lesson>` | `<relevance>`                     | `<notes>` |

### 30.4 Mistakes and Corrections

| Mistake     | Impact     | Correction     | Prevention     |
| ----------- | ---------- | -------------- | -------------- |
| `<mistake>` | `<impact>` | `<correction>` | `<prevention>` |

---

## 31. Report Review Checklist

* [ ] Lab metadata complete
* [ ] Scope and authorization documented
* [ ] Target details documented
* [ ] Environment setup reproducible
* [ ] Commands placed in fenced code blocks
* [ ] Outputs placed in fenced code blocks
* [ ] HTTP requests/responses placed in fenced code blocks
* [ ] Evidence separated from hypotheses
* [ ] Findings include severity and confidence
* [ ] Findings include CWE and CVSS where applicable
* [ ] Impact separates confirmed lab impact from potential real-world impact
* [ ] Remediation is specific and actionable
* [ ] Detection opportunities documented
* [ ] Evidence index complete
* [ ] Screenshot index complete
* [ ] Reproducibility checklist complete
* [ ] KSAT extraction complete
* [ ] Student reflection complete
* [ ] Open questions documented
* [ ] Unsafe real-world exploitation instructions excluded

---

## 32. Open Questions / Follow-Up Tasks

### 32.1 Open Questions

| Question ID | Question     | Why It Matters     | Owner     | Status                         |
| ----------- | ------------ | ------------------ | --------- | ------------------------------ |
| `<Q-001>`   | `<question>` | `<why_it_matters>` | `<owner>` | `<Open / Answered / Deferred>` |

### 32.2 Follow-Up Tasks

| Task ID      | Task                 | Priority                | Owner     | Due Date       | Status                                       |
| ------------ | -------------------- | ----------------------- | --------- | -------------- | -------------------------------------------- |
| `<TASK-001>` | `<task_description>` | `<High / Medium / Low>` | `<owner>` | `<YYYY-MM-DD>` | `<Open / In Progress / Complete / Deferred>` |

### 32.3 Future Research

| Topic     | Reason     | Suggested Resource | Notes     |
| --------- | ---------- | ------------------ | --------- |
| `<topic>` | `<reason>` | `<resource>`       | `<notes>` |

### 32.4 Final Notes

```text
<Freeform notes, caveats, unresolved issues, additional observations, or context not captured elsewhere.>
```
