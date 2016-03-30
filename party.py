# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.modules.party.party import STATES, DEPENDS

__all__ = ['Party', 'Invoice', 'Sale', 'Purchase']


class Party:
    __name__ = 'party.party'
    __metaclass__ = PoolMeta

    validated = fields.Boolean('Validated', states=STATES, depends=DEPENDS)


class PartyValidatedMixin:
    __metaclass__ = PoolMeta

    @classmethod
    def __setup__(cls):
        super(PartyValidatedMixin, cls).__setup__()
        cls.party.domain.append(('validated', '=', True))


class Invoice(PartyValidatedMixin):
    __name__ = 'account.invoice'
    __metaclass__ = PoolMeta


class Sale(PartyValidatedMixin):
    __name__ = 'sale.sale'
    __metaclass__ = PoolMeta


class Purchase(PartyValidatedMixin):
    __name__ = 'purchase.purchase'
    __metaclass__ = PoolMeta
