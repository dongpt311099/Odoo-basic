from odoo import models, fields, api


class Player(models.Model):
    _name = 'player'
    _description = 'Player'
    
    name = fields.Char(string='Name', required=True, translate=True, groups="base.group_system", help="abc")
    image = fields.Binary(string='Image', attachment=True)
    country = fields.Char(string='Country')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    date_of_birth = fields.Datetime(string='Date of birth')
    position = fields.Char(string='Position')
    height = fields.Float(string='Height')
    weight = fields.Float(string='Weight')
    number = fields.Integer(string='Number')
    basic_salary = fields.Integer(string='Basic salary')
    skill = fields.Selection([('100000', '1'), ('200000', '2'), ('300000', '3'), ('400000', '4'), ('500000', '5')], string='Skill', default='100000')
    salary = fields.Float(string='Salary', compute='_compute_gpa')
    language = fields.Char(compute='_test_language')
    # clbs = fields.Many2many('clb', 'player_clb_rel', 'player_id', 'clb_id', string='Clbs')
    
    clb_id = fields.Many2one('clb','Football Club', domain = "[('name', '=', 'Real Madrid')]")
    
    title_id = fields.Many2one('title','Title')
        
    @api.depends('basic_salary', 'skill')
    def _compute_gpa(self):
        for s in self:
            # if s.skill:
                s.salary = s.basic_salary * int(s.skill)
            # else: s.salary = 0
            
    @api.onchange('name')
    def _onchange_class_id(self):
        if self.name:
            self.gender = 'female'
            
    def remove_player(self):
        for player in self:
            player.unlink()
        
    @api.depends_context('lang')
    def _test_language(self):
        for rc in self:
            if rc.env.context.get('lang') == "vi_VN":
                rc.language = "Việt Nam"
            else: rc.language = "English"
            
    
    
    
    
    