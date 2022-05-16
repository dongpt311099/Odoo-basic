from odoo import models, fields


class ClbClb(models.Model):
    _name = 'clb'
    _description = 'Clb'
    
    name = fields.Char(string='Name', required=True)
    
    player_ids = fields.One2many('player', 'clb_id', string="players")