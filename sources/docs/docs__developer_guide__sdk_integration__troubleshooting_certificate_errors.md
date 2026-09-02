---
url: https://www.braze.com/docs/developer_guide/sdk_integration/troubleshooting_certificate_errors
slug: docs__developer_guide__sdk_integration__troubleshooting_certificate_errors
title: "Troubleshooting SDK certificate trust errors"
description: "Troubleshoot HTTPS certificate trust errors that can block Braze SDK initialization across Android, Swift, and other SDKs."
section: developer_guide/sdk_integration
fetched: 2026-09-02
evidence: company-own (technical)
---
# Troubleshooting SDK certificate trust errors

If SDK initialization fails with SSL or TLS certificate trust errors, this usually means the device, simulator, browser, or server cannot validate the certificate chain for the Braze endpoint.

For example, on Android or other JVM-based environments, you may see:

```

1

```
 | 
```
javax.net.ssl.SSLHandshakeException: java.security.cert.CertPathValidatorException: Trust anchor for certification path not found

```
 | 

This is generally a network or certificate trust configuration issue in your environment, rather than an SDK integration bug.

## Common causes

- A corporate proxy, firewall, or traffic inspection tool is intercepting HTTPS traffic with a certificate that your runtime does not trust.
 
- A required root or intermediate certificate is missing from the trust store on the device, simulator, browser, or server.
 
- Local security settings block outbound HTTPS to Braze endpoints.
 
- App-level certificate or transport security settings block the connection.

## Troubleshooting steps

- Confirm your SDK endpoint and network access.

- Verify you are using the correct SDK endpoint for your workspace.
 
- Verify your environment can reach that endpoint over HTTPS.

- Compare behavior across networks.

- Test on a different network (for example, mobile data instead of corporate Wi-Fi).
 
- If the issue only occurs on one network, the root cause is likely proxy or firewall configuration.

- Validate your trust configuration.

- Confirm required root and intermediate certificates are installed and trusted in the runtime where the SDK is running.
 
- If your environment uses custom certificate authorities, confirm those certificates are distributed correctly.

- Review platform security settings.

- If your app or environment has explicit transport or certificate rules, confirm those settings allow HTTPS requests to Braze endpoints.

- Work with your network or security team.

- Share the full error and timestamp so they can verify certificate chains, TLS inspection settings, and allowlist rules.

note

Because Braze SDK traffic uses HTTPS, certificate trust failures can affect any Braze SDK (including Android, Swift, Web, React Native, Flutter, Unity, and Cordova) in environments with restrictive network policies.

- 

New Stuff!
