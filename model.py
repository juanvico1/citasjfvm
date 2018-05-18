# -*- coding: utf-8 -*-

from odoo import models, fields


class Citas(models.Model):
	_name = "x_citasjfvm.citas"
	name = fields.Char(string='Autor', required=True)
	fecha_visualizacion = fields.Date(string='Fecha de visualización')
	texto = fields.Text(string='Texto')
	vista = fields.Boolean(string="Vista", default=False)
#	indice=fields.Integer(string='Número')
    
