from odoo import models, fields

class SMSMarketingLine(models.Model):
    _name = 'sms.marketing.line'
    _description = 'SMS Send Log'

    campaign_id = fields.Many2one(
        'sms.marketing',
        string='Campaign',
        required=True,
        ondelete='cascade'
    )
    contact_id = fields.Many2one(
        'sms.contact',
        string='Contact',
        required=True,
        ondelete='cascade'
    )
    message_id = fields.Many2one(
        'sms.marketing.message',
        string='Message',
        required=True,
        ondelete='set null'
    )
    status = fields.Selection([
        ('sent', 'Sent'),
        ('delivered', 'Delivered'),
        ('failed', 'Failed'),
        ('clicked', 'Clicked')
    ], string='Status', default='sent')