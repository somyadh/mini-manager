from .apps.v1.views.company import CompaniesApi
from .apps.v1.views.color import ColorList
from .apps.v1.views.warehouse import WarehouseList
from .apps.v1.views.vendor import VendorList
from .apps.v1.views.wattage import WattageList
from .apps.v1.views.sku import SkuList
from .apps.v1.views.sku import Sku
from .migrations.seed import seed
from .apps.v1.views.welcome import Welcome
# from .apps.v1.views.item import ItemList


def initialize_routes(api):
    api.add_resource(CompaniesApi, '/company-list')
    api.add_resource(ColorList, '/color-list')
    api.add_resource(WarehouseList, '/warehouse-list')
    api.add_resource(VendorList, '/vendor-list')
    api.add_resource(WattageList, '/wattage-list')
    api.add_resource(SkuList, '/sku-list')
    api.add_resource(seed, '/seed')
    api.add_resource(Welcome, '/')
    # api.add_resource(ItemList, '/item-list')
    api.add_resource(Sku, '/sku/<name>')
