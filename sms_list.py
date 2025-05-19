from odoo import models, fields

class SMSList(models.Model):
    _name = 'sms.list'
    _description = 'SMS Recipient List'

    name = fields.Char(string='List Name', required=True)
    subscription_ids = fields.One2many('sms.contact.subscription', 'list_id', string='Subscriptions')