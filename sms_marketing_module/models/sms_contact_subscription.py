from odoo import models, fields

class SMSContactSubscription(models.Model):
    _name = 'sms.contact.subscription'
    _description = 'Contact - List Subscription'

    contact_id = fields.Many2one('sms.contact', required=True)
    list_id = fields.Many2one('sms.list', required=True)