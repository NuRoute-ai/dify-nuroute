# NuRoute

Route Dify's LLM calls through your [NuRoute](https://nuroute.ai) gateway. Model `auto` lets
NuRoute's routing engine pick the best model for each request; you can also specify a model ID
directly (e.g. `gpt-4o`, `claude-sonnet-4-6`).

## Setup

1. In Dify, go to **Settings → Model Provider → NuRoute → Add Model**.
2. **Model Name**: `auto`, or a specific model ID from your NuRoute catalog.
3. **NuRoute Gateway URL**: your gateway's base URL, including `/v1` (e.g.
   `https://your-nuroute-gateway/v1`).
4. **API Key**: an `aicp-...` key from your project's (or org's) API Keys page in the NuRoute
   dashboard.
5. **Model context size**: the context window of the model you're routing to. If you're using
   `auto`, set this to the smallest context window in your catalog to stay safe, or the largest
   if you're confident every request fits.

Add it again with a different **Model Name** to make several NuRoute-routed models (e.g. `auto`
and a pinned `claude-sonnet-4-6`) available side by side in Dify's model dropdown.

## Usage

Once added, select **NuRoute** as the model for any LLM node in a chatflow, workflow, or agent —
it works exactly like any other model provider in Dify. For example, pick the `auto` model on a
chatflow's LLM node to let NuRoute route each message to whichever model fits best, without
committing to one model ID for the whole flow.

## What this doesn't do

This is a model provider only — it sends chat completions through NuRoute, nothing else.
Projects, routing configuration, policies, budgets, and API keys are all still managed from the
NuRoute dashboard.

## How it works

NuRoute's gateway exposes an OpenAI-compatible `/v1/chat/completions` endpoint, so this plugin
is a thin subclass of the Dify Plugin SDK's own OpenAI-compatible model base class rather than a
reimplementation from scratch.

## Source repository

https://github.com/NuRoute-ai/dify-nuroute

## Support

For issues with this plugin, open an issue at the source repository above. For anything about
your NuRoute gateway itself (routing, providers, billing), see [nuroute.ai/docs](https://nuroute.ai/docs).
