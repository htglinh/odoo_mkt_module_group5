SMS Marketing Module for Odoo
=============================

This module allows managing SMS campaigns similar to mass_mailing.

Main Models:
- sms.list: recipient lists
- sms.contact: contacts with phone numbers
- sms.contact.subscription: link between contact and list
- sms.marketing: SMS campaigns
- sms.marketing.message: versions for A/B testing
- sms.marketing.line: sending logs with status tracking

How to use:
1. Create recipient lists and contacts.
2. Create a campaign, add message variants.
3. Link lists and schedule or send now.
4. Logs will be created and statuses tracked.