from odoo import models, fields

class SMSMarketingLine(models.Model):
    _name = 'sms.marketing.line'
    _description = 'SMS Send Log'

    campaign_id = fields.Many2one('sms.marketing')
    contact_id = fields.Many2one('sms.contact')
    message_id = fields.Many2one('sms.marketing.message')
    status = fields.Selection([
        ('sent', 'Sent'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
        ('clicked', 'Clicked')
    ], default='sent')