from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Clb(models.Model):
    _name = 'clb'
    _description = 'Clb'
    
    name = fields.Char(string='Name', required=True)
    avatar = fields.Binary(string='Avatar')
    image_128 = fields.Image(string='Logo', max_width=128, max_height=128)
    currency_id = fields.Many2one('res.currency', string='Đơn vị')
    class_fund = fields.Monetary(string='Giá trị Clb', currency_field='currency_id')
    introduce_yourself = fields.Html(string='Introduce Clb')
    founding = fields.Date(string='Founding')
    
    player_ids = fields.One2many('player', 'clb_id', string="players")
    
    def remove_clb(self):
        for clb in self:
            clb.unlink()
      
    def create_clb(self):      
        new_clb = self.env['clb'].create([
           {'name': 'Liverpool'}
        ])
        
    @api.model
    def create(self, vals):
        if 'name' in vals:
            vals['name'] = vals['name'].upper()
        return super(Clb, self).create(vals)   
        
    def copy_clb(self):
        clb = self.env['clb'].browse(1)
        new = clb.copy()
        
    def search_clb(self):
        print(clb = self.env['clb'].search_count([('name', '=', 'Real Madrid')]))
        
    def filter_clb(self):
        clbs = self.env['clb'].search([])
        print(clbs.filtered(lambda clb: clb.name == 'Liverpool'))
        
    def filter_domain_clb(self):
        clbs = self.env['clb'].search([])
        print(clbs.filtered_domain([('name', '=', 'Real Madrid')]))
        
    def map_clb(self):
        clbs = self.env['clb'].search([])
        print(clbs.mapped(lambda clb: '%s, %s' % (clb.name, clb.id)))
        
    def sort_clb(self):
        clbs = self.env['clb'].search([])
        print(clbs.sorted(key=lambda c: c.name))
        
    @api.constrains('name')
    def _check_name(self):
        for n in self:
            if n.name == "A":
                raise ValidationError("Không đc đặt tên a")
    
    def environment(self):
        print(self.env)   
        print(self.env.user)    
        print(self.env.cr) 
        print(self.env['clb'])
        print(self.env['clb'].search([('name', 'ilike', 'liverpool')]))
        
    def recordset(self):
        print(self.ids)
        print(self.environment)
        print(self.ensure_one())
        print(self.name_get())
        print(self.get_metadata())
        print(self.with_context(dong='Phan Thanh Dong')._context)
        
    def thu_thi_sql(self):
        print(self.env.cr.dbname)
        
        # self.flush()
        print(self.env.cr.execute("SELECT * FROM clb"))
        print(self.env.cr.fetchall())
        # self.env.cr.execute("INSERT INTO clb(name) VALUES('Man city')")
    
        
     
    
    
        
        
        
        
        
        
        
        
        
        
        