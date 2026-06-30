# Bug Bounty Finding Template

> **Scope:** Authorized bug bounty testing only. Do not use this template to document unauthorized testing, destructive actions, credential theft, persistence, stealth, evasion, or activity outside the program’s published scope.

---

## 1. Title

`<Clear vulnerability title>`

Example format:

```text
<Vulnerability Type> in <Affected Feature/Endpoint> Allows <Impact>
```

---

## 2. Program / Asset

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| Program                | `<program_name>`                                       |
| Asset                  | `<asset_name>`                                         |
| Asset URL / Identifier | `<asset_url_or_identifier>`                            |
| Environment            | `<production / staging / test / mobile / API / other>` |
| Submission Date        | `<YYYY-MM-DD>`                                         |
| Researcher             | `<researcher_handle>`                                  |

---

## 3. Scope Confirmation

| Scope Item                    | Value                                         |
| ----------------------------- | --------------------------------------------- |
| Asset In Scope                | `<Yes / No>`                                  |
| Scope Reference               | `<program_scope_reference>`                   |
| Testing Account Used          | `<test_account_or_role>`                      |
| Data Used                     | `<test_data_only / redacted / non-sensitive>` |
| Out-of-Scope Activity Avoided | `<Yes / No>`                                  |

```text
<Briefly explain why this asset and testing activity are within the program’s authorized scope.>
```

---

## 4. Vulnerability Type

| Field                       | Value                                         |
| --------------------------- | --------------------------------------------- |
| Vulnerability Type          | `<vulnerability_type>`                        |
| CWE                         | `<CWE-ID: CWE Name>`                          |
| OWASP Category              | `<OWASP_category_if_applicable>`              |
| Affected Feature / Endpoint | `<endpoint_or_feature>`                       |
| Affected Method             | `<GET / POST / PUT / PATCH / DELETE / other>` |
| Affected Parameter / Object | `<parameter_object_or_resource>`              |

---

## 5. Severity

| Field              | Value                                              |
| ------------------ | -------------------------------------------------- |
| Severity           | `<Informational / Low / Medium / High / Critical>` |
| Confidence         | `<Low / Medium / High>`                            |
| CVSS Vector        | `<CVSS_vector_if_applicable>`                      |
| CVSS Score         | `<CVSS_score_if_applicable>`                       |
| Severity Rationale | `<short_rationale>`                                |

---

## 6. Summary

```text
<Provide a concise summary of the vulnerability, where it exists, what causes it, and what impact it has. Keep this clear enough for triage and program staff to understand quickly.>
```

---

## 7. Technical Details

### 7.1 Vulnerable Behavior

```text
<Describe the vulnerable behavior and why the current control is insufficient.>
```

### 7.2 Affected Endpoint or Feature

| Field                     | Value                   |
| ------------------------- | ----------------------- |
| Endpoint / Feature        | `<endpoint_or_feature>` |
| HTTP Method               | `<method>`              |
| Parameter / Field         | `<parameter_or_field>`  |
| Required Role             | `<required_role>`       |
| Authentication Required   | `<Yes / No>`            |
| User Interaction Required | `<Yes / No>`            |

### 7.3 Preconditions

* [ ] `<precondition_1>`
* [ ] `<precondition_2>`
* [ ] `<precondition_3>`

---

## 8. Steps to Reproduce

> Use only authorized test accounts, test data, and non-destructive actions.

1. `<step_1>`
2. `<step_2>`
3. `<step_3>`
4. `<step_4>`

### Expected Result

```text
<Describe the secure expected behavior.>
```

### Actual Result

```text
<Describe the observed vulnerable behavior.>
```

---

## 9. Proof of Concept

### 9.1 Request

```http
<sanitized_HTTP_request>
```

### 9.2 Response

```http
<sanitized_HTTP_response>
```

### 9.3 Command, Script, or Tool Output

```bash
<safe_authorized_command_if_applicable>
```

```text
<observed_output>
```

### 9.4 What This Proves

```text
<Explain exactly what the proof demonstrates. Avoid overstating impact beyond the evidence.>
```

### 9.5 What This Does Not Prove

```text
<Explain limitations, untested roles, untested assets, or impact that was not validated.>
```

---

## 10. Impact

### 10.1 Technical Impact

* [ ] Unauthorized data access
* [ ] Unauthorized data modification
* [ ] Privilege escalation
* [ ] Authentication bypass
* [ ] Authorization bypass
* [ ] Account takeover
* [ ] Information disclosure
* [ ] Tenant isolation failure
* [ ] Remote code execution
* [ ] Denial of service
* [ ] Business logic abuse
* [ ] Other: `<other_technical_impact>`

```text
<Describe the confirmed technical impact based on evidence.>
```

### 10.2 Business Impact

```text
<Describe realistic business impact, such as customer data exposure, fraud risk, account compromise, regulatory exposure, operational disruption, or reputational harm.>
```

---

## 11. Attack Scenario

```text
<Describe a realistic abuse scenario using only high-level, defensive language. Do not include instructions for attacking unrelated systems or scaling exploitation outside the authorized program.>
```

Example structure:

```text
An authenticated user with <role> could abuse <vulnerable_feature> to <impact>. This could allow access to <affected_data_or_action> belonging to <affected_user_or_tenant>, resulting in <business_or_security_impact>.
```

---

## 12. Supporting Evidence

| Evidence ID  | Description     | Type                                                               | Path / Reference      |
| ------------ | --------------- | ------------------------------------------------------------------ | --------------------- |
| `<EVID-001>` | `<description>` | `<screenshot / request / response / log / video / command_output>` | `<path_or_reference>` |
| `<EVID-002>` | `<description>` | `<type>`                                                           | `<path_or_reference>` |

### Screenshot

```markdown
![<description>](<screenshot_path>)
```

### Additional Notes

```text
<Additional sanitized evidence or explanation.>
```

---

## 13. Remediation Recommendation

### 13.1 Recommended Fix

```text
<Describe the specific remediation. Include the control that should be added or corrected.>
```

### 13.2 Secure Implementation Guidance

* [ ] Enforce server-side authorization checks
* [ ] Validate object ownership before access or modification
* [ ] Use allowlisted inputs and strict validation
* [ ] Apply output encoding or sanitization where applicable
* [ ] Use parameterized queries where applicable
* [ ] Restrict sensitive actions to authorized roles
* [ ] Add rate limiting or abuse controls where applicable
* [ ] Remove sensitive data from responses
* [ ] Add regression tests for the vulnerable condition
* [ ] Add logging and alerting for suspicious attempts

### 13.3 Verification Guidance

```text
<Describe how the program can verify that the issue is fixed safely.>
```

---

## 14. Safe Testing Notes

| Item                          | Notes                                        |
| ----------------------------- | -------------------------------------------- |
| Test Accounts Used            | `<test_accounts>`                            |
| Test Data Used                | `<test_data>`                                |
| Production Data Accessed      | `<No / Redacted / Minimal / Not Applicable>` |
| Destructive Actions Performed | `<No>`                                       |
| Cleanup Required              | `<Yes / No>`                                 |
| Cleanup Completed             | `<Yes / No / Not Applicable>`                |

```text
<Describe safeguards used to avoid data exposure, service disruption, or out-of-scope testing.>
```

---

## 15. Disclosure Notes

| Field                       | Value                                                                        |
| --------------------------- | ---------------------------------------------------------------------------- |
| Disclosure Type             | `<private_bug_bounty_submission / coordinated_disclosure / internal_report>` |
| Disclosure Restrictions     | `<program_policy_or_notes>`                                                  |
| Public Disclosure Requested | `<Yes / No>`                                                                 |
| Duplicate Risk              | `<known_related_reports_if_any>`                                             |
| Researcher Contact          | `<contact_or_handle>`                                                        |

```text
<Add any program-specific disclosure notes, coordination details, or handling requests.>
```

---

## 16. References

| Reference                                | Description     |
| ---------------------------------------- | --------------- |
| `<CWE_reference>`                        | `<description>` |
| `<OWASP_reference>`                      | `<description>` |
| `<Vendor_or_framework_documentation>`    | `<description>` |
| `<CVSS_calculator_or_scoring_reference>` | `<description>` |
| `<Related_program_policy>`               | `<description>` |

---

## 17. Analyst Notes / Open Questions

| ID           | Question / Note      | Status                         |
| ------------ | -------------------- | ------------------------------ |
| `<NOTE-001>` | `<question_or_note>` | `<Open / Answered / Deferred>` |
| `<NOTE-002>` | `<question_or_note>` | `<Open / Answered / Deferred>` |

```text
<Freeform notes, assumptions, caveats, and follow-up items.>
```
