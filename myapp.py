from odoo import models, fields, api

class myapp(models.Model):
    _name = 'myapp.product'
    name = fields.Char('Product Name')
    description = fields.Char('Product Description')
    warehouse_from = fields.Many2one('stock.warehouse', 'From Warehouse')
    warehouse_to = fields.Many2one('stock.warehouse', 'To Warehouse')
    quantity = fields.Integer('Quantity')
    status = fields.Selection([
        ('purchase', 'Purchase'),
        ('transfer', 'Transfer'),
        ('sale', 'Sale')], 'Status')

    @api.model
    def create_product(self, name, description, warehouse_from, warehouse_to, quantity, status):
        product = self.create({
            'name': "Кросовки Nike",
            'description': "Описание товара",
            'warehouse_from': "Склад, с которого будет перемещен товар",
            'warehouse_to': "Склад, на который будет перемещен товар",
            'quantity': "Количество товара",
            'status': "Статус товара",
        })
        return product

    @api.model
    def create_property_change_act(self, name, description, warehouse_from, warehouse_to, quantity, status):
        property_change_act = self.env['myapp.property_change_act'].create({
            'name': "Название акта изменения свойств товара",
            'description': "Описание акта изменения свойств товара",
            'warehouse_from': "Склад, с которого будет перемещен товар",
            'warehouse_to': "Склад, на который будет перемещен товар ",
            'quantity': " Количество товара",
            'status': "Статус акта изменения свойств товара,",
        })
        return property_change_act

    @api.model
    def conduct_property_change_act(self, property_change_act):
       #result = myapp.conduct_property_change_act(my_property_change_act)
       return True