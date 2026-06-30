# Web Application Penetration Test Report Template

> **Use Case:** Authorized web application, API, SaaS, single-page application, microservice, mobile backend, and cloud-hosted application assessments.
> **Scope Boundary:** This template is for ethical, authorized, contractual, internal, bug bounty, educational, and controlled lab environments only. Do not use it to document unauthorized access, credential theft against third parties, stealth, persistence, malware deployment, destructive testing, or real-world misuse. Any proof-of-concept or exploitation content must be framed as safe validation within explicitly authorized scope.

---

## 1. Cover Page

| Field                        | Value                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------- |
| Report Title                 | `Web Application Penetration Test Report`                                                                 |
| Client / Organization        | `<client_name>`                                                                                           |
| Application Name             | `<application_name>`                                                                                      |
| Engagement Name              | `<engagement_name>`                                                                                       |
| Assessment Type              | `<web_application / API / SaaS / SPA / microservice / mobile_backend / cloud_hosted_application / mixed>` |
| Assessment Dates             | `<assessment_start_date> to <assessment_end_date>`                                                        |
| Report Date                  | `<YYYY-MM-DD>`                                                                                            |
| Report Version               | `<report_version>`                                                                                        |
| Classification / Sensitivity | `<public / internal / confidential / restricted>`                                                         |
| Prepared By                  | `<tester_or_company_name>`                                                                                |
| Reviewed By                  | `<reviewer_name>`                                                                                         |
| Distribution List            | `<authorized_recipients>`                                                                                 |
| Evidence Root                | `<evidence_root_path>`                                                                                    |

### 1.1 Confidentiality Notice

```text
<Insert confidentiality notice, distribution restrictions, report handling requirements, evidence handling requirements, and client-specific limitations.>
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
<Describe who may receive, store, copy, transmit, or reference this report. Include client-specific restrictions.>
```

### 2.2 Report Handling

* [ ] Report shared only with authorized recipients.
* [ ] Sensitive evidence redacted before distribution.
* [ ] Raw evidence stored in approved location.
* [ ] Report classification applied.
* [ ] Retention period documented.
* [ ] Deletion or archival requirements documented.

---

## 3. Legal Authorization and Scope Statement

### 3.1 Authorization Statement

```text
<Describe the written authorization for the assessment, including contract/SOW reference, letter of engagement reference, authorized targets, approved environments, approved testing dates, and legal boundaries.>
```

### 3.2 Scope Summary

| Scope Item                      | Value                                |
| ------------------------------- | ------------------------------------ |
| Application Name                | `<application_name>`                 |
| Base URL(s)                     | `<base_urls>`                        |
| API Base URL(s)                 | `<api_base_urls>`                    |
| Authorized Environments         | `<production / staging / dev / lab>` |
| Authorized Test Accounts        | `<accounts>`                         |
| Authorized Source IPs           | `<source_ips>`                       |
| Approved Testing Dates          | `<approved_testing_dates>`           |
| Testing Window                  | `<testing_window>`                   |
| Emergency Contact               | `<contact>`                          |
| Escalation Contact              | `<escalation_contact>`               |
| Contract / SOW Reference        | `<contract_or_sow_reference>`        |
| Letter of Engagement Reference  | `<letter_of_engagement_reference>`   |
| Excluded Targets                | `<excluded_targets>`                 |
| Data Handling Requirements      | `<data_handling_requirements>`       |
| Evidence Retention Requirements | `<evidence_retention_requirements>`  |

### 3.3 Out-of-Scope URLs, Domains, APIs, or Functions

| Asset / URL / Function         | Reason Excluded | Notes     |
| ------------------------------ | --------------- | --------- |
| `<excluded_asset_or_function>` | `<reason>`      | `<notes>` |

### 3.4 Prohibited Actions

* [ ] Testing outside approved scope.
* [ ] Targeting third-party systems.
* [ ] Destructive testing.
* [ ] Credential theft against third parties.
* [ ] Malware deployment.
* [ ] Persistence, stealth, or evasion.
* [ ] Unauthorized access to production-sensitive data.
* [ ] Excessive automated traffic outside approved rate limits.
* [ ] Payment, email, SMS, or third-party workflow abuse outside approved limits.
* [ ] Denial-of-service testing unless explicitly authorized.

---

## 4. Executive Summary

### 4.1 Plain-Language Summary

```text
<Provide a concise, non-technical summary of the assessment, overall application risk, primary attack paths, most important findings, business impact, and recommended next actions.>
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

| Finding ID     | Title             | Severity     | Affected Asset / Endpoint      | Business Impact     |
| -------------- | ----------------- | ------------ | ------------------------------ | ------------------- |
| `<finding_id>` | `<finding_title>` | `<severity>` | `<affected_asset_or_endpoint>` | `<business_impact>` |

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
<Describe remaining risk after immediate remediation, compensating controls, or accepted-risk decisions.>
```

---

## 5. Business Impact Summary

### 5.1 Impact Narrative

```text
<Explain the business impact of confirmed findings and validated attack paths. Separate confirmed impact from potential impact.>
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

* [ ] Map the application attack surface.
* [ ] Validate authentication and session management controls.
* [ ] Test authorization and object-level access controls.
* [ ] Identify injection vulnerabilities.
* [ ] Assess client-side and browser security controls.
* [ ] Evaluate API security controls.
* [ ] Identify business logic flaws.
* [ ] Validate file upload and parser security.
* [ ] Assess rate limiting and abuse protections.
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

| Phase                                | Objective     | Activities Performed | Evidence        |
| ------------------------------------ | ------------- | -------------------- | --------------- |
| Pre-Engagement Review                | `<objective>` | `<activities>`       | `<evidence_id>` |
| Scope Validation                     | `<objective>` | `<activities>`       | `<evidence_id>` |
| Application Mapping                  | `<objective>` | `<activities>`       | `<evidence_id>` |
| Authentication Testing               | `<objective>` | `<activities>`       | `<evidence_id>` |
| Session Management Testing           | `<objective>` | `<activities>`       | `<evidence_id>` |
| Authorization Testing                | `<objective>` | `<activities>`       | `<evidence_id>` |
| Input Validation Testing             | `<objective>` | `<activities>`       | `<evidence_id>` |
| Injection Testing                    | `<objective>` | `<activities>`       | `<evidence_id>` |
| Client-Side Testing                  | `<objective>` | `<activities>`       | `<evidence_id>` |
| API Testing                          | `<objective>` | `<activities>`       | `<evidence_id>` |
| Business Logic Testing               | `<objective>` | `<activities>`       | `<evidence_id>` |
| File Handling Testing                | `<objective>` | `<activities>`       | `<evidence_id>` |
| Configuration and Deployment Testing | `<objective>` | `<activities>`       | `<evidence_id>` |
| Vulnerability Validation             | `<objective>` | `<activities>`       | `<evidence_id>` |
| Impact Analysis                      | `<objective>` | `<activities>`       | `<evidence_id>` |
| Cleanup                              | `<objective>` | `<activities>`       | `<evidence_id>` |
| Reporting                            | `<objective>` | `<activities>`       | `<evidence_id>` |
| Retest Planning                      | `<objective>` | `<activities>`       | `<evidence_id>` |

### 7.2 Methodology Flow

```text
[Pre-Engagement Review]
        |
        v
[Scope Validation]
        |
        v
[Application Mapping]
        |
        v
[Control Testing]
        |
        v
[Vulnerability Identification]
        |
        v
[Safe Validation]
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

| Rule Area                            | Requirement                              |
| ------------------------------------ | ---------------------------------------- |
| Testing Windows                      | `<testing_windows>`                      |
| Rate Limits                          | `<rate_limits>`                          |
| Account Lockout Restrictions         | `<account_lockout_restrictions>`         |
| Password Attack Restrictions         | `<password_attack_restrictions>`         |
| Destructive Testing Restrictions     | `<destructive_testing_restrictions>`     |
| File Upload Restrictions             | `<file_upload_restrictions>`             |
| Email / SMS Triggering Restrictions  | `<email_sms_restrictions>`               |
| Payment Workflow Restrictions        | `<payment_workflow_restrictions>`        |
| Third-Party Integration Restrictions | `<third_party_integration_restrictions>` |
| Production Safety Requirements       | `<production_safety_requirements>`       |
| Data Exfiltration Limits             | `<data_exfiltration_limits>`             |
| Notification Requirements            | `<notification_requirements>`            |
| Stop Conditions                      | `<stop_conditions>`                      |
| Cleanup Requirements                 | `<cleanup_requirements>`                 |

### 8.2 ROE Checklist

* [ ] Scope confirmed before testing.
* [ ] Testing windows observed.
* [ ] Source IPs approved.
* [ ] Emergency contacts confirmed.
* [ ] Test accounts confirmed.
* [ ] Rate limits followed.
* [ ] Sensitive data access minimized.
* [ ] Evidence redacted.
* [ ] Production safety restrictions followed.
* [ ] Client notified of critical findings.
* [ ] Cleanup completed.
* [ ] Evidence package handled according to requirements.

---

## 9. Environment and Tooling

### 9.1 Tester Environment

| Field                   | Value                     |
| ----------------------- | ------------------------- |
| Tester Workstation      | `<tester_workstation>`    |
| Operating System        | `<tester_os>`             |
| Browser Versions        | `<browser_versions>`      |
| Proxy Configuration     | `<proxy_configuration>`   |
| VPN / Jump Host         | `<vpn_or_jump_host>`      |
| Authorized Source IPs   | `<source_ips>`            |
| Working Directory       | `<working_directory>`     |
| Packet Capture Location | `<pcap_path>`             |
| Logging Configuration   | `<logging_configuration>` |

### 9.2 Tools Used

| Tool          | Version     | Purpose     | Output Path     |
| ------------- | ----------- | ----------- | --------------- |
| `<tool_name>` | `<version>` | `<purpose>` | `<output_path>` |

### 9.3 Browser Extensions

| Extension          | Version     | Purpose     | Notes     |
| ------------------ | ----------- | ----------- | --------- |
| `<extension_name>` | `<version>` | `<purpose>` | `<notes>` |

### 9.4 Test Accounts

| Role     | Account          | Privileges     | MFA Enabled  | Notes     |
| -------- | ---------------- | -------------- | ------------ | --------- |
| `<role>` | `<test_account>` | `<privileges>` | `<Yes / No>` | `<notes>` |

### 9.5 API Clients

| Client         | Purpose     | Authentication Method | Notes     |
| -------------- | ----------- | --------------------- | --------- |
| `<api_client>` | `<purpose>` | `<auth_method>`       | `<notes>` |

### 9.6 Wordlists

| Wordlist          | Path              | Purpose     |
| ----------------- | ----------------- | ----------- |
| `<wordlist_name>` | `<wordlist_path>` | `<purpose>` |

### 9.7 Scanner Policies

| Scanner     | Policy Name     | Authenticated? | Scope     | Notes     |
| ----------- | --------------- | -------------- | --------- | --------- |
| `<scanner>` | `<policy_name>` | `<Yes / No>`   | `<scope>` | `<notes>` |

### 9.8 Tool Version Commands

```bash
<tool_version_commands>
```

```text
<tool_version_output>
```

---

## 10. Application Scope Inventory

### 10.1 Web Applications

| Application          | Base URL     | Environment     | Auth Required | In Scope               | Notes     |
| -------------------- | ------------ | --------------- | ------------- | ---------------------- | --------- |
| `<application_name>` | `<base_url>` | `<environment>` | `<Yes / No>`  | `<Yes / No / Partial>` | `<notes>` |

### 10.2 APIs

| API          | Base URL    | Type                             | Auth Method     | In Scope               | Notes     |
| ------------ | ----------- | -------------------------------- | --------------- | ---------------------- | --------- |
| `<api_name>` | `<api_url>` | `<REST / GraphQL / SOAP / gRPC>` | `<auth_method>` | `<Yes / No / Partial>` | `<notes>` |

### 10.3 User Roles

| Role     | Account     | Privileges     | Test Coverage                   | Notes     |
| -------- | ----------- | -------------- | ------------------------------- | --------- |
| `<role>` | `<account>` | `<privileges>` | `<full / partial / not_tested>` | `<notes>` |

### 10.4 Out-of-Scope Assets

| Asset / URL / Function    | Reason Excluded | Notes     |
| ------------------------- | --------------- | --------- |
| `<asset_url_or_function>` | `<reason>`      | `<notes>` |

---

## 11. Application Architecture Summary

### 11.1 Architecture Narrative

```text
<Describe the high-level application architecture, trust boundaries, data flows, identity model, and security-relevant dependencies.>
```

### 11.2 Architecture Details

| Area                      | Value                                    |
| ------------------------- | ---------------------------------------- |
| Frontend Framework        | `<frontend_framework>`                   |
| Backend Framework         | `<backend_framework>`                    |
| API Architecture          | `<REST / GraphQL / SOAP / gRPC / mixed>` |
| Identity Provider         | `<identity_provider>`                    |
| Session / Token Mechanism | `<session_or_token_mechanism>`           |
| Database / Storage Layer  | `<database_or_storage>`                  |
| Cloud Services            | `<cloud_services>`                       |
| Third-Party Integrations  | `<third_party_integrations>`             |
| Administrative Interfaces | `<admin_interfaces>`                     |
| Sensitive Workflows       | `<sensitive_workflows>`                  |
| Data Classification       | `<data_classification>`                  |

### 11.3 Architecture Diagram

```text
<insert application architecture diagram here>

Example:

[User Browser / Mobile Client]
        |
        v
[Frontend / SPA]
        |
        v
[API Gateway / Reverse Proxy]
        |
        v
[Application Service]
   |          |          |
   v          v          v
[Database] [Object Storage] [Message Queue]
        |
        v
[Logging / Monitoring / SIEM]
```

---

## 12. Attack Surface Summary

### 12.1 Summary

```text
<Summarize discovered application entry points, authenticated areas, unauthenticated areas, administrative interfaces, APIs, file upload points, sensitive workflows, and third-party integrations.>
```

### 12.2 Attack Surface Table

| Area     | URL / Endpoint      | Auth Required          | Input Vectors     | Risk Notes     |
| -------- | ------------------- | ---------------------- | ----------------- | -------------- |
| `<area>` | `<url_or_endpoint>` | `<Yes / No / Unknown>` | `<input_vectors>` | `<risk_notes>` |

### 12.3 Notable Entry Points

* [ ] Hosts and domains
* [ ] Authenticated areas
* [ ] Unauthenticated areas
* [ ] Admin interfaces
* [ ] API endpoints
* [ ] File upload points
* [ ] Search/filter/sort parameters
* [ ] Redirect parameters
* [ ] Webhooks
* [ ] Password reset flows
* [ ] Registration flows
* [ ] Payment or transaction flows
* [ ] User-generated content
* [ ] Background jobs
* [ ] Third-party integrations

---

## 13. Application Mapping Results

### 13.1 Mapping Summary

```text
<Summarize crawled content, manually discovered functionality, hidden endpoints, JavaScript-discovered routes, API schemas, parameters, cookies, headers, state-changing requests, and privileged workflows.>
```

### 13.2 Functionality Map

| Functionality     | Endpoint / Route      | Method                                | Role Required | Parameters     | Notes     |
| ----------------- | --------------------- | ------------------------------------- | ------------- | -------------- | --------- |
| `<functionality>` | `<endpoint_or_route>` | `<GET / POST / PUT / PATCH / DELETE>` | `<role>`      | `<parameters>` | `<notes>` |

### 13.3 Crawled Content

| URL / Route      | Method     | Status          | Auth Required | Notes     |
| ---------------- | ---------- | --------------- | ------------- | --------- |
| `<url_or_route>` | `<method>` | `<status_code>` | `<Yes / No>`  | `<notes>` |

### 13.4 JavaScript-Discovered Routes

| Source File | Route / Endpoint      | Method     | Notes     | Evidence        |
| ----------- | --------------------- | ---------- | --------- | --------------- |
| `<js_file>` | `<route_or_endpoint>` | `<method>` | `<notes>` | `<evidence_id>` |

### 13.5 API Schema Discovery

| Schema Type                                              | Location     | Auth Required | Notes     | Evidence        |
| -------------------------------------------------------- | ------------ | ------------- | --------- | --------------- |
| `<OpenAPI / Swagger / GraphQL / WSDL / gRPC reflection>` | `<location>` | `<Yes / No>`  | `<notes>` | `<evidence_id>` |

### 13.6 Parameters

| Endpoint     | Parameter     | Location                                  | Type     | Notes     |
| ------------ | ------------- | ----------------------------------------- | -------- | --------- |
| `<endpoint>` | `<parameter>` | `<query / body / path / header / cookie>` | `<type>` | `<notes>` |

### 13.7 Cookies and Headers

| Name                      | Type                | Purpose     | Security-Relevant Notes |
| ------------------------- | ------------------- | ----------- | ----------------------- |
| `<cookie_or_header_name>` | `<cookie / header>` | `<purpose>` | `<notes>`               |

---

## 14. Authentication Testing

### 14.1 Authentication Summary

```text
<Summarize authentication model, tested workflows, observed weaknesses, and control effectiveness.>
```

### 14.2 Authentication Test Areas

| Test Area                       | Observation     | Risk     | Evidence        | Recommendation     |
| ------------------------------- | --------------- | -------- | --------------- | ------------------ |
| Login                           | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Registration                    | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Password Reset                  | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Password Change                 | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| MFA                             | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| SSO                             | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| OAuth                           | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| OIDC                            | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| SAML                            | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Magic Links                     | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Account Recovery                | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Remember-Me Functionality       | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Brute-Force Protections         | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Username Enumeration            | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Credential Stuffing Protections | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Default Credentials             | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Authentication Bypass           | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Session Creation After Login    | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |

### 14.3 Authentication Evidence

```http
<sanitized_authentication_request>
```

```http
<sanitized_authentication_response>
```

---

## 15. Session Management Testing

### 15.1 Session Management Summary

```text
<Summarize session and token handling, cookie protections, expiration behavior, revocation behavior, CSRF posture, and notable gaps.>
```

### 15.2 Session Management Controls

| Control                           | Expected Behavior | Observed Behavior | Risk     | Evidence        |
| --------------------------------- | ----------------- | ----------------- | -------- | --------------- |
| Session Token Entropy             | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| Cookie Flags                      | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| Session Fixation                  | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| Session Expiration                | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| Logout Behavior                   | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| Concurrent Sessions               | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| Refresh Tokens                    | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| JWT Signing                       | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| JWT Claims                        | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| Token Revocation                  | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| Token Storage                     | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| Cross-Device Session Invalidation | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| CSRF Protections                  | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |
| SameSite Behavior                 | `<expected>`      | `<observed>`      | `<risk>` | `<evidence_id>` |

### 15.3 Cookie Review

| Cookie          | Purpose     | HttpOnly     | Secure       | SameSite                        | Domain     | Path     | Notes     |
| --------------- | ----------- | ------------ | ------------ | ------------------------------- | ---------- | -------- | --------- |
| `<cookie_name>` | `<purpose>` | `<Yes / No>` | `<Yes / No>` | `<Strict / Lax / None / Unset>` | `<domain>` | `<path>` | `<notes>` |

### 15.4 Token Evidence

```text
<sanitized_token_or_claim_observation>
```

---

## 16. Authorization and Access Control Testing

### 16.1 Authorization Summary

```text
<Summarize tested roles, protected functions, object-level access controls, tenant isolation, and authorization failures.>
```

### 16.2 Access Control Test Matrix

| Test Case     | Role A     | Role B     | Endpoint / Object      | Expected Result     | Actual Result     | Evidence        |
| ------------- | ---------- | ---------- | ---------------------- | ------------------- | ----------------- | --------------- |
| `<test_case>` | `<role_a>` | `<role_b>` | `<endpoint_or_object>` | `<expected_result>` | `<actual_result>` | `<evidence_id>` |

### 16.3 Authorization Areas Tested

* [ ] Horizontal privilege escalation
* [ ] Vertical privilege escalation
* [ ] IDOR / BOLA
* [ ] Function-level authorization
* [ ] Object-level authorization
* [ ] Tenant isolation
* [ ] Admin-only operations
* [ ] Forced browsing
* [ ] Mass assignment
* [ ] GraphQL authorization
* [ ] API authorization
* [ ] Role downgrade / upgrade testing
* [ ] Direct access to static resources
* [ ] Server-side authorization versus client-side-only controls

### 16.4 Authorization Evidence

```http
<sanitized_authorization_test_request>
```

```http
<sanitized_authorization_test_response>
```

---

## 17. Input Validation and Injection Testing

### 17.1 Input Validation Summary

```text
<Summarize input validation, parsing, encoding, injection testing, and findings related to unsafe handling of user-controlled input.>
```

### 17.2 Input and Injection Test Matrix

| Input Vector     | Endpoint     | Parameter     | Test Type     | Result     | Evidence        |
| ---------------- | ------------ | ------------- | ------------- | ---------- | --------------- |
| `<input_vector>` | `<endpoint>` | `<parameter>` | `<test_type>` | `<result>` | `<evidence_id>` |

### 17.3 Injection Areas Tested

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

### 17.4 Evidence

```http
<sanitized_injection_test_request>
```

```http
<sanitized_injection_test_response>
```

```text
<sanitized_tool_output_or_validation_notes>
```

---

## 18. Client-Side and Browser Security Testing

### 18.1 Client-Side Summary

```text
<Summarize client-side attack surface, JavaScript exposure, browser security controls, client-side trust decisions, and frontend security issues.>
```

### 18.2 Client-Side Control Table

| Control / Issue                    | Location     | Observation     | Risk     | Evidence        |
| ---------------------------------- | ------------ | --------------- | -------- | --------------- |
| Reflected XSS                      | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| Stored XSS                         | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| DOM XSS                            | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| CSP                                | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| CORS                               | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| postMessage                        | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| Clickjacking                       | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| Same-Origin Policy Issues          | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| Sensitive Data in JavaScript       | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| Source Maps                        | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| Local Storage / Session Storage    | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| Mixed Content                      | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| Browser Cache Behavior             | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| Client-Side Authorization Controls | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| Third-Party Scripts                | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |
| Dependency Exposure                | `<location>` | `<observation>` | `<risk>` | `<evidence_id>` |

### 18.3 Browser Console Evidence

```text
<sanitized_browser_console_output>
```

---

## 19. API Security Testing

### 19.1 API Summary

```text
<Summarize API endpoints tested, authentication and authorization posture, data exposure risk, abuse controls, and API-specific findings.>
```

### 19.2 API Test Matrix

| Endpoint     | Method     | Auth Required | Role Required | Sensitive Data | Finding / Observation      | Evidence        |
| ------------ | ---------- | ------------- | ------------- | -------------- | -------------------------- | --------------- |
| `<endpoint>` | `<method>` | `<Yes / No>`  | `<role>`      | `<Yes / No>`   | `<finding_or_observation>` | `<evidence_id>` |

### 19.3 API Areas Tested

* [ ] Endpoint inventory
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
* [ ] SOAP/XML security
* [ ] Webhook validation
* [ ] API versioning
* [ ] Error handling

### 19.4 API Evidence

```http
<sanitized_api_request>
```

```http
<sanitized_api_response>
```

---

## 20. Business Logic Testing

### 20.1 Business Logic Summary

```text
<Summarize sensitive workflows, expected business rules, tested abuse cases, and confirmed logic weaknesses.>
```

### 20.2 Workflow Testing Table

| Workflow     | Expected Control     | Test Performed     | Observed Result     | Risk     | Evidence        |
| ------------ | -------------------- | ------------------ | ------------------- | -------- | --------------- |
| `<workflow>` | `<expected_control>` | `<test_performed>` | `<observed_result>` | `<risk>` | `<evidence_id>` |

### 20.3 Business Logic Areas Tested

* [ ] Multi-step workflow bypass
* [ ] Transaction manipulation
* [ ] Price manipulation
* [ ] Quantity manipulation
* [ ] Coupon/discount abuse
* [ ] Race conditions
* [ ] Replay attacks
* [ ] Approval bypass
* [ ] Subscription logic
* [ ] Payment workflow abuse
* [ ] Account lifecycle abuse
* [ ] Privilege workflow abuse
* [ ] Trust boundary violations
* [ ] State-machine flaws

### 20.4 Business Logic Evidence

```http
<sanitized_business_logic_request>
```

```http
<sanitized_business_logic_response>
```

---

## 21. File Upload and Parser Security Testing

### 21.1 File Handling Summary

```text
<Summarize file upload points, parser behavior, validation controls, storage behavior, access control, and file-processing risks.>
```

### 21.2 File Upload Testing Table

| Upload Point     | Allowed Types     | Validation Observed     | Risk     | Evidence        |
| ---------------- | ----------------- | ----------------------- | -------- | --------------- |
| `<upload_point>` | `<allowed_types>` | `<validation_observed>` | `<risk>` | `<evidence_id>` |

### 21.3 File Handling Areas Tested

* [ ] File type validation
* [ ] MIME validation
* [ ] Extension validation
* [ ] Magic-byte validation
* [ ] File size limits
* [ ] Malware scanning
* [ ] Image processing
* [ ] Archive extraction
* [ ] Zip slip
* [ ] Path traversal
* [ ] SVG/script handling
* [ ] Metadata exposure
* [ ] Public file access
* [ ] Signed URL access
* [ ] Stored XSS via uploaded files

### 21.4 File Upload Evidence

```http
<sanitized_file_upload_request>
```

```http
<sanitized_file_upload_response>
```

---

## 22. Configuration and Deployment Testing

### 22.1 Configuration Summary

```text
<Summarize application configuration, deployment posture, headers, TLS, exposed files, debug behavior, and cloud/storage exposure.>
```

### 22.2 Configuration Testing Table

| Configuration Area                 | Observation     | Risk     | Evidence        | Recommendation     |
| ---------------------------------- | --------------- | -------- | --------------- | ------------------ |
| Security Headers                   | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| TLS Configuration                  | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| HSTS                               | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Cookies                            | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| CORS Configuration                 | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Debug Mode                         | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Stack Traces                       | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Error Pages                        | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Default Content                    | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Directory Listing                  | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Admin Panels                       | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Dangerous HTTP Methods             | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Backup Files                       | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Exposed Environment Files          | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Exposed `.git` or Source Artifacts | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Dependency Exposure                | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |
| Cloud Storage Exposure             | `<observation>` | `<risk>` | `<evidence_id>` | `<recommendation>` |

### 22.3 Configuration Evidence

```text
<sanitized_configuration_or_header_output>
```

---

## 23. Cryptography, Secrets, and Sensitive Data Handling

### 23.1 Crypto and Secrets Summary

```text
<Summarize secrets handling, cryptographic controls, token handling, sensitive data exposure, and related observations.>
```

### 23.2 Secrets and Sensitive Data Table

| Data / Secret Type      | Location     | Exposure     | Risk     | Evidence        |
| ----------------------- | ------------ | ------------ | -------- | --------------- |
| `<secret_or_data_type>` | `<location>` | `<exposure>` | `<risk>` | `<evidence_id>` |

### 23.3 Areas Tested

* [ ] Hardcoded secrets
* [ ] API keys
* [ ] Tokens
* [ ] Password handling
* [ ] Password reset tokens
* [ ] Weak crypto
* [ ] Custom crypto
* [ ] Predictable randomness
* [ ] Static IVs
* [ ] Missing integrity protection
* [ ] Secrets in frontend code
* [ ] Secrets in logs
* [ ] PII exposure
* [ ] Sensitive data caching
* [ ] Sensitive data in URLs

### 23.4 Evidence

```text
<sanitized_secret_crypto_or_sensitive_data_evidence>
```

---

## 24. Rate Limiting and Abuse Case Testing

### 24.1 Abuse Testing Summary

```text
<Summarize tested abuse cases, rate limits, anti-automation controls, quotas, and observed gaps.>
```

### 24.2 Abuse Case Table

| Abuse Case                   | Control Expected | Observed Behavior | Risk     | Evidence        |
| ---------------------------- | ---------------- | ----------------- | -------- | --------------- |
| Login Rate Limiting          | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |
| Password Reset Rate Limiting | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |
| MFA Code Rate Limiting       | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |
| Registration Abuse           | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |
| Email / SMS Bombing          | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |
| Search Scraping              | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |
| Checkout Abuse               | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |
| API Quota Enforcement        | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |
| Resource Exhaustion          | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |
| GraphQL Query Abuse          | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |
| File Upload Abuse            | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |
| Account Enumeration          | `<expected>`     | `<observed>`      | `<risk>` | `<evidence_id>` |

### 24.3 Abuse Testing Evidence

```text
<sanitized_rate_limit_or_abuse_test_output>
```

---

## 25. Logging and Monitoring Observations

### 25.1 Logging Summary

```text
<Summarize observed logging, security event visibility, monitoring coverage, and gaps.>
```

### 25.2 Logging and Monitoring Table

| Event Type                 | Logged?                | Useful Fields | Gap     | Recommendation     |
| -------------------------- | ---------------------- | ------------- | ------- | ------------------ |
| Authentication Logs        | `<Yes / No / Unknown>` | `<fields>`    | `<gap>` | `<recommendation>` |
| Authorization Failure Logs | `<Yes / No / Unknown>` | `<fields>`    | `<gap>` | `<recommendation>` |
| Admin Action Logs          | `<Yes / No / Unknown>` | `<fields>`    | `<gap>` | `<recommendation>` |
| Sensitive Workflow Logs    | `<Yes / No / Unknown>` | `<fields>`    | `<gap>` | `<recommendation>` |
| API Abuse Logs             | `<Yes / No / Unknown>` | `<fields>`    | `<gap>` | `<recommendation>` |
| File Upload Logs           | `<Yes / No / Unknown>` | `<fields>`    | `<gap>` | `<recommendation>` |
| Error Logs                 | `<Yes / No / Unknown>` | `<fields>`    | `<gap>` | `<recommendation>` |
| Security Event Visibility  | `<Yes / No / Unknown>` | `<fields>`    | `<gap>` | `<recommendation>` |

---

## 26. Vulnerability Validation Summary

### 26.1 Summary

```text
<Summarize scanner findings, manual validation, false positives removed, confirmed vulnerabilities, unvalidated vulnerabilities, environmental constraints, and exploitability notes.>
```

### 26.2 Validation Table

| Vulnerability     | Asset / Endpoint      | Source                                             | Validation Method     | Status                                                  | Evidence        |
| ----------------- | --------------------- | -------------------------------------------------- | --------------------- | ------------------------------------------------------- | --------------- |
| `<vulnerability>` | `<asset_or_endpoint>` | `<scanner / manual / code_review / proxy_capture>` | `<validation_method>` | `<confirmed / false_positive / unvalidated / accepted>` | `<evidence_id>` |

### 26.3 Scanner Findings

| Scanner Finding     | Asset / Endpoint      | Scanner Severity | Validation Status                            | Notes     |
| ------------------- | --------------------- | ---------------- | -------------------------------------------- | --------- |
| `<scanner_finding>` | `<asset_or_endpoint>` | `<severity>`     | `<confirmed / false_positive / unvalidated>` | `<notes>` |

### 26.4 Manual Validation Notes

```text
<Describe how findings were safely validated without destructive actions or unauthorized access.>
```

### 26.5 False Positives Removed

| Finding     | Reason Removed | Evidence        |
| ----------- | -------------- | --------------- |
| `<finding>` | `<reason>`     | `<evidence_id>` |

### 26.6 Environmental Constraints

| Constraint     | Impact     | Notes     |
| -------------- | ---------- | --------- |
| `<constraint>` | `<impact>` | `<notes>` |

---

## 27. Attack Path Narrative

### 27.1 Attack Path Summary

```text
Attack Path <ID>:
<entry_point>
  -> <validated_weakness>
  -> <access_or_data_impact>
  -> <business_impact>
```

### 27.2 Attack Path Table

| Step | Action     | Result     | Evidence        | Risk     |
| ---: | ---------- | ---------- | --------------- | -------- |
|  `1` | `<action>` | `<result>` | `<evidence_id>` | `<risk>` |
|  `2` | `<action>` | `<result>` | `<evidence_id>` | `<risk>` |
|  `3` | `<action>` | `<result>` | `<evidence_id>` | `<risk>` |

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
<Entry Point>
      |
      v
<Validated Weakness>
      |
      v
<Access / Data / Workflow Impact>
      |
      v
<Business Impact>
```

---

## 28. Findings Summary

| ID             | Finding Title     | Severity                                           | Confidence              | Affected Asset / Endpoint      | Status                                                                                         |
| -------------- | ----------------- | -------------------------------------------------- | ----------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------- |
| `<finding_id>` | `<finding_title>` | `<Informational / Low / Medium / High / Critical>` | `<Low / Medium / High>` | `<affected_asset_or_endpoint>` | `<Open / Fixed / Partially Fixed / Accepted Risk / False Positive / Duplicate / Needs Retest>` |

---

## 29. Detailed Finding Template

## Finding `<finding_id>`: `<finding_title>`

| Field                 | Value                                                                                          |
| --------------------- | ---------------------------------------------------------------------------------------------- |
| Severity              | `<Informational / Low / Medium / High / Critical>`                                             |
| Confidence            | `<Low / Medium / High>`                                                                        |
| Status                | `<Open / Fixed / Partially Fixed / Accepted Risk / False Positive / Duplicate / Needs Retest>` |
| Affected Asset(s)     | `<affected_assets>`                                                                            |
| Affected Endpoint(s)  | `<affected_endpoints>`                                                                         |
| Affected Parameter(s) | `<affected_parameters>`                                                                        |
| Affected Role(s)      | `<affected_roles>`                                                                             |
| CVSS                  | `<vector_score>`                                                                               |
| CWE                   | `<CWE-ID>`                                                                                     |
| OWASP Web Top 10      | `<category_if_applicable>`                                                                     |
| OWASP API Top 10      | `<category_if_applicable>`                                                                     |
| MITRE ATT&CK          | `<technique_id_if_applicable>`                                                                 |
| Evidence IDs          | `<evidence_ids>`                                                                               |
| Related Attack Path   | `<attack_path_id>`                                                                             |

### 29.1 Executive Description

```text
<Explain the issue in plain business language. Describe why it matters and what risk it creates.>
```

### 29.2 Technical Description

```text
<Explain the technical weakness, affected endpoint, parameter, workflow, control failure, or vulnerable behavior.>
```

### 29.3 Facts

| Fact ID      | Fact               | Evidence        | Confidence              |
| ------------ | ------------------ | --------------- | ----------------------- |
| `<FACT-001>` | `<confirmed_fact>` | `<evidence_id>` | `<Low / Medium / High>` |

### 29.4 Hypotheses

| Hypothesis ID | Hypothesis     | Validation Method          | Result                                  | Confidence              |
| ------------- | -------------- | -------------------------- | --------------------------------------- | ----------------------- |
| `<HYP-001>`   | `<hypothesis>` | `<safe_validation_method>` | `<confirmed / rejected / inconclusive>` | `<Low / Medium / High>` |

### 29.5 Evidence

```text
<sanitized_evidence>
```

### 29.6 HTTP Request / Response Evidence

```http
<sanitized_request>
```

```http
<sanitized_response>
```

### 29.7 Safe Reproduction / Validation Steps

1. `<step_1>`
2. `<step_2>`
3. `<step_3>`

### 29.8 Impact

```text
<Describe technical and business impact. Separate confirmed impact from potential impact.>
```

### 29.9 Likelihood

```text
<Describe exploitability, preconditions, exposure, required role, user interaction, and attacker effort.>
```

### 29.10 Root Cause

```text
<Describe the underlying code, configuration, design, process, or control failure.>
```

### 29.11 Remediation

```text
<Provide direct remediation steps, including tactical fixes and strategic improvements.>
```

### 29.12 Secure Implementation Guidance

```text
<Provide secure design, code-level, configuration, or framework-specific guidance.>
```

### 29.13 Detection Opportunities

```text
<Describe logs, telemetry, alert logic, or monitoring opportunities.>
```

### 29.14 Retest Procedure

```text
<Describe how to safely verify remediation.>
```

### 29.15 References

| Reference     | Description     |
| ------------- | --------------- |
| `<reference>` | `<description>` |

---

## 30. Security Control Observations

| Control                  | Observation     | Effectiveness                                                    | Recommendation     |
| ------------------------ | --------------- | ---------------------------------------------------------------- | ------------------ |
| WAF Behavior             | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Bot Protection           | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Rate Limiting            | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| MFA Enforcement          | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Security Headers         | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Logging                  | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Monitoring               | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Alerting                 | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Error Handling           | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Secure SDLC              | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |
| Vulnerability Management | `<observation>` | `<effective / partially_effective / ineffective / not_observed>` | `<recommendation>` |

---

## 31. Risk Rating Methodology

### 31.1 Severity Model

| Severity      | Definition     |
| ------------- | -------------- |
| Critical      | `<definition>` |
| High          | `<definition>` |
| Medium        | `<definition>` |
| Low           | `<definition>` |
| Informational | `<definition>` |

### 31.2 Confidence Model

| Confidence | Definition     |
| ---------- | -------------- |
| High       | `<definition>` |
| Medium     | `<definition>` |
| Low        | `<definition>` |

### 31.3 Likelihood Factors

| Factor                      | Description     |
| --------------------------- | --------------- |
| Exposure                    | `<description>` |
| Exploitability              | `<description>` |
| Required Access             | `<description>` |
| Attack Complexity           | `<description>` |
| Existing Controls           | `<description>` |
| Public Exploit Availability | `<description>` |
| Required User Interaction   | `<description>` |

### 31.4 Impact Factors

| Factor                 | Description     |
| ---------------------- | --------------- |
| Confidentiality        | `<description>` |
| Integrity              | `<description>` |
| Availability           | `<description>` |
| Business Criticality   | `<description>` |
| Regulatory Exposure    | `<description>` |
| Fraud Potential        | `<description>` |
| Operational Disruption | `<description>` |

### 31.5 Environmental Modifiers

| Modifier               | Description     |
| ---------------------- | --------------- |
| Asset Criticality      | `<description>` |
| Compensating Controls  | `<description>` |
| Tenant Isolation       | `<description>` |
| Monitoring Visibility  | `<description>` |
| Remediation Complexity | `<description>` |

---

## 32. Remediation Roadmap

### 32.1 Prioritized Roadmap

| Priority              | Finding ID     | Remediation     | Owner     | Effort                  | Target Date    | Risk Reduction     |
| --------------------- | -------------- | --------------- | --------- | ----------------------- | -------------- | ------------------ |
| `<P0 / P1 / P2 / P3>` | `<finding_id>` | `<remediation>` | `<owner>` | `<Low / Medium / High>` | `<YYYY-MM-DD>` | `<risk_reduction>` |

### 32.2 Immediate Actions

* [ ] `<immediate_action_1>`
* [ ] `<immediate_action_2>`
* [ ] `<immediate_action_3>`

### 32.3 30-Day Actions

* [ ] `<30_day_action_1>`
* [ ] `<30_day_action_2>`
* [ ] `<30_day_action_3>`

### 32.4 60-Day Actions

* [ ] `<60_day_action_1>`
* [ ] `<60_day_action_2>`
* [ ] `<60_day_action_3>`

### 32.5 90-Day Actions

* [ ] `<90_day_action_1>`
* [ ] `<90_day_action_2>`
* [ ] `<90_day_action_3>`

### 32.6 Strategic Improvements

* [ ] `<strategic_improvement_1>`
* [ ] `<strategic_improvement_2>`
* [ ] `<strategic_improvement_3>`

### 32.7 Secure SDLC Improvements

* [ ] Add security requirements for affected risk classes.
* [ ] Add threat modeling for sensitive workflows.
* [ ] Add abuse-case testing.
* [ ] Add authorization regression tests.
* [ ] Add SAST/DAST/API security checks in CI/CD.
* [ ] Add dependency and secrets scanning.
* [ ] Add secure code review gates for high-risk changes.

### 32.8 Long-Term Architecture Changes

* [ ] `<architecture_change_1>`
* [ ] `<architecture_change_2>`
* [ ] `<architecture_change_3>`

---

## 33. Detection and Monitoring Recommendations

### 33.1 Detection Opportunities

| Detection Opportunity     | Data Source     | Logic Summary     | Related Finding | Priority                |
| ------------------------- | --------------- | ----------------- | --------------- | ----------------------- |
| `<detection_opportunity>` | `<data_source>` | `<logic_summary>` | `<finding_id>`  | `<High / Medium / Low>` |

### 33.2 Monitoring Areas

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

### 33.3 Detection Pseudocode Placeholder

```text
<insert vendor-neutral detection logic or SIEM rule placeholder>
```

---

## 34. Cleanup and Data Handling

### 34.1 Cleanup Summary

```text
<Describe cleanup actions performed after testing, including test accounts, data created, files uploaded, API keys, tokens, temporary users, temporary configuration changes, and evidence handling.>
```

### 34.2 Cleanup Table

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

### 34.3 Evidence Redaction Guidance

* [ ] Redact passwords, tokens, API keys, private keys, session identifiers, and reset links.
* [ ] Redact PII unless explicitly required for proof.
* [ ] Redact customer data and regulated data.
* [ ] Preserve enough context for validation.
* [ ] Store raw evidence only in approved restricted locations.
* [ ] Reference raw evidence by evidence ID when direct inclusion is inappropriate.

---

## 35. Retest Plan

### 35.1 Retest Scope

```text
<Describe which findings, endpoints, roles, workflows, or controls should be retested.>
```

### 35.2 Retest Table

| Finding ID     | Retest Step     | Expected Result     | Status                                      | Evidence        |
| -------------- | --------------- | ------------------- | ------------------------------------------- | --------------- |
| `<finding_id>` | `<retest_step>` | `<expected_result>` | `<not_started / passed / failed / partial>` | `<evidence_id>` |

### 35.3 Retest Methodology

```text
<Describe safe retest methodology, required access, test environment, validation criteria, and evidence requirements.>
```

### 35.4 Responsible Parties

| Role              | Name / Team  | Responsibility     |
| ----------------- | ------------ | ------------------ |
| Client Owner      | `<owner>`    | `<responsibility>` |
| Technical Owner   | `<owner>`    | `<responsibility>` |
| Retest Tester     | `<tester>`   | `<responsibility>` |
| Security Reviewer | `<reviewer>` | `<responsibility>` |

---

## 36. Evidence Index

| Evidence ID     | Description     | Type                                                                                                                                                                                                        | Path / Link      | Timestamp     | Related Finding |
| --------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------- | --------------- |
| `<evidence_id>` | `<description>` | `<screenshot / proxy_capture / HTTP_request / HTTP_response / browser_console_output / scanner_output / application_log / tool_output / source_code_snippet / configuration_snippet / client_confirmation>` | `<path_or_link>` | `<timestamp>` | `<finding_id>`  |

### 36.1 Evidence Storage Layout

```text
<evidence_root>/
├── 00_scope/
├── 01_mapping/
├── 02_authentication/
├── 03_session_management/
├── 04_authorization/
├── 05_input_validation/
├── 06_api_testing/
├── 07_business_logic/
├── 08_file_uploads/
├── 09_configuration/
├── 10_findings/
├── 11_screenshots/
├── 12_requests_responses/
├── 13_tool_output/
├── 14_cleanup/
├── 15_retest/
└── 16_report/
```

---

## 37. Screenshot Index

| Screenshot ID     | Description     | Path                | Related Finding |
| ----------------- | --------------- | ------------------- | --------------- |
| `<screenshot_id>` | `<description>` | `<screenshot_path>` | `<finding_id>`  |

### 37.1 Screenshot Placeholder

```markdown
![<description>](<screenshot_path>)
```

---

## 38. Request / Response Appendix

### 38.1 Request / Response Index

| Request ID  | Endpoint     | Purpose     | Related Finding | Evidence Path     |
| ----------- | ------------ | ----------- | --------------- | ----------------- |
| `<REQ-001>` | `<endpoint>` | `<purpose>` | `<finding_id>`  | `<evidence_path>` |

### 38.2 Sanitized HTTP Request

```http
<sanitized_http_request>
```

### 38.3 Sanitized HTTP Response

```http
<sanitized_http_response>
```

---

## 39. Tool Output Appendix

### 39.1 Burp Suite Results

```text
<sanitized_burp_suite_results>
```

### 39.2 OWASP ZAP Results

```text
<sanitized_zap_results>
```

### 39.3 Nuclei Results

```text
<sanitized_nuclei_results>
```

### 39.4 Nikto Results, If Applicable

```text
<sanitized_nikto_results>
```

### 39.5 Dirsearch / Gobuster / Feroxbuster Output

```text
<sanitized_content_discovery_output>
```

### 39.6 API Schema Output

```text
<sanitized_api_schema_output>
```

### 39.7 GraphQL Introspection Notes

```text
<sanitized_graphql_introspection_notes>
```

### 39.8 TLS Scan Output

```text
<sanitized_tls_scan_output>
```

### 39.9 Dependency Scan Output, If Applicable

```text
<sanitized_dependency_scan_output>
```

### 39.10 Manual Validation Logs

```text
<sanitized_manual_validation_logs>
```

---

## 40. Limitations

### 40.1 Assessment Limitations

| Limitation                           | Impact     | Notes     |
| ------------------------------------ | ---------- | --------- |
| Scope Limitations                    | `<impact>` | `<notes>` |
| Time Limitations                     | `<impact>` | `<notes>` |
| Credential Limitations               | `<impact>` | `<notes>` |
| Testing Window Limitations           | `<impact>` | `<notes>` |
| Production Safety Restrictions       | `<impact>` | `<notes>` |
| Unreachable Functionality            | `<impact>` | `<notes>` |
| Missing Roles / Accounts             | `<impact>` | `<notes>` |
| Unavailable Source Code              | `<impact>` | `<notes>` |
| Unavailable API Documentation        | `<impact>` | `<notes>` |
| Third-Party Integration Restrictions | `<impact>` | `<notes>` |
| Unvalidated Findings                 | `<impact>` | `<notes>` |
| Assumptions                          | `<impact>` | `<notes>` |

### 40.2 Untested Areas

| Area     | Reason Not Tested | Risk     | Recommendation     |
| -------- | ----------------- | -------- | ------------------ |
| `<area>` | `<reason>`        | `<risk>` | `<recommendation>` |

---

## 41. Appendix: Terms and Definitions

| Term                 | Definition     |
| -------------------- | -------------- |
| Authentication       | `<definition>` |
| Authorization        | `<definition>` |
| Session Management   | `<definition>` |
| IDOR                 | `<definition>` |
| BOLA                 | `<definition>` |
| CSRF                 | `<definition>` |
| XSS                  | `<definition>` |
| SSRF                 | `<definition>` |
| Injection            | `<definition>` |
| Business Logic Flaw  | `<definition>` |
| Exploitability       | `<definition>` |
| Exposure             | `<definition>` |
| Attack Path          | `<definition>` |
| Vulnerability        | `<definition>` |
| Risk                 | `<definition>` |
| Impact               | `<definition>` |
| Likelihood           | `<definition>` |
| Compensating Control | `<definition>` |
| False Positive       | `<definition>` |
| Accepted Risk        | `<definition>` |
| Residual Risk        | `<definition>` |

---

## 42. Appendix: References

| Reference Type                   | Reference     | Notes     |
| -------------------------------- | ------------- | --------- |
| OWASP Web Security Testing Guide | `<reference>` | `<notes>` |
| OWASP Web Top 10                 | `<reference>` | `<notes>` |
| OWASP API Top 10                 | `<reference>` | `<notes>` |
| CWE Reference                    | `<reference>` | `<notes>` |
| CVSS Calculator                  | `<reference>` | `<notes>` |
| MITRE ATT&CK                     | `<reference>` | `<notes>` |
| Vendor Advisory                  | `<reference>` | `<notes>` |
| Framework Documentation          | `<reference>` | `<notes>` |
| Tool Documentation               | `<reference>` | `<notes>` |
| Client Standard                  | `<reference>` | `<notes>` |
| Internal Policy                  | `<reference>` | `<notes>` |

---

## 43. Appendix: Report Review Checklist

* [ ] Cover page complete.
* [ ] Document control complete.
* [ ] Authorization and scope documented.
* [ ] Executive summary written for non-technical stakeholders.
* [ ] Business impact documented.
* [ ] Methodology documented.
* [ ] Rules of engagement documented.
* [ ] Environment and tooling documented.
* [ ] Application scope inventory complete.
* [ ] Architecture summary documented.
* [ ] Attack surface summarized.
* [ ] Application mapping documented.
* [ ] Authentication testing documented.
* [ ] Session management testing documented.
* [ ] Authorization testing documented.
* [ ] Input validation and injection testing documented.
* [ ] Client-side and browser security testing documented.
* [ ] API security testing documented.
* [ ] Business logic testing documented.
* [ ] File upload and parser testing documented.
* [ ] Configuration and deployment testing documented.
* [ ] Cryptography, secrets, and sensitive data handling reviewed.
* [ ] Rate limiting and abuse-case testing documented.
* [ ] Logging and monitoring observations documented.
* [ ] Vulnerability validation documented.
* [ ] Attack path narrative included where applicable.
* [ ] Findings summary complete.
* [ ] Detailed findings include evidence.
* [ ] Detailed findings include severity and confidence.
* [ ] Detailed findings include CVSS, CWE, OWASP, and ATT&CK mappings where relevant.
* [ ] Remediation roadmap included.
* [ ] Detection recommendations included.
* [ ] Cleanup and data handling documented.
* [ ] Retest plan included.
* [ ] Evidence index complete.
* [ ] Screenshot index complete.
* [ ] Request/response appendix sanitized.
* [ ] Tool output sanitized.
* [ ] Limitations documented.
* [ ] References included.
* [ ] Weaponized exploitation instructions excluded.
* [ ] Sensitive evidence redacted.
* [ ] Final report reviewed and approved.
