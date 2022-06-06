from odoo import models, fields

class CreateClb(models.TransientModel): 
    _name = 'create.clb'
    _description = 'Create.Clb'
    _inherit = 'clb'
    
    name = fields.Char(string = 'Name')
    
    def create_clb(self):
            if self.name:
                self.env['clb'].create([{'name':self.name}])