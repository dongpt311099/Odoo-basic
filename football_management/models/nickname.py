from odoo import models, fields


class Nickname(models.Model):
    _name ='player' 
    _description = 'Player'
    _inherit = "player"
    
    nickname = fields.Char(string = "Nickname")