# -*- coding: utf-8 -*-
from odoo import http

# class CustomCss(http.Controller):
#     @http.route('/custom_css/custom_css/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_css/custom_css/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_css.listing', {
#             'root': '/custom_css/custom_css',
#             'objects': http.request.env['custom_css.custom_css'].search([]),
#         })

#     @http.route('/custom_css/custom_css/objects/<model("custom_css.custom_css"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_css.object', {
#             'object': obj
#         })