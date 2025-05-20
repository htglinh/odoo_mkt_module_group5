from odoo import models, fields

class SMSMarketingMessage(models.Model):
    _name = 'sms.marketing.message'
    _description = 'SMS Message Variant for A/B Test'

    campaign_id = fields.Many2one(
        'sms.marketing',
        string='Campaign',
        required=True,
        ondelete='cascade'
    )
    content = fields.Text(
        string='Message Content',
        required=True
    )

    line_ids = fields.One2many(
        'sms.marketing.line',
        'message_id',
        string='Send Logs'
    )