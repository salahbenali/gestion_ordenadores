from odoo import models, fields

class Componente(models.Model):
    _name = "gestion.componente"
    _description = "Componente de ordenador"

    name = fields.Char(string="Nombre técnico", required=True)
    especificaciones = fields.Text(string="Especificaciones")
    currency_id = fields.Many2one(
        'res.currency',
        string="Moneda",
        default=lambda self: self.env.company.currency_id.id,
    )
    price = fields.Monetary(
        string="Precio",
        currency_field='currency_id'
    )
