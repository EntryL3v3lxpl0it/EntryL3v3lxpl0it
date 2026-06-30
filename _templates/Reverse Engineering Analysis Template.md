# Reverse Engineering Analysis Template

> **Use Case:** Authorized reverse engineering, vulnerability research, malware triage, firmware analysis, driver review, protocol analysis, software assurance, lab challenge analysis, and defensive validation only.
> **Scope Boundary:** Do not use this template to support unauthorized access, malware deployment, persistence, stealth, credential theft, or exploitation of real-world systems without explicit written authorization.

---

## 1. Case Metadata

| Field                           | Value                                                     |
| ------------------------------- | --------------------------------------------------------- |
| Analysis Title                  | `<analysis_title>`                                        |
| Analyst                         | `<analyst_name>`                                          |
| Reviewer                        | `<reviewer_name>`                                         |
| Date Started                    | `<YYYY-MM-DD>`                                            |
| Date Completed                  | `<YYYY-MM-DD>`                                            |
| Engagement / Lab Name           | `<engagement_or_lab_name>`                                |
| Case / Ticket ID                | `<case_id>`                                               |
| Authorization / Scope           | `<authorization_scope_summary>`                           |
| Target Artifact Name            | `<sample_name>`                                           |
| Original File Name              | `<original_file_name>`                                    |
| Working File Name               | `<working_file_name>`                                     |
| File Path                       | `<artifact_path>`                                         |
| Evidence Root                   | `<evidence_root_path>`                                    |
| File Type                       | `<file_type>`                                             |
| Architecture                    | `<x86/x64/ARM/MIPS/PowerPC/etc>`                          |
| Platform                        | `<Windows/Linux/macOS/Android/iOS/Embedded/Firmware/etc>` |
| Compiler / Toolchain Indicators | `<compiler_or_toolchain_indicators>`                      |
| Source of Artifact              | `<how_artifact_was_acquired>`                             |
| Acquisition Date                | `<YYYY-MM-DD>`                                            |
| Handling Notes                  | `<handling_notes>`                                        |
| Chain of Custody Required       | `<Yes/No>`                                                |
| Chain of Custody Location       | `<chain_of_custody_log_path>`                             |
| Classification / Sensitivity    | `<classification_or_sensitivity>`                         |
| Distribution Restrictions       | `<distribution_limitations>`                              |

### 1.1 Scope Statement

```text
<Describe the authorized scope, lab boundary, systems involved, and explicit limitations.>
```

### 1.2 Chain of Custody

| Time          | Handler  | Action                                 | Location                     | Hash Before       | Hash After       | Notes     |
| ------------- | -------- | -------------------------------------- | ---------------------------- | ----------------- | ---------------- | --------- |
| `<timestamp>` | `<name>` | `<received/copied/hashed/transferred>` | `<path_or_storage_location>` | `<sha256_before>` | `<sha256_after>` | `<notes>` |

---

## 2. Executive Summary

### 2.1 Non-Technical Summary

```text
<One-paragraph summary explaining what the artifact is, what was analyzed, what was found, why it matters, and what action is recommended. Avoid unnecessary jargon.>
```

### 2.2 Key Findings

| ID           | Finding             | Severity                                   | Confidence          | Impact                          |
| ------------ | ------------------- | ------------------------------------------ | ------------------- | ------------------------------- |
| `<FIND-001>` | `<finding_summary>` | `<Critical/High/Medium/Low/Informational>` | `<Low/Medium/High>` | `<business_or_security_impact>` |

### 2.3 Overall Risk Rating

| Field                          | Value                                                                   |
| ------------------------------ | ----------------------------------------------------------------------- |
| Overall Risk                   | `<Critical/High/Medium/Low/Informational>`                              |
| Primary Impact                 | `<confidentiality/integrity/availability/safety/financial/operational>` |
| Recommended Action             | `<recommended_action>`                                                  |
| Confidence Level               | `<Low/Medium/High>`                                                     |
| Immediate Containment Required | `<Yes/No/Not Applicable>`                                               |
| Further Analysis Required      | `<Yes/No>`                                                              |

### 2.4 Executive-Level Recommendation

```text
<Concise recommendation for leadership, product owners, system owners, or security stakeholders.>
```

---

## 3. Artifact Identification

### 3.1 Hashes

| Algorithm     | Value          |
| ------------- | -------------- |
| MD5           | `<md5>`        |
| SHA1          | `<sha1>`       |
| SHA256        | `<sha256>`     |
| SHA512        | `<sha512>`     |
| ssdeep / TLSH | `<fuzzy_hash>` |

### 3.2 File Properties

| Property                      | Value                                                    |
| ----------------------------- | -------------------------------------------------------- |
| File Size                     | `<file_size_bytes>`                                      |
| Magic Bytes                   | `<magic_bytes>`                                          |
| File Format                   | `<PE/ELF/Mach-O/APK/JAR/DEX/Firmware/Container/Raw/etc>` |
| MIME Type                     | `<mime_type>`                                            |
| Architecture                  | `<architecture>`                                         |
| Endianness                    | `<little/big/unknown>`                                   |
| Word Size                     | `<32-bit/64-bit/unknown>`                                |
| Entry Point                   | `<entry_point_address>`                                  |
| Base Address                  | `<base_address>`                                         |
| Image Base                    | `<image_base>`                                           |
| Number of Sections / Segments | `<section_count>`                                        |
| Entropy Summary               | `<entropy_summary>`                                      |
| Packed / Obfuscated           | `<Yes/No/Suspected>`                                     |
| Signed                        | `<Yes/No/Invalid/Unknown>`                               |
| Debug Symbols                 | `<Present/Absent/Stripped/Partial>`                      |
| Build Timestamp               | `<timestamp_or_unknown>`                                 |
| Version Metadata              | `<version_metadata>`                                     |

### 3.3 Identification Commands

```bash
<file_identification_commands>
```

### 3.4 Identification Output

```text
<file_identification_output>
```

### 3.5 Format-Specific Details

#### PE Details

| Field               | Value                              |
| ------------------- | ---------------------------------- |
| Subsystem           | `<windows_subsystem>`              |
| DLL Characteristics | `<dll_characteristics>`            |
| ASLR Enabled        | `<Yes/No/Unknown>`                 |
| DEP/NX Enabled      | `<Yes/No/Unknown>`                 |
| CFG Enabled         | `<Yes/No/Unknown>`                 |
| SafeSEH             | `<Yes/No/Unknown/Not Applicable>`  |
| Stack Cookie        | `<Detected/Not Detected/Unknown>`  |
| Authenticode Status | `<valid/invalid/unsigned/unknown>` |
| Certificate Subject | `<certificate_subject>`            |
| Certificate Issuer  | `<certificate_issuer>`             |

#### ELF Details

| Field           | Value                             |
| --------------- | --------------------------------- |
| ELF Type        | `<EXEC/DYN/REL/CORE>`             |
| Interpreter     | `<ld_path>`                       |
| RELRO           | `<Full/Partial/None/Unknown>`     |
| PIE             | `<Enabled/Disabled/Unknown>`      |
| NX              | `<Enabled/Disabled/Unknown>`      |
| Stack Canary    | `<Detected/Not Detected/Unknown>` |
| RPATH / RUNPATH | `<rpath_or_runpath>`              |
| Symbols         | `<present/stripped/partial>`      |

#### Mach-O Details

| Field          | Value                              |
| -------------- | ---------------------------------- |
| CPU Type       | `<cpu_type>`                       |
| File Type      | `<mach_o_file_type>`               |
| Load Commands  | `<load_command_summary>`           |
| Code Signature | `<present/absent/invalid/unknown>` |
| Entitlements   | `<entitlements_summary>`           |

#### Firmware / Container Details

| Field                     | Value                               |
| ------------------------- | ----------------------------------- |
| Container Type            | `<squashfs/cpio/tar/ubifs/ext/etc>` |
| Extracted Filesystem Path | `<extracted_fs_path>`               |
| Bootloader Indicators     | `<bootloader_indicators>`           |
| Kernel Version            | `<kernel_version>`                  |
| Root Filesystem Type      | `<filesystem_type>`                 |
| Embedded Services         | `<embedded_services>`               |
| Default Configs Found     | `<yes/no/unknown>`                  |

### 3.6 Packing / Obfuscation Indicators

| Indicator     | Evidence                | Interpretation     | Confidence          |
| ------------- | ----------------------- | ------------------ | ------------------- |
| `<indicator>` | `<evidence_id_or_path>` | `<interpretation>` | `<Low/Medium/High>` |

---

## 4. Analysis Environment

### 4.1 Host and Sandbox

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| Host OS                | `<host_os_version>`                            |
| Analysis VM            | `<vm_name>`                                    |
| VM OS                  | `<guest_os_version>`                           |
| Snapshot Name          | `<snapshot_name>`                              |
| Snapshot Date          | `<snapshot_date>`                              |
| Network Mode           | `<isolated/host-only/NAT/disabled/simulated>`  |
| Internet Access        | `<disabled/controlled/allowed/not_applicable>` |
| DNS Sinkhole           | `<dns_sinkhole_details>`                       |
| Packet Capture Enabled | `<Yes/No>`                                     |
| Logging Enabled        | `<Yes/No>`                                     |
| Time Source            | `<system_time_or_fake_time>`                   |
| Safety Controls        | `<safety_controls>`                            |

### 4.2 Tools and Versions

| Tool          | Version     | Purpose                                    | Notes     |
| ------------- | ----------- | ------------------------------------------ | --------- |
| `<tool_name>` | `<version>` | `<static/dynamic/debugging/emulation/etc>` | `<notes>` |

### 4.3 Debugger Configuration

| Field                     | Value                                     |
| ------------------------- | ----------------------------------------- |
| Debugger                  | `<x64dbg/WinDbg/GDB/LLDB/IDA/Ghidra/etc>` |
| Symbol Path               | `<symbol_path>`                           |
| Source Path               | `<source_path_if_available>`              |
| Breakpoint Policy         | `<breakpoint_policy>`                     |
| Exception Handling Policy | `<exception_policy>`                      |
| Logging Path              | `<debugger_log_path>`                     |

### 4.4 Emulator / Harness Details

| Field               | Value                                   |
| ------------------- | --------------------------------------- |
| Emulator            | `<QEMU/Unicorn/Bochs/Docker/etc>`       |
| Harness Path        | `<harness_path>`                        |
| Input Corpus Path   | `<corpus_path>`                         |
| Output Path         | `<output_path>`                         |
| Coverage Collection | `<coverage_method>`                     |
| Sanitizers          | `<ASAN/UBSAN/MSAN/None/Not Applicable>` |

### 4.5 Safety Controls

* [ ] Artifact stored in controlled evidence directory
* [ ] Hashes recorded before analysis
* [ ] VM snapshot created before execution
* [ ] Network isolation configured
* [ ] Packet capture configured if runtime behavior is analyzed
* [ ] Host-to-guest shared clipboard reviewed
* [ ] Shared folders disabled or limited
* [ ] No production credentials present in environment
* [ ] No access to production networks
* [ ] Execution approved for sandbox/lab scope
* [ ] Cleanup and rollback plan documented

---

## 5. Initial Triage Checklist

### 5.1 Required Triage Steps

* [ ] Confirm artifact source and authorization
* [ ] Copy artifact to evidence directory
* [ ] Record original filename and path
* [ ] Compute MD5, SHA1, SHA256
* [ ] Identify file type and magic bytes
* [ ] Determine architecture and platform
* [ ] Extract basic metadata
* [ ] Check signature/certificate status
* [ ] Review headers and sections
* [ ] Review imports and exports
* [ ] Extract strings
* [ ] Identify embedded resources
* [ ] Check entropy
* [ ] Look for packer/obfuscation indicators
* [ ] Identify debug symbols or stripped status
* [ ] Compare against known-good or known-bad samples
* [ ] Decide whether sandbox-safe execution is appropriate
* [ ] Record triage findings in evidence index

### 5.2 Triage Commands

```bash
<triage_commands>
```

### 5.3 Triage Output

```text
<triage_output>
```

### 5.4 Initial Decision Point

| Question                                  | Answer             | Evidence        | Decision                                                |
| ----------------------------------------- | ------------------ | --------------- | ------------------------------------------------------- |
| Is the file recognized and parseable?     | `<Yes/No/Partial>` | `<evidence_id>` | `<continue_static_analysis/extract_container/escalate>` |
| Is packing or obfuscation suspected?      | `<Yes/No>`         | `<evidence_id>` | `<unpack/deobfuscate/proceed>`                          |
| Is execution safe in current sandbox?     | `<Yes/No>`         | `<evidence_id>` | `<execute/do_not_execute/build_harness>`                |
| Is source or debug information available? | `<Yes/No/Partial>` | `<evidence_id>` | `<load_symbols/proceed_without_symbols>`                |
| Is this similar to a known-good sample?   | `<Yes/No/Unknown>` | `<evidence_id>` | `<diff/continue/baseline>`                              |
| Is this similar to known-bad behavior?    | `<Yes/No/Unknown>` | `<evidence_id>` | `<malware_triage/containment/continue>`                 |

---

## 6. Static Analysis

### 6.1 Static Analysis Summary

```text
<Summarize static analysis findings. Separate confirmed facts from hypotheses.>
```

### 6.2 Facts, Evidence, Hypotheses, Conclusions

#### Facts

| ID           | Fact               | Evidence        | Confidence          |
| ------------ | ------------------ | --------------- | ------------------- |
| `<FACT-001>` | `<confirmed_fact>` | `<evidence_id>` | `<Low/Medium/High>` |

#### Evidence

| ID           | Evidence Description | Location                | Tool     |
| ------------ | -------------------- | ----------------------- | -------- |
| `<EVID-001>` | `<description>`      | `<file_path_or_offset>` | `<tool>` |

#### Hypotheses

| ID          | Hypothesis     | Supporting Evidence | Test Required   | Confidence          |
| ----------- | -------------- | ------------------- | --------------- | ------------------- |
| `<HYP-001>` | `<hypothesis>` | `<evidence_id>`     | `<test_method>` | `<Low/Medium/High>` |

#### Conclusions

| ID           | Conclusion     | Basis                  | Confidence          |
| ------------ | -------------- | ---------------------- | ------------------- |
| `<CONC-001>` | `<conclusion>` | `<facts_and_evidence>` | `<Low/Medium/High>` |

---

### 6.3 Headers and Sections

| Section / Segment |              Address / Offset |     Size | Permissions         |     Entropy | Notes     |
| ----------------- | ----------------------------: | -------: | ------------------- | ----------: | --------- |
| `<section_name>`  | `<virtual_address_or_offset>` | `<size>` | `<rwx_permissions>` | `<entropy>` | `<notes>` |

#### Header / Section Evidence

```text
<header_or_section_output>
```

#### Observations

```text
<observations_about_headers_sections_permissions_alignment_entropy_or_anomalies>
```

---

### 6.4 Imports and Exports

#### Imports

| Library     | Imported Symbol / API | Address / Thunk | Security Relevance | Notes     |
| ----------- | --------------------- | --------------: | ------------------ | --------- |
| `<library>` | `<imported_function>` |     `<address>` | `<why_it_matters>` | `<notes>` |

#### Exports

| Export Name     |     Ordinal |     Address | Purpose / Notes |
| --------------- | ----------: | ----------: | --------------- |
| `<export_name>` | `<ordinal>` | `<address>` | `<notes>`       |

#### Import / Export Evidence

```text
<import_export_output>
```

#### Dangerous or Security-Relevant API Usage

| API / Function | Category                                        | Caller(s)            | Risk                 | Evidence        | Confidence          |
| -------------- | ----------------------------------------------- | -------------------- | -------------------- | --------------- | ------------------- |
| `<api_name>`   | `<memory/file/network/process/crypto/auth/etc>` | `<caller_functions>` | `<risk_description>` | `<evidence_id>` | `<Low/Medium/High>` |

Common categories to review:

* [ ] Memory copy / string handling
* [ ] Dynamic memory allocation / free
* [ ] File creation / deletion / overwrite
* [ ] Process creation
* [ ] Command execution
* [ ] Dynamic library loading
* [ ] Network communication
* [ ] Registry access
* [ ] IPC / RPC / named pipes
* [ ] Cryptographic operations
* [ ] Authentication / authorization checks
* [ ] Deserialization / parsing
* [ ] Compression / decompression
* [ ] Update / patch mechanisms
* [ ] Driver / kernel interfaces

---

### 6.5 Strings

#### String Extraction Commands

```bash
<string_extraction_commands>
```

#### Notable Strings

| String           |      Offset / Address | Category                                         | Interpretation     | Evidence        | Confidence          |
| ---------------- | --------------------: | ------------------------------------------------ | ------------------ | --------------- | ------------------- |
| `<string_value>` | `<offset_or_address>` | `<path/url/api/error/crypto/command/config/etc>` | `<interpretation>` | `<evidence_id>` | `<Low/Medium/High>` |

#### Error Messages

| Error String      |      Address / Offset | Referencing Function | Interpretation     |
| ----------------- | --------------------: | -------------------- | ------------------ |
| `<error_message>` | `<address_or_offset>` | `<function_name>`    | `<interpretation>` |

#### Command Strings

| Command String     |      Address / Offset | Referencing Function | Security Relevance     |
| ------------------ | --------------------: | -------------------- | ---------------------- |
| `<command_string>` | `<address_or_offset>` | `<function_name>`    | `<security_relevance>` |

#### File Paths

| Path          |      Address / Offset | Referencing Function | Notes     |
| ------------- | --------------------: | -------------------- | --------- |
| `<file_path>` | `<address_or_offset>` | `<function_name>`    | `<notes>` |

#### Registry Keys

| Registry Key     |      Address / Offset | Referencing Function | Notes     |
| ---------------- | --------------------: | -------------------- | --------- |
| `<registry_key>` | `<address_or_offset>` | `<function_name>`    | `<notes>` |

#### Network Indicators

| Indicator               | Type                             |      Address / Offset | Referencing Function | Notes     |
| ----------------------- | -------------------------------- | --------------------: | -------------------- | --------- |
| `<domain_or_ip_or_url>` | `<domain/ip/url/uri/user-agent>` | `<address_or_offset>` | `<function_name>`    | `<notes>` |

---

### 6.6 Embedded Resources

| Resource ID / Name | Type              |     Size |     Offset | Extracted Path     | Notes     |
| ------------------ | ----------------- | -------: | ---------: | ------------------ | --------- |
| `<resource_id>`    | `<resource_type>` | `<size>` | `<offset>` | `<extracted_path>` | `<notes>` |

#### Resource Extraction Output

```text
<resource_extraction_output>
```

---

### 6.7 Cryptographic Constants and Algorithms

| Indicator               | Location                | Possible Algorithm | Evidence        | Confidence          | Notes     |
| ----------------------- | ----------------------- | ------------------ | --------------- | ------------------- | --------- |
| `<constant_or_pattern>` | `<address_or_function>` | `<algorithm>`      | `<evidence_id>` | `<Low/Medium/High>` | `<notes>` |

Review checklist:

* [ ] Hardcoded keys
* [ ] Static IVs / nonces
* [ ] Weak algorithms
* [ ] Custom cryptography
* [ ] Reused secrets
* [ ] Predictable randomness
* [ ] Certificate validation logic
* [ ] Signature verification logic
* [ ] Update verification logic

---

### 6.8 Anti-Debugging and Anti-Analysis Indicators

| Indicator     | Location                | Technique     | Impact on Analysis | Evidence        | Confidence          |
| ------------- | ----------------------- | ------------- | ------------------ | --------------- | ------------------- |
| `<indicator>` | `<function_or_address>` | `<technique>` | `<impact>`         | `<evidence_id>` | `<Low/Medium/High>` |

Checklist:

* [ ] Debugger detection
* [ ] Timing checks
* [ ] VM / sandbox checks
* [ ] Process enumeration
* [ ] Parent process checks
* [ ] Exception-based control flow
* [ ] Self-modifying code
* [ ] Encrypted strings
* [ ] Dynamic import resolution
* [ ] Packed code
* [ ] Integrity checks
* [ ] Environment-specific execution gates

---

### 6.9 Memory Management Patterns

| Function          | Allocation Pattern      | Free Pattern      | Risk                 | Evidence        | Confidence          |
| ----------------- | ----------------------- | ----------------- | -------------------- | --------------- | ------------------- |
| `<function_name>` | `<allocation_behavior>` | `<free_behavior>` | `<risk_description>` | `<evidence_id>` | `<Low/Medium/High>` |

Checklist:

* [ ] Fixed-size buffers
* [ ] Stack buffers
* [ ] Heap allocations
* [ ] Length-controlled copies
* [ ] Unbounded copies
* [ ] Integer-derived allocation sizes
* [ ] Reference counting
* [ ] Ownership transfer
* [ ] Error-path cleanup
* [ ] Double-free potential
* [ ] Use-after-free potential
* [ ] Out-of-bounds access potential

---

### 6.10 Input Parsing Routines

| Parser / Function | Input Source                     | Format     | Validation             | Sensitive Sink | Risk     |
| ----------------- | -------------------------------- | ---------- | ---------------------- | -------------- | -------- |
| `<function_name>` | `<file/network/cli/ipc/env/etc>` | `<format>` | `<validation_summary>` | `<sink>`       | `<risk>` |

Checklist:

* [ ] Input length validation
* [ ] Type validation
* [ ] Bounds checks
* [ ] Integer range checks
* [ ] Encoding / decoding
* [ ] Compression / decompression
* [ ] Recursive structures
* [ ] Nested object handling
* [ ] Error handling
* [ ] Authentication before parsing
* [ ] Authorization before sensitive action

---

### 6.11 Authentication and Authorization Logic

| Function          | Role                                | Decision Logic    | Security Assumption | Evidence        | Confidence          |
| ----------------- | ----------------------------------- | ----------------- | ------------------- | --------------- | ------------------- |
| `<function_name>` | `<authn/authz/session/license/etc>` | `<logic_summary>` | `<assumption>`      | `<evidence_id>` | `<Low/Medium/High>` |

Questions:

* [ ] Where is identity established?
* [ ] Where is authorization checked?
* [ ] Is authentication required before sensitive parsing?
* [ ] Are roles or permissions enforced client-side, server-side, or locally?
* [ ] Are cryptographic checks enforced correctly?
* [ ] Are error paths fail-open or fail-closed?
* [ ] Can state be skipped or desynchronized?

---

### 6.12 Deserialization / Parsing Logic

| Function          | Format     | Trusted Input?     | Validation             | Object Creation             | Risk     |
| ----------------- | ---------- | ------------------ | ---------------------- | --------------------------- | -------- |
| `<function_name>` | `<format>` | `<Yes/No/Unknown>` | `<validation_summary>` | `<object_creation_summary>` | `<risk>` |

Checklist:

* [ ] Untrusted input reaches deserializer
* [ ] Type restrictions present
* [ ] Schema validation present
* [ ] Signature verification present
* [ ] Dangerous constructors or callbacks present
* [ ] File/network/command side effects possible
* [ ] Parser depth limits present
* [ ] Parser size limits present

---

### 6.13 Function Graph Observations

```text
<function_graph_summary>
```

| Function          |     Address | Role     | Callers         | Callees         | Security Relevance     |
| ----------------- | ----------: | -------- | --------------- | --------------- | ---------------------- |
| `<function_name>` | `<address>` | `<role>` | `<caller_list>` | `<callee_list>` | `<security_relevance>` |

---

### 6.14 Cross-References

| Source Function     | Target Function / Data      | XREF Type                      | Interpretation     | Evidence        |
| ------------------- | --------------------------- | ------------------------------ | ------------------ | --------------- |
| `<source_function>` | `<target_function_or_data>` | `<call/read/write/string/etc>` | `<interpretation>` | `<evidence_id>` |

---

### 6.15 Decompiled Pseudocode Notes

#### Function: `<function_name>`

Address:

```text
<function_address>
```

Decompiler Snippet:

```c
<decompiled_pseudocode_snippet>
```

Observations:

```text
<observations_about_logic_inputs_outputs_branches_and_security_relevance>
```

Evidence:

```text
<decompiler_evidence_reference>
```

---

### 6.16 Repeatable Function Analysis Block

Copy this block for each important function.

#### Function Analysis: `<function_name>`

| Field                         | Value                                                                       |
| ----------------------------- | --------------------------------------------------------------------------- |
| Function Name                 | `<function_name>`                                                           |
| Address / Offset              | `<function_address>`                                                        |
| Binary / Module               | `<module_name>`                                                             |
| Function Type                 | `<entrypoint/parser/crypto/auth/file/network/memory/helper/etc>`            |
| Caller(s)                     | `<caller_functions>`                                                        |
| Callee(s)                     | `<callee_functions>`                                                        |
| Inputs                        | `<input_sources_and_types>`                                                 |
| Outputs                       | `<return_values_outputs>`                                                   |
| Side Effects                  | `<files/network/registry/process/memory/state/etc>`                         |
| Important Branches            | `<branch_conditions>`                                                       |
| Security-Relevant Assumptions | `<assumptions>`                                                             |
| Related Strings               | `<string_refs>`                                                             |
| Related Imports / APIs        | `<api_refs>`                                                                |
| Evidence                      | `<evidence_id_or_path>`                                                     |
| Hypothesis                    | `<hypothesis>`                                                              |
| Confidence                    | `<Low/Medium/High>`                                                         |
| Next Steps                    | `<continue_static/switch_to_debugging/build_harness/patch_diff/fuzz/other>` |

Disassembly Snippet:

```asm
<disassembly_snippet>
```

Decompiler Snippet:

```c
<decompiled_pseudocode_snippet>
```

Analyst Notes:

```text
<notes>
```

---

### 6.17 Static Analysis Decision Points

| Decision Point             | Criteria     | Selected Path | Rationale     | Evidence        |
| -------------------------- | ------------ | ------------- | ------------- | --------------- |
| Continue static analysis   | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Switch to debugging        | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Build a harness            | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Perform patch diffing      | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Extract firmware/container | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Deobfuscate/unpack         | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Request source/symbols     | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |

---

## 7. Dynamic Analysis

### 7.1 Dynamic Analysis Summary

```text
<Summarize runtime behavior, observed side effects, crashes, network activity, file activity, and limitations.>
```

### 7.2 Execution Setup

| Field                 | Value                                      |
| --------------------- | ------------------------------------------ |
| Execution Approved    | `<Yes/No>`                                 |
| Execution Environment | `<vm/sandbox/emulator/harness>`            |
| Snapshot              | `<snapshot_name>`                          |
| Network Mode          | `<isolated/simulated/disabled/controlled>` |
| Arguments             | `<runtime_arguments>`                      |
| Environment Variables | `<environment_variables>`                  |
| Working Directory     | `<working_directory>`                      |
| Required Files        | `<required_files>`                         |
| Input Samples         | `<input_sample_paths>`                     |
| Monitoring Tools      | `<monitoring_tools>`                       |
| Packet Capture Path   | `<pcap_path>`                              |
| Runtime Log Path      | `<runtime_log_path>`                       |

### 7.3 Runtime Commands

```bash
<dynamic_analysis_commands>
```

### 7.4 Runtime Output

```text
<dynamic_analysis_output>
```

---

### 7.5 Runtime Arguments and Inputs

| Input ID   | Type                             | Value / Path      | Source     | Purpose     | Notes     |
| ---------- | -------------------------------- | ----------------- | ---------- | ----------- | --------- |
| `<IN-001>` | `<cli/file/network/ipc/env/etc>` | `<value_or_path>` | `<source>` | `<purpose>` | `<notes>` |

---

### 7.6 Breakpoints and Watchpoints

| ID         | Type                             |      Address / Symbol | Condition     | Purpose     |     Hit Count | Notes     |
| ---------- | -------------------------------- | --------------------: | ------------- | ----------- | ------------: | --------- |
| `<BP-001>` | `<software/hardware/watchpoint>` | `<address_or_symbol>` | `<condition>` | `<purpose>` | `<hit_count>` | `<notes>` |

Debugger Commands:

```text
<debugger_breakpoint_commands>
```

Debugger Output:

```text
<debugger_breakpoint_output>
```

---

### 7.7 Memory Observations

| Address / Region      |     Size | Permissions | Contents / Pattern   | Interpretation     | Evidence        |
| --------------------- | -------: | ----------- | -------------------- | ------------------ | --------------- |
| `<address_or_region>` | `<size>` | `<rwx>`     | `<contents_summary>` | `<interpretation>` | `<evidence_id>` |

Memory Dump Reference:

```text
<memory_dump_path_or_output>
```

---

### 7.8 Register Observations

| Time / Breakpoint   | Register     |     Value | Interpretation     |
| ------------------- | ------------ | --------: | ------------------ |
| `<timestamp_or_bp>` | `<register>` | `<value>` | `<interpretation>` |

Register Snapshot:

```text
<register_snapshot>
```

---

### 7.9 API Tracing

| Time          | API          | Arguments             | Return Value     | Caller     | Interpretation     |
| ------------- | ------------ | --------------------- | ---------------- | ---------- | ------------------ |
| `<timestamp>` | `<api_name>` | `<arguments_summary>` | `<return_value>` | `<caller>` | `<interpretation>` |

API Trace Output:

```text
<api_trace_output>
```

---

### 7.10 Syscall Tracing

| Time          | Syscall          | Arguments             | Return Value     | Interpretation     |
| ------------- | ---------------- | --------------------- | ---------------- | ------------------ |
| `<timestamp>` | `<syscall_name>` | `<arguments_summary>` | `<return_value>` | `<interpretation>` |

Syscall Trace Output:

```text
<syscall_trace_output>
```

---

### 7.11 File Activity

| Time          | Operation                           | Path          | Result     | Process     | Interpretation     |
| ------------- | ----------------------------------- | ------------- | ---------- | ----------- | ------------------ |
| `<timestamp>` | `<create/read/write/delete/rename>` | `<file_path>` | `<result>` | `<process>` | `<interpretation>` |

---

### 7.12 Registry Activity

| Time          | Operation                   | Key / Value               | Data     | Result     | Interpretation     |
| ------------- | --------------------------- | ------------------------- | -------- | ---------- | ------------------ |
| `<timestamp>` | `<query/set/delete/create>` | `<registry_key_or_value>` | `<data>` | `<result>` | `<interpretation>` |

---

### 7.13 Network Activity

| Time          | Protocol                     | Source          | Destination     | Data Summary | Evidence        | Interpretation     |
| ------------- | ---------------------------- | --------------- | --------------- | ------------ | --------------- | ------------------ |
| `<timestamp>` | `<tcp/udp/http/dns/tls/etc>` | `<src_ip_port>` | `<dst_ip_port>` | `<summary>`  | `<pcap_or_log>` | `<interpretation>` |

Packet Capture Evidence:

```text
<pcap_summary_or_extracted_log>
```

---

### 7.14 Process and Thread Activity

| Time          | Process / Thread           |   PID / TID | Action                          | Parent     | Command Line     | Notes     |
| ------------- | -------------------------- | ----------: | ------------------------------- | ---------- | ---------------- | --------- |
| `<timestamp>` | `<process_or_thread_name>` | `<pid_tid>` | `<create/exit/inject/load/etc>` | `<parent>` | `<command_line>` | `<notes>` |

---

### 7.15 Loaded Modules

| Module          |     Base Address |     Size | Path     | Signed             | Notes     |
| --------------- | ---------------: | -------: | -------- | ------------------ | --------- |
| `<module_name>` | `<base_address>` | `<size>` | `<path>` | `<Yes/No/Unknown>` | `<notes>` |

---

### 7.16 Exceptions and Crashes

| Time          | Exception Code     |     Faulting Address | Module     | First Chance / Second Chance | Notes     |
| ------------- | ------------------ | -------------------: | ---------- | ---------------------------- | --------- |
| `<timestamp>` | `<exception_code>` | `<faulting_address>` | `<module>` | `<first_or_second_chance>`   | `<notes>` |

Crash Output:

```text
<crash_output>
```

---

### 7.17 Coverage Notes

| Run ID      | Input          | Coverage Method   | Coverage Summary     | New Paths     | Notes     |
| ----------- | -------------- | ----------------- | -------------------- | ------------- | --------- |
| `<RUN-001>` | `<input_path>` | `<coverage_tool>` | `<coverage_summary>` | `<new_paths>` | `<notes>` |

---

### 7.18 Behavioral Timeline

| Time          | Action/Event        | Tool     | Evidence        | Interpretation     | Confidence          |
| ------------- | ------------------- | -------- | --------------- | ------------------ | ------------------- |
| `<timestamp>` | `<action_or_event>` | `<tool>` | `<evidence_id>` | `<interpretation>` | `<Low/Medium/High>` |

---

### 7.19 Dynamic Analysis Decision Points

| Decision Point            | Criteria     | Selected Path | Rationale     | Evidence        |
| ------------------------- | ------------ | ------------- | ------------- | --------------- |
| Continue dynamic analysis | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Add targeted breakpoints  | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Build or improve harness  | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Collect memory dump       | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Collect network capture   | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Stop execution            | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |
| Roll back snapshot        | `<criteria>` | `<Yes/No>`    | `<rationale>` | `<evidence_id>` |

---

## 8. Debugging Notes

### 8.1 Debugging Session Metadata

| Field             | Value                         |
| ----------------- | ----------------------------- |
| Debugger Used     | `<debugger_name_version>`     |
| Target Binary     | `<binary_path>`               |
| Arguments         | `<arguments>`                 |
| Working Directory | `<working_directory>`         |
| Symbols Loaded    | `<Yes/No/Partial>`            |
| Symbol Path       | `<symbol_path>`               |
| Session Log       | `<debugger_session_log_path>` |
| Memory Dumps      | `<memory_dump_paths>`         |
| Crash Dumps       | `<crash_dump_paths>`          |

### 8.2 Debugger Setup Commands

```text
<debugger_setup_commands>
```

### 8.3 Symbols Loaded

```text
<symbol_loading_output>
```

### 8.4 Breakpoints

| ID         |      Address / Symbol | Type                  | Condition     | Purpose     | Status               |
| ---------- | --------------------: | --------------------- | ------------- | ----------- | -------------------- |
| `<BP-001>` | `<address_or_symbol>` | `<software/hardware>` | `<condition>` | `<purpose>` | `<enabled/disabled>` |

### 8.5 Hardware Breakpoints / Watchpoints

| ID           |     Address | Access Type            |     Size | Purpose     |     Hit Count |
| ------------ | ----------: | ---------------------- | -------: | ----------- | ------------: |
| `<HWBP-001>` | `<address>` | `<read/write/execute>` | `<size>` | `<purpose>` | `<hit_count>` |

### 8.6 Register Snapshots

```text
<register_snapshot_output>
```

### 8.7 Stack Traces

```text
<stack_trace_output>
```

### 8.8 Stack Observations

|           Address |     Value | Symbol / Interpretation      | Notes     |
| ----------------: | --------: | ---------------------------- | --------- |
| `<stack_address>` | `<value>` | `<symbol_or_interpretation>` | `<notes>` |

### 8.9 Heap Observations

|     Heap Address | Allocation Size | State                                 | Referencing Function | Notes     |
| ---------------: | --------------: | ------------------------------------- | -------------------- | --------- |
| `<heap_address>` |        `<size>` | `<allocated/freed/corrupted/unknown>` | `<function_name>`    | `<notes>` |

### 8.10 Memory Dumps

| Dump ID      | Address Range   | File Path     | Purpose     | Notes     |
| ------------ | --------------- | ------------- | ----------- | --------- |
| `<DUMP-001>` | `<start>-<end>` | `<dump_path>` | `<purpose>` | `<notes>` |

### 8.11 Crash State

| Field                        | Value                              |
| ---------------------------- | ---------------------------------- |
| Crash ID                     | `<CRASH-001>`                      |
| Exception Code               | `<exception_code>`                 |
| Exception Description        | `<exception_description>`          |
| Faulting Module              | `<module_name>`                    |
| Faulting Instruction Address | `<faulting_instruction_address>`   |
| Faulting Instruction         | `<faulting_instruction>`           |
| Access Type                  | `<read/write/execute/unknown>`     |
| Access Address               | `<access_address>`                 |
| Controllable Data Observed   | `<Yes/No/Unknown>`                 |
| Reproducible                 | `<Yes/No/Intermittent>`            |
| Exploitability Notes         | `<safe_exploitability_assessment>` |

Faulting Instruction Context:

```asm
<faulting_instruction_context>
```

Crash Register State:

```text
<crash_register_state>
```

Crash Stack State:

```text
<crash_stack_state>
```

### 8.12 Exploitability Notes

```text
<Assess whether the crash or behavior indicates memory corruption, control-flow influence, data-only impact, denial of service, or non-security failure. Avoid weaponized payload steps.>
```

### 8.13 Reproduction Steps

```text
<Safe, lab-only reproduction steps that trigger the observed condition without weaponized payloads.>
```

---

## 9. Data Flow and Control Flow Analysis

### 9.1 Entry Points

| Entry Point          |     Address | Trigger                                                        | Notes     |
| -------------------- | ----------: | -------------------------------------------------------------- | --------- |
| `<entry_point_name>` | `<address>` | `<process_start/export/handler/callback/protocol_message/etc>` | `<notes>` |

### 9.2 Trust Boundaries

| Boundary          | Untrusted Side   | Trusted Side           | Validation Point        | Notes     |
| ----------------- | ---------------- | ---------------------- | ----------------------- | --------- |
| `<boundary_name>` | `<input_source>` | `<internal_component>` | `<validation_function>` | `<notes>` |

### 9.3 User-Controlled Inputs

| Input          | Source                               | Format     | Parser              | Validation             | Sensitive Sink    |
| -------------- | ------------------------------------ | ---------- | ------------------- | ---------------------- | ----------------- |
| `<input_name>` | `<cli/file/network/ipc/env/gui/etc>` | `<format>` | `<parser_function>` | `<validation_summary>` | `<sink_function>` |

### 9.4 Parsing Paths

| Path ID      | Input     | Function Chain     | Validation             | Output / State Change | Risk     |
| ------------ | --------- | ------------------ | ---------------------- | --------------------- | -------- |
| `<PATH-001>` | `<input>` | `<function_chain>` | `<validation_summary>` | `<state_change>`      | `<risk>` |

### 9.5 Validation Routines

| Function          | Validation Type                          | Checks Performed | Missing Checks     | Evidence        |
| ----------------- | ---------------------------------------- | ---------------- | ------------------ | --------------- |
| `<function_name>` | `<length/type/range/auth/signature/etc>` | `<checks>`       | `<missing_checks>` | `<evidence_id>` |

### 9.6 Transformation / Decoding Steps

| Step            | Function          | Input     | Output     | Security Relevance     |
| --------------- | ----------------- | --------- | ---------- | ---------------------- |
| `<step_number>` | `<function_name>` | `<input>` | `<output>` | `<security_relevance>` |

### 9.7 Sensitive Sinks

| Sink Function / API | Sink Type                                                       | Input Source     | Validation Before Sink | Risk     |
| ------------------- | --------------------------------------------------------------- | ---------------- | ---------------------- | -------- |
| `<sink_function>`   | `<memory/file/command/network/auth/crypto/deserialization/etc>` | `<input_source>` | `<validation_summary>` | `<risk>` |

### 9.8 Dangerous Call Sites

| Call Site           |     Address | Source Data     | Guard Conditions     | Risk     | Evidence        |
| ------------------- | ----------: | --------------- | -------------------- | -------- | --------------- |
| `<function_or_api>` | `<address>` | `<source_data>` | `<guard_conditions>` | `<risk>` | `<evidence_id>` |

### 9.9 State Transitions

| State          | Trigger     | Function          | Next State     | Security Relevance     |
| -------------- | ----------- | ----------------- | -------------- | ---------------------- |
| `<state_name>` | `<trigger>` | `<function_name>` | `<next_state>` | `<security_relevance>` |

### 9.10 Protocol / State-Machine Notes

```text
<Describe message types, state transitions, parsing order, authentication requirements, length fields, checksums, compression, encryption, and error handling.>
```

### 9.11 Control / Data Flow Diagram

```text
<ASCII_CONTROL_DATA_FLOW_DIAGRAM>

Example structure:

[Untrusted Input]
       |
       v
[Parser: <function_name>]
       |
       v
[Validation: <function_name>]
       |
       +---- invalid ----> [Error Path]
       |
       v
[Transform/Decode: <function_name>]
       |
       v
[Security-Sensitive Sink: <function_or_api>]
       |
       v
[Side Effect: <file/network/memory/process/state>]
```

---

## 10. Vulnerability Hypothesis Tracking

### 10.1 Hypothesis Table

| ID          | Hypothesis                   | Evidence        | Test Method          | Result     | Confidence          | Status                                       |
| ----------- | ---------------------------- | --------------- | -------------------- | ---------- | ------------------- | -------------------------------------------- |
| `<HYP-001>` | `<vulnerability_hypothesis>` | `<evidence_id>` | `<safe_test_method>` | `<result>` | `<Low/Medium/High>` | `<Open/Testing/Confirmed/Rejected/Deferred>` |

### 10.2 Vulnerability Categories Reviewed

| Category                               | Reviewed   | Evidence        | Result                              | Notes     |
| -------------------------------------- | ---------- | --------------- | ----------------------------------- | --------- |
| Buffer overflow                        | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Integer overflow / underflow           | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Format string                          | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Use-after-free                         | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Double free                            | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Out-of-bounds read                     | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Out-of-bounds write                    | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Command injection                      | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Path traversal                         | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Insecure deserialization               | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Authentication bypass                  | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Authorization bypass                   | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Logic flaw                             | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Race condition                         | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Cryptographic weakness                 | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Unsafe update mechanism                | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Insecure IPC / RPC / protocol handling | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Hardcoded secret                       | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Insecure permissions                   | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |
| Denial of service                      | `<Yes/No>` | `<evidence_id>` | `<confirmed/rejected/inconclusive>` | `<notes>` |

### 10.3 Finding Candidate Block

#### Candidate Finding: `<candidate_finding_title>`

| Field                 | Value                                |
| --------------------- | ------------------------------------ |
| Candidate ID          | `<FIND-CAND-001>`                    |
| Vulnerability Class   | `<vulnerability_class>`              |
| Affected Function(s)  | `<function_names>`                   |
| Affected Component    | `<component_name>`                   |
| User-Controlled Input | `<input_source>`                     |
| Sensitive Sink        | `<sink_function>`                    |
| Preconditions         | `<preconditions>`                    |
| Confirmed Impact      | `<confirmed_impact>`                 |
| Potential Impact      | `<potential_impact>`                 |
| Evidence              | `<evidence_ids>`                     |
| Confidence            | `<Low/Medium/High>`                  |
| Status                | `<Open/Confirmed/Rejected/Deferred>` |

Facts:

```text
<facts>
```

Evidence:

```text
<evidence_summary>
```

Hypothesis:

```text
<hypothesis>
```

Conclusion:

```text
<current_conclusion>
```

Next Test:

```text
<safe_next_test>
```

---

## 11. Crash Analysis

### 11.1 Crash Summary

| Field                        | Value                                                      |
| ---------------------------- | ---------------------------------------------------------- |
| Crash ID                     | `<CRASH-001>`                                              |
| Crash Trigger                | `<trigger_summary>`                                        |
| Input Used                   | `<input_path_or_description>`                              |
| Reproducibility              | `<Always/Sometimes/Once/Not Reproduced>`                   |
| Exception Code               | `<exception_code>`                                         |
| Exception Description        | `<exception_description>`                                  |
| Faulting Module              | `<faulting_module>`                                        |
| Faulting Instruction Address | `<faulting_instruction_address>`                           |
| Faulting Instruction         | `<faulting_instruction>`                                   |
| Access Type                  | `<read/write/execute/unknown>`                             |
| Access Address               | `<access_address>`                                         |
| Triage Classification        | `<DoS/memory_corruption/assertion/null_deref/OOB/UAF/etc>` |
| Exploitability Assessment    | `<safe_assessment_only>`                                   |
| Root Cause Hypothesis        | `<root_cause_hypothesis>`                                  |
| Minimization Status          | `<not_started/in_progress/minimized>`                      |
| Safe PoC Status              | `<not_started/in_progress/complete/not_applicable>`        |
| Confidence                   | `<Low/Medium/High>`                                        |

### 11.2 Crash Input

```text
<crash_input_description_or_path>
```

### 11.3 Exception Details

```text
<exception_details>
```

### 11.4 Faulting Instruction Context

```asm
<faulting_instruction_context>
```

### 11.5 Register State

```text
<register_state_at_crash>
```

### 11.6 Stack State

```text
<stack_state_at_crash>
```

### 11.7 Memory State

```text
<memory_state_at_crash>
```

### 11.8 Reproduction Procedure

```text
<safe_lab_only_reproduction_procedure>
```

### 11.9 Reproduction Output

```text
<reproduction_output>
```

### 11.10 Crash Triage Classification

| Question                                            | Answer                   | Evidence        | Notes     |
| --------------------------------------------------- | ------------------------ | --------------- | --------- |
| Is the crash reproducible?                          | `<Yes/No/Intermittent>`  | `<evidence_id>` | `<notes>` |
| Is the faulting address influenced by input?        | `<Yes/No/Unknown>`       | `<evidence_id>` | `<notes>` |
| Is instruction pointer/control flow influenced?     | `<Yes/No/Unknown>`       | `<evidence_id>` | `<notes>` |
| Is attacker-controlled data present near the fault? | `<Yes/No/Unknown>`       | `<evidence_id>` | `<notes>` |
| Is the crash before or after validation?            | `<before/after/unknown>` | `<evidence_id>` | `<notes>` |
| Is the crash security-relevant?                     | `<Yes/No/Unknown>`       | `<evidence_id>` | `<notes>` |
| Is the result limited to denial of service?         | `<Yes/No/Unknown>`       | `<evidence_id>` | `<notes>` |

### 11.11 Root Cause Hypothesis

```text
<root_cause_hypothesis_with_supporting_evidence>
```

### 11.12 Minimization Notes

```text
<minimization_status_input_reduction_notes_and_remaining_dependencies>
```

---

## 12. Safe Proof-of-Concept Validation

### 12.1 Scope Statement

```text
<This validation is limited to the authorized lab, sandbox, or approved engagement environment. It is designed to demonstrate the condition safely and non-destructively. It does not include weaponized payloads, persistence, stealth, credential theft, or unauthorized access.>
```

### 12.2 Validation Objective

```text
<Describe exactly what the PoC is intended to prove.>
```

### 12.3 Validation Preconditions

| Requirement            | Value                                  |
| ---------------------- | -------------------------------------- |
| Environment            | `<lab_vm_or_test_system>`              |
| Artifact Hash          | `<sha256>`                             |
| Required Input         | `<input_file_or_argument>`             |
| Required Configuration | `<configuration>`                      |
| Network Requirement    | `<none/isolated/simulated/controlled>` |
| Privileges Required    | `<user/admin/root/kernel/etc>`         |
| Safety Limitations     | `<limitations>`                        |

### 12.4 Non-Destructive Trigger

```text
<Describe the benign trigger condition. Do not include weaponized payloads or instructions for unauthorized exploitation.>
```

### 12.5 Lab-Only Validation Steps

```text
<step_1>
<step_2>
<step_3>
```

### 12.6 Expected Result

```text
<expected_result>
```

### 12.7 Actual Result

```text
<actual_result>
```

### 12.8 Logs and Screenshots

| Evidence ID      | Type                                    | Path              | Description     |
| ---------------- | --------------------------------------- | ----------------- | --------------- |
| `<EVID-POC-001>` | `<log/screenshot/pcap/debugger_output>` | `<evidence_path>` | `<description>` |

### 12.9 Reproduction Reliability

| Metric                   | Value                     |
| ------------------------ | ------------------------- |
| Attempts                 | `<number>`                |
| Successful Reproductions | `<number>`                |
| Failure Cases            | `<failure_cases>`         |
| Reliability              | `<percentage_or_summary>` |

### 12.10 Cleanup Steps

```text
<cleanup_steps>
```

### 12.11 What This Proves

```text
<Describe the validated behavior or vulnerability condition.>
```

### 12.12 What This Does Not Prove

```text
<Describe limitations, unproven impact, untested platforms, missing exploitability evidence, or assumptions.>
```

---

## 13. Indicators and Artifacts

### 13.1 File Indicators

| Indicator Type | Value         | Context     | Confidence          |
| -------------- | ------------- | ----------- | ------------------- |
| MD5            | `<md5>`       | `<context>` | `<Low/Medium/High>` |
| SHA1           | `<sha1>`      | `<context>` | `<Low/Medium/High>` |
| SHA256         | `<sha256>`    | `<context>` | `<Low/Medium/High>` |
| File Name      | `<file_name>` | `<context>` | `<Low/Medium/High>` |
| File Path      | `<file_path>` | `<context>` | `<Low/Medium/High>` |

### 13.2 Network Indicators

| Indicator     | Type                             | Port / Protocol   | Context     | Confidence          |
| ------------- | -------------------------------- | ----------------- | ----------- | ------------------- |
| `<indicator>` | `<domain/ip/url/uri/user-agent>` | `<port_protocol>` | `<context>` | `<Low/Medium/High>` |

### 13.3 Host Indicators

| Indicator     | Type                                 | Context     | Confidence          |
| ------------- | ------------------------------------ | ----------- | ------------------- |
| `<indicator>` | `<file/process/service/task/module>` | `<context>` | `<Low/Medium/High>` |

### 13.4 Registry Indicators

| Key / Value               | Operation                   | Data     | Context     | Confidence          |
| ------------------------- | --------------------------- | -------- | ----------- | ------------------- |
| `<registry_key_or_value>` | `<query/create/set/delete>` | `<data>` | `<context>` | `<Low/Medium/High>` |

### 13.5 Mutexes / Events / Pipes / IPC

| Indicator | Type                                | Context     | Confidence          |
| --------- | ----------------------------------- | ----------- | ------------------- |
| `<name>`  | `<mutex/event/pipe/socket/rpc/etc>` | `<context>` | `<Low/Medium/High>` |

### 13.6 Certificates

| Field            | Value                     |
| ---------------- | ------------------------- |
| Subject          | `<certificate_subject>`   |
| Issuer           | `<certificate_issuer>`    |
| Serial Number    | `<serial_number>`         |
| Thumbprint       | `<thumbprint>`            |
| Valid From       | `<valid_from>`            |
| Valid To         | `<valid_to>`              |
| Signature Status | `<valid/invalid/unknown>` |

### 13.7 YARA Placeholder

```yara
rule <rule_name>
{
    meta:
        author = "<analyst_name>"
        description = "<description>"
        date = "<YYYY-MM-DD>"
        hash = "<sha256>"
        scope = "authorized defensive detection or lab use"

    strings:
        $s1 = "<string_placeholder>" ascii wide
        $x1 = { <hex_pattern_placeholder> }

    condition:
        <condition_placeholder>
}
```

### 13.8 Sigma Placeholder

```yaml
title: <detection_title>
id: <uuid_placeholder>
status: experimental
description: <description>
author: <analyst_name>
date: <YYYY-MM-DD>
references:
  - <reference_placeholder>
logsource:
  product: <windows/linux/network/application>
  service: <service_name>
detection:
  selection:
    <field>: <value>
  condition: selection
fields:
  - <field_1>
  - <field_2>
falsepositives:
  - <false_positive_notes>
level: <low/medium/high/critical>
```

---

## 14. Risk, Impact, and Mapping

### 14.1 Impact Narrative

```text
<Explain the technical and business/security impact. Include affected users, systems, data, operational processes, and safety implications if applicable.>
```

### 14.2 Affected Assets

| Asset          | Version     | Environment           | Exposure                              | Owner     | Notes     |
| -------------- | ----------- | --------------------- | ------------------------------------- | --------- | --------- |
| `<asset_name>` | `<version>` | `<dev/test/prod/lab>` | `<local/network/remote/physical/etc>` | `<owner>` | `<notes>` |

### 14.3 Preconditions

| Precondition           | Required?  | Notes     |
| ---------------------- | ---------- | --------- |
| Local access           | `<Yes/No>` | `<notes>` |
| Network access         | `<Yes/No>` | `<notes>` |
| Authentication         | `<Yes/No>` | `<notes>` |
| User interaction       | `<Yes/No>` | `<notes>` |
| Specific configuration | `<Yes/No>` | `<notes>` |
| Specific file/input    | `<Yes/No>` | `<notes>` |
| Elevated privileges    | `<Yes/No>` | `<notes>` |

### 14.4 CVSS

| Field        | Value                        |
| ------------ | ---------------------------- |
| CVSS Version | `<3.1/4.0>`                  |
| Vector       | `<CVSS_vector_placeholder>`  |
| Base Score   | `<score>`                    |
| Severity     | `<Critical/High/Medium/Low>` |
| Rationale    | `<cvss_rationale>`           |

### 14.5 CIA Impact

| Impact Area     | Rating            | Rationale     |
| --------------- | ----------------- | ------------- |
| Confidentiality | `<None/Low/High>` | `<rationale>` |
| Integrity       | `<None/Low/High>` | `<rationale>` |
| Availability    | `<None/Low/High>` | `<rationale>` |

### 14.6 Vulnerability Mapping

| Standard     | ID                      | Name               | Rationale                           | Confidence          |
| ------------ | ----------------------- | ------------------ | ----------------------------------- | ------------------- |
| CWE          | `<CWE-ID>`              | `<CWE_name>`       | `<mapping_rationale>`               | `<Low/Medium/High>` |
| CAPEC        | `<CAPEC-ID>`            | `<CAPEC_name>`     | `<mapping_rationale>`               | `<Low/Medium/High>` |
| MITRE ATT&CK | `<Tactic/Technique ID>` | `<technique_name>` | `<mapping_rationale_if_applicable>` | `<Low/Medium/High>` |

### 14.7 Attack Complexity and Required Conditions

| Factor              | Value                               | Rationale     |
| ------------------- | ----------------------------------- | ------------- |
| Attack Complexity   | `<Low/High>`                        | `<rationale>` |
| Privileges Required | `<None/Low/High>`                   | `<rationale>` |
| User Interaction    | `<None/Required>`                   | `<rationale>` |
| Scope               | `<Unchanged/Changed>`               | `<rationale>` |
| Exposure            | `<local/adjacent/network/physical>` | `<rationale>` |

### 14.8 Business Impact

| Impact Category    | Description                    | Severity     |
| ------------------ | ------------------------------ | ------------ |
| Operational        | `<operational_impact>`         | `<severity>` |
| Financial          | `<financial_impact>`           | `<severity>` |
| Legal / Regulatory | `<legal_or_regulatory_impact>` | `<severity>` |
| Safety             | `<safety_impact>`              | `<severity>` |
| Reputation         | `<reputation_impact>`          | `<severity>` |
| Mission Impact     | `<mission_impact>`             | `<severity>` |

### 14.9 Detection Opportunities

| Detection Opportunity | Data Source                         | Detection Logic   | Notes     |
| --------------------- | ----------------------------------- | ----------------- | --------- |
| `<opportunity>`       | `<logs/edr/network/sysmon/app/etc>` | `<logic_summary>` | `<notes>` |

---

## 15. Remediation and Hardening

### 15.1 Root Cause

```text
<Describe the root cause at the code, design, configuration, or process level.>
```

### 15.2 Code-Level Remediation

```text
<Describe specific code-level fixes, safer APIs, validation improvements, memory ownership corrections, bounds checks, and error handling changes.>
```

### 15.3 Compiler and Binary Hardening

| Control                | Current State                 | Recommended State  | Notes     |
| ---------------------- | ----------------------------- | ------------------ | --------- |
| Stack canaries         | `<enabled/disabled/unknown>`  | `<recommendation>` | `<notes>` |
| ASLR / PIE             | `<enabled/disabled/unknown>`  | `<recommendation>` | `<notes>` |
| DEP / NX               | `<enabled/disabled/unknown>`  | `<recommendation>` | `<notes>` |
| RELRO                  | `<full/partial/none/unknown>` | `<recommendation>` | `<notes>` |
| CFG / CFI              | `<enabled/disabled/unknown>`  | `<recommendation>` | `<notes>` |
| SafeSEH / SEHOP        | `<enabled/disabled/unknown>`  | `<recommendation>` | `<notes>` |
| Fortify / checked APIs | `<enabled/disabled/unknown>`  | `<recommendation>` | `<notes>` |
| Sanitizers             | `<enabled/disabled/unknown>`  | `<recommendation>` | `<notes>` |
| Code signing           | `<valid/invalid/absent>`      | `<recommendation>` | `<notes>` |

### 15.4 Input Validation Guidance

* [ ] Validate length before copy, allocation, parsing, or transformation
* [ ] Validate integer ranges before arithmetic or allocation
* [ ] Validate format before deep parsing
* [ ] Validate authentication and authorization before sensitive actions
* [ ] Enforce parser depth and size limits
* [ ] Reject malformed or ambiguous input
* [ ] Use allowlists for expected values
* [ ] Fail closed on validation errors
* [ ] Log validation failures safely without exposing secrets

### 15.5 Memory Safety Guidance

* [ ] Replace unsafe string/memory routines where applicable
* [ ] Track allocation ownership clearly
* [ ] Initialize memory before use
* [ ] Clear sensitive data when no longer needed
* [ ] Avoid use-after-free by nulling or invalidating stale references
* [ ] Centralize cleanup paths
* [ ] Use bounds-checked abstractions where possible
* [ ] Add sanitizer-backed tests
* [ ] Add regression cases for edge lengths and malformed inputs

### 15.6 Dependency / Update Guidance

| Component      | Current Version     | Recommended Version     | Reason     |
| -------------- | ------------------- | ----------------------- | ---------- |
| `<dependency>` | `<current_version>` | `<recommended_version>` | `<reason>` |

### 15.7 Logging and Detection Guidance

```text
<Describe logs, telemetry, events, or alerts that would help detect exploitation attempts, crashes, malformed inputs, suspicious behavior, or abuse patterns.>
```

### 15.8 Regression Test Ideas

| Test ID      | Purpose     | Input                 | Expected Result     |
| ------------ | ----------- | --------------------- | ------------------- |
| `<TEST-001>` | `<purpose>` | `<input_description>` | `<expected_result>` |

### 15.9 Verification Steps

```text
<Describe how to verify the remediation safely in a lab or test environment.>
```

### 15.10 Remediation Decision Points

| Decision                      | Criteria     | Recommendation     | Owner     |
| ----------------------------- | ------------ | ------------------ | --------- |
| Patch code                    | `<criteria>` | `<recommendation>` | `<owner>` |
| Add hardening flags           | `<criteria>` | `<recommendation>` | `<owner>` |
| Disable vulnerable feature    | `<criteria>` | `<recommendation>` | `<owner>` |
| Add detection                 | `<criteria>` | `<recommendation>` | `<owner>` |
| Require compensating controls | `<criteria>` | `<recommendation>` | `<owner>` |
| Accept risk                   | `<criteria>` | `<recommendation>` | `<owner>` |

---

## 16. Evidence Index

| Evidence ID  | Description     | File / Path      | Tool     | Timestamp     | Notes     |
| ------------ | --------------- | ---------------- | -------- | ------------- | --------- |
| `<EVID-001>` | `<description>` | `<file_or_path>` | `<tool>` | `<timestamp>` | `<notes>` |

### 16.1 Evidence Storage Layout

```text
<evidence_root>/
├── hashes/
├── triage/
├── static/
├── dynamic/
├── debugger/
├── memory_dumps/
├── crash_dumps/
├── pcaps/
├── screenshots/
├── extracted/
├── scripts/
├── reports/
└── notes/
```

### 16.2 Evidence Handling Notes

```text
<notes_about_evidence_integrity_redaction_sensitive_data_and_storage_controls>
```

---

## 17. Reproducibility Appendix

### 17.1 Environment Setup

```bash
<environment_setup_commands>
```

### 17.2 Tool Versions

```text
<tool_version_output>
```

### 17.3 Sample Hash Verification

```bash
<hash_verification_commands>
```

Expected Output:

```text
<expected_hash_output>
```

### 17.4 Static Analysis Commands

```bash
<static_analysis_commands>
```

Expected Output:

```text
<expected_static_analysis_output>
```

### 17.5 Dynamic Analysis Commands

```bash
<dynamic_analysis_commands>
```

Expected Output:

```text
<expected_dynamic_analysis_output>
```

### 17.6 Debugger Commands

```text
<debugger_commands>
```

Expected Output:

```text
<expected_debugger_output>
```

### 17.7 Emulator / Harness Commands

```bash
<emulator_or_harness_commands>
```

Expected Output:

```text
<expected_harness_output>
```

### 17.8 Analysis Scripts

| Script          | Purpose     | Path            | Notes     |
| --------------- | ----------- | --------------- | --------- |
| `<script_name>` | `<purpose>` | `<script_path>` | `<notes>` |

Script Snippet:

```python
<analysis_script_snippet>
```

### 17.9 Patch Diffing Commands

```bash
<patch_diffing_commands>
```

Expected Output:

```text
<expected_patch_diffing_output>
```

### 17.10 Troubleshooting Notes

| Issue     | Cause     | Resolution     | Notes     |
| --------- | --------- | -------------- | --------- |
| `<issue>` | `<cause>` | `<resolution>` | `<notes>` |

### 17.11 Reproduction Checklist

* [ ] Correct sample hash verified
* [ ] Correct VM snapshot restored
* [ ] Required tools installed
* [ ] Tool versions recorded
* [ ] Network mode matches analysis notes
* [ ] Required symbols loaded
* [ ] Required inputs present
* [ ] Commands copied exactly from fenced blocks
* [ ] Expected output compared against actual output
* [ ] Deviations documented

---

## 18. Analyst Notes and Open Questions

### 18.1 Unknowns

| ID          | Unknown     | Why It Matters     | Proposed Resolution | Owner     | Status                   |
| ----------- | ----------- | ------------------ | ------------------- | --------- | ------------------------ |
| `<UNK-001>` | `<unknown>` | `<why_it_matters>` | `<resolution_step>` | `<owner>` | `<open/closed/deferred>` |

### 18.2 Assumptions

| ID          | Assumption     | Basis     | Risk if Wrong     | Confidence          |
| ----------- | -------------- | --------- | ----------------- | ------------------- |
| `<ASM-001>` | `<assumption>` | `<basis>` | `<risk_if_wrong>` | `<Low/Medium/High>` |

### 18.3 Blockers

| ID          | Blocker     | Impact     | Required Action     | Owner     |
| ----------- | ----------- | ---------- | ------------------- | --------- |
| `<BLK-001>` | `<blocker>` | `<impact>` | `<required_action>` | `<owner>` |

### 18.4 Follow-Up Analysis Tasks

| Task ID      | Task                 | Priority            | Owner     | Due Date       | Status                                 |
| ------------ | -------------------- | ------------------- | --------- | -------------- | -------------------------------------- |
| `<TASK-001>` | `<task_description>` | `<High/Medium/Low>` | `<owner>` | `<YYYY-MM-DD>` | `<open/in_progress/complete/deferred>` |

### 18.5 Research References

| Reference ID | Title               | Source            | Relevance     | Notes     |
| ------------ | ------------------- | ----------------- | ------------- | --------- |
| `<REF-001>`  | `<reference_title>` | `<source_or_url>` | `<relevance>` | `<notes>` |

### 18.6 Reviewer Comments

| Reviewer          | Date           | Comment     | Resolution     |
| ----------------- | -------------- | ----------- | -------------- |
| `<reviewer_name>` | `<YYYY-MM-DD>` | `<comment>` | `<resolution>` |

### 18.7 Final Analyst Notes

```text
<freeform_notes_observations_lessons_learned_and_context_not_captured_elsewhere>
```
