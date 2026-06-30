# Finding Template

> **Use Case:** Authorized penetration testing, secure code review, vulnerability assessment, bug bounty reporting, vulnerability management, AppSec workflows, lab documentation, and defensive validation only.
> **Source Requirements:** Based on the provided finding-template requirements. 
> **Scope Boundary:** Do not use this template to document unauthorized exploitation, credential theft, persistence, stealth, evasion, malware deployment, or misuse outside an approved testing environment. Proof-of-concept sections must be limited to safe validation in authorized scope.

---

## 1. Finding Header

| Field                                 | Value                                                                                                          |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Finding ID                            | `<finding_id>`                                                                                                 |
| Title                                 | `<finding_title>`                                                                                              |
| Severity                              | `<Informational / Low / Medium / High / Critical>`                                                             |
| Confidence                            | `<Low / Medium / High>`                                                                                        |
| Status                                | `<Open / Fixed / Partially Fixed / Accepted Risk / False Positive / Duplicate / Informational / Needs Retest>` |
| Finding Owner                         | `<finding_owner>`                                                                                              |
| Reporter                              | `<reporter_name>`                                                                                              |
| Reviewer                              | `<reviewer_name>`                                                                                              |
| Date Discovered                       | `<YYYY-MM-DD>`                                                                                                 |
| Date Reported                         | `<YYYY-MM-DD>`                                                                                                 |
| Date Remediated                       | `<YYYY-MM-DD>`                                                                                                 |
| Date Retested                         | `<YYYY-MM-DD>`                                                                                                 |
| Affected Organization / Business Unit | `<affected_organization_or_business_unit>`                                                                     |
| Affected Application / System         | `<affected_application_or_system>`                                                                             |
| Affected Environment                  | `<dev / test / staging / production / lab>`                                                                    |
| Affected Asset(s)                     | `<affected_assets>`                                                                                            |
| Affected Endpoint(s)                  | `<affected_endpoints>`                                                                                         |
| Affected User Role(s)                 | `<affected_roles>`                                                                                             |
| Affected Data                         | `<affected_data>`                                                                                              |
| Vulnerability Class                   | `<vulnerability_class>`                                                                                        |
| CWE                                   | `<CWE-ID: CWE Name>`                                                                                           |
| OWASP Category                        | `<OWASP_category>`                                                                                             |
| CVSS Version                          | `<CVSS v3.1 / CVSS v4.0>`                                                                                      |
| CVSS Vector                           | `<CVSS_vector>`                                                                                                |
| CVSS Score                            | `<CVSS_score>`                                                                                                 |
| Related Tickets                       | `<related_tickets>`                                                                                            |
| Related Evidence IDs                  | `<evidence_ids>`                                                                                               |

---

## 2. Severity, Confidence, and Status

### 2.1 Severity

| Severity      | Meaning                                 |
| ------------- | --------------------------------------- |
| Critical      | `<critical_definition_or_context>`      |
| High          | `<high_definition_or_context>`          |
| Medium        | `<medium_definition_or_context>`        |
| Low           | `<low_definition_or_context>`           |
| Informational | `<informational_definition_or_context>` |

### 2.2 Confidence

| Confidence | Meaning                                                  |
| ---------- | -------------------------------------------------------- |
| High       | `<evidence_strongly_confirms_issue>`                     |
| Medium     | `<evidence_supports_issue_but_some_uncertainty_remains>` |
| Low        | `<issue_is_plausible_but_requires_more_validation>`      |

### 2.3 Status

| Status          | Meaning                                   |
| --------------- | ----------------------------------------- |
| Open            | `<finding_is_valid_and_unresolved>`       |
| Fixed           | `<fix_has_been_implemented_and_verified>` |
| Partially Fixed | `<some_controls_added_but_risk_remains>`  |
| Accepted Risk   | `<risk_formally_accepted_by_owner>`       |
| False Positive  | `<finding_rejected_after_review>`         |
| Duplicate       | `<finding_already_tracked_elsewhere>`     |
| Informational   | `<documented_for_awareness>`              |
| Needs Retest    | `<fix_claimed_or_pending_validation>`     |

---

## 3. Executive Summary

```text
<Provide a concise executive summary written for business and risk stakeholders. Explain what the issue is, where it exists, why it matters, what could happen if exploited, and what should be done first. Avoid excessive jargon.>
```

### 3.1 Executive Summary Checklist

* [ ] Issue is explained in plain language
* [ ] Affected system or asset is identified
* [ ] Business risk is stated
* [ ] Recommended first action is clear
* [ ] Severity and confidence are justified
* [ ] Confirmed impact is separated from potential impact

---

## 4. Technical Summary

| Field                                                 | Value                                 |
| ----------------------------------------------------- | ------------------------------------- |
| Vulnerable Component                                  | `<vulnerable_component>`              |
| Vulnerable Endpoint / Route                           | `<endpoint_or_route>`                 |
| Vulnerable Function / Method                          | `<function_or_method>`                |
| Vulnerable Service / Package / Binary / Configuration | `<service_package_binary_or_config>`  |
| Vulnerability Class                                   | `<vulnerability_class>`               |
| Root Technical Weakness                               | `<root_technical_weakness>`           |
| Attack Preconditions                                  | `<attack_preconditions>`              |
| Required Privileges                                   | `<None / Low / High / Specific Role>` |
| User Interaction Required                             | `<Yes / No>`                          |
| Exploitability Summary                                | `<exploitability_summary>`            |
| Security Control Failure                              | `<failed_security_control>`           |
| Affected Data or Operation                            | `<affected_data_or_operation>`        |

---

## 5. Affected Assets

| Asset              | Type                                                                                                                                                                                                               | Environment     | Location                        | Role           | Exposure                                                    | Notes     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ------------------------------- | -------------- | ----------------------------------------------------------- | --------- |
| `<affected_asset>` | `<web_application / API_endpoint / mobile_application / cloud_resource / identity_provider / database / server / container / kubernetes_resource / source_code_repository / binary / firmware / internal_service>` | `<environment>` | `<url_ip_hostname_path_region>` | `<asset_role>` | `<internet-facing / internal / private / local / lab-only>` | `<notes>` |

### 5.1 Affected Users, Roles, and Data

| Category            | Value                                                         | Notes     |
| ------------------- | ------------------------------------------------------------- | --------- |
| Affected User(s)    | `<affected_users>`                                            | `<notes>` |
| Affected Role(s)    | `<affected_roles>`                                            | `<notes>` |
| Affected Tenant(s)  | `<affected_tenants>`                                          | `<notes>` |
| Affected Data       | `<affected_data>`                                             | `<notes>` |
| Data Classification | `<public / internal / confidential / restricted / regulated>` | `<notes>` |

---

## 6. Preconditions and Attack Requirements

| Requirement                        | Value                                             | Notes     |
| ---------------------------------- | ------------------------------------------------- | --------- |
| Network Access Required            | `<none / local / adjacent / internal / internet>` | `<notes>` |
| Authentication Required            | `<Yes / No>`                                      | `<notes>` |
| User Role Required                 | `<role_required>`                                 | `<notes>` |
| User Interaction Required          | `<Yes / No>`                                      | `<notes>` |
| Known Identifiers Required         | `<Yes / No>`                                      | `<notes>` |
| Environmental Assumptions          | `<environmental_assumptions>`                     | `<notes>` |
| Required Configuration State       | `<configuration_state>`                           | `<notes>` |
| Rate Limit / Timing Assumptions    | `<rate_limit_or_timing_assumptions>`              | `<notes>` |
| Browser / Client Assumptions       | `<browser_or_client_assumptions>`                 | `<notes>` |
| Feature Flag / License Requirement | `<feature_or_license_requirement>`                | `<notes>` |

---

## 7. Vulnerability Description

### 7.1 Description

```text
<Explain what the vulnerability is, how the vulnerable logic works, why the current control is insufficient, what trust boundary is violated, what user-controlled input or condition triggers the issue, and what security property is affected.>
```

### 7.2 Security Property Affected

| Security Property | Affected?              | Notes     |
| ----------------- | ---------------------- | --------- |
| Confidentiality   | `<Yes / No / Partial>` | `<notes>` |
| Integrity         | `<Yes / No / Partial>` | `<notes>` |
| Availability      | `<Yes / No / Partial>` | `<notes>` |
| Authentication    | `<Yes / No / Partial>` | `<notes>` |
| Authorization     | `<Yes / No / Partial>` | `<notes>` |
| Non-Repudiation   | `<Yes / No / Partial>` | `<notes>` |
| Privacy           | `<Yes / No / Partial>` | `<notes>` |
| Tenant Isolation  | `<Yes / No / Partial>` | `<notes>` |

### 7.3 Trust Boundary

```text
<Describe the trust boundary crossed or violated by the vulnerable behavior.>
```

### 7.4 User-Controlled Input or Trigger

```text
<Describe the user-controlled input, state, request, file, parameter, message, role, or condition that triggers the issue.>
```

---

## 8. Facts, Evidence, Hypotheses, and Confirmed Impact

### 8.1 Facts

| Fact ID      | Fact               | Evidence        | Confidence              |
| ------------ | ------------------ | --------------- | ----------------------- |
| `<FACT-001>` | `<confirmed_fact>` | `<evidence_id>` | `<Low / Medium / High>` |

### 8.2 Evidence

| Evidence ID  | Description     | Source              | Timestamp     | Notes     |
| ------------ | --------------- | ------------------- | ------------- | --------- |
| `<EVID-001>` | `<description>` | `<tool_log_system>` | `<timestamp>` | `<notes>` |

### 8.3 Hypotheses

| Hypothesis ID | Hypothesis     | Basis     | Validation Method          | Result                                  | Confidence              |
| ------------- | -------------- | --------- | -------------------------- | --------------------------------------- | ----------------------- |
| `<HYP-001>`   | `<hypothesis>` | `<basis>` | `<safe_validation_method>` | `<confirmed / rejected / inconclusive>` | `<Low / Medium / High>` |

### 8.4 Confirmed Impact

```text
<Describe what was directly confirmed through evidence. Do not overstate beyond observed results.>
```

### 8.5 Potential Impact

```text
<Describe realistic potential impact if the weakness were exploited under plausible conditions. Clearly separate this from confirmed impact.>
```

---

## 9. Root Cause Analysis

### 9.1 Root Cause Summary

```text
<Describe the immediate root cause, contributing factors, missing control, broken assumption, secure design failure, affected code/configuration location, and why existing controls did not prevent the issue.>
```

### 9.2 Root Cause Table

| Root Cause Area               | Observation                            | Evidence        |
| ----------------------------- | -------------------------------------- | --------------- |
| Immediate Root Cause          | `<observation>`                        | `<evidence_id>` |
| Contributing Factor           | `<observation>`                        | `<evidence_id>` |
| Missing Control               | `<observation>`                        | `<evidence_id>` |
| Broken Assumption             | `<observation>`                        | `<evidence_id>` |
| Secure Design Failure         | `<observation>`                        | `<evidence_id>` |
| Code / Configuration Location | `<file_path_function_endpoint_config>` | `<evidence_id>` |
| Existing Control Failure      | `<why_existing_controls_failed>`       | `<evidence_id>` |

### 9.3 Root Cause Checklist

* [ ] Missing authorization check
* [ ] Missing authentication check
* [ ] Insufficient input validation
* [ ] Unsafe output encoding
* [ ] Unsafe deserialization
* [ ] Unsafe file handling
* [ ] Unsafe command execution
* [ ] Insecure cryptographic design
* [ ] Weak secret management
* [ ] Insecure default configuration
* [ ] Excessive permissions
* [ ] Missing tenant isolation
* [ ] Missing rate limiting
* [ ] Missing audit logging
* [ ] Vulnerable dependency
* [ ] Business logic flaw
* [ ] Memory safety issue
* [ ] Insecure CI/CD or supply-chain control

---

## 10. Evidence

### 10.1 Evidence Block

```text
Evidence ID: <evidence_id>
Description: <description>
Source: <tool_log_system>
Timestamp: <timestamp>
Related Finding: <finding_id>
```

```text
<paste sanitized evidence here>
```

### 10.2 HTTP Request / Response Evidence

```http
<sanitized HTTP request>
```

```http
<sanitized HTTP response>
```

### 10.3 Command and Terminal Output Evidence

```bash
<safe_authorized_command>
```

```text
<command_output>
```

### 10.4 Source Code Evidence

```text
<source_code_snippet>
```

### 10.5 Log Evidence

```text
<log_output>
```

### 10.6 Debugger Output Evidence

```text
<debugger_output>
```

### 10.7 Cloud Audit Event Evidence

```json
<sanitized_cloud_audit_event>
```

### 10.8 Database Observation Evidence

```text
<sanitized_database_observation>
```

### 10.9 Packet Capture Summary

```text
<pcap_summary_or_packet_metadata>
```

### 10.10 Screenshot Evidence

```markdown
![<description>](<screenshot_path>)
```

---

## 11. Safe Reproduction Steps

> Reproduction must use authorized systems, lab-safe data, and non-destructive validation. Avoid dumping sensitive production data. Use redacted outputs, limited proof records, or screenshots where possible.

### 11.1 Steps

1. `<step_1>`
2. `<step_2>`
3. `<step_3>`
4. `<step_4>`

### 11.2 Step Rationale

| Step | What It Proves         | Evidence        |
| ---- | ---------------------- | --------------- |
| `1`  | `<what_step_1_proves>` | `<evidence_id>` |
| `2`  | `<what_step_2_proves>` | `<evidence_id>` |
| `3`  | `<what_step_3_proves>` | `<evidence_id>` |

### 11.3 Expected Result

```text
<expected vulnerable behavior>
```

### 11.4 Actual Result

```text
<observed behavior>
```

### 11.5 Safety Notes

```text
<Describe test-scope limits, data minimization, non-destructive safeguards, and cleanup requirements.>
```

---

## 12. Proof of Concept

> This PoC is for safe validation in an authorized environment only. Do not include weaponized payloads, persistence, stealth, credential theft, destructive actions, or instructions for real-world misuse.

### 12.1 PoC Scope Statement

```text
<Confirm the test environment, authorization boundary, test accounts, test data, and safety limits.>
```

### 12.2 PoC Metadata

| Field                      | Value                          |
| -------------------------- | ------------------------------ |
| Test Account Used          | `<test_account>`               |
| Test Environment           | `<test_environment>`           |
| Input Used                 | `<input_used>`                 |
| Expected Secure Behavior   | `<expected_secure_behavior>`   |
| Actual Vulnerable Behavior | `<actual_vulnerable_behavior>` |
| Safety Limitations         | `<safety_limitations>`         |
| Cleanup Required           | `<Yes / No>`                   |
| Cleanup Completed          | `<Yes / No / Not Applicable>`  |

### 12.3 PoC Request

```http
<sanitized HTTP request>
```

### 12.4 PoC Response

```http
<sanitized HTTP response>
```

### 12.5 PoC Command

```bash
<safe_authorized_command>
```

### 12.6 PoC Output

```text
<observed_output>
```

### 12.7 Cleanup Steps

```text
<cleanup_steps>
```

### 12.8 What This Proves

```text
<Describe the exact security condition proven by the PoC.>
```

### 12.9 What This Does Not Prove

```text
<Describe limitations, untested environments, untested roles, and impact that was not validated.>
```

---

## 13. Impact Analysis

### 13.1 Technical Impact

| Technical Impact               | Applicable?              | Description     | Evidence        |
| ------------------------------ | ------------------------ | --------------- | --------------- |
| Unauthorized Data Access       | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |
| Unauthorized Data Modification | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |
| Privilege Escalation           | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |
| Authentication Bypass          | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |
| Account Takeover               | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |
| Remote Code Execution          | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |
| Information Disclosure         | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |
| Denial of Service              | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |
| Tenant Isolation Failure       | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |
| Supply-Chain Compromise        | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |
| Integrity Violation            | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |
| Audit / Logging Bypass         | `<Yes / No / Potential>` | `<description>` | `<evidence_id>` |

### 13.2 Business Impact

| Business Impact           | Applicable?              | Description     | Severity Contribution     |
| ------------------------- | ------------------------ | --------------- | ------------------------- |
| Customer Data Exposure    | `<Yes / No / Potential>` | `<description>` | `<severity_contribution>` |
| Regulatory Exposure       | `<Yes / No / Potential>` | `<description>` | `<severity_contribution>` |
| Financial Loss            | `<Yes / No / Potential>` | `<description>` | `<severity_contribution>` |
| Service Disruption        | `<Yes / No / Potential>` | `<description>` | `<severity_contribution>` |
| Fraud Risk                | `<Yes / No / Potential>` | `<description>` | `<severity_contribution>` |
| Operational Disruption    | `<Yes / No / Potential>` | `<description>` | `<severity_contribution>` |
| Brand / Reputation Damage | `<Yes / No / Potential>` | `<description>` | `<severity_contribution>` |
| Contractual Impact        | `<Yes / No / Potential>` | `<description>` | `<severity_contribution>` |
| Internal Control Failure  | `<Yes / No / Potential>` | `<description>` | `<severity_contribution>` |

### 13.3 Impact Summary Table

| Impact Area     | Description     | Evidence        | Severity Contribution     |
| --------------- | --------------- | --------------- | ------------------------- |
| `<impact_area>` | `<description>` | `<evidence_id>` | `<severity_contribution>` |

---

## 14. Likelihood and Exploitability

| Factor                           | Assessment                              | Notes     |
| -------------------------------- | --------------------------------------- | --------- |
| Ease of Discovery                | `<Low / Medium / High>`                 | `<notes>` |
| Ease of Exploitation             | `<Low / Medium / High>`                 | `<notes>` |
| Required Skill Level             | `<Low / Medium / High>`                 | `<notes>` |
| Required Access Level            | `<None / Low / High / Specific Role>`   | `<notes>` |
| Automation Potential             | `<Low / Medium / High>`                 | `<notes>` |
| Public Exploit Availability      | `<Yes / No / Unknown / Not Applicable>` | `<notes>` |
| Attack Complexity                | `<Low / High>`                          | `<notes>` |
| Environmental Constraints        | `<constraints>`                         | `<notes>` |
| Existing Mitigating Controls     | `<controls>`                            | `<notes>` |
| Monitoring Visibility            | `<Low / Medium / High>`                 | `<notes>` |
| Rate Limiting / Abuse Resistance | `<present / absent / partial>`          | `<notes>` |

### 14.1 Exploitability Summary

```text
<Explain how practical exploitation is under the tested conditions. Avoid providing weaponized or real-world misuse instructions.>
```

---

## 15. Severity Rating

```text
Severity: <Informational / Low / Medium / High / Critical>
CVSS Version: <CVSS v3.1 / CVSS v4.0>
CVSS Vector: <vector>
CVSS Score: <score>
Rationale: <why this severity is appropriate>
```

### 15.1 CVSS Details

| Metric                 | Value         | Rationale     |
| ---------------------- | ------------- | ------------- |
| Attack Vector          | `<AV metric>` | `<rationale>` |
| Attack Complexity      | `<AC metric>` | `<rationale>` |
| Privileges Required    | `<PR metric>` | `<rationale>` |
| User Interaction       | `<UI metric>` | `<rationale>` |
| Scope                  | `<S metric>`  | `<rationale>` |
| Confidentiality Impact | `<C metric>`  | `<rationale>` |
| Integrity Impact       | `<I metric>`  | `<rationale>` |
| Availability Impact    | `<A metric>`  | `<rationale>` |

### 15.2 Business / Environmental Adjustment

| Adjustment                        | Value                                              | Rationale     |
| --------------------------------- | -------------------------------------------------- | ------------- |
| Business Severity Adjustment      | `<none / increased / decreased>`                   | `<rationale>` |
| Environmental Severity Adjustment | `<none / increased / decreased>`                   | `<rationale>` |
| Compensating Control Adjustment   | `<none / increased / decreased>`                   | `<rationale>` |
| Final Severity                    | `<Informational / Low / Medium / High / Critical>` | `<rationale>` |

---

## 16. CWE / OWASP / ATT&CK / CAPEC Mapping

| Framework    | Mapping                        | Rationale     |
| ------------ | ------------------------------ | ------------- |
| CWE          | `<CWE-ID: CWE Name>`           | `<rationale>` |
| OWASP        | `<OWASP category>`             | `<rationale>` |
| MITRE ATT&CK | `<technique_id_if_applicable>` | `<rationale>` |
| CAPEC        | `<CAPEC-ID_if_applicable>`     | `<rationale>` |

---

## 17. Remediation

### 17.1 Remediation Summary

```text
<Describe the recommended fix at a practical level. Include the immediate control change and the long-term design or process improvement.>
```

### 17.2 Tactical Fixes

* [ ] Immediate patch
* [ ] Configuration change
* [ ] Input validation update
* [ ] Authorization check
* [ ] Authentication enforcement
* [ ] Parameterization
* [ ] Safer API usage
* [ ] Secret rotation
* [ ] Dependency upgrade
* [ ] Infrastructure hardening
* [ ] Permission reduction
* [ ] Logging improvement
* [ ] Feature disablement until fixed

### 17.3 Strategic Fixes

* [ ] Secure design improvement
* [ ] Centralized security control
* [ ] Regression tests
* [ ] Secure coding standard update
* [ ] Threat model update
* [ ] Monitoring improvement
* [ ] Developer training
* [ ] CI/CD security gate
* [ ] Security requirements update
* [ ] Abuse-case testing
* [ ] Secure architecture review

### 17.4 Remediation Plan

| Priority              | Recommendation     | Owner     | Effort                  | Risk Reduction     |
| --------------------- | ------------------ | --------- | ----------------------- | ------------------ |
| `<P0 / P1 / P2 / P3>` | `<recommendation>` | `<owner>` | `<Low / Medium / High>` | `<risk_reduction>` |

---

## 18. Secure Implementation Guidance

### 18.1 Secure Pattern

```text
<insert secure implementation example or pseudocode>
```

### 18.2 Unsafe Pattern to Avoid

```text
<insert unsafe pattern placeholder or pseudocode>
```

### 18.3 Safer API / Framework Feature

```text
<Describe safer API, framework control, library feature, configuration setting, or design pattern.>
```

### 18.4 Code-Level Recommendation

```text
<Describe concrete code-level changes, validation checks, authorization checks, encoding requirements, error handling, or memory-safety recommendations.>
```

### 18.5 Configuration Example Placeholder

```text
<insert secure configuration example placeholder>
```

### 18.6 Test Coverage Recommendation

```text
<Describe unit, integration, regression, and abuse-case tests that should be added.>
```

---

## 19. Detection and Monitoring Opportunities

### 19.1 Detection Ideas

| Detection Idea     | Data Source     | Logic Summary     | Priority                |
| ------------------ | --------------- | ----------------- | ----------------------- |
| `<detection_idea>` | `<data_source>` | `<logic_summary>` | `<High / Medium / Low>` |

### 19.2 Relevant Logs and Events

| Log / Event      | Source     | Why It Matters | Notes     |
| ---------------- | ---------- | -------------- | --------- |
| `<log_or_event>` | `<source>` | `<reason>`     | `<notes>` |

### 19.3 Monitoring Opportunities

* [ ] Failed authorization events
* [ ] Sensitive endpoint access
* [ ] Suspicious request patterns
* [ ] Rate anomalies
* [ ] Privileged action attempts
* [ ] Unexpected data export volume
* [ ] Unusual authentication patterns
* [ ] Suspicious API parameter usage
* [ ] Suspicious file access
* [ ] Cloud audit events
* [ ] Application error spikes
* [ ] Security control failures
* [ ] Administrative configuration changes

### 19.4 Detection Pseudocode Placeholder

```text
<insert vendor-neutral detection logic placeholder>
```

---

## 20. Compensating Controls

> Compensating controls may reduce short-term risk but do not replace root-cause remediation unless risk is formally accepted.

| Control                        | Description     | Owner     | Duration                  | Residual Risk     |
| ------------------------------ | --------------- | --------- | ------------------------- | ----------------- |
| WAF Rule                       | `<description>` | `<owner>` | `<temporary / permanent>` | `<residual_risk>` |
| Feature Flag Disablement       | `<description>` | `<owner>` | `<temporary / permanent>` | `<residual_risk>` |
| Access Restriction             | `<description>` | `<owner>` | `<temporary / permanent>` | `<residual_risk>` |
| Rate Limiting                  | `<description>` | `<owner>` | `<temporary / permanent>` | `<residual_risk>` |
| Network Segmentation           | `<description>` | `<owner>` | `<temporary / permanent>` | `<residual_risk>` |
| Additional Monitoring          | `<description>` | `<owner>` | `<temporary / permanent>` | `<residual_risk>` |
| Temporary Permission Reduction | `<description>` | `<owner>` | `<temporary / permanent>` | `<residual_risk>` |
| Manual Review Process          | `<description>` | `<owner>` | `<temporary / permanent>` | `<residual_risk>` |

---

## 21. Retest Plan

### 21.1 Retest Metadata

| Field                  | Value                       |
| ---------------------- | --------------------------- |
| Retest Owner           | `<retest_owner>`            |
| Retest Date            | `<YYYY-MM-DD>`              |
| Fixed Version / Commit | `<fixed_version_or_commit>` |
| Retest Environment     | `<retest_environment>`      |
| Retest Scope           | `<retest_scope>`            |
| Residual Risk          | `<residual_risk>`           |

### 21.2 Retest Steps

| Retest Step | Expected Result              | Actual Result     | Pass / Fail     | Evidence        |
| ----------- | ---------------------------- | ----------------- | --------------- | --------------- |
| `<step_1>`  | `<expected_secure_behavior>` | `<actual_result>` | `<Pass / Fail>` | `<evidence_id>` |
| `<step_2>`  | `<expected_secure_behavior>` | `<actual_result>` | `<Pass / Fail>` | `<evidence_id>` |

### 21.3 Retest Evidence

```text
<retest_output_or_notes>
```

### 21.4 Retest Conclusion

```text
<Describe whether the fix fully mitigates the finding, partially mitigates it, introduces residual risk, or requires additional remediation.>
```

---

## 22. Regression Tests

| Test Type        | Test Case                 | Expected Secure Behavior     |
| ---------------- | ------------------------- | ---------------------------- |
| Unit Test        | `<unit_test_case>`        | `<expected_secure_behavior>` |
| Integration Test | `<integration_test_case>` | `<expected_secure_behavior>` |
| Security Test    | `<security_test_case>`    | `<expected_secure_behavior>` |
| Negative Test    | `<negative_test_case>`    | `<expected_secure_behavior>` |
| Abuse-Case Test  | `<abuse_case_test>`       | `<expected_secure_behavior>` |
| CI/CD Gate       | `<pipeline_check>`        | `<expected_secure_behavior>` |
| SAST / SCA Rule  | `<rule_recommendation>`   | `<expected_secure_behavior>` |

### 22.1 Regression Test Notes

```text
<Describe where tests should live, who owns them, what they should cover, and when they should run.>
```

---

## 23. Evidence Index

| Evidence ID  | Description     | Type                                                                                                                                          | Path / Link      | Timestamp     | Related Section     |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------- | ------------------- |
| `<EVID-001>` | `<description>` | `<screenshot / log / HTTP / command_output / source_code / debugger_output / database_observation / cloud_audit / pcap / hash / report_note>` | `<path_or_link>` | `<timestamp>` | `<related_section>` |

### 23.1 Evidence Storage Layout

```text
<evidence_root>/
├── screenshots/
├── http/
├── logs/
├── commands/
├── code/
├── debugger/
├── database/
├── cloud/
├── pcaps/
├── hashes/
├── retest/
└── notes/
```

### 23.2 Evidence Handling Notes

```text
<Describe evidence integrity, redaction requirements, sensitive data handling, retention expectations, and access restrictions.>
```

---

## 24. References

| Reference Type                | Title / Description           | Link / Identifier      | Notes     |
| ----------------------------- | ----------------------------- | ---------------------- | --------- |
| Vendor Documentation          | `<vendor_doc_title>`          | `<link_or_identifier>` | `<notes>` |
| Framework Documentation       | `<framework_doc_title>`       | `<link_or_identifier>` | `<notes>` |
| CWE Reference                 | `<CWE_reference>`             | `<link_or_identifier>` | `<notes>` |
| OWASP Reference               | `<OWASP_reference>`           | `<link_or_identifier>` | `<notes>` |
| CVSS Calculator               | `<CVSS_calculator_reference>` | `<link_or_identifier>` | `<notes>` |
| Advisory                      | `<advisory_reference>`        | `<link_or_identifier>` | `<notes>` |
| Internal Standard             | `<internal_standard>`         | `<link_or_identifier>` | `<notes>` |
| Secure Coding Guideline       | `<secure_coding_guideline>`   | `<link_or_identifier>` | `<notes>` |
| Related Ticket / Pull Request | `<ticket_or_pr>`              | `<link_or_identifier>` | `<notes>` |

---

## 25. Analyst Notes / Open Questions

### 25.1 Assumptions

| ID          | Assumption     | Risk if Incorrect     | Status                          |
| ----------- | -------------- | --------------------- | ------------------------------- |
| `<ASM-001>` | `<assumption>` | `<risk_if_incorrect>` | `<Open / Confirmed / Rejected>` |

### 25.2 Unknowns

| ID          | Unknown     | Why It Matters     | Owner     | Status                         |
| ----------- | ----------- | ------------------ | --------- | ------------------------------ |
| `<UNK-001>` | `<unknown>` | `<why_it_matters>` | `<owner>` | `<Open / Answered / Deferred>` |

### 25.3 Follow-Up Questions

| ID        | Question / Note      | Owner     | Status                         |
| --------- | -------------------- | --------- | ------------------------------ |
| `<Q-001>` | `<question_or_note>` | `<owner>` | `<Open / Answered / Deferred>` |

### 25.4 Additional Testing Needed

| Test     | Reason     | Priority                | Owner     | Status                                       |
| -------- | ---------- | ----------------------- | --------- | -------------------------------------------- |
| `<test>` | `<reason>` | `<High / Medium / Low>` | `<owner>` | `<Open / In Progress / Complete / Deferred>` |

### 25.5 Areas Not Reviewed

| Area     | Reason Not Reviewed | Risk     | Follow-Up     |
| -------- | ------------------- | -------- | ------------- |
| `<area>` | `<reason>`          | `<risk>` | `<follow_up>` |

### 25.6 Reviewer Comments

| Reviewer          | Date           | Comment     | Resolution     |
| ----------------- | -------------- | ----------- | -------------- |
| `<reviewer_name>` | `<YYYY-MM-DD>` | `<comment>` | `<resolution>` |

### 25.7 Final Analyst Notes

```text
<Freeform notes, caveats, context, unresolved questions, lessons learned, and reviewer observations.>
```
