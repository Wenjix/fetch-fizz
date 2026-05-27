# Foxglove Studio (optional)

Foxglove is **not required** for fetch-fizz development, CI, or the default demo path. Use it only if you want 2D costmap click-to-nav during rehearsal.

## When to use

- Rehearsing spatial navigation with visual goal picking
- Watching costmap + pose alongside Rerun 3D (DimOS serves both on port `7779`)

## When to skip

- CI, laptop-only dev, replay smoke tests
- Demo day if you rely on `humancli` + scripted MCP choreo

## One-time setup

1. Install [Foxglove Studio](https://foxglove.dev/download)
2. Get the extension from DimOS (requires git-lfs):

```bash
# From a dimos checkout, or after dimos install pulls LFS assets:
git lfs pull --include "assets/dimensional.command-center-extension-0.0.1.foxe"
cp assets/dimensional.command-center-extension-0.0.1.foxe ~/.foxglove-studio/extensions/
```

Source: [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) @ `b45e5d5`, path `assets/dimensional.command-center-extension-0.0.1.foxe`

3. Restart Foxglove → **Add panel** → search **`command-center`**
4. Start DimOS stack (`make demo` or `make nav`)
5. Panel connects to `http://localhost:7779` via **Socket.IO** (not raw WebSocket)

## Notes

- DimOS does not use ROS or `foxglove_bridge`
- Browser route `http://localhost:7779/command-center` may 500 offline (missing LFS HTML) — use the Foxglove panel instead
- Human override: stop skills and Ctrl+C still win over agent/Foxglove goals
