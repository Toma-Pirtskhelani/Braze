---
url: https://www.braze.com/docs/user_guide/messaging/landing_pages/customize_the_url
slug: docs__user_guide__messaging__landing_pages__customize_the_url
title: "Customize landing page URLs"
description: "Learn how to customize your landing page URLs with your company's brand, by connecting your domain to your Braze workspace."
section: user_guide/messaging
fetched: 2026-09-02
evidence: company-own (technical)
---
# Customize landing page URLs

Learn how to customize your landing page URLs with your company’s brand by connecting your domain to your Braze workspace.

## How it works

When you connect your domain to Braze, it will be used as the default domain for all landing pages. For example, if you connect the subdomain forms.example.com, your landing page URLs would now be forms.example.com/holiday-sale.

The number of custom domains you can connect to your Braze account depends on your plan tier. To increase your limit, contact your Braze account manager.

## Connect your domain to Braze

To connect a domain to your Braze account, have an administrator follow these steps.

- Go to Settings > Landing Page Settings.
 
- Enter the domain you want to connect to and select Submit. For example, forms.example.com.
 
- Copy and paste the TXT and CNAME records into the DNS settings of your domain provider.
 
- Return to the Braze dashboard to verify the connection.

note

Depending on your domain provider, the connection can take up to 48 hours. When the process is complete, we’ll start using your custom domain for your landing pages in the Braze dashboard.

### SSL certificate setup

Braze uses Cloudflare to automatically provision SSL certificates for your custom domain through an ACME DNS-01 challenge. This continuous validation method is enabled by one of the CNAME records you provided during setup, and allows the certificate authority (LetsEncrypt) to verify your domain ownership through DNS records without requiring Braze to own your domain.

## Remove your domain

If you’re a Braze administrator, you can remove a previously-configured domain by completing the following steps:

- Go to Settings > Landing Page Settings.
 
- Select Remove Custom Domain
 
- Confirm removal of the domain.
 
- Remove the listed DNS records from your domain settings.

important

When you remove a custom domain, that URL will no longer be valid. Any landing pages that were using this domain will automatically revert to the default domain set by Braze.

## Migrate your domain

To migrate a custom domain to another workspace:

- Remove the custom domain.
 
- Create a new custom domain in the desired workspace.
 
- Reconfigure the custom domain with the new DNS records. Note that your subdomain will be unavailable during this process.

## DNS resources

The following table contains resources for creating and managing DNS records with commonly used domain providers. If you’re using a different provider, refer to that provider’s documentation or contact their support team for information.

 Domain provider | 
 Resources | 

 Bluehost | 
 DNS Records Explained
 DNS Management Add Edit or Delete DNS Entries | 

 Dreamhost | 
 How do I add custom DNS records? | 

 GoDaddy | 
 Add a CNAME record | 

 Cloudflare | 
 Manage DNS records | 

 Squarespace | 
 Adding custom DNS settings | 

 Amazon Route 53 | 
 Creating records by using the Amazon Route 53 console | 

 Google Cloud DNS | 
 Quickstart: Set up DNS records for a domain name with Cloud DNS | 

## Troubleshooting

### My domain connection failed

Verify that your domain was entered correctly and that it matches what you submitted to Braze from your domain provider account. If it’s correct and matches, check the TXT and CNAME records provided by Braze. They should match the records you entered into your domain provider account.

## Frequently asked questions

### Can I use nested subdomains for my custom domain?

Yes, you can use nested subdomains for your landing pages. For example, forms.braze.com, pages.forms.braze.com, or deeper levels are all supported. The only requirement is that you cannot use an apex domain (such as braze.com) because Braze uses CNAME records for the connection.

### Can I connect multiple subdomains to my workspace, or connect one subdomain to multiple workspaces?

No, you currently can only connect one subdomain to a workspace.

### Can I use the same subdomain that I currently use for my main website or my sending domain?

No, you can’t use subdomains that are already in use. While these subdomains are valid, they can’t be used for landing pages if they are already assigned to other purposes or have DNS records that conflict with the required CNAME records.

### Why is my custom domain stuck on “Connecting” despite valid DNS records?

If your custom domain shows all DNS records as “Connected” but the domain status remains on “Connecting” for more than four hours, your organization may be using CAA (Certificate Authority Authorization) records or Cloudflare zone holds that prevent Braze from securing your page.

#### CAA records

CAA records restrict which certificate authorities can issue SSL certificates for your domain. If your CAA records don’t include LetsEncrypt, Braze (through Cloudflare) can’t issue the required SSL certificate.

To resolve this, ask your IT team to add a CAA record to your subdomain with the following values:

- Record type: CAA
 
- Value: 0 issue "letsencrypt.org"

For more information, refer to LetsEncrypt’s CAA documentation.

#### Cloudflare zone holds

If your organization uses Cloudflare, a zone hold security feature may be preventing Braze from creating your custom domain.

To resolve this, ask your IT team to temporarily release the zone hold. For more information, refer to Cloudflare’s zone hold documentation.

#### Restarting the validation process

After resolving either issue, delete and recreate your custom domain in the Braze dashboard to restart the validation process.

### Can I use a reverse proxy to serve landing pages under my main domain or a subdirectory?

No, landing page URL Liquid tags will not work correctly with reverse proxies.

- 

New Stuff!
