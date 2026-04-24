# Routing Order

Use the earliest viable layer:

1. local repository context and filesystem facts
2. local scripts and installed CLIs
3. authenticated APIs and official programmatic interfaces
4. existing domain skills
5. browser automation
6. broad exploratory fallback

## Switch Conditions

Switch only if:

- the current layer cannot produce the target
- the current layer is blocked by missing access
- the current layer is materially less reliable than the next one

If a later layer is chosen, keep the explanation short and concrete.
