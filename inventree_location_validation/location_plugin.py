import structlog
from plugin import InvenTreePlugin
from plugin.mixins import SettingsMixin, ValidationMixin
from .meta_access import MetaAccess
from stock.models import StockItem
from .version import PLUGIN_VERSION

logger = structlog.get_logger('inventree')


class LocationValidatorPlugin(SettingsMixin, ValidationMixin, InvenTreePlugin):

    NAME = 'LocationValidatorPlugin'
    SLUG = 'locationvalidatorplugin'
    TITLE = 'Location Validator Plugin'
    DESCRIPTION = 'A plugin that checks if the target location is full'
    PUBLISH_DATE = "2025-11-25:00:00"
    VERSION = PLUGIN_VERSION

    SETTINGS = {
    }

    def validate_model_instance(self, instance, deltas=None):
        if isinstance(instance, StockItem):
            try:
                max_quantity = int(MetaAccess.get_value(self, instance.location, 'MaxQuantity'))
            except Exception:
                logger.debug('Max Quantity not set, exiting')
                return
            try:
                change = deltas['location']
            except Exception:
                logger.debug('No location change, exiting')
                return
            if (instance.location.get_stock_items().count() > max_quantity - 1):
                self.raise_error(f'Target location can contain only {max_quantity} stockitem')
