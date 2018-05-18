#-*- coding: utf-8 -*-
from odoo import models, fields
class ControlCitas(models, Model):
	_name = "citasjfvm.citas"
	autor = fields.String(string='Autor')
	fecha_creacion = fields.Date(string='Creada')
	fecha_visionada = fields.Date(string='Vista')
	texto = fields.Text(string='Texto')
	isChecked = fields.Boolean('Vista', default=False)
	indice=fields.Integer(string='Número')