# Supabase Integration Patterns

Supabase can provide Postgres storage, authentication, and realtime updates for AI applications. Keep documents, task events, and agent metrics in separate tables so the dashboard can query operational views without coupling to model logic.

Use row-level security for user-owned data and server-side secrets only. API clients should call a backend boundary rather than exposing privileged keys in the browser.
