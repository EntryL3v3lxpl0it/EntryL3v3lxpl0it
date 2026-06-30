# Source Code Penetration Test Report Template

> **Use Case:** Authorized source-assisted penetration testing, white-box application security assessment, secure code review with exploitability validation, API source review, SaaS review, microservice review, mobile backend review, and secure SDLC consulting.
> **Scope Boundary:** This template is for ethical, authorized, contractual, internal, educational, and controlled lab environments only. Do not use it to document unauthorized access, credential theft against third parties, stealth, persistence, malware deployment, destructive testing, or real-world misuse. Proof-of-concept content must be limited to safe validation within explicitly authorized scope.
> **Source Requirements:** Based on the provided source-code penetration test report template requirements. 

---

## 1. Cover Page

| Field                        | Value                                                                                                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Report Title                 | `Source Code Penetration Test Report`                                                                                                                                                                           |
| Client / Organization        | `<client_name>`                                                                                                                                                                                                 |
| Application Name             | `<application_name>`                                                                                                                                                                                            |
| Engagement Name              | `<engagement_name>`                                                                                                                                                                                             |
| Assessment Type              | `<source-assisted_penetration_test / white-box_application_test / secure_code_review_with_validation / API_source_review / SaaS_review / microservice_review / mobile_backend_review / secure_SDLC_assessment>` |
| Assessment Dates             | `<assessment_start_date> to <assessment_end_date>`                                                                                                                                                              |
| Report Date                  | `<YYYY-MM-DD>`                                                                                                                                                                                                  |
| Report Version               | `<report_version>`                                                                                                                                                                                              |
| Classification / Sensitivity | `<public / internal / confidential / restricted>`                                                                                                                                                               |
| Prepared By                  | `<tester_or_company_name>`                                                                                                                                                                                      |
| Reviewed By                  | `<reviewer_name>`                                                                                                                                                                                               |
| Distribution List            | `<authorized_recipients>`                                                                                                                                                                                       |
| Evidence Root                | `<evidence_root_path>`                                                                                                                                                                                          |

### 1.1 Confidentiality Notice

```text
<Insert confidentiality notice, distribution restrictions, report handling requirements, source-code handling requirements, evidence handling requirements, and client-specific limitations.>
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
<Describe who may receive, store, copy, transmit, or reference this report. Include restrictions for source code, screenshots, proof artifacts, raw logs, and exploitability evidence.>
```

### 2.2 Report Handling Checklist

* [ ] Report shared only with authorized recipients.
* [ ] Raw source-code excerpts minimized.
* [ ] Sensitive code, secrets, tokens, and keys redacted.
* [ ] Screenshots reviewed for sensitive data.
* [ ] Raw evidence stored in approved restricted location.
* [ ] Report classification applied.
* [ ] Retention period documented.
* [ ] Deletion or archival requirements documented.

---

## 3. Legal Authorization and Scope Statement

### 3.1 Authorization Statement

```text
<Describe the written authorization for the assessment, including contract/SOW reference, letter of engagement reference, repositories in scope, applications in scope, environments in scope, approved testing dates, and legal boundaries.>
```

### 3.2 Scope Summary

| Scope Item                      | Value                                |
| ------------------------------- | ------------------------------------ |
| Application Name                | `<application_name>`                 |
| Repository URL(s)               | `<repository_urls>`                  |
| Branch(es)                      | `<branches>`                         |
| Commit Hash(es)                 | `<commit_hashes>`                    |
| Environment(s)                  | `<production / staging / dev / lab>` |
| Base URL(s)                     | `<base_urls>`                        |
| API Base URL(s)                 | `<api_base_urls>`                    |
| Test Accounts                   | `<test_accounts>`                    |
| Excluded Areas                  | `<excluded_components>`              |
| Testing Window                  | `<testing_window>`                   |
| Emergency Contact               | `<contact>`                          |
| Escalation Contact              | `<escalation_contact>`               |
| Contract / SOW Reference        | `<contract_or_sow_reference>`        |
| Letter of Engagement Reference  | `<letter_of_engagement_reference>`   |
| Evidence Retention Requirements | `<evidence_retention_requirements>`  |

### 3.3 In-Scope Repositories

| Repository          | URL                | Branch     | Commit          | In Scope               | Notes     |
| ------------------- | ------------------ | ---------- | --------------- | ---------------------- | --------- |
| `<repository_name>` | `<repository_url>` | `<branch>` | `<commit_hash>` | `<Yes / No / Partial>` | `<notes>` |

### 3.4 In-Scope Applications and APIs

| Application / API      | Base URL     | Environment     | Auth Required | In Scope               | Notes     |
| ---------------------- | ------------ | --------------- | ------------- | ---------------------- | --------- |
| `<application_or_api>` | `<base_url>` | `<environment>` | `<Yes / No>`  | `<Yes / No / Partial>` | `<notes>` |

### 3.5 Out-of-Scope Repositories, Services, APIs, or Features

| Area                                  | Reason Excluded | Risk Accepted By | Notes     |
| ------------------------------------- | --------------- | ---------------- | --------- |
| `<repository_service_api_or_feature>` | `<reason>`      | `<owner>`        | `<notes>` |

### 3.6 Prohibited Actions

* [ ] Testing outside approved scope.
* [ ] Targeting third-party systems.
* [ ] Destructive testing.
* [ ] Credential theft against third parties.
* [ ] Malware deployment.
* [ ] Persistence, stealth, or evasion.
* [ ] Unauthorized access to production-sensitive data.
* [ ] Excessive automated traffic outside approved limits.
* [ ] Exploit validation outside the authorized environment.
* [ ] Modifying production data unless explicitly authorized.

---

## 4. Executive Summary

### 4.1 Plain-Language Summary

```text
<Provide a concise, non-technical summary of the source-assisted assessment, overall application risk, most important findings, exploitability themes, business impact, and recommended next actions.>
```

### 4.2 Overall Metrics

| Metric                         | Value                              |
| ------------------------------ | ---------------------------------- |
| Overall Risk                   | `<Critical / High / Medium / Low>` |
| Critical Findings              | `<count>`                          |
| High Findings                  | `<count>`                          |
| Medium Findings                | `<count>`                          |
| Low Findings                   | `<count>`                          |
| Informational Findings         | `<count>`                          |
| Repositories Reviewed          | `<count>`                          |
| Critical Code Paths Reviewed   | `<count>`                          |
| Confirmed Exploitability Paths | `<count>`                          |
| Retest Recommended             | `<Yes / No>`                       |
| Overall Confidence             | `<Low / Medium / High>`            |

### 4.3 Key Business Risks

| Risk              | Business Impact | Related Finding(s) | Recommended Action     |
| ----------------- | --------------- | ------------------ | ---------------------- |
| `<business_risk>` | `<impact>`      | `<finding_ids>`    | `<recommended_action>` |

### 4.4 Most Critical Findings

| Finding ID     | Title             | Severity     | Affected Component     | Business Impact     |
| -------------- | ----------------- | ------------ | ---------------------- | ------------------- |
| `<finding_id>` | `<finding_title>` | `<severity>` | `<affected_component>` | `<business_impact>` |

### 4.5 Primary Exploitability Themes

| Theme     | Description     | Related Finding(s) | Risk     |
| --------- | --------------- | ------------------ | -------- |
| `<theme>` | `<description>` | `<finding_ids>`    | `<risk>` |

### 4.6 Security Strengths Observed

| Strength              | Evidence        | Security Value     |
| --------------------- | --------------- | ------------------ |
| `<security_strength>` | `<evidence_id>` | `<security_value>` |

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
<Describe remaining risk after immediate remediation, compensating controls, or accepted-risk decisions.>
```

---

## 5. Business Impact Summary

### 5.1 Impact Narrative

```text
<Explain the business impact of confirmed findings and validated exploitability paths. Separate confirmed impact from potential impact.>
```

### 5.2 Business Impact Table

| Business Risk             | Impact                 | Evidence        | Recommended Action     |
| ------------------------- | ---------------------- | --------------- | ---------------------- |
| Confidentiality Impact    | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Integrity Impact          | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Availability Impact       | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Account Takeover Risk     | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Privilege Escalation Risk | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Data Exposure Risk        | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Fraud Risk                | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Tenant Isolation Risk     | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Regulatory Impact         | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Financial Impact          | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Customer Impact           | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |
| Reputational Impact       | `<impact_description>` | `<evidence_id>` | `<recommended_action>` |

---

## 6. Engagement Objectives

### 6.1 Primary Objectives

* [ ] Identify exploitable vulnerabilities through source-assisted review.
* [ ] Trace user-controlled input from sources to dangerous sinks.
* [ ] Validate authentication and authorization logic.
* [ ] Identify business logic flaws.
* [ ] Review API security controls.
* [ ] Assess secrets and cryptography usage.
* [ ] Identify vulnerable dependencies and supply-chain risks.
* [ ] Review deployment and configuration risks.
* [ ] Provide prioritized remediation and regression test guidance.

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

| Deliverable                     | Status                                  | Notes     |
| ------------------------------- | --------------------------------------- | --------- |
| Executive report                | `<complete / pending / not_applicable>` | `<notes>` |
| Technical report                | `<complete / pending / not_applicable>` | `<notes>` |
| Findings register               | `<complete / pending / not_applicable>` | `<notes>` |
| Evidence package                | `<complete / pending / not_applicable>` | `<notes>` |
| Code reference index            | `<complete / pending / not_applicable>` | `<notes>` |
| Retest plan                     | `<complete / pending / not_applicable>` | `<notes>` |
| Remediation roadmap             | `<complete / pending / not_applicable>` | `<notes>` |
| Regression test recommendations | `<complete / pending / not_applicable>` | `<notes>` |

---

## 7. Assessment Methodology

### 7.1 Methodology Phases

| Phase                                      | Objective     | Activities Performed | Evidence        |
| ------------------------------------------ | ------------- | -------------------- | --------------- |
| Pre-Engagement Review                      | `<objective>` | `<activities>`       | `<evidence_id>` |
| Scope Validation                           | `<objective>` | `<activities>`       | `<evidence_id>` |
| Repository Inventory                       | `<objective>` | `<activities>`       | `<evidence_id>` |
| Build and Environment Setup                | `<objective>` | `<activities>`       | `<evidence_id>` |
| Architecture Review                        | `<objective>` | `<activities>`       | `<evidence_id>` |
| Threat Model Review                        | `<objective>` | `<activities>`       | `<evidence_id>` |
| Security-Critical Code Path Identification | `<objective>` | `<activities>`       | `<evidence_id>` |
| Source-to-Sink Tracing                     | `<objective>` | `<activities>`       | `<evidence_id>` |
| Manual Secure Code Review                  | `<objective>` | `<activities>`       | `<evidence_id>` |
| SAST-Assisted Review                       | `<objective>` | `<activities>`       | `<evidence_id>` |
| Dependency and Supply-Chain Review         | `<objective>` | `<activities>`       | `<evidence_id>` |
| Configuration and IaC Review               | `<objective>` | `<activities>`       | `<evidence_id>` |
| Dynamic Validation, If Authorized          | `<objective>` | `<activities>`       | `<evidence_id>` |
| Exploitability Analysis                    | `<objective>` | `<activities>`       | `<evidence_id>` |
| False-Positive Reduction                   | `<objective>` | `<activities>`       | `<evidence_id>` |
| Root-Cause Analysis                        | `<objective>` | `<activities>`       | `<evidence_id>` |
| Remediation Planning                       | `<objective>` | `<activities>`       | `<evidence_id>` |
| Reporting                                  | `<objective>` | `<activities>`       | `<evidence_id>` |
| Retest Planning                            | `<objective>` | `<activities>`       | `<evidence_id>` |

### 7.2 Methodology Flow

```text
[Pre-Engagement Review]
        |
        v
[Scope + Repository Validation]
        |
        v
[Build + Environment Setup]
        |
        v
[Architecture + Threat Model Review]
        |
        v
[Security-Critical Code Path Identification]
        |
        v
[Source-to-Sink Analysis]
        |
        v
[Manual + Tool-Assisted Review]
        |
        v
[Safe Exploitability Validation]
        |
        v
[Root Cause + Impact Analysis]
        |
        v
[Remediation + Regression Guidance]
        |
        v
[Reporting + Retest Planning]
```

---

## 8. Rules of Engagement

### 8.1 ROE Summary

| Rule Area                        | Requirement                          |
| -------------------------------- | ------------------------------------ |
| Testing Windows                  | `<testing_windows>`                  |
| Test Environment Restrictions    | `<test_environment_restrictions>`    |
| Production Testing Restrictions  | `<production_testing_restrictions>`  |
| Destructive Testing Restrictions | `<destructive_testing_restrictions>` |
| Account Lockout Restrictions     | `<account_lockout_restrictions>`     |
| Data Exfiltration Limits         | `<data_exfiltration_limits>`         |
| Sensitive Data Handling Limits   | `<sensitive_data_handling_limits>`   |
| Third-Party Service Restrictions | `<third_party_service_restrictions>` |
| Dependency Scanning Limits       | `<dependency_scanning_limits>`       |
| CI/CD Testing Restrictions       | `<cicd_testing_restrictions>`        |
| Notification Requirements        | `<notification_requirements>`        |
| Stop Conditions                  | `<stop_conditions>`                  |
| Cleanup Requirements             | `<cleanup_requirements>`             |

### 8.2 ROE Checklist

* [ ] Scope confirmed before testing.
* [ ] Repository access approved.
* [ ] Commit hashes recorded.
* [ ] Build environment documented.
* [ ] Test accounts confirmed.
* [ ] Dynamic validation approved.
* [ ] Sensitive data access minimized.
* [ ] Evidence redacted.
* [ ] Cleanup completed.
* [ ] Critical findings escalated.
* [ ] Source-code excerpts minimized in final report.
* [ ] Client-approved evidence handling followed.

---

## 9. Environment and Tooling

### 9.1 Reviewer Environment

| Field                | Value                    |
| -------------------- | ------------------------ |
| Reviewer Workstation | `<reviewer_workstation>` |
| Operating System     | `<operating_system>`     |
| IDE / Editor         | `<ide_or_editor>`        |
| Language Runtimes    | `<language_runtimes>`    |
| Package Managers     | `<package_managers>`     |
| Build Tools          | `<build_tools>`          |
| Containers           | `<container_runtime>`    |
| Local Services       | `<local_services>`       |
| Databases            | `<databases>`            |
| Test Environment     | `<test_environment>`     |
| Proxy Tools          | `<proxy_tools>`          |
| Working Directory    | `<working_directory>`    |

### 9.2 Tools Used

| Tool          | Version     | Purpose     | Command / Config      | Output Path     |
| ------------- | ----------- | ----------- | --------------------- | --------------- |
| `<tool_name>` | `<version>` | `<purpose>` | `<command_or_config>` | `<output_path>` |

### 9.3 Tool Categories

* [ ] IDE/editor
* [ ] Build tools
* [ ] Package managers
* [ ] Containers
* [ ] Local services
* [ ] Databases
* [ ] Proxy tools
* [ ] SAST tools
* [ ] SCA tools
* [ ] Secret scanners
* [ ] IaC scanners
* [ ] Linters
* [ ] Test frameworks
* [ ] API clients
* [ ] Debuggers
* [ ] Coverage tools

### 9.4 Setup Commands

```bash
<build_or_setup_command>
```

### 9.5 Setup Output

```text
<build_or_setup_output>
```

### 9.6 Tool Version Commands

```bash
<tool_version_commands>
```

### 9.7 Tool Version Output

```text
<tool_version_output>
```

---

## 10. Repository and Codebase Inventory

### 10.1 Repositories Reviewed

| Repository     | Branch     | Commit          | Language / Framework   | In Scope               | Notes     |
| -------------- | ---------- | --------------- | ---------------------- | ---------------------- | --------- |
| `<repository>` | `<branch>` | `<commit_hash>` | `<language_framework>` | `<Yes / No / Partial>` | `<notes>` |

### 10.2 Components Reviewed

| Component     | Path     | Purpose     | Risk Level                         | Review Status                                       | Notes     |
| ------------- | -------- | ----------- | ---------------------------------- | --------------------------------------------------- | --------- |
| `<component>` | `<path>` | `<purpose>` | `<Low / Medium / High / Critical>` | `<not_started / in_progress / reviewed / deferred>` | `<notes>` |

### 10.3 Files or Paths Excluded

| Path     | Reason Excluded | Risk Accepted By | Notes     |
| -------- | --------------- | ---------------- | --------- |
| `<path>` | `<reason>`      | `<owner>`        | `<notes>` |

### 10.4 Build and Runtime Entry Points

| Entry Point     | Path     | Runtime     | Purpose     | Notes     |
| --------------- | -------- | ----------- | ----------- | --------- |
| `<entry_point>` | `<path>` | `<runtime>` | `<purpose>` | `<notes>` |

---

## 11. Application Architecture Summary

### 11.1 Architecture Narrative

```text
<Describe the high-level application architecture, trust boundaries, data flows, identity model, deployment model, and security-relevant dependencies.>
```

### 11.2 Architecture Details

| Area                      | Value                                    |
| ------------------------- | ---------------------------------------- |
| Frontend Framework        | `<frontend_framework>`                   |
| Backend Framework         | `<backend_framework>`                    |
| API Architecture          | `<REST / GraphQL / SOAP / gRPC / mixed>` |
| Authentication Provider   | `<authentication_provider>`              |
| Authorization Model       | `<RBAC / ABAC / ACL / ReBAC / custom>`   |
| Session / Token Mechanism | `<session_or_token_mechanism>`           |
| Database / Storage Layer  | `<database_or_storage>`                  |
| Message Queues            | `<message_queues>`                       |
| Background Workers        | `<background_workers>`                   |
| Cloud Services            | `<cloud_services>`                       |
| Third-Party Integrations  | `<third_party_integrations>`             |
| Administrative Interfaces | `<admin_interfaces>`                     |
| Sensitive Workflows       | `<sensitive_workflows>`                  |
| Data Classification       | `<data_classification>`                  |

### 11.3 Architecture Diagram

```text
<insert architecture diagram here>

Example:

[User / Client]
      |
      v
[Frontend / API Client]
      |
      v
[API Gateway / Router / Middleware]
      |
      v
[Application Service]
   |       |        |
   v       v        v
[DB]   [Queue]   [Object Storage]
   |
   v
[Logging / Monitoring]
```

---

## 12. Threat Model Summary

### 12.1 Threat Model Narrative

```text
<Describe assets, actors, trust boundaries, abuse cases, sensitive data flows, authentication zones, authorization zones, attack surfaces, privileged operations, and high-risk workflows.>
```

### 12.2 Threat Model Table

| Asset     | Threat Actor     | Abuse Case     | Existing Control     | Review Focus     | Risk     |
| --------- | ---------------- | -------------- | -------------------- | ---------------- | -------- |
| `<asset>` | `<threat_actor>` | `<abuse_case>` | `<existing_control>` | `<review_focus>` | `<risk>` |

### 12.3 Trust Boundaries

| Boundary     | Untrusted Side     | Trusted Side     | Enforcement Point            | Notes     |
| ------------ | ------------------ | ---------------- | ---------------------------- | --------- |
| `<boundary>` | `<untrusted_side>` | `<trusted_side>` | `<file_function_or_control>` | `<notes>` |

### 12.4 Sensitive Data Flows

| Flow ID      | Source     | Destination     | Data Type     | Controls     | Risk     |
| ------------ | ---------- | --------------- | ------------- | ------------ | -------- |
| `<FLOW-001>` | `<source>` | `<destination>` | `<data_type>` | `<controls>` | `<risk>` |

### 12.5 Abuse Cases

| Abuse Case ID | Scenario     | Impact     | Relevant Code Paths | Notes     |
| ------------- | ------------ | ---------- | ------------------- | --------- |
| `<ABUSE-001>` | `<scenario>` | `<impact>` | `<code_paths>`      | `<notes>` |

---

## 13. Security-Critical Code Path Inventory

| Code Path                       | File(s)        | Function(s)        | Security Relevance     | Review Status | Evidence        |
| ------------------------------- | -------------- | ------------------ | ---------------------- | ------------- | --------------- |
| Authentication                  | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Authorization                   | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Session Management              | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Token Generation and Validation | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Password Reset                  | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| MFA                             | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| File Upload                     | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Payment or Transaction Logic    | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Admin Actions                   | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| User Role Changes               | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Tenant Isolation                | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Deserialization                 | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Template Rendering              | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| SQL / NoSQL Queries             | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| OS Command Execution            | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| SSRF-Prone Outbound Requests    | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Webhooks                        | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Cryptography                    | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Secrets Handling                | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Logging of Sensitive Events     | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| Background Jobs                 | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |
| API Gateways or Middleware      | `<file_paths>` | `<function_names>` | `<security_relevance>` | `<status>`    | `<evidence_id>` |

---

## 14. Source-to-Sink Analysis

### 14.1 Source-to-Sink Summary

```text
<Describe the major source-to-sink traces reviewed, including user-controlled sources, transformations, validation points, authorization checks, encoding points, dangerous sinks, trust boundary crossings, data stores, and output contexts.>
```

### 14.2 Source-to-Sink Trace Table

| Trace ID     | Source           | Transformations     | Control Checks                | Sink               | Risk     | Status                                            |
| ------------ | ---------------- | ------------------- | ----------------------------- | ------------------ | -------- | ------------------------------------------------- |
| `<trace_id>` | `<input_source>` | `<transformations>` | `<validation_authz_encoding>` | `<dangerous_sink>` | `<risk>` | `<confirmed_safe / vulnerable / needs_follow_up>` |

### 14.3 Trace Detail Block

```text
Trace ID: <trace_id>
Source: <input_source>
Path: <file:function -> file:function -> sink>
Security Controls Observed: <validation/authz/encoding>
Sink: <dangerous_sink>
Conclusion: <confirmed_safe / vulnerable / needs_follow_up>
Confidence: <Low / Medium / High>
```

### 14.4 Source Categories

* [ ] HTTP query parameters
* [ ] HTTP body parameters
* [ ] HTTP headers
* [ ] Cookies
* [ ] File uploads
* [ ] Webhooks
* [ ] Message queues
* [ ] CLI arguments
* [ ] Environment variables
* [ ] Configuration files
* [ ] External API responses
* [ ] Database records from lower-trust sources
* [ ] GraphQL variables
* [ ] WebSocket messages
* [ ] Serialized objects

### 14.5 Sink Categories

* [ ] SQL / NoSQL query
* [ ] OS command execution
* [ ] Template rendering
* [ ] File path access
* [ ] File write or overwrite
* [ ] Outbound HTTP request
* [ ] Deserialization
* [ ] XML parsing
* [ ] HTML rendering
* [ ] Redirect or forward
* [ ] Authentication decision
* [ ] Authorization decision
* [ ] Cryptographic operation
* [ ] Logging
* [ ] LDAP query
* [ ] Expression evaluation
* [ ] Reflection or dynamic invocation
* [ ] Dynamic code loading

---

## 15. Authentication Review

### 15.1 Authentication Summary

```text
<Summarize authentication design, code paths reviewed, control effectiveness, and notable gaps.>
```

### 15.2 Authentication Review Table

| Area                         | File / Function   | Observation     | Risk     | Evidence        | Recommendation     |
| ---------------------------- | ----------------- | --------------- | -------- | --------------- | ------------------ |
| Login Logic                  | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Registration Logic           | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Password Reset               | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Password Change              | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| MFA                          | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| SSO                          | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| OAuth / OIDC / SAML          | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Magic Links                  | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Account Recovery             | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Remember-Me Tokens           | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Brute-Force Protections      | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Username Enumeration         | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Credential Storage           | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Default Credentials          | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Authentication Bypass Paths  | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Session Creation After Login | `<file_function>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |

### 15.3 Authentication Evidence

```text
<sanitized_authentication_code_or_tool_output>
```

```http
<sanitized_authentication_request_or_response>
```

---

## 16. Authorization and Access Control Review

### 16.1 Authorization Summary

```text
<Summarize authorization model, role checks, object-level controls, tenant isolation, middleware behavior, and confirmed gaps.>
```

### 16.2 Authorization Review Matrix

| Test / Review Case | Role A     | Role B     | File / Function / Endpoint | Expected Control     | Observed Control     | Evidence        |
| ------------------ | ---------- | ---------- | -------------------------- | -------------------- | -------------------- | --------------- |
| `<case>`           | `<role_a>` | `<role_b>` | `<file_function_endpoint>` | `<expected_control>` | `<observed_control>` | `<evidence_id>` |

### 16.3 Authorization Areas Reviewed

* [ ] Role checks
* [ ] Permission checks
* [ ] Object-level authorization
* [ ] Function-level authorization
* [ ] Tenant isolation
* [ ] Admin-only operations
* [ ] Horizontal privilege escalation
* [ ] Vertical privilege escalation
* [ ] IDOR / BOLA
* [ ] Mass assignment
* [ ] Forced browsing
* [ ] API authorization
* [ ] GraphQL authorization
* [ ] Server-side authorization versus client-side-only controls
* [ ] Middleware bypasses
* [ ] Background job authorization

### 16.4 Authorization Evidence

```text
<sanitized_authorization_code_or_tool_output>
```

```http
<sanitized_authorization_request_or_response>
```

---

## 17. Input Validation and Injection Review

### 17.1 Input Validation Summary

```text
<Summarize input validation, parsing, encoding, injection testing, and source-code patterns related to unsafe handling of user-controlled input.>
```

### 17.2 Input and Injection Review Matrix

| Input Vector     | File / Function   | Sink     | Control Observed                  | Result                                  | Evidence        |
| ---------------- | ----------------- | -------- | --------------------------------- | --------------------------------------- | --------------- |
| `<input_vector>` | `<file_function>` | `<sink>` | `<validation_or_missing_control>` | `<safe / vulnerable / needs_follow_up>` | `<evidence_id>` |

### 17.3 Injection Areas Reviewed

* [ ] SQL injection
* [ ] NoSQL injection
* [ ] LDAP injection
* [ ] XPath injection
* [ ] OS command injection
* [ ] Server-side template injection
* [ ] Expression language injection
* [ ] Header injection
* [ ] CRLF injection
* [ ] Log injection
* [ ] XML injection
* [ ] XXE
* [ ] HTML injection
* [ ] Unsafe deserialization
* [ ] Path traversal
* [ ] File inclusion
* [ ] Unsafe eval / reflection / dynamic execution

### 17.4 Evidence

```text
<sanitized_code_snippet_or_tool_output>
```

```http
<sanitized_validation_request_or_response>
```

---

## 18. API Security Review

### 18.1 API Summary

```text
<Summarize API endpoints reviewed, route definitions, middleware, authentication, authorization, data exposure, abuse controls, and API-specific findings.>
```

### 18.2 API Review Table

| Endpoint     | Method     | File / Handler      | Auth Required | Role Required | Sensitive Data | Finding / Observation      |
| ------------ | ---------- | ------------------- | ------------- | ------------- | -------------- | -------------------------- |
| `<endpoint>` | `<method>` | `<file_or_handler>` | `<Yes / No>`  | `<role>`      | `<Yes / No>`   | `<finding_or_observation>` |

### 18.3 API Areas Reviewed

* [ ] Endpoint inventory
* [ ] Route definitions
* [ ] Middleware
* [ ] Authentication enforcement
* [ ] Authorization enforcement
* [ ] BOLA / IDOR
* [ ] Mass assignment
* [ ] Excessive data exposure
* [ ] Rate limiting
* [ ] Pagination abuse
* [ ] Filtering abuse
* [ ] Sorting abuse
* [ ] GraphQL introspection
* [ ] GraphQL query depth
* [ ] GraphQL query complexity
* [ ] REST method override
* [ ] SOAP / XML handling
* [ ] Webhook validation
* [ ] API versioning
* [ ] Error handling

### 18.4 API Evidence

```text
<sanitized_api_route_or_handler_code>
```

```http
<sanitized_api_request_or_response>
```

---

## 19. Business Logic Review

### 19.1 Business Logic Summary

```text
<Summarize sensitive workflows, expected business rules, observed logic, abuse cases, and confirmed logic weaknesses.>
```

### 19.2 Business Logic Review Table

| Workflow     | File / Function   | Expected Control     | Observed Logic     | Risk     | Evidence        |
| ------------ | ----------------- | -------------------- | ------------------ | -------- | --------------- |
| `<workflow>` | `<file_function>` | `<expected_control>` | `<observed_logic>` | `<risk>` | `<evidence_id>` |

### 19.3 Business Logic Areas Reviewed

* [ ] Multi-step workflow bypass
* [ ] Transaction manipulation
* [ ] Price manipulation
* [ ] Quantity manipulation
* [ ] Coupon / discount abuse
* [ ] Race conditions
* [ ] Replay attacks
* [ ] Approval bypass
* [ ] Subscription logic
* [ ] Payment workflow abuse
* [ ] Account lifecycle abuse
* [ ] Privilege workflow abuse
* [ ] Trust boundary violations
* [ ] State-machine flaws

### 19.4 Business Logic Evidence

```text
<sanitized_business_logic_code_or_notes>
```

```http
<sanitized_business_logic_request_or_response>
```

---

## 20. File Upload and Parser Review

### 20.1 File Handling Summary

```text
<Summarize file upload paths, parser behavior, validation controls, storage behavior, access control, and file-processing risks.>
```

### 20.2 File Upload and Parser Review Table

| Upload / Parser Path      | File / Function   | Validation Observed     | Risk     | Evidence        |
| ------------------------- | ----------------- | ----------------------- | -------- | --------------- |
| `<upload_or_parser_path>` | `<file_function>` | `<validation_observed>` | `<risk>` | `<evidence_id>` |

### 20.3 File Handling Areas Reviewed

* [ ] File type validation
* [ ] MIME validation
* [ ] Extension validation
* [ ] Magic-byte validation
* [ ] File size limits
* [ ] Malware scanning integration
* [ ] Image processing
* [ ] Archive extraction
* [ ] Zip slip
* [ ] Path traversal
* [ ] SVG / script handling
* [ ] Metadata exposure
* [ ] Public file access
* [ ] Signed URL access
* [ ] Stored XSS via uploaded files

### 20.4 File Handling Evidence

```text
<sanitized_file_upload_or_parser_code>
```

```http
<sanitized_file_upload_request_or_response>
```

---

## 21. Cryptography and Secrets Review

### 21.1 Cryptography and Secrets Summary

```text
<Summarize secrets handling, cryptographic controls, token handling, key storage, key rotation, TLS validation, and related observations.>
```

### 21.2 Crypto and Secrets Table

| Secret / Crypto Area      | Location     | Observation     | Risk     | Evidence        | Recommendation     |
| ------------------------- | ------------ | --------------- | -------- | --------------- | ------------------ |
| `<secret_or_crypto_area>` | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |

### 21.3 Areas Reviewed

* [ ] Hardcoded secrets
* [ ] API keys
* [ ] Private keys
* [ ] Tokens
* [ ] Password handling
* [ ] Password reset tokens
* [ ] Weak algorithms
* [ ] Custom crypto
* [ ] Insecure randomness
* [ ] Static IVs
* [ ] Missing integrity protection
* [ ] Key storage
* [ ] Key rotation
* [ ] TLS validation
* [ ] Certificate validation
* [ ] Secrets in logs
* [ ] Secrets in frontend code
* [ ] Secrets in CI/CD

### 21.4 Evidence

```text
<sanitized_secret_crypto_or_sensitive_data_evidence>
```

---

## 22. Dependency and Supply-Chain Review

### 22.1 Dependency Summary

```text
<Summarize dependency review, vulnerable packages, dependency reachability, lockfile review, package manager configuration, container base images, SBOM location, and supply-chain risks.>
```

### 22.2 Dependency Review Table

| Dependency     | Version     | Risk / CVE      | Reachability                            | Recommendation     | Evidence        |
| -------------- | ----------- | --------------- | --------------------------------------- | ------------------ | --------------- |
| `<dependency>` | `<version>` | `<risk_or_cve>` | `<reachable / not_reachable / unknown>` | `<recommendation>` | `<evidence_id>` |

### 22.3 Supply-Chain Areas Reviewed

* [ ] Direct dependencies
* [ ] Transitive dependencies
* [ ] Vulnerable packages
* [ ] Unmaintained libraries
* [ ] Typosquatting risk
* [ ] Dependency confusion risk
* [ ] Lockfile review
* [ ] Build scripts
* [ ] Package manager configuration
* [ ] Container base images
* [ ] SBOM location
* [ ] CI/CD dependency policies
* [ ] License risk

### 22.4 Dependency Tool Output

```text
<sanitized_sca_or_dependency_audit_output>
```

---

## 23. Configuration, IaC, and Deployment Review

### 23.1 Configuration Summary

```text
<Summarize application configuration, IaC posture, deployment risk, IAM, storage, network controls, container configuration, CI/CD workflows, secrets management, and logging configuration.>
```

### 23.2 Configuration Review Table

| Configuration Area     | File / Resource      | Observation     | Risk     | Recommendation     |
| ---------------------- | -------------------- | --------------- | -------- | ------------------ |
| `<configuration_area>` | `<file_or_resource>` | `<observation>` | `<risk>` | `<recommendation>` |

### 23.3 Areas Reviewed

* [ ] Environment variables
* [ ] Debug mode
* [ ] CORS configuration
* [ ] Security headers
* [ ] TLS settings
* [ ] Cloud IAM
* [ ] Storage bucket permissions
* [ ] Security groups / firewall rules
* [ ] Kubernetes manifests
* [ ] Dockerfiles
* [ ] CI/CD workflows
* [ ] Secrets management
* [ ] Logging configuration
* [ ] Least privilege
* [ ] Network segmentation

### 23.4 Configuration Evidence

```text
<sanitized_configuration_iac_or_deployment_output>
```

---

## 24. Error Handling, Logging, and Monitoring Review

### 24.1 Error Handling and Logging Summary

```text
<Summarize sensitive data in logs, stack traces, verbose errors, audit events, admin action logs, security alerting, log injection risk, PII handling, correlation IDs, and tamper resistance.>
```

### 24.2 Error Handling and Logging Table

| Event / Error Area      | File / Function   | Observation     | Risk     | Recommendation     |
| ----------------------- | ----------------- | --------------- | -------- | ------------------ |
| `<event_or_error_area>` | `<file_function>` | `<observation>` | `<risk>` | `<recommendation>` |

### 24.3 Areas Reviewed

* [ ] Sensitive data in logs
* [ ] Stack traces
* [ ] Verbose errors
* [ ] Authentication failure logs
* [ ] Authorization failure logs
* [ ] Audit events
* [ ] Admin action logs
* [ ] Security alerting
* [ ] Log injection
* [ ] PII handling
* [ ] Correlation IDs
* [ ] Tamper resistance

### 24.4 Evidence

```text
<sanitized_log_error_or_monitoring_evidence>
```

---

## 25. Vulnerability Validation Summary

### 25.1 Validation Summary

```text
<Summarize candidate issues identified, false positives removed, confirmed vulnerabilities, unvalidated issues, dynamic validation performed, environmental constraints, and exploitability notes.>
```

### 25.2 Candidate and Confirmed Issue Table

| Candidate Vulnerability     | File / Function / Endpoint | Source                                                                      | Validation Method     | Status                                                  | Evidence        |
| --------------------------- | -------------------------- | --------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------- | --------------- |
| `<candidate_vulnerability>` | `<file_function_endpoint>` | `<manual / SAST / SCA / secret_scan / source_to_sink / dynamic_validation>` | `<validation_method>` | `<confirmed / false_positive / unvalidated / accepted>` | `<evidence_id>` |

### 25.3 Dynamic Validation Notes

```text
<Describe any authorized dynamic validation performed and the safety limits used.>
```

### 25.4 False Positives Removed

| Suspected Issue     | Reason Removed | Evidence        |
| ------------------- | -------------- | --------------- |
| `<suspected_issue>` | `<reason>`     | `<evidence_id>` |

### 25.5 Environmental Constraints

| Constraint     | Impact     | Notes     |
| -------------- | ---------- | --------- |
| `<constraint>` | `<impact>` | `<notes>` |

---

## 26. Exploitability Analysis

### 26.1 Exploitability Summary

```text
<Summarize whether confirmed or high-risk issues are reachable, controllable, impactful, and safely validated. Avoid weaponized exploitation instructions.>
```

### 26.2 Exploitability Table

| Finding ID     | Reachable?                       | Controllable?                    | Impactful?                       | Exploitability          | Evidence        |
| -------------- | -------------------------------- | -------------------------------- | -------------------------------- | ----------------------- | --------------- |
| `<finding_id>` | `<Yes / No / Partial / Unknown>` | `<Yes / No / Partial / Unknown>` | `<Yes / No / Partial / Unknown>` | `<Low / Medium / High>` | `<evidence_id>` |

### 26.3 Exploitability Factors

| Factor                  | Value                                 | Notes     |
| ----------------------- | ------------------------------------- | --------- |
| Preconditions           | `<preconditions>`                     | `<notes>` |
| Required Privileges     | `<None / Low / High / Specific Role>` | `<notes>` |
| User Interaction        | `<Yes / No>`                          | `<notes>` |
| Attack Complexity       | `<Low / High>`                        | `<notes>` |
| Reachability            | `<reachable_status>`                  | `<notes>` |
| Controllability         | `<controllability_status>`            | `<notes>` |
| Existing Controls       | `<existing_controls>`                 | `<notes>` |
| Proof of Exploitability | `<safe_validation_summary>`           | `<notes>` |
| Business Impact         | `<business_impact>`                   | `<notes>` |
| Safety Limitations      | `<safety_limitations>`                | `<notes>` |

---

## 27. Attack Path Narrative

### 27.1 Attack Path Summary

```text
Attack Path <ID>:
<source_code_weakness>
  -> <reachable_endpoint_or_workflow>
  -> <validated_security_control_failure>
  -> <impact>
  -> <business_risk>
```

### 27.2 Attack Path Table

| Step | Code Path / Endpoint      | Action     | Result     | Evidence        | Risk     |
| ---: | ------------------------- | ---------- | ---------- | --------------- | -------- |
|  `1` | `<code_path_or_endpoint>` | `<action>` | `<result>` | `<evidence_id>` | `<risk>` |
|  `2` | `<code_path_or_endpoint>` | `<action>` | `<result>` | `<evidence_id>` | `<risk>` |
|  `3` | `<code_path_or_endpoint>` | `<action>` | `<result>` | `<evidence_id>` | `<risk>` |

### 27.3 Attack Path Metadata

| Field                    | Value                         |
| ------------------------ | ----------------------------- |
| Attack Path ID           | `<AP-001>`                    |
| Preconditions            | `<preconditions>`             |
| Access Level Required    | `<access_level_required>`     |
| Role Required            | `<role_required>`             |
| Data Exposed or Modified | `<data_exposed_or_modified>`  |
| Business Impact          | `<business_impact>`           |
| Detection Opportunities  | `<detection_opportunities>`   |
| Cleanup Performed        | `<Yes / No / Not Applicable>` |

### 27.4 Attack Path Diagram

```text
<Source-Code Weakness>
        |
        v
<Reachable Endpoint or Workflow>
        |
        v
<Missing or Failed Control>
        |
        v
<Validated Security Impact>
        |
        v
<Business Risk>
```

---

## 28. Findings Summary

| ID             | Finding Title     | Severity                                           | Confidence              | Affected File / Component      | Affected Endpoint     | Status                                                                                         |
| -------------- | ----------------- | -------------------------------------------------- | ----------------------- | ------------------------------ | --------------------- | ---------------------------------------------------------------------------------------------- |
| `<finding_id>` | `<finding_title>` | `<Informational / Low / Medium / High / Critical>` | `<Low / Medium / High>` | `<affected_file_or_component>` | `<affected_endpoint>` | `<Open / Fixed / Partially Fixed / Accepted Risk / False Positive / Duplicate / Needs Retest>` |

---

## 29. Detailed Finding Template

## Finding `<finding_id>`: `<finding_title>`

| Field                | Value                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| Severity             | `<Informational / Low / Medium / High / Critical>`                                             |
| Confidence           | `<Low / Medium / High>`                                                                        |
| Status               | `<Open / Fixed / Partially Fixed / Accepted Risk / False Positive / Duplicate / Needs Retest>` |
| Affected Repository  | `<repository>`                                                                                 |
| Branch / Commit      | `<branch_commit>`                                                                              |
| Affected File(s)     | `<file_paths>`                                                                                 |
| Affected Function(s) | `<function_names>`                                                                             |
| Affected Endpoint(s) | `<endpoints>`                                                                                  |
| Affected Role(s)     | `<roles>`                                                                                      |
| CVSS                 | `<vector_score>`                                                                               |
| CWE                  | `<CWE-ID>`                                                                                     |
| OWASP Web Top 10     | `<category_if_applicable>`                                                                     |
| OWASP API Top 10     | `<category_if_applicable>`                                                                     |
| MITRE ATT&CK         | `<technique_id_if_applicable>`                                                                 |
| Evidence IDs         | `<evidence_ids>`                                                                               |
| Related Attack Path  | `<attack_path_id>`                                                                             |

### 29.1 Executive Description

```text
<Explain the issue in plain business language. Describe why it matters and what risk it creates.>
```

### 29.2 Technical Description

```text
<Explain the technical weakness, affected code path, endpoint, parameter, workflow, control failure, or vulnerable behavior.>
```

### 29.3 Facts

| Fact ID      | Fact               | Evidence        | Confidence              |
| ------------ | ------------------ | --------------- | ----------------------- |
| `<FACT-001>` | `<confirmed_fact>` | `<evidence_id>` | `<Low / Medium / High>` |

### 29.4 Hypotheses

| Hypothesis ID | Hypothesis     | Validation Method          | Result                                  | Confidence              |
| ------------- | -------------- | -------------------------- | --------------------------------------- | ----------------------- |
| `<HYP-001>`   | `<hypothesis>` | `<safe_validation_method>` | `<confirmed / rejected / inconclusive>` | `<Low / Medium / High>` |

### 29.5 Vulnerable Code Reference

```text
File: <file_path>
Function: <function_name>
Lines: <line_numbers>
Commit: <commit_hash>
```

```text
<sanitized_vulnerable_code_snippet>
```

### 29.6 Source-to-Sink Trace

```text
<source>
  -> <intermediate_function>
  -> <validation_or_missing_control>
  -> <sink>
```

### 29.7 Evidence

```text
<sanitized_evidence>
```

### 29.8 HTTP Request / Response Evidence, If Applicable

```http
<sanitized_request>
```

```http
<sanitized_response>
```

### 29.9 Safe Reproduction / Validation Steps

1. `<step_1>`
2. `<step_2>`
3. `<step_3>`

### 29.10 Impact

```text
<Describe technical and business impact. Separate confirmed impact from potential impact.>
```

### 29.11 Likelihood

```text
<Describe exploitability, preconditions, exposure, required role, user interaction, and attacker effort.>
```

### 29.12 Root Cause

```text
<Describe the underlying code, configuration, design, process, or control failure.>
```

### 29.13 Remediation

```text
<Provide direct remediation steps, including tactical fixes and strategic improvements.>
```

### 29.14 Secure Implementation Guidance

```text
<secure_code_example_or_pseudocode>
```

### 29.15 Regression Test Recommendation

```text
<test_case_or_pseudocode>
```

### 29.16 Detection Opportunities

```text
<Describe logs, telemetry, alert logic, or monitoring opportunities.>
```

### 29.17 Retest Procedure

```text
<Describe how to safely verify remediation.>
```

### 29.18 References

| Reference     | Description     |
| ------------- | --------------- |
| `<reference>` | `<description>` |

---

## 30. False Positive / Dismissed Finding Log

| ID         | Suspected Issue     | File / Function   | Reason Dismissed     | Evidence        | Reviewer     |
| ---------- | ------------------- | ----------------- | -------------------- | --------------- | ------------ |
| `<FP-001>` | `<suspected_issue>` | `<file_function>` | `<reason_dismissed>` | `<evidence_id>` | `<reviewer>` |

---

## 31. Security Control Observations

| Control                    | Observation     | Effectiveness                                                    | Recommendation     |
| -------------------------- | --------------- | ---------------------------------------------------------------- | ------------------ |
| Authentication Framework   | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Authorization Framework    | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Input Validation Framework | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Output Encoding Framework  | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| ORM Usage                  | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| CSRF Protection            | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| CORS Handling              | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Error Handling             | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Logging                    | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Dependency Management      | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| CI/CD Security Gates       | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Secure Coding Standards    | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Threat Model Maturity      | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |

---

## 32. Risk Rating Methodology

### 32.1 Severity Model

| Severity      | Definition     |
| ------------- | -------------- |
| Critical      | `<definition>` |
| High          | `<definition>` |
| Medium        | `<definition>` |
| Low           | `<definition>` |
| Informational | `<definition>` |

### 32.2 Confidence Model

| Confidence | Definition     |
| ---------- | -------------- |
| High       | `<definition>` |
| Medium     | `<definition>` |
| Low        | `<definition>` |

### 32.3 Likelihood Factors

| Factor                    | Description     |
| ------------------------- | --------------- |
| Exposure                  | `<description>` |
| Exploitability            | `<description>` |
| Required Access           | `<description>` |
| Attack Complexity         | `<description>` |
| Existing Controls         | `<description>` |
| Reachability              | `<description>` |
| Controllability           | `<description>` |
| Required User Interaction | `<description>` |

### 32.4 Impact Factors

| Factor                 | Description     |
| ---------------------- | --------------- |
| Confidentiality        | `<description>` |
| Integrity              | `<description>` |
| Availability           | `<description>` |
| Business Criticality   | `<description>` |
| Regulatory Exposure    | `<description>` |
| Fraud Potential        | `<description>` |
| Operational Disruption | `<description>` |
| Tenant Isolation       | `<description>` |

### 32.5 Environmental Modifiers

| Modifier               | Description     |
| ---------------------- | --------------- |
| Asset Criticality      | `<description>` |
| Compensating Controls  | `<description>` |
| Monitoring Visibility  | `<description>` |
| Remediation Complexity | `<description>` |
| Deployment Exposure    | `<description>` |

---

## 33. Remediation Roadmap

### 33.1 Prioritized Roadmap

| Priority              | Finding ID     | Remediation     | Owner     | Effort                  | Target Date    | Risk Reduction     |
| --------------------- | -------------- | --------------- | --------- | ----------------------- | -------------- | ------------------ |
| `<P0 / P1 / P2 / P3>` | `<finding_id>` | `<remediation>` | `<owner>` | `<Low / Medium / High>` | `<YYYY-MM-DD>` | `<risk_reduction>` |

### 33.2 Immediate Actions

* [ ] `<immediate_action_1>`
* [ ] `<immediate_action_2>`
* [ ] `<immediate_action_3>`

### 33.3 30-Day Actions

* [ ] `<30_day_action_1>`
* [ ] `<30_day_action_2>`
* [ ] `<30_day_action_3>`

### 33.4 60-Day Actions

* [ ] `<60_day_action_1>`
* [ ] `<60_day_action_2>`
* [ ] `<60_day_action_3>`

### 33.5 90-Day Actions

* [ ] `<90_day_action_1>`
* [ ] `<90_day_action_2>`
* [ ] `<90_day_action_3>`

### 33.6 Strategic Improvements

* [ ] `<strategic_improvement_1>`
* [ ] `<strategic_improvement_2>`
* [ ] `<strategic_improvement_3>`

### 33.7 Secure SDLC Improvements

* [ ] Add security requirements for affected risk classes.
* [ ] Add threat modeling for sensitive workflows.
* [ ] Add abuse-case testing.
* [ ] Add authorization regression tests.
* [ ] Add SAST checks in CI/CD.
* [ ] Add SCA checks in CI/CD.
* [ ] Add secret scanning in CI/CD.
* [ ] Add IaC scanning in CI/CD.
* [ ] Add code-owner reviews for security-critical paths.
* [ ] Add secure code review gates for high-risk changes.

### 33.8 Long-Term Architecture Changes

* [ ] `<architecture_change_1>`
* [ ] `<architecture_change_2>`
* [ ] `<architecture_change_3>`

---

## 34. Secure Patch Guidance

### 34.1 Patch Guidance Table

| Finding ID     | Unsafe Pattern     | Safe Pattern     | Patch Owner     | Regression Test     |
| -------------- | ------------------ | ---------------- | --------------- | ------------------- |
| `<finding_id>` | `<unsafe_pattern>` | `<safe_pattern>` | `<patch_owner>` | `<regression_test>` |

### 34.2 Code-Level Recommendations

```text
<Describe code-level remediation recommendations, safer APIs, validation controls, authorization checks, error handling changes, and data handling improvements.>
```

### 34.3 Framework-Specific Secure APIs

```text
<Describe recommended framework features, libraries, middleware, or secure APIs.>
```

### 34.4 Centralized Control Recommendations

```text
<Describe controls that should be centralized, such as authorization middleware, validation schemas, output encoding helpers, logging redaction, or secret retrieval.>
```

### 34.5 Migration and Compatibility Risks

| Risk                        | Impact     | Mitigation     |
| --------------------------- | ---------- | -------------- |
| Migration Risk              | `<impact>` | `<mitigation>` |
| Backward Compatibility Risk | `<impact>` | `<mitigation>` |
| Performance Risk            | `<impact>` | `<mitigation>` |
| Operational Risk            | `<impact>` | `<mitigation>` |

### 34.6 Test Coverage Requirements

```text
<Describe unit, integration, security, negative, authorization matrix, and regression tests required to validate the patch.>
```

---

## 35. Regression and Verification Testing

### 35.1 Regression Testing Table

| Test Type                 | Finding ID     | Test Case     | Expected Secure Behavior     | Owner     |
| ------------------------- | -------------- | ------------- | ---------------------------- | --------- |
| Unit Test                 | `<finding_id>` | `<test_case>` | `<expected_secure_behavior>` | `<owner>` |
| Integration Test          | `<finding_id>` | `<test_case>` | `<expected_secure_behavior>` | `<owner>` |
| Security Test             | `<finding_id>` | `<test_case>` | `<expected_secure_behavior>` | `<owner>` |
| Negative Test             | `<finding_id>` | `<test_case>` | `<expected_secure_behavior>` | `<owner>` |
| Authorization Matrix Test | `<finding_id>` | `<test_case>` | `<expected_secure_behavior>` | `<owner>` |
| API Test                  | `<finding_id>` | `<test_case>` | `<expected_secure_behavior>` | `<owner>` |
| Source-to-Sink Test       | `<finding_id>` | `<test_case>` | `<expected_secure_behavior>` | `<owner>` |
| SAST Rule                 | `<finding_id>` | `<test_case>` | `<expected_secure_behavior>` | `<owner>` |
| SCA Rule                  | `<finding_id>` | `<test_case>` | `<expected_secure_behavior>` | `<owner>` |
| CI/CD Gate                | `<finding_id>` | `<test_case>` | `<expected_secure_behavior>` | `<owner>` |
| Manual Retest Step        | `<finding_id>` | `<test_case>` | `<expected_secure_behavior>` | `<owner>` |

### 35.2 Test Example Placeholder

```text
<unit_integration_or_security_test_pseudocode>
```

### 35.3 Verification Commands

```bash
<safe_verification_command>
```

### 35.4 Verification Output

```text
<verification_output>
```

---

## 36. Detection and Monitoring Recommendations

### 36.1 Detection Opportunities

| Detection Opportunity     | Data Source     | Logic Summary     | Related Finding | Priority                |
| ------------------------- | --------------- | ----------------- | --------------- | ----------------------- |
| `<detection_opportunity>` | `<data_source>` | `<logic_summary>` | `<finding_id>`  | `<High / Medium / Low>` |

### 36.2 Monitoring Areas

* [ ] Authentication anomalies
* [ ] Authorization failures
* [ ] IDOR / BOLA attempts
* [ ] Suspicious parameter tampering
* [ ] Injection attempts
* [ ] File upload anomalies
* [ ] SSRF indicators
* [ ] Deserialization errors
* [ ] Excessive API requests
* [ ] Sensitive workflow abuse
* [ ] Admin action monitoring
* [ ] Payment or transaction anomalies
* [ ] Unexpected export activity
* [ ] Error spikes
* [ ] WAF or bot-control events
* [ ] Application security exceptions
* [ ] Dependency exploitation attempts

### 36.3 Detection Pseudocode Placeholder

```text
<insert vendor-neutral detection logic or SIEM rule placeholder>
```

---

## 37. Cleanup and Data Handling

### 37.1 Cleanup Summary

```text
<Describe cleanup actions performed after testing, including test accounts, data created, data modified, files uploaded, API keys, tokens, temporary users, temporary configuration changes, and evidence handling.>
```

### 37.2 Cleanup Table

| Item                            | Location     | Action Taken     | Evidence        | Status                                  |
| ------------------------------- | ------------ | ---------------- | --------------- | --------------------------------------- |
| Test Accounts Used              | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Data Created                    | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Data Modified                   | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Files Uploaded                  | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| API Keys or Tokens Generated    | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Temporary Users                 | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Temporary Configuration Changes | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Sensitive Data Observed         | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Evidence Redaction              | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Evidence Storage                | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |
| Evidence Deletion Schedule      | `<location>` | `<action_taken>` | `<evidence_id>` | `<complete / pending / not_applicable>` |

### 37.3 Evidence Redaction Guidance

* [ ] Redact passwords, tokens, API keys, private keys, session identifiers, and reset links.
* [ ] Redact PII unless explicitly required for proof.
* [ ] Redact customer data and regulated data.
* [ ] Redact proprietary source code unless required to support a finding.
* [ ] Preserve enough context for validation.
* [ ] Store raw evidence only in approved restricted locations.
* [ ] Reference raw evidence by evidence ID when direct inclusion is inappropriate.

---

## 38. Retest Plan

### 38.1 Retest Scope

```text
<Describe which findings, files, functions, endpoints, roles, workflows, controls, or code paths should be retested.>
```

### 38.2 Retest Table

| Finding ID     | Retest Step     | Expected Result     | Status                                      | Evidence        |
| -------------- | --------------- | ------------------- | ------------------------------------------- | --------------- |
| `<finding_id>` | `<retest_step>` | `<expected_result>` | `<not_started / passed / failed / partial>` | `<evidence_id>` |

### 38.3 Retest Metadata

| Field                    | Value                        |
| ------------------------ | ---------------------------- |
| Retest Timeline          | `<retest_timeline>`          |
| Fixed Branch / Commit    | `<fixed_branch_commit>`      |
| Required Evidence        | `<required_evidence>`        |
| Retest Methodology       | `<retest_methodology>`       |
| Expected Secure Behavior | `<expected_secure_behavior>` |
| Responsible Parties      | `<responsible_parties>`      |

### 38.4 Responsible Parties

| Role              | Name / Team  | Responsibility     |
| ----------------- | ------------ | ------------------ |
| Client Owner      | `<owner>`    | `<responsibility>` |
| Engineering Owner | `<owner>`    | `<responsibility>` |
| Retest Tester     | `<tester>`   | `<responsibility>` |
| Security Reviewer | `<reviewer>` | `<responsibility>` |

---

## 39. Evidence Index

| Evidence ID     | Description     | Type                                                                                                                                                                                                                                 | Path / Link      | Timestamp     | Related Finding |
| --------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | ------------- | --------------- |
| `<evidence_id>` | `<description>` | `<code_snippet / source_to_sink_trace / SAST_output / SCA_output / secret_scan_output / HTTP_request / HTTP_response / screenshot / application_log / stack_trace / test_output / pull_request / commit_diff / client_confirmation>` | `<path_or_link>` | `<timestamp>` | `<finding_id>`  |

### 39.1 Evidence Storage Layout

```text
<evidence_root>/
├── 00_scope/
├── 01_repository_inventory/
├── 02_build_setup/
├── 03_architecture/
├── 04_threat_model/
├── 05_source_to_sink/
├── 06_manual_review/
├── 07_sast/
├── 08_sca/
├── 09_secrets/
├── 10_iac/
├── 11_dynamic_validation/
├── 12_findings/
├── 13_requests_responses/
├── 14_code_references/
├── 15_tool_output/
├── 16_cleanup/
├── 17_retest/
└── 18_report/
```

---

## 40. Code Reference Index

| Reference ID | Repository     | Branch / Commit   | File          | Function          | Lines            | Related Finding |
| ------------ | -------------- | ----------------- | ------------- | ----------------- | ---------------- | --------------- |
| `<CODE-001>` | `<repository>` | `<branch_commit>` | `<file_path>` | `<function_name>` | `<line_numbers>` | `<finding_id>`  |

---

## 41. Request / Response Appendix

### 41.1 Request / Response Index

| Request ID  | Endpoint     | Purpose     | Related Finding | Evidence Path     |
| ----------- | ------------ | ----------- | --------------- | ----------------- |
| `<REQ-001>` | `<endpoint>` | `<purpose>` | `<finding_id>`  | `<evidence_path>` |

### 41.2 Sanitized HTTP Request

```http
<sanitized_http_request>
```

### 41.3 Sanitized HTTP Response

```http
<sanitized_http_response>
```

---

## 42. Tool Output Appendix

### 42.1 SAST Results

```text
<sanitized_sast_results>
```

### 42.2 SCA Results

```text
<sanitized_sca_results>
```

### 42.3 Secret Scanning Results

```text
<sanitized_secret_scanning_results>
```

### 42.4 IaC Scanning Results

```text
<sanitized_iac_scanning_results>
```

### 42.5 Dependency Audit Output

```text
<sanitized_dependency_audit_output>
```

### 42.6 Unit / Security Test Output

```text
<sanitized_unit_or_security_test_output>
```

### 42.7 Build Output

```text
<sanitized_build_output>
```

### 42.8 Manual Validation Logs

```text
<sanitized_manual_validation_logs>
```

---

## 43. Limitations

### 43.1 Assessment Limitations

| Limitation                           | Impact     | Notes     |
| ------------------------------------ | ---------- | --------- |
| Scope Limitations                    | `<impact>` | `<notes>` |
| Time Limitations                     | `<impact>` | `<notes>` |
| Repository Access Limitations        | `<impact>` | `<notes>` |
| Build Limitations                    | `<impact>` | `<notes>` |
| Test Environment Limitations         | `<impact>` | `<notes>` |
| Missing Roles / Accounts             | `<impact>` | `<notes>` |
| Unavailable Documentation            | `<impact>` | `<notes>` |
| Unavailable API Specifications       | `<impact>` | `<notes>` |
| Third-Party Integration Restrictions | `<impact>` | `<notes>` |
| Dynamic Testing Restrictions         | `<impact>` | `<notes>` |
| Unvalidated Findings                 | `<impact>` | `<notes>` |
| Assumptions                          | `<impact>` | `<notes>` |

### 43.2 Untested Areas

| Area     | Reason Not Tested | Risk     | Recommendation     |
| -------- | ----------------- | -------- | ------------------ |
| `<area>` | `<reason>`        | `<risk>` | `<recommendation>` |

---

## 44. Appendix: Terms and Definitions

| Term                    | Definition     |
| ----------------------- | -------------- |
| Source-to-Sink Analysis | `<definition>` |
| Source                  | `<definition>` |
| Sink                    | `<definition>` |
| Trust Boundary          | `<definition>` |
| Authentication          | `<definition>` |
| Authorization           | `<definition>` |
| IDOR                    | `<definition>` |
| BOLA                    | `<definition>` |
| Injection               | `<definition>` |
| XSS                     | `<definition>` |
| SSRF                    | `<definition>` |
| Deserialization         | `<definition>` |
| Business Logic Flaw     | `<definition>` |
| Exploitability          | `<definition>` |
| Reachability            | `<definition>` |
| Controllability         | `<definition>` |
| Impact                  | `<definition>` |
| Likelihood              | `<definition>` |
| Compensating Control    | `<definition>` |
| False Positive          | `<definition>` |
| Accepted Risk           | `<definition>` |
| Residual Risk           | `<definition>` |

---

## 45. Appendix: References

| Reference Type                   | Reference     | Notes     |
| -------------------------------- | ------------- | --------- |
| OWASP Web Security Testing Guide | `<reference>` | `<notes>` |
| OWASP Web Top 10                 | `<reference>` | `<notes>` |
| OWASP API Top 10                 | `<reference>` | `<notes>` |
| OWASP ASVS                       | `<reference>` | `<notes>` |
| CWE Reference                    | `<reference>` | `<notes>` |
| CVSS Calculator                  | `<reference>` | `<notes>` |
| MITRE ATT&CK                     | `<reference>` | `<notes>` |
| Vendor Advisory                  | `<reference>` | `<notes>` |
| Framework Documentation          | `<reference>` | `<notes>` |
| Tool Documentation               | `<reference>` | `<notes>` |
| Client Secure Coding Standard    | `<reference>` | `<notes>` |
| Internal SDLC Standard           | `<reference>` | `<notes>` |
| Related Pull Request             | `<reference>` | `<notes>` |
| Related Ticket                   | `<reference>` | `<notes>` |

---

## 46. Appendix: Report Review Checklist

* [ ] Cover page complete.
* [ ] Document control complete.
* [ ] Authorization and scope documented.
* [ ] Repository URLs, branches, and commit hashes recorded.
* [ ] Executive summary written for non-technical stakeholders.
* [ ] Business impact documented.
* [ ] Engagement objectives documented.
* [ ] Methodology documented.
* [ ] Rules of engagement documented.
* [ ] Environment and tooling documented.
* [ ] Repository and codebase inventory complete.
* [ ] Architecture summary documented.
* [ ] Threat model summary documented.
* [ ] Security-critical code paths inventoried.
* [ ] Source-to-sink analysis documented.
* [ ] Authentication review documented.
* [ ] Authorization review documented.
* [ ] Input validation and injection review documented.
* [ ] API security review documented.
* [ ] Business logic review documented.
* [ ] File upload and parser review documented.
* [ ] Cryptography and secrets review documented.
* [ ] Dependency and supply-chain review documented.
* [ ] Configuration and IaC review documented.
* [ ] Error handling, logging, and monitoring review documented.
* [ ] Vulnerability validation documented.
* [ ] Exploitability analysis documented.
* [ ] Attack path narrative included where applicable.
* [ ] Findings summary complete.
* [ ] Detailed findings include evidence.
* [ ] Detailed findings include severity and confidence.
* [ ] Detailed findings include CVSS, CWE, OWASP, and ATT&CK mappings where relevant.
* [ ] False positives and dismissed findings documented.
* [ ] Security control observations documented.
* [ ] Remediation roadmap included.
* [ ] Secure patch guidance included.
* [ ] Regression and verification testing included.
* [ ] Detection recommendations included.
* [ ] Cleanup and data handling documented.
* [ ] Retest plan included.
* [ ] Evidence index complete.
* [ ] Code reference index complete.
* [ ] Request/response appendix sanitized.
* [ ] Tool output appendix sanitized.
* [ ] Limitations documented.
* [ ] References included.
* [ ] Weaponized exploitation instructions excluded.
* [ ] Sensitive evidence redacted.
* [ ] Source-code excerpts minimized.
* [ ] Final report reviewed and approved.
