# -*- coding: utf-8 -*-
from odoo import http

# class Citasjfvm(http.Controller):
#     @http.route('/citasjfvm/citasjfvm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citasjfvm/citasjfvm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasjfvm.listing', {
#             'root': '/citasjfvm/citasjfvm',
#             'objects': http.request.env['citasjfvm.citasjfvm'].search([]),
#         })

#     @http.route('/citasjfvm/citasjfvm/objects/<model("citasjfvm.citasjfvm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasjfvm.object', {
#             'object': obj
#         })