#This file is part of Tryton.  The COPYRIGHT file at the top level
#of this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields


class Location(ModelSQL, ModelView):
    "Stock Location"
    _name = 'stock.location'
    sequence = fields.Integer('Sequence', states= {'readonly': "not active"})

    def __init__(self):
        super(Location, self).__init__()
        self._order.insert(0, ('sequence', 'ASC'))

Location()