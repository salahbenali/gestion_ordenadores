from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo import fields as odoo_fields

class Ordenador(models.Model):
    _name = "gestion.ordenador"
    _description = "Gestión de Ordenador"

    name = fields.Char(string="Referencia", required=True)
    user_id = fields.Many2one('res.users', string='Usuario asignado')
    
    components_ids = fields.Many2many(
        "gestion.componente", string="Componentes seleccionados")

    ultima_modificacion = fields.Datetime(
        string='Fecha última modificación',
        default=fields.Datetime.now,
    )

    currency_id = fields.Many2one(
        'res.currency',
        string="Moneda",
        required=True,
        default=lambda self: self.env.company.currency_id.id,
    )

    precio = fields.Monetary(
        string="Coste total",
        currency_field='currency_id',
        compute='_compute_total',
        store=True,
    )

    sistema_operativo_ids = fields.Many2many(
        comodel_name="gestion.sistema_operativo",
        string="Sistemas Operativos instalados"
    )

    @api.depends("components_ids.price")
    def _compute_total(self):
        for record in self:
            total = 0.0
            for componente in record.components_ids:
                total += componente.price or 0.0
            record.precio = total



    @api.constrains('ultima_modificacion')
    def _comprobar_fecha(self):
        ahora = odoo_fields.Datetime.now()
        for record in self:
            if record.ultima_modificacion and record.ultima_modificacion > ahora:
                raise ValidationError("La fecha de modificación no puede estar en el futuro.")

class SistemaOperativo(models.Model):
    _name = "gestion.sistema_operativo"
    _description = "Tipo de Sistema Operativo"

    name = fields.Char(string="Nombre del SO", required=True)
