import logging
from collections.abc import Mapping

from dify_plugin import ModelProvider

logger = logging.getLogger(__name__)


class NuRouteProvider(ModelProvider):
    def validate_provider_credentials(self, credentials: Mapping) -> None:
        # customizable-model only — each model carries its own gateway URL / API key,
        # validated per-model by NuRouteLargeLanguageModel.validate_credentials instead.
        pass
