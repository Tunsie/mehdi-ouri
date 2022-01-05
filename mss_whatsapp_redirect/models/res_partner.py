# -*- coding: utf-8 -*-
#############################################################################################
#                                                                                           #
#    Maurya Software Solutions                                                              #
#    Copyright (C) 2018-TODAY Maurya Software Solutions(<http://www.maurysolutions.com>).   #
#    Author: Om Prakash Maurya(<https://www.maurysolutions.com>)                            #
#    you can modify it under the terms of the GNU LESSER                                    #
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.                                           #
#                                                                                           #
#    It is forbidden to publish, distribute, sublicense, or sell copies                     #
#    of the Software or modified copies of the Software.                                    #
#                                                                                           #
#    This program is distributed in the hope that it will be useful,                        #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                         #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                          #
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.                          #
#                                                                                           #
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE               #
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.                              #
#    If not, see <http://www.gnu.org/licenses/>.                                            #
#                                                                                           #
#############################################################################################

from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'


    def mobile_whatsapp_link(self):
        for rec in self:
            if rec.mobile:
                return {
                    'type': 'ir.actions.act_url',
                    'url': "https://web.whatsapp.com/send?phone=" + rec.mobile or "https://api.whatsapp.com/send?phone=" + rec.mobile,
                    'target': 'new',
                    'res_id': rec.id,
                }
