from odoo import models, fields

class SMSContact(models.Model):
    _name = 'sms.contact'
    _description = 'SMS Contact'

    name = fields.Char(string='Full Name')
    phone = fields.Char(string='Phone Number')
    company = fields.Char(string='Company')
    subscription_ids = fields.One2many('sms.contact.subscription', 'contact_id', string='Subscriptions')