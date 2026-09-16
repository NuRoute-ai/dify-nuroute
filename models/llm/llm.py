from dify_plugin.interfaces.model.openai_compatible.llm import OAICompatLargeLanguageModel


class NuRouteLargeLanguageModel(OAICompatLargeLanguageModel):
    """NuRoute's gateway is a standard OpenAI-compatible /v1/chat/completions endpoint, so this
    is a thin subclass of the SDK's own OAICompatLargeLanguageModel rather than a
    reimplementation — request/response handling, streaming, and token counting all come from
    the base class, already exercised by every other OpenAI-compatible provider in the
    marketplace. Nothing NuRoute-specific needs overriding here: the "auto" routing model and
    provider name are just free-form strings the customizable-model config already supports.
    """
