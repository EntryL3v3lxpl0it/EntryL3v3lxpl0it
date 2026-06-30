# Secure Code Review Template

> **Use Case:** Authorized secure code review, application security assessment, defensive engineering, compliance support, secure SDLC improvement, remediation review, and software assurance.
> **Scope Boundary:** This template must not be used to support unauthorized exploitation, credential theft, persistence, stealth, or attack execution against systems without explicit written authorization. Safe proof-of-concept validation is permitted only in controlled, authorized environments.

---

## 1. Review Metadata

| Field                        | Value                                                                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Application Name             | `<application_name>`                                                                                                                  |
| Business Owner               | `<business_owner>`                                                                                                                    |
| Engineering Owner            | `<engineering_owner>`                                                                                                                 |
| Security Owner               | `<security_owner>`                                                                                                                    |
| Reviewer                     | `<reviewer_name>`                                                                                                                     |
| Reviewer Team / Organization | `<reviewer_team>`                                                                                                                     |
| Date Started                 | `<YYYY-MM-DD>`                                                                                                                        |
| Date Completed               | `<YYYY-MM-DD>`                                                                                                                        |
| Review Type                  | `<manual_secure_code_review / SAST-assisted_review / threat-model-assisted_review / dependency_review / remediation_review / retest>` |
| Repository URL               | `<repository_url>`                                                                                                                    |
| Repository Visibility        | `<internal/private/public>`                                                                                                           |
| Branch Reviewed              | `<branch_name>`                                                                                                                       |
| Commit Hash                  | `<commit_hash>`                                                                                                                       |
| Build / Version Reviewed     | `<build_or_version>`                                                                                                                  |
| Environment Reviewed         | `<local/dev/test/staging/prod-readonly/lab>`                                                                                          |
| Languages                    | `<languages>`                                                                                                                         |
| Frameworks                   | `<frameworks>`                                                                                                                        |
| Review Timeframe             | `<review_timeframe>`                                                                                                                  |
| Ticket / Case ID             | `<ticket_or_case_id>`                                                                                                                 |
| Report Classification        | `<internal/confidential/restricted/public>`                                                                                           |
| Evidence Root                | `<evidence_root_path>`                                                                                                                |

### 1.1 Authorization / Scope Statement

```text
<Describe the written authorization, review boundaries, repositories, systems, environments, and approved validation activities.>
```

### 1.2 Out-of-Scope Components

| Component          | Reason Out of Scope | Risk Accepted By | Notes     |
| ------------------ | ------------------- | ---------------- | --------- |
| `<component_name>` | `<reason>`          | `<owner>`        | `<notes>` |

### 1.3 Assumptions

| ID          | Assumption     | Basis     | Risk if Incorrect | Confidence          |
| ----------- | -------------- | --------- | ----------------- | ------------------- |
| `<ASM-001>` | `<assumption>` | `<basis>` | `<risk_if_wrong>` | `<Low/Medium/High>` |

### 1.4 Constraints

| Constraint     | Impact on Review | Mitigation / Notes      |
| -------------- | ---------------- | ----------------------- |
| `<constraint>` | `<impact>`       | `<mitigation_or_notes>` |

---

## 2. Executive Summary

### 2.1 Non-Technical Summary

```text
<One-paragraph summary describing what was reviewed, why it matters, the overall security posture, the most important risks, and recommended next actions.>
```

### 2.2 Overall Security Posture

| Field                    | Value                                                                            |
| ------------------------ | -------------------------------------------------------------------------------- |
| Overall Security Posture | `<Strong / Moderate / Weak / Unknown>`                                           |
| Overall Risk Rating      | `<Informational/Low/Medium/High/Critical>`                                       |
| Reviewer Confidence      | `<Low/Medium/High>`                                                              |
| Residual Risk            | `<residual_risk_summary>`                                                        |
| Primary Risk Theme       | `<authz/input_validation/secrets/dependencies/crypto/config/business_logic/etc>` |

### 2.3 Finding Counts

| Severity      |                   Count |
| ------------- | ----------------------: |
| Critical      |      `<critical_count>` |
| High          |          `<high_count>` |
| Medium        |        `<medium_count>` |
| Low           |           `<low_count>` |
| Informational | `<informational_count>` |

### 2.4 Top Risks

| Rank | Risk             | Severity     | Affected Asset / Component | Business Impact     | Recommended Priority |
| ---: | ---------------- | ------------ | -------------------------- | ------------------- | -------------------- |
|  `1` | `<risk_summary>` | `<severity>` | `<asset_or_component>`     | `<business_impact>` | `<priority>`         |

### 2.5 Key Affected Assets

| Asset          | Data / Functionality Exposed | Business Criticality         | Notes     |
| -------------- | ---------------------------- | ---------------------------- | --------- |
| `<asset_name>` | `<data_or_functionality>`    | `<Low/Medium/High/Critical>` | `<notes>` |

### 2.6 Recommended Priority Actions

| Priority        | Action                 | Owner     | Target Date    | Notes     |
| --------------- | ---------------------- | --------- | -------------- | --------- |
| `<P0/P1/P2/P3>` | `<recommended_action>` | `<owner>` | `<YYYY-MM-DD>` | `<notes>` |

---

## 3. Scope and Codebase Inventory

### 3.1 Repositories Reviewed

| Repository    | URL                | Branch          | Commit Hash     | In Scope           | Notes     |
| ------------- | ------------------ | --------------- | --------------- | ------------------ | --------- |
| `<repo_name>` | `<repository_url>` | `<branch_name>` | `<commit_hash>` | `<Yes/No/Partial>` | `<notes>` |

### 3.2 Component Inventory

| Component          | Path / Repository      | Language / Framework   | Purpose     | In Scope           | Notes     |
| ------------------ | ---------------------- | ---------------------- | ----------- | ------------------ | --------- |
| `<component_name>` | `<path_or_repository>` | `<language_framework>` | `<purpose>` | `<Yes/No/Partial>` | `<notes>` |

### 3.3 Services Reviewed

| Service          | Path     | Runtime     | Exposure                    | Authentication Required | Notes     |
| ---------------- | -------- | ----------- | --------------------------- | ----------------------- | --------- |
| `<service_name>` | `<path>` | `<runtime>` | `<public/internal/private>` | `<Yes/No/Partial>`      | `<notes>` |

### 3.4 APIs Reviewed

| API          | Base Path     | Type                                     | Authentication   | Authorization Model | Notes     |
| ------------ | ------------- | ---------------------------------------- | ---------------- | ------------------- | --------- |
| `<api_name>` | `<base_path>` | `<REST/GraphQL/gRPC/SOAP/WebSocket/RPC>` | `<authn_method>` | `<authz_model>`     | `<notes>` |

### 3.5 Frontend Components Reviewed

| Component              | Path     | Framework     | Security-Relevant Concerns | Notes     |
| ---------------------- | -------- | ------------- | -------------------------- | --------- |
| `<frontend_component>` | `<path>` | `<framework>` | `<concerns>`               | `<notes>` |

### 3.6 Backend Components Reviewed

| Component             | Path     | Framework     | Security-Relevant Concerns | Notes     |
| --------------------- | -------- | ------------- | -------------------------- | --------- |
| `<backend_component>` | `<path>` | `<framework>` | `<concerns>`               | `<notes>` |

### 3.7 Mobile Components Reviewed

| Component            | Path     | Platform                       | Security-Relevant Concerns | Notes     |
| -------------------- | -------- | ------------------------------ | -------------------------- | --------- |
| `<mobile_component>` | `<path>` | `<iOS/Android/Cross-platform>` | `<concerns>`               | `<notes>` |

### 3.8 Infrastructure-as-Code Reviewed

| IaC Component     | Path     | Technology                                               | Purpose     | Notes     |
| ----------------- | -------- | -------------------------------------------------------- | ----------- | --------- |
| `<iac_component>` | `<path>` | `<Terraform/CloudFormation/Kubernetes/Helm/Ansible/etc>` | `<purpose>` | `<notes>` |

### 3.9 CI/CD Pipelines Reviewed

| Pipeline          | Path / URL      | Platform                                           | Purpose     | Notes     |
| ----------------- | --------------- | -------------------------------------------------- | ----------- | --------- |
| `<pipeline_name>` | `<path_or_url>` | `<GitHub Actions/GitLab/Jenkins/Azure DevOps/etc>` | `<purpose>` | `<notes>` |

### 3.10 Configuration Files Reviewed

| File            | Path     | Purpose     | Security-Relevant Keys | Notes     |
| --------------- | -------- | ----------- | ---------------------- | --------- |
| `<config_file>` | `<path>` | `<purpose>` | `<keys>`               | `<notes>` |

### 3.11 Third-Party Dependencies Reviewed

| Ecosystem                                   | Manifest / Lock File | Tool Used | Notes     |
| ------------------------------------------- | -------------------- | --------- | --------- |
| `<npm/pip/maven/gradle/nuget/go/cargo/etc>` | `<manifest_path>`    | `<tool>`  | `<notes>` |

### 3.12 Excluded Files / Modules

| File / Module | Reason Excluded | Risk     | Notes     |
| ------------- | --------------- | -------- | --------- |
| `<path>`      | `<reason>`      | `<risk>` | `<notes>` |

---

## 4. Architecture Overview

### 4.1 High-Level Architecture

```text
<Insert architecture diagram here>

Example:

[Client / Browser / Mobile App]
            |
            v
[API Gateway / Load Balancer]
            |
            v
[Application Service]
      |             |
      v             v
[Database]     [Message Queue]
      |
      v
[Logging / Monitoring]
```

### 4.2 Deployment Model

| Field                      | Value                                                                     |
| -------------------------- | ------------------------------------------------------------------------- |
| Deployment Model           | `<monolith/microservices/serverless/containerized/hybrid/desktop/mobile>` |
| Hosting Environment        | `<cloud/on-prem/hybrid/local/lab>`                                        |
| Cloud Provider             | `<AWS/Azure/GCP/Other/Not Applicable>`                                    |
| Runtime Platform           | `<Kubernetes/ECS/App Service/VM/Bare Metal/etc>`                          |
| Public Exposure            | `<internet/internal/private/local>`                                       |
| Administrative Access Path | `<admin_access_path>`                                                     |

### 4.3 Entry Points

| Entry Point     | Type                                               | Path / Location      | Auth Required      | Notes     |
| --------------- | -------------------------------------------------- | -------------------- | ------------------ | --------- |
| `<entry_point>` | `<HTTP/API/CLI/queue/webhook/file/upload/RPC/etc>` | `<path_or_location>` | `<Yes/No/Partial>` | `<notes>` |

### 4.4 External Dependencies

| Dependency          | Purpose     | Data Shared | Trust Level                             | Notes     |
| ------------------- | ----------- | ----------- | --------------------------------------- | --------- |
| `<dependency_name>` | `<purpose>` | `<data>`    | `<trusted/partially_trusted/untrusted>` | `<notes>` |

### 4.5 Internal Services

| Service          | Purpose     | Protocol     | Authentication  | Notes     |
| ---------------- | ----------- | ------------ | --------------- | --------- |
| `<service_name>` | `<purpose>` | `<protocol>` | `<auth_method>` | `<notes>` |

### 4.6 Data Stores

| Data Store     | Type                                              | Data Classification | Encryption                    | Access Control     | Notes     |
| -------------- | ------------------------------------------------- | ------------------- | ----------------------------- | ------------------ | --------- |
| `<data_store>` | `<SQL/NoSQL/cache/object_storage/filesystem/etc>` | `<classification>`  | `<at_rest/in_transit/status>` | `<access_control>` | `<notes>` |

### 4.7 Message Queues and Event Flows

| Queue / Topic      | Producer     | Consumer     | Message Type     | Security Concerns |
| ------------------ | ------------ | ------------ | ---------------- | ----------------- |
| `<queue_or_topic>` | `<producer>` | `<consumer>` | `<message_type>` | `<concerns>`      |

### 4.8 Identity Providers

| Identity Provider | Protocol                         | Claims / Roles Used | Trust Boundary | Notes     |
| ----------------- | -------------------------------- | ------------------- | -------------- | --------- |
| `<idp_name>`      | `<OIDC/OAuth2/SAML/LDAP/Custom>` | `<claims_roles>`    | `<boundary>`   | `<notes>` |

### 4.9 Secrets Stores

| Secrets Store     | Secrets Stored   | Access Pattern     | Rotation            | Notes     |
| ----------------- | ---------------- | ------------------ | ------------------- | --------- |
| `<secrets_store>` | `<secret_types>` | `<access_pattern>` | `<rotation_status>` | `<notes>` |

### 4.10 Administrative Interfaces

| Interface           | Path / Location | Access Control     | Exposure                    | Notes     |
| ------------------- | --------------- | ------------------ | --------------------------- | --------- |
| `<admin_interface>` | `<path>`        | `<access_control>` | `<public/internal/private>` | `<notes>` |

### 4.11 Logging and Monitoring Systems

| System             | Logs Collected | Sensitive Data Risk | Detection Use     | Notes     |
| ------------------ | -------------- | ------------------- | ----------------- | --------- |
| `<logging_system>` | `<log_types>`  | `<risk>`            | `<detection_use>` | `<notes>` |

---

## 5. Threat Model and Trust Boundaries

### 5.1 Security Objectives

| Objective     | Description     | Priority            |
| ------------- | --------------- | ------------------- |
| `<objective>` | `<description>` | `<High/Medium/Low>` |

### 5.2 Protected Assets

| Asset          | Classification                              | Location     | Threats     | Notes     |
| -------------- | ------------------------------------------- | ------------ | ----------- | --------- |
| `<asset_name>` | `<public/internal/confidential/restricted>` | `<location>` | `<threats>` | `<notes>` |

### 5.3 Actors and Roles

| Actor / Role  | Description     | Privileges     | Trust Level                             | Notes     |
| ------------- | --------------- | -------------- | --------------------------------------- | --------- |
| `<role_name>` | `<description>` | `<privileges>` | `<trusted/partially_trusted/untrusted>` | `<notes>` |

### 5.4 Trust Boundaries

| Boundary          | Untrusted Side | Trusted Side    | Enforcement Point             | Notes     |
| ----------------- | -------------- | --------------- | ----------------------------- | --------- |
| `<boundary_name>` | `<source>`     | `<destination>` | `<validation_or_authz_point>` | `<notes>` |

### 5.5 Threat Scenarios

| ID          | Threat Scenario | Affected Asset | Existing Control | Gap / Concern | Confidence          |
| ----------- | --------------- | -------------- | ---------------- | ------------- | ------------------- |
| `<THR-001>` | `<scenario>`    | `<asset>`      | `<control>`      | `<gap>`       | `<Low/Medium/High>` |

### 5.6 Abuse Cases

| Abuse Case     | Actor     | Preconditions     | Potential Impact | Relevant Code Paths |
| -------------- | --------- | ----------------- | ---------------- | ------------------- |
| `<abuse_case>` | `<actor>` | `<preconditions>` | `<impact>`       | `<code_paths>`      |

---

## 6. Review Methodology

### 6.1 Review Approach

| Method                       | Used       | Notes     |
| ---------------------------- | ---------- | --------- |
| Manual secure code review    | `<Yes/No>` | `<notes>` |
| SAST-assisted review         | `<Yes/No>` | `<notes>` |
| Threat-model-assisted review | `<Yes/No>` | `<notes>` |
| Dependency review            | `<Yes/No>` | `<notes>` |
| IaC review                   | `<Yes/No>` | `<notes>` |
| CI/CD review                 | `<Yes/No>` | `<notes>` |
| Remediation review           | `<Yes/No>` | `<notes>` |
| Retest                       | `<Yes/No>` | `<notes>` |

### 6.2 Commands and Tool Output

All commands, tool output, logs, traces, stack traces, HTTP requests, HTTP responses, and code snippets must be stored in fenced code blocks.

#### Example Command Block

```bash
<command_here>
```

#### Example Tool Output Block

```text
<tool_output_here>
```

#### Example HTTP Request Block

```http
<http_request_here>
```

#### Example HTTP Response Block

```http
<http_response_here>
```

#### Example Code Snippet Block

```text
<code_snippet_here>
```

### 6.3 Review Checklist

* [ ] Confirm authorization and scope
* [ ] Confirm exact repository, branch, and commit reviewed
* [ ] Identify application architecture
* [ ] Identify trust boundaries
* [ ] Identify protected assets
* [ ] Identify roles and permissions
* [ ] Identify entry points
* [ ] Identify user-controlled inputs
* [ ] Identify source-to-sink data flows
* [ ] Review authentication logic
* [ ] Review authorization logic
* [ ] Review session and token handling
* [ ] Review input validation and output encoding
* [ ] Review file upload and file access logic
* [ ] Review deserialization and parsing logic
* [ ] Review database query construction
* [ ] Review command execution patterns
* [ ] Review SSRF-relevant network calls
* [ ] Review dependency and supply-chain risk
* [ ] Review secrets handling
* [ ] Review cryptography usage
* [ ] Review error handling and logging
* [ ] Review business logic and workflow controls
* [ ] Review configuration and IaC
* [ ] Review CI/CD security controls
* [ ] Validate findings safely in authorized environment
* [ ] Document evidence
* [ ] Map findings to CWE, OWASP, CVSS, and remediation
* [ ] Record open questions and follow-up tasks

---

## 7. Facts, Evidence, Hypotheses, Findings, and Recommendations

### 7.1 Facts

| ID           | Fact               | Evidence        | Confidence          |
| ------------ | ------------------ | --------------- | ------------------- |
| `<FACT-001>` | `<confirmed_fact>` | `<evidence_id>` | `<Low/Medium/High>` |

### 7.2 Evidence

| Evidence ID  | Description     | File / Path      | Line(s)        | Tool     | Timestamp     | Notes     |
| ------------ | --------------- | ---------------- | -------------- | -------- | ------------- | --------- |
| `<EVID-001>` | `<description>` | `<file_or_path>` | `<line_range>` | `<tool>` | `<timestamp>` | `<notes>` |

### 7.3 Hypotheses

| ID          | Hypothesis     | Supporting Evidence | Safe Test Method | Result     | Confidence          | Status                                       |
| ----------- | -------------- | ------------------- | ---------------- | ---------- | ------------------- | -------------------------------------------- |
| `<HYP-001>` | `<hypothesis>` | `<evidence_id>`     | `<test_method>`  | `<result>` | `<Low/Medium/High>` | `<Open/Testing/Confirmed/Rejected/Deferred>` |

### 7.4 Confirmed Findings

| Finding ID   | Title             | Severity     | Affected Component | Evidence        | Status                                                   |
| ------------ | ----------------- | ------------ | ------------------ | --------------- | -------------------------------------------------------- |
| `<FIND-001>` | `<finding_title>` | `<severity>` | `<component>`      | `<evidence_id>` | `<Open/Fixed/Retest Passed/Retest Failed/Accepted Risk>` |

### 7.5 Recommendations

| Recommendation ID | Recommendation     | Related Finding | Owner     | Priority        | Status     |
| ----------------- | ------------------ | --------------- | --------- | --------------- | ---------- |
| `<REC-001>`       | `<recommendation>` | `<finding_id>`  | `<owner>` | `<P0/P1/P2/P3>` | `<status>` |

---

## 8. Authentication Review

### 8.1 Authentication Model

| Field                             | Value                                                 |
| --------------------------------- | ----------------------------------------------------- |
| Authentication Type               | `<session/OAuth2/OIDC/SAML/API key/mTLS/custom/none>` |
| Identity Provider                 | `<idp_name>`                                          |
| Login Endpoint(s)                 | `<login_endpoints>`                                   |
| Logout Endpoint(s)                | `<logout_endpoints>`                                  |
| Registration Endpoint(s)          | `<registration_endpoints>`                            |
| Password Reset Endpoint(s)        | `<password_reset_endpoints>`                          |
| MFA Supported                     | `<Yes/No/Partial>`                                    |
| MFA Required                      | `<Yes/No/Conditional>`                                |
| Service-to-Service Authentication | `<method>`                                            |

### 8.2 Authentication Checklist

* [ ] Authentication required for protected resources
* [ ] Authentication enforced server-side
* [ ] MFA implemented where required
* [ ] Password reset flow validates ownership
* [ ] Registration flow prevents privilege self-assignment
* [ ] Account enumeration protections considered
* [ ] Failed login behavior rate-limited or monitored
* [ ] Logout invalidates session or token where applicable
* [ ] Service-to-service authentication is enforced
* [ ] API keys are scoped, rotated, and protected
* [ ] Authentication bypass paths reviewed
* [ ] Test, debug, or backdoor authentication paths reviewed

### 8.3 Authentication Code Paths

| Function / Handler | File          | Endpoint     | Purpose     | Evidence        | Notes     |
| ------------------ | ------------- | ------------ | ----------- | --------------- | --------- |
| `<function_name>`  | `<file_path>` | `<endpoint>` | `<purpose>` | `<evidence_id>` | `<notes>` |

### 8.4 Authentication Evidence

```text
<authentication_code_snippet_or_tool_output>
```

### 8.5 Authentication Concerns

| ID            | Concern     | Evidence        | Impact     | Confidence          | Status                      |
| ------------- | ----------- | --------------- | ---------- | ------------------- | --------------------------- |
| `<AUTHN-001>` | `<concern>` | `<evidence_id>` | `<impact>` | `<Low/Medium/High>` | `<Open/Confirmed/Rejected>` |

---

## 9. Authorization and Access Control Review

### 9.1 Authorization Model

| Field                  | Value                                                 |
| ---------------------- | ----------------------------------------------------- |
| Authorization Type     | `<RBAC/ABAC/ReBAC/ACL/custom/none>`                   |
| Role Source            | `<database/token/IdP/config/code>`                    |
| Permission Source      | `<database/token/IdP/config/code>`                    |
| Enforcement Location   | `<middleware/controller/service/repository/database>` |
| Default Policy         | `<allow/deny/unknown>`                                |
| Tenant Isolation Model | `<tenant_id/org_id/account_id/project_id/etc>`        |

### 9.2 Roles and Permissions

| Role          | Permissions     | Sensitive Actions     | Notes     |
| ------------- | --------------- | --------------------- | --------- |
| `<role_name>` | `<permissions>` | `<sensitive_actions>` | `<notes>` |

### 9.3 Authorization Checklist

* [ ] Authorization enforced server-side
* [ ] Authorization enforced on every protected endpoint
* [ ] Object-level authorization reviewed
* [ ] Function-level authorization reviewed
* [ ] Tenant isolation reviewed
* [ ] Administrative actions reviewed
* [ ] Horizontal privilege escalation paths reviewed
* [ ] Vertical privilege escalation paths reviewed
* [ ] Default-deny behavior confirmed
* [ ] Authorization checks cannot be bypassed through alternate routes
* [ ] Authorization checks cannot be bypassed through direct object references
* [ ] Background jobs and async consumers enforce authorization where applicable
* [ ] GraphQL resolvers enforce authorization per object and field where applicable
* [ ] WebSocket or streaming actions enforce authorization after connection establishment

### 9.4 Authorization Enforcement Points

| Enforcement Point     | File          | Function          | Protected Action | Roles Allowed | Evidence        |
| --------------------- | ------------- | ----------------- | ---------------- | ------------- | --------------- |
| `<enforcement_point>` | `<file_path>` | `<function_name>` | `<action>`       | `<roles>`     | `<evidence_id>` |

### 9.5 Authorization Gaps

| ID            | Gap     | Affected Endpoint / Function | Affected Role | Evidence        | Confidence          |
| ------------- | ------- | ---------------------------- | ------------- | --------------- | ------------------- |
| `<AUTHZ-001>` | `<gap>` | `<endpoint_or_function>`     | `<role>`      | `<evidence_id>` | `<Low/Medium/High>` |

---

## 10. Session, Cookie, and Token Handling

### 10.1 Session / Token Model

| Field                | Value                                                             |
| -------------------- | ----------------------------------------------------------------- |
| Session Type         | `<server-side/session-cookie/JWT/OAuth token/API key/custom>`     |
| Token Format         | `<JWT/opaque/custom/not_applicable>`                              |
| Token Storage        | `<cookie/localStorage/sessionStorage/memory/mobile_keystore/etc>` |
| Token Issuer         | `<issuer>`                                                        |
| Token Audience       | `<audience>`                                                      |
| Token Lifetime       | `<duration>`                                                      |
| Refresh Token Used   | `<Yes/No>`                                                        |
| Revocation Supported | `<Yes/No/Partial>`                                                |

### 10.2 Cookie Security Review

| Cookie          | Purpose     | HttpOnly   | Secure     | SameSite                  | Domain     | Path     | Notes     |
| --------------- | ----------- | ---------- | ---------- | ------------------------- | ---------- | -------- | --------- |
| `<cookie_name>` | `<purpose>` | `<Yes/No>` | `<Yes/No>` | `<Strict/Lax/None/Unset>` | `<domain>` | `<path>` | `<notes>` |

### 10.3 Token Claims Review

| Claim          | Purpose     | Trusted?           | Validation Location  | Notes     |
| -------------- | ----------- | ------------------ | -------------------- | --------- |
| `<claim_name>` | `<purpose>` | `<Yes/No/Partial>` | `<file_or_function>` | `<notes>` |

### 10.4 Session and Token Checklist

* [ ] Session identifiers are generated securely
* [ ] Cookies use `HttpOnly` where applicable
* [ ] Cookies use `Secure` where applicable
* [ ] Cookies use appropriate `SameSite`
* [ ] Token signature validation is enforced
* [ ] Token issuer validation is enforced
* [ ] Token audience validation is enforced
* [ ] Token expiration validation is enforced
* [ ] Refresh token rotation reviewed
* [ ] Logout and revocation behavior reviewed
* [ ] Privilege changes invalidate or refresh authorization context
* [ ] Tokens are not logged
* [ ] Tokens are not stored in unsafe client-side storage without justification
* [ ] API keys are scoped and rotated
* [ ] Session fixation protections reviewed

### 10.5 Session / Token Evidence

```text
<session_or_token_code_snippet_http_response_or_tool_output>
```

---

## 11. User-Controlled Inputs and Entry Points

### 11.1 Input Inventory

| Input ID   | Source                                                | Endpoint / Function      | Parameter / Field | Type     | Trust Level                             | Validation             |
| ---------- | ----------------------------------------------------- | ------------------------ | ----------------- | -------- | --------------------------------------- | ---------------------- |
| `<IN-001>` | `<HTTP/CLI/file/queue/webhook/env/header/cookie/etc>` | `<endpoint_or_function>` | `<parameter>`     | `<type>` | `<trusted/untrusted/partially_trusted>` | `<validation_summary>` |

### 11.2 Input Validation Checklist

* [ ] Required fields validated
* [ ] Type validation implemented
* [ ] Length validation implemented
* [ ] Range validation implemented
* [ ] Format validation implemented
* [ ] Allowlist validation used where appropriate
* [ ] Nested object validation implemented
* [ ] File type validation implemented where applicable
* [ ] File size validation implemented where applicable
* [ ] Parser depth and recursion limits implemented
* [ ] Canonicalization performed before authorization or path decisions
* [ ] Validation failures handled safely
* [ ] Validation logic is centralized where appropriate

### 11.3 Input Validation Code Evidence

```text
<input_validation_code_snippet>
```

### 11.4 Untrusted Input Concerns

| ID            | Input          | Concern     | Evidence        | Potential Sink | Confidence          |
| ------------- | -------------- | ----------- | --------------- | -------------- | ------------------- |
| `<INPUT-001>` | `<input_name>` | `<concern>` | `<evidence_id>` | `<sink>`       | `<Low/Medium/High>` |

---

## 12. Source-to-Sink Data Flow Review

### 12.1 Data Flow Summary

```text
<Describe important source-to-sink flows, including user-controlled inputs, transformations, validation, authorization decisions, and sensitive sinks.>
```

### 12.2 Source-to-Sink Table

| Flow ID      | Source     | Transformation / Validation | Sink     | Affected Component | Risk     | Evidence        | Confidence          |
| ------------ | ---------- | --------------------------- | -------- | ------------------ | -------- | --------------- | ------------------- |
| `<FLOW-001>` | `<source>` | `<transform_validation>`    | `<sink>` | `<component>`      | `<risk>` | `<evidence_id>` | `<Low/Medium/High>` |

### 12.3 Source Categories

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
* [ ] Database records from lower-trust sources
* [ ] External API responses
* [ ] Mobile client inputs
* [ ] Desktop client inputs
* [ ] IPC / RPC messages
* [ ] Serialized objects
* [ ] GraphQL variables
* [ ] WebSocket messages

### 12.4 Sink Categories

* [ ] SQL / NoSQL queries
* [ ] OS command execution
* [ ] Template rendering
* [ ] File path access
* [ ] File write / overwrite
* [ ] SSRF-relevant outbound requests
* [ ] Deserialization
* [ ] XML parsing
* [ ] HTML rendering
* [ ] Redirects / forwards
* [ ] Authentication decisions
* [ ] Authorization decisions
* [ ] Cryptographic operations
* [ ] Logging
* [ ] Email / notification generation
* [ ] LDAP queries
* [ ] XPath queries
* [ ] Expression language evaluation
* [ ] Reflection / dynamic invocation
* [ ] Dynamic code loading
* [ ] Memory-unsafe operations

### 12.5 Data Flow Diagram

```text
<Insert source-to-sink data flow diagram here>

Example:

[Untrusted Source: <input>]
          |
          v
[Parser / Binder: <function>]
          |
          v
[Validation: <function>]
          |
          v
[Authorization: <function>]
          |
          v
[Sink: <database/file/network/command/etc>]
          |
          v
[Security Impact: <impact>]
```

---

## 13. Dangerous APIs and Risky Patterns

### 13.1 Dangerous API Inventory

| API / Function      | File          |        Line(s) | Category     | Input Source     | Risk     | Evidence        |
| ------------------- | ------------- | -------------: | ------------ | ---------------- | -------- | --------------- |
| `<api_or_function>` | `<file_path>` | `<line_range>` | `<category>` | `<input_source>` | `<risk>` | `<evidence_id>` |

### 13.2 Risky Pattern Checklist

* [ ] Raw SQL query construction
* [ ] Dynamic NoSQL query construction
* [ ] OS command execution
* [ ] Dynamic code evaluation
* [ ] Unsafe reflection
* [ ] Unsafe deserialization
* [ ] Unsafe XML parsing
* [ ] Path concatenation with user input
* [ ] File upload to executable or public paths
* [ ] SSRF-capable HTTP clients
* [ ] Open redirect logic
* [ ] Template rendering with user-controlled content
* [ ] Unsafe regular expressions
* [ ] Hardcoded secrets
* [ ] Weak cryptographic algorithms
* [ ] Custom cryptography
* [ ] Insecure randomness
* [ ] Sensitive data in logs
* [ ] Missing authorization checks
* [ ] Client-side trust decisions
* [ ] Missing rate limits on sensitive actions
* [ ] Business logic state transitions without server-side validation
* [ ] Use of deprecated libraries or APIs
* [ ] Unsafe C/C++ memory functions where applicable

### 13.3 Risky Pattern Evidence

```text
<risky_pattern_code_snippet_or_tool_output>
```

### 13.4 Review Decision Points

| Decision Point                      | Criteria     | Decision   | Rationale     | Evidence        |
| ----------------------------------- | ------------ | ---------- | ------------- | --------------- |
| Continue manual review              | `<criteria>` | `<Yes/No>` | `<rationale>` | `<evidence_id>` |
| Add SAST query                      | `<criteria>` | `<Yes/No>` | `<rationale>` | `<evidence_id>` |
| Perform targeted dynamic validation | `<criteria>` | `<Yes/No>` | `<rationale>` | `<evidence_id>` |
| Request developer clarification     | `<criteria>` | `<Yes/No>` | `<rationale>` | `<evidence_id>` |
| Escalate to architecture review     | `<criteria>` | `<Yes/No>` | `<rationale>` | `<evidence_id>` |
| Mark as false positive              | `<criteria>` | `<Yes/No>` | `<rationale>` | `<evidence_id>` |

---

## 14. Injection and Parser Security Review

### 14.1 SQL / NoSQL Injection Review

| Query Location     | File          | Function          | Query Construction Method | Parameterized?     | Evidence        | Notes     |
| ------------------ | ------------- | ----------------- | ------------------------- | ------------------ | --------------- | --------- |
| `<query_location>` | `<file_path>` | `<function_name>` | `<method>`                | `<Yes/No/Partial>` | `<evidence_id>` | `<notes>` |

Checklist:

* [ ] Parameterized queries used
* [ ] ORM usage reviewed for unsafe raw queries
* [ ] Dynamic query filters constrained
* [ ] Sort/order fields allowlisted
* [ ] NoSQL operators protected from user control
* [ ] Stored procedures reviewed for dynamic SQL
* [ ] Error messages do not expose query internals

### 14.2 Command Injection Review

| Call Site     | File          | Function          | Command Source | Input Validation | Evidence        |
| ------------- | ------------- | ----------------- | -------------- | ---------------- | --------------- |
| `<call_site>` | `<file_path>` | `<function_name>` | `<source>`     | `<validation>`   | `<evidence_id>` |

Checklist:

* [ ] Avoid shell invocation where possible
* [ ] Use fixed executable paths
* [ ] Use argument arrays instead of command strings where possible
* [ ] Validate and allowlist user-controlled arguments
* [ ] Avoid passing user input into shell metacharacter contexts
* [ ] Run with least privilege
* [ ] Log failures safely

### 14.3 XML / XXE Review

| Parser Location     | File          | Function          | External Entities Disabled | DTD Disabled       | Evidence        |
| ------------------- | ------------- | ----------------- | -------------------------- | ------------------ | --------------- |
| `<parser_location>` | `<file_path>` | `<function_name>` | `<Yes/No/Unknown>`         | `<Yes/No/Unknown>` | `<evidence_id>` |

Checklist:

* [ ] External entities disabled
* [ ] DTDs disabled where not required
* [ ] XInclude disabled where not required
* [ ] Network access blocked for XML parser where possible
* [ ] Large entity expansion protections enabled
* [ ] XML parser settings are explicit

### 14.4 Deserialization Review

| Deserialization Location | Format                                        | File          | Function          | Type Restrictions | Evidence        |
| ------------------------ | --------------------------------------------- | ------------- | ----------------- | ----------------- | --------------- |
| `<location>`             | `<JSON/XML/YAML/pickle/java/.NET/php/custom>` | `<file_path>` | `<function_name>` | `<restrictions>`  | `<evidence_id>` |

Checklist:

* [ ] Untrusted serialized data is not deserialized into arbitrary object types
* [ ] Type allowlists are enforced
* [ ] Schema validation is enforced
* [ ] Signatures or integrity checks are used where required
* [ ] Dangerous callbacks, constructors, or magic methods reviewed
* [ ] Parser size and depth limits enforced

### 14.5 Template Injection Review

| Template Location     | Engine     | File          | User-Controlled Input | Escaping             | Evidence        |
| --------------------- | ---------- | ------------- | --------------------- | -------------------- | --------------- |
| `<template_location>` | `<engine>` | `<file_path>` | `<input>`             | `<escaping_summary>` | `<evidence_id>` |

---

## 15. Cross-Site Scripting, Output Encoding, and Client Trust

### 15.1 Output Rendering Review

| Sink     | File          | Context                            | Encoding / Escaping | Input Source     | Evidence        |
| -------- | ------------- | ---------------------------------- | ------------------- | ---------------- | --------------- |
| `<sink>` | `<file_path>` | `<HTML/attribute/JS/CSS/URL/JSON>` | `<encoding>`        | `<input_source>` | `<evidence_id>` |

Checklist:

* [ ] Output encoding appropriate to context
* [ ] HTML sanitization used where rich text is required
* [ ] Dangerous HTML bypasses reviewed
* [ ] Client-side template rendering reviewed
* [ ] DOM sinks reviewed
* [ ] Markdown rendering reviewed
* [ ] CSP reviewed
* [ ] User-controlled URLs validated
* [ ] Open redirects reviewed
* [ ] Sensitive decisions not trusted to client-side code

### 15.2 CSRF Review

| Endpoint     | State-Changing? | Authenticated? | CSRF Protection        | Evidence        |
| ------------ | --------------- | -------------- | ---------------------- | --------------- |
| `<endpoint>` | `<Yes/No>`      | `<Yes/No>`     | `<protection_summary>` | `<evidence_id>` |

Checklist:

* [ ] CSRF tokens used where applicable
* [ ] SameSite cookie strategy reviewed
* [ ] State-changing GET requests avoided
* [ ] CORS does not weaken CSRF assumptions
* [ ] API authentication model evaluated for CSRF relevance

### 15.3 CORS Review

| Origin Policy     | Credentials Allowed | Affected Endpoint(s) | Risk     | Evidence        |
| ----------------- | ------------------- | -------------------- | -------- | --------------- |
| `<origin_policy>` | `<Yes/No>`          | `<endpoints>`        | `<risk>` | `<evidence_id>` |

---

## 16. File Handling and Upload Review

### 16.1 File Upload Inventory

| Upload Endpoint | File Types | Storage Location     | Access Control     | Processing Performed | Evidence        |
| --------------- | ---------- | -------------------- | ------------------ | -------------------- | --------------- |
| `<endpoint>`    | `<types>`  | `<storage_location>` | `<access_control>` | `<processing>`       | `<evidence_id>` |

### 16.2 File Handling Checklist

* [ ] File type validation performed server-side
* [ ] File size limits enforced
* [ ] File extension allowlist used
* [ ] MIME type not trusted alone
* [ ] Magic bytes checked where appropriate
* [ ] Uploaded files stored outside executable paths
* [ ] Uploaded files renamed safely
* [ ] Path traversal prevented
* [ ] Archive extraction protects against zip slip
* [ ] File permissions restricted
* [ ] Malware scanning or content inspection considered where appropriate
* [ ] Authorization enforced on file access
* [ ] Temporary files cleaned safely

### 16.3 File Access Review

| File Access Location | Path Construction     | User Input Involved | Canonicalization             | Evidence        |
| -------------------- | --------------------- | ------------------- | ---------------------------- | --------------- |
| `<location>`         | `<path_construction>` | `<Yes/No>`          | `<canonicalization_summary>` | `<evidence_id>` |

---

## 17. SSRF, Outbound Network Calls, and Webhooks

### 17.1 Outbound Request Inventory

| Call Site     | File          | Function          | Destination Source                        | Protocols Allowed | Evidence        |
| ------------- | ------------- | ----------------- | ----------------------------------------- | ----------------- | --------------- |
| `<call_site>` | `<file_path>` | `<function_name>` | `<fixed/user-controlled/config/external>` | `<protocols>`     | `<evidence_id>` |

### 17.2 SSRF Review Checklist

* [ ] User-controlled URLs reviewed
* [ ] Redirect handling reviewed
* [ ] DNS rebinding protections considered
* [ ] Internal IP ranges blocked where applicable
* [ ] Metadata service access blocked where applicable
* [ ] Protocol allowlist enforced
* [ ] Host allowlist enforced where applicable
* [ ] Request timeout enforced
* [ ] Response size limits enforced
* [ ] Authentication headers not forwarded unsafely
* [ ] Webhook targets validated
* [ ] Server-side fetch behavior logged and monitored

### 17.3 Webhook Security

| Webhook          | Direction            | Signature Validation | Replay Protection  | Evidence        |
| ---------------- | -------------------- | -------------------- | ------------------ | --------------- |
| `<webhook_name>` | `<inbound/outbound>` | `<Yes/No/Partial>`   | `<Yes/No/Partial>` | `<evidence_id>` |

---

## 18. Secrets Handling Review

### 18.1 Secret Inventory

| Secret Type                                     | Location     | Storage Mechanism | Rotation            | Exposure Risk | Evidence        |
| ----------------------------------------------- | ------------ | ----------------- | ------------------- | ------------- | --------------- |
| `<api_key/password/token/private_key/cert/etc>` | `<location>` | `<storage>`       | `<rotation_status>` | `<risk>`      | `<evidence_id>` |

### 18.2 Secrets Checklist

* [ ] No secrets hardcoded in source
* [ ] No secrets committed in config files
* [ ] No secrets stored in frontend code
* [ ] No secrets stored in mobile app bundles without compensating control
* [ ] No secrets printed in logs
* [ ] No secrets included in error messages
* [ ] Secrets loaded from approved secret store
* [ ] Secrets scoped to least privilege
* [ ] Rotation process documented
* [ ] CI/CD secrets protected
* [ ] Local development secrets excluded from repository
* [ ] Private keys protected and access-controlled

### 18.3 Secret Scanning Evidence

```text
<secret_scanning_tool_output>
```

### 18.4 Secret Handling Concerns

| ID          | Concern     | Location         | Evidence        | Impact     | Confidence          |
| ----------- | ----------- | ---------------- | --------------- | ---------- | ------------------- |
| `<SEC-001>` | `<concern>` | `<file_or_path>` | `<evidence_id>` | `<impact>` | `<Low/Medium/High>` |

---

## 19. Cryptography Review

### 19.1 Cryptographic Use Cases

| Use Case     | Algorithm / Library      | Key Source     | Mode     | Purpose     | Evidence        |
| ------------ | ------------------------ | -------------- | -------- | ----------- | --------------- |
| `<use_case>` | `<algorithm_or_library>` | `<key_source>` | `<mode>` | `<purpose>` | `<evidence_id>` |

### 19.2 Cryptography Checklist

* [ ] Approved cryptographic libraries used
* [ ] No custom cryptography without formal review
* [ ] Deprecated algorithms avoided
* [ ] Keys generated securely
* [ ] Randomness uses cryptographically secure RNG
* [ ] IVs / nonces are unique where required
* [ ] Passwords hashed with password-specific KDFs
* [ ] TLS certificate validation enforced
* [ ] Sensitive data encrypted at rest where required
* [ ] Sensitive data encrypted in transit
* [ ] Signature validation cannot be bypassed
* [ ] JWT algorithms restricted and validated
* [ ] Key rotation supported
* [ ] Error handling does not leak cryptographic details

### 19.3 Cryptography Evidence

```text
<cryptography_code_snippet_or_tool_output>
```

### 19.4 Cryptography Concerns

| ID             | Concern     | File / Function      | Evidence        | Risk     | Confidence          |
| -------------- | ----------- | -------------------- | --------------- | -------- | ------------------- |
| `<CRYPTO-001>` | `<concern>` | `<file_or_function>` | `<evidence_id>` | `<risk>` | `<Low/Medium/High>` |

---

## 20. Dependency and Supply-Chain Review

### 20.1 Dependency Inventory

| Package          | Version     | Ecosystem     | Direct / Transitive   | Known Issue     | Evidence        |
| ---------------- | ----------- | ------------- | --------------------- | --------------- | --------------- |
| `<package_name>` | `<version>` | `<ecosystem>` | `<direct/transitive>` | `<known_issue>` | `<evidence_id>` |

### 20.2 Dependency Review Checklist

* [ ] Lock files present
* [ ] Dependency versions pinned where appropriate
* [ ] Known vulnerabilities reviewed
* [ ] Deprecated packages reviewed
* [ ] Unmaintained packages reviewed
* [ ] Typosquatting risk considered
* [ ] Dependency confusion risk considered
* [ ] Private package registries configured safely
* [ ] Build scripts reviewed
* [ ] Post-install scripts reviewed where applicable
* [ ] License constraints reviewed where applicable
* [ ] Container base images reviewed
* [ ] SBOM generated or reviewed where applicable
* [ ] Dependency update process documented

### 20.3 Dependency Tool Output

```text
<dependency_scanning_tool_output>
```

### 20.4 Supply-Chain Controls

| Control              | Present            | Evidence        | Notes     |
| -------------------- | ------------------ | --------------- | --------- |
| SBOM                 | `<Yes/No/Partial>` | `<evidence_id>` | `<notes>` |
| Signed commits       | `<Yes/No/Partial>` | `<evidence_id>` | `<notes>` |
| Signed artifacts     | `<Yes/No/Partial>` | `<evidence_id>` | `<notes>` |
| Protected branches   | `<Yes/No/Partial>` | `<evidence_id>` | `<notes>` |
| Required reviews     | `<Yes/No/Partial>` | `<evidence_id>` | `<notes>` |
| CI secret protection | `<Yes/No/Partial>` | `<evidence_id>` | `<notes>` |
| Artifact provenance  | `<Yes/No/Partial>` | `<evidence_id>` | `<notes>` |

---

## 21. Error Handling, Logging, and Monitoring Review

### 21.1 Error Handling Review

| Error Path     | File / Function      | User-Facing Message | Internal Detail Exposed | Evidence        |
| -------------- | -------------------- | ------------------- | ----------------------- | --------------- |
| `<error_path>` | `<file_or_function>` | `<message>`         | `<Yes/No/Partial>`      | `<evidence_id>` |

### 21.2 Logging Review

| Log Event     | File / Function      | Data Logged     | Sensitive Data Risk | Evidence        |
| ------------- | -------------------- | --------------- | ------------------- | --------------- |
| `<log_event>` | `<file_or_function>` | `<data_logged>` | `<risk>`            | `<evidence_id>` |

### 21.3 Logging and Error Checklist

* [ ] Sensitive data is not logged
* [ ] Tokens and secrets are redacted
* [ ] Passwords are never logged
* [ ] PII logging is minimized and justified
* [ ] Error responses do not expose stack traces in production
* [ ] Error responses do not expose internal paths
* [ ] Security-relevant events are logged
* [ ] Authorization failures are logged safely
* [ ] Authentication failures are logged safely
* [ ] Rate-limit events are logged
* [ ] Audit logs are tamper-resistant where required
* [ ] Logs include sufficient context for investigation
* [ ] Logs avoid excessive sensitive context
* [ ] Monitoring and alerting exist for critical events

### 21.4 Stack Trace / Log Evidence

```text
<log_or_stack_trace_output>
```

---

## 22. Business Logic and Workflow Review

### 22.1 Critical Workflows

| Workflow          | Steps              | Roles Involved | Security Objective | Notes     |
| ----------------- | ------------------ | -------------- | ------------------ | --------- |
| `<workflow_name>` | `<workflow_steps>` | `<roles>`      | `<objective>`      | `<notes>` |

### 22.2 Business Logic Checklist

* [ ] Workflow state transitions enforced server-side
* [ ] Users cannot skip required workflow steps
* [ ] Approval workflows cannot be self-approved unless intended
* [ ] Pricing, quotas, limits, or balances cannot be modified client-side
* [ ] Idempotency and replay behavior reviewed
* [ ] Race conditions considered for sensitive workflows
* [ ] Authorization enforced at each workflow transition
* [ ] Tenant boundaries enforced in workflows
* [ ] Time-based constraints enforced server-side
* [ ] Business rules are centralized or consistently enforced
* [ ] Sensitive actions require appropriate confirmation
* [ ] Audit trail captures critical workflow events

### 22.3 Workflow State Diagram

```text
<Insert business workflow or state-machine diagram here>

Example:

[Created]
    |
    v
[Pending Approval] -- rejected --> [Rejected]
    |
 approved
    v
[Active] -- revoke --> [Revoked]
```

### 22.4 Business Logic Concerns

| ID            | Workflow     | Concern     | Evidence        | Impact     | Confidence          |
| ------------- | ------------ | ----------- | --------------- | ---------- | ------------------- |
| `<LOGIC-001>` | `<workflow>` | `<concern>` | `<evidence_id>` | `<impact>` | `<Low/Medium/High>` |

---

## 23. Configuration, Infrastructure-as-Code, and Cloud Review

### 23.1 Configuration Review

| File          | Setting     | Current Value         | Risk     | Recommendation     |
| ------------- | ----------- | --------------------- | -------- | ------------------ |
| `<file_path>` | `<setting>` | `<value_or_redacted>` | `<risk>` | `<recommendation>` |

### 23.2 IaC Review Checklist

* [ ] Public exposure reviewed
* [ ] Security groups / firewall rules reviewed
* [ ] IAM permissions follow least privilege
* [ ] Storage buckets are not publicly exposed unless intended
* [ ] Encryption at rest configured where required
* [ ] TLS enforced where required
* [ ] Secrets not stored in IaC state or source
* [ ] Logging enabled for critical resources
* [ ] Monitoring and alerting configured
* [ ] Backups configured where required
* [ ] Administrative access restricted
* [ ] Metadata service protections configured where applicable
* [ ] Container privileges reviewed
* [ ] Kubernetes RBAC reviewed where applicable
* [ ] Network policies reviewed where applicable

### 23.3 Cloud / IaC Evidence

```text
<iac_or_cloud_configuration_snippet_or_tool_output>
```

### 23.4 IAM and Permission Review

| Principal     | Permission / Role      | Resource     | Risk     | Evidence        |
| ------------- | ---------------------- | ------------ | -------- | --------------- |
| `<principal>` | `<permission_or_role>` | `<resource>` | `<risk>` | `<evidence_id>` |

---

## 24. CI/CD and Build Pipeline Review

### 24.1 Pipeline Inventory

| Pipeline          | Path     | Trigger     | Secrets Used | Deployment Target | Notes     |
| ----------------- | -------- | ----------- | ------------ | ----------------- | --------- |
| `<pipeline_name>` | `<path>` | `<trigger>` | `<secrets>`  | `<target>`        | `<notes>` |

### 24.2 CI/CD Checklist

* [ ] Branch protections enabled
* [ ] Required code review enforced
* [ ] Required security checks enforced
* [ ] Secrets stored in approved secret manager
* [ ] Secrets not printed in logs
* [ ] Build artifacts protected
* [ ] Deployment approvals configured where required
* [ ] Pull request workflows cannot access privileged secrets unsafely
* [ ] Third-party actions pinned by version or commit
* [ ] Build scripts reviewed for command injection risk
* [ ] Artifact signing reviewed where applicable
* [ ] Test and production credentials separated
* [ ] Least privilege used for pipeline tokens
* [ ] Dependency scanning integrated
* [ ] SAST or code scanning integrated where appropriate

### 24.3 CI/CD Evidence

```yaml
<cicd_configuration_snippet>
```

### 24.4 Pipeline Concerns

| ID           | Concern     | File / Pipeline      | Evidence        | Impact     | Confidence          |
| ------------ | ----------- | -------------------- | --------------- | ---------- | ------------------- |
| `<CICD-001>` | `<concern>` | `<file_or_pipeline>` | `<evidence_id>` | `<impact>` | `<Low/Medium/High>` |

---

## 25. Privacy and Sensitive Data Review

### 25.1 Sensitive Data Inventory

| Data Type     | Location     | Classification     | Protection     | Notes     |
| ------------- | ------------ | ------------------ | -------------- | --------- |
| `<data_type>` | `<location>` | `<classification>` | `<protection>` | `<notes>` |

### 25.2 Privacy Checklist

* [ ] Sensitive data collected only when necessary
* [ ] Sensitive data minimized
* [ ] Sensitive data encrypted in transit
* [ ] Sensitive data encrypted at rest where required
* [ ] Sensitive data not logged unnecessarily
* [ ] Sensitive data redacted in errors
* [ ] Data retention requirements documented
* [ ] Data deletion workflow reviewed
* [ ] Access to sensitive data audited
* [ ] Cross-border or regulatory constraints considered where applicable

### 25.3 Sensitive Data Flow

```text
<Insert sensitive data flow diagram here>
```

---

## 26. SAST, Semgrep, CodeQL, and Tool-Assisted Review

### 26.1 Tooling Summary

| Tool          | Version     | Ruleset / Query Pack | Scope     | Notes     |
| ------------- | ----------- | -------------------- | --------- | --------- |
| `<tool_name>` | `<version>` | `<ruleset>`          | `<scope>` | `<notes>` |

### 26.2 Tool Commands

```bash
<sast_or_query_command>
```

### 26.3 Tool Output

```text
<sast_or_query_output>
```

### 26.4 Tool Findings Triage

| Tool Finding ID     | Rule     | Location      | Initial Severity | Triage Result                                 | Evidence        | Notes     |
| ------------------- | -------- | ------------- | ---------------- | --------------------------------------------- | --------------- | --------- |
| `<tool_finding_id>` | `<rule>` | `<file_line>` | `<severity>`     | `<true_positive/false_positive/needs_review>` | `<evidence_id>` | `<notes>` |

### 26.5 Custom Query Notes

```text
<Describe custom SAST, Semgrep, CodeQL, grep, AST, or data-flow queries used during the review.>
```

---

## 27. Safe Validation Guidance

### 27.1 Validation Scope

```text
<Describe the authorized environment where validation was performed. Include boundaries, test accounts, test data, and limitations.>
```

### 27.2 Validation Rules

* [ ] Validation performed only in approved environment
* [ ] Test data used instead of production-sensitive data
* [ ] Non-destructive validation method used
* [ ] No weaponized payloads used
* [ ] No persistence, stealth, credential theft, or unauthorized access attempted
* [ ] Validation steps documented clearly
* [ ] Expected and actual results recorded
* [ ] Cleanup completed
* [ ] Retest evidence captured

### 27.3 Safe Validation Steps

```text
<Step 1: Describe safe setup>
<Step 2: Describe benign trigger or controlled test>
<Step 3: Describe expected observable result>
<Step 4: Describe cleanup>
```

### 27.4 Expected Result

```text
<expected_result>
```

### 27.5 Actual Result

```text
<actual_result>
```

### 27.6 HTTP Evidence

```http
<safe_http_request_or_response>
```

### 27.7 Validation Logs

```text
<validation_log_output>
```

### 27.8 What This Proves

```text
<Describe the security condition proven by the validation.>
```

### 27.9 What This Does Not Prove

```text
<Describe limitations, assumptions, untested environments, and unproven exploitability.>
```

---

## 28. Findings Register

| Finding ID   | Title             | Severity                                   | Confidence          | CWE        | OWASP Category     | Affected Component | Affected Endpoint | Status                                                   |
| ------------ | ----------------- | ------------------------------------------ | ------------------- | ---------- | ------------------ | ------------------ | ----------------- | -------------------------------------------------------- |
| `<FIND-001>` | `<finding_title>` | `<Informational/Low/Medium/High/Critical>` | `<Low/Medium/High>` | `<CWE-ID>` | `<OWASP_category>` | `<component>`      | `<endpoint>`      | `<Open/Fixed/Retest Passed/Retest Failed/Accepted Risk>` |

---

## 29. Finding Detail Template

Copy this section for each confirmed finding.

### `<finding_id>` — `<finding_title>`

| Field                     | Value                                                    |
| ------------------------- | -------------------------------------------------------- |
| Finding ID                | `<finding_id>`                                           |
| Title                     | `<finding_title>`                                        |
| Severity                  | `<Informational/Low/Medium/High/Critical>`               |
| Confidence                | `<Low/Medium/High>`                                      |
| Status                    | `<Open/Fixed/Retest Passed/Retest Failed/Accepted Risk>` |
| Affected Application      | `<application_name>`                                     |
| Affected Component        | `<affected_component>`                                   |
| Affected Repository       | `<repository_url>`                                       |
| Affected Branch           | `<branch_name>`                                          |
| Affected Commit           | `<commit_hash>`                                          |
| Affected File(s)          | `<affected_files>`                                       |
| Affected Function(s)      | `<affected_functions>`                                   |
| Affected Endpoint(s)      | `<affected_endpoints>`                                   |
| Affected Role(s)          | `<affected_roles>`                                       |
| Affected Asset(s)         | `<affected_assets>`                                      |
| CWE                       | `<CWE-ID: CWE Name>`                                     |
| OWASP Category            | `<OWASP_category>`                                       |
| CVSS Vector               | `<CVSS_vector>`                                          |
| CVSS Score                | `<CVSS_score>`                                           |
| Exploitability            | `<Low/Medium/High>`                                      |
| Business Impact           | `<business_impact>`                                      |
| Technical Impact          | `<technical_impact>`                                     |
| Preconditions             | `<preconditions>`                                        |
| User Interaction Required | `<Yes/No>`                                               |
| Privileges Required       | `<None/Low/High>`                                        |
| Detection Opportunity     | `<detection_opportunity>`                                |
| Remediation Owner         | `<owner>`                                                |
| Target Fix Date           | `<YYYY-MM-DD>`                                           |

### 29.1 Summary

```text
<Concise explanation of the issue, why it exists, and why it matters.>
```

### 29.2 Facts

| ID           | Fact     | Evidence        | Confidence          |
| ------------ | -------- | --------------- | ------------------- |
| `<FACT-001>` | `<fact>` | `<evidence_id>` | `<Low/Medium/High>` |

### 29.3 Evidence

| Evidence ID  | Description     | File / Path   | Line(s)        | Notes     |
| ------------ | --------------- | ------------- | -------------- | --------- |
| `<EVID-001>` | `<description>` | `<file_path>` | `<line_range>` | `<notes>` |

### 29.4 Vulnerable / Risky Code

```text
<code_snippet>
```

### 29.5 Source-to-Sink Explanation

| Source     | Path / Transformation | Sink     | Missing Control     | Evidence        |
| ---------- | --------------------- | -------- | ------------------- | --------------- |
| `<source>` | `<path>`              | `<sink>` | `<missing_control>` | `<evidence_id>` |

### 29.6 Safe Validation

```text
<Describe controlled, non-destructive validation steps performed in an authorized environment.>
```

### 29.7 Validation Evidence

```http
<http_request_or_response_if_applicable>
```

```text
<logs_tool_output_or_runtime_evidence>
```

### 29.8 Impact

```text
<Describe realistic security and business impact. Separate confirmed impact from potential impact.>
```

### 29.9 Root Cause

```text
<Describe the code, design, configuration, or process root cause.>
```

### 29.10 Remediation

```text
<Describe specific remediation steps, safer implementation patterns, configuration changes, dependency upgrades, or architectural changes.>
```

### 29.11 Secure Code Example / Pattern

```text
<safe_code_pattern_or_pseudocode>
```

### 29.12 Verification Steps

```text
<Describe how reviewers or engineers should verify the fix safely.>
```

### 29.13 Retest Result

| Field           | Value                                  |
| --------------- | -------------------------------------- |
| Retest Date     | `<YYYY-MM-DD>`                         |
| Retested By     | `<reviewer_name>`                      |
| Retest Commit   | `<commit_hash>`                        |
| Retest Result   | `<Passed/Failed/Partial/Not Retested>` |
| Retest Evidence | `<evidence_id_or_path>`                |
| Notes           | `<notes>`                              |

---

## 30. Remediation Plan

| Finding ID     | Remediation Action | Owner     | Priority        | Target Date    | Status                             | Notes     |
| -------------- | ------------------ | --------- | --------------- | -------------- | ---------------------------------- | --------- |
| `<finding_id>` | `<action>`         | `<owner>` | `<P0/P1/P2/P3>` | `<YYYY-MM-DD>` | `<open/in_progress/done/deferred>` | `<notes>` |

### 30.1 Remediation Themes

| Theme     | Related Findings | Recommendation     | Notes     |
| --------- | ---------------- | ------------------ | --------- |
| `<theme>` | `<finding_ids>`  | `<recommendation>` | `<notes>` |

### 30.2 Secure SDLC Improvements

* [ ] Add security requirements for identified risk areas
* [ ] Add security unit tests
* [ ] Add integration tests for access control
* [ ] Add abuse-case tests
* [ ] Add SAST checks to CI
* [ ] Add dependency scanning to CI
* [ ] Add secret scanning to CI
* [ ] Add IaC scanning to CI
* [ ] Add code-owner review for security-sensitive modules
* [ ] Add threat modeling for high-risk changes
* [ ] Add secure coding guidance for recurring issue classes
* [ ] Add regression tests for fixed findings

---

## 31. Risk Acceptance

| Finding ID     | Risk Accepted? | Accepted By   | Date           | Expiration     | Compensating Controls | Notes     |
| -------------- | -------------- | ------------- | -------------- | -------------- | --------------------- | --------- |
| `<finding_id>` | `<Yes/No>`     | `<name_role>` | `<YYYY-MM-DD>` | `<YYYY-MM-DD>` | `<controls>`          | `<notes>` |

### 31.1 Risk Acceptance Rationale

```text
<Describe why the risk is being accepted, what compensating controls exist, and when it should be reviewed again.>
```

---

## 32. Evidence Index

| Evidence ID  | Description     | File / Path      | Tool     | Timestamp     | Related Section | Notes     |
| ------------ | --------------- | ---------------- | -------- | ------------- | --------------- | --------- |
| `<EVID-001>` | `<description>` | `<file_or_path>` | `<tool>` | `<timestamp>` | `<section>`     | `<notes>` |

### 32.1 Evidence Storage Layout

```text
<evidence_root>/
├── 00_metadata/
├── 01_scope/
├── 02_architecture/
├── 03_threat_model/
├── 04_static_review/
├── 05_sast/
├── 06_dependencies/
├── 07_iac/
├── 08_cicd/
├── 09_validation/
├── 10_findings/
├── 11_retest/
└── 12_report/
```

### 32.2 Evidence Handling Notes

```text
<Describe evidence integrity, sensitive data handling, redaction requirements, storage controls, and retention expectations.>
```

---

## 33. Reproducibility Appendix

### 33.1 Repository Checkout

```bash
<git_clone_checkout_commands>
```

### 33.2 Build Commands

```bash
<build_commands>
```

### 33.3 Test Commands

```bash
<test_commands>
```

### 33.4 SAST / Query Commands

```bash
<sast_query_commands>
```

### 33.5 Dependency Review Commands

```bash
<dependency_review_commands>
```

### 33.6 IaC Review Commands

```bash
<iac_review_commands>
```

### 33.7 Secret Scanning Commands

```bash
<secret_scanning_commands>
```

### 33.8 Expected Output

```text
<expected_output>
```

### 33.9 Troubleshooting Notes

| Issue     | Cause     | Resolution     | Notes     |
| --------- | --------- | -------------- | --------- |
| `<issue>` | `<cause>` | `<resolution>` | `<notes>` |

### 33.10 Reproduction Checklist

* [ ] Correct repository URL used
* [ ] Correct branch checked out
* [ ] Correct commit hash checked out
* [ ] Tool versions recorded
* [ ] Build completed successfully
* [ ] Tests completed successfully
* [ ] Review commands copied from fenced blocks
* [ ] Output compared against expected output
* [ ] Deviations documented
* [ ] Evidence paths updated

---

## 34. Review Quality Checklist

* [ ] Scope is clear
* [ ] Authorization is documented
* [ ] Commit hash is documented
* [ ] Architecture is documented
* [ ] Threat model is documented
* [ ] Trust boundaries are documented
* [ ] Authentication reviewed
* [ ] Authorization reviewed
* [ ] Session/token handling reviewed
* [ ] User-controlled inputs reviewed
* [ ] Source-to-sink flows reviewed
* [ ] Dangerous APIs reviewed
* [ ] Dependencies reviewed
* [ ] Secrets reviewed
* [ ] Cryptography reviewed
* [ ] Logging/error handling reviewed
* [ ] Business logic reviewed
* [ ] IaC reviewed where applicable
* [ ] CI/CD reviewed where applicable
* [ ] Findings have evidence
* [ ] Findings separate facts from hypotheses
* [ ] Findings include severity and confidence
* [ ] Findings include CWE and OWASP mapping
* [ ] Findings include remediation
* [ ] Validation is safe and authorized
* [ ] Retest status is recorded
* [ ] Open questions are documented

---

## 35. Open Questions / Follow-Up Tasks

### 35.1 Open Questions

| ID        | Question     | Why It Matters     | Owner     | Status                     |
| --------- | ------------ | ------------------ | --------- | -------------------------- |
| `<Q-001>` | `<question>` | `<why_it_matters>` | `<owner>` | `<open/answered/deferred>` |

### 35.2 Follow-Up Tasks

| Task ID      | Task                 | Priority            | Owner     | Due Date       | Status                                 |
| ------------ | -------------------- | ------------------- | --------- | -------------- | -------------------------------------- |
| `<TASK-001>` | `<task_description>` | `<High/Medium/Low>` | `<owner>` | `<YYYY-MM-DD>` | `<open/in_progress/complete/deferred>` |

### 35.3 Reviewer Comments

| Reviewer          | Date           | Comment     | Resolution     |
| ----------------- | -------------- | ----------- | -------------- |
| `<reviewer_name>` | `<YYYY-MM-DD>` | `<comment>` | `<resolution>` |

### 35.4 Final Analyst Notes

```text
<Freeform notes, caveats, context, lessons learned, and observations not captured elsewhere.>
```
