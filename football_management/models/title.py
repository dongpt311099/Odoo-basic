from odoo import models, fields
from odoo.tools import date_utils

class Title(models.Model):
    _name = 'title'
    _description = 'Title'
    
    name = fields.Char(string='Name', required=True)
    day = fields.Date(string="Day")
    attendance_time_start = fields.Datetime(string='Attendance time start')
    
    player_ids = fields.One2many('player', 'title_id', string="players")
    
    
    
    def test_to_date(self):
        date = fields.Date.to_date("2020-10-31") #định dạng"%Y-%m-%d"
        print(date)
        print(type(date))
        
    def test_to_string(self):
        if self.day:
            date = fields.Date.to_string(self.day)
            print(date)
            print(type(date))
        
    def test_today(self):
        today = fields.Date.today()
        print(today)
        
    def test_datetime(self):
        today = fields.Datetime.now()
        print(today)
        
        
    def test_addtime(self):
        add = fields.Datetime.add(fields.Datetime.now(), hours = 7)
        print(add)
        
    def test_start_of(self):
        date = fields.Date.to_date("2020-10-31")
        start = date_utils.start_of(date, "week")
        print(start)
        
    def test_end_of(self):
        date = fields.Date.to_date("2020-10-31")
        end = date_utils.end_of(date, "week")
        print(end)
        
        
        
        
        
        
        
        
        
        
        
        