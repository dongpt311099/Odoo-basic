from odoo import models, fields


class goal(models.Model):
    _name = 'player.goal'
    _description = 'Player'
    _inherit = "player"
    
    goal = fields.Integer(string='Goal')