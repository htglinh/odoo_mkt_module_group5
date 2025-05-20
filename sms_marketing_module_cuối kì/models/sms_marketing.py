from odoo import models, fields

class SMSMarketing(models.Model):
    _name = 'sms.marketing'
    _description = 'SMS Campaign'

    name = fields.Char(string='Campaign Name', required=True)
    list_ids = fields.Many2many('sms.list', string='Recipient Lists')
    message_ids = fields.One2many('sms.marketing.message', 'campaign_id', string='SMS Versions')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent')
    ], default='draft')
    send_time = fields.Datetime(string='Scheduled Send Time')
    line_ids = fields.One2many('sms.marketing.line', 'campaign_id', string='Send Logs')

    def send_sms_campaign(self):
        for campaign in self:
            for sms_msg in campaign.message_ids:
                for contact in campaign._get_subscribers():
                    self.env['sms.marketing.line'].create({
                        'campaign_id': campaign.id,
                        'contact_id': contact.id,
                        'message_id': sms_msg.id,
                        'status': 'sent',
                    })
            campaign.state = 'sent'

    def _get_subscribers(self):
        return self.env['sms.contact'].search([
            ('subscription_ids.list_id', 'in', self.list_ids.ids)
        ])