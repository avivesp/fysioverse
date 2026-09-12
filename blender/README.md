# Fysioverse Blender Asset Pipeline

This folder defines the production asset standard for replacing procedural Babylon.js clinic objects with lightweight 3D `.glb` assets.

## Asset set
- `clinic_reception.glb`
- `treatment_bed.glb`
- `exercise_mat.glb`
- `exercise_station.glb`
- `hybrid_screen.glb`
- `waiting_chair.glb`
- `plant.glb`
- `access_ramp.glb`
- `physio_character.glb`
- `patient_character.glb`

## Style
Stylised, friendly, low-poly healthcare simulation. Rounded forms, clean silhouettes, simple materials, no photorealistic patient data or branding. Keep assets visually coherent as one game world.

## Technical target
- Prefer `.glb` for browser delivery.
- Apply transforms before export.
- Keep origins/pivots useful for placement in Babylon.js.
- Avoid unnecessary modifiers and hidden geometry.
- Use a small number of materials per asset.
- Keep textures small and only where they add meaningful visual value.
- Export only the mesh/material/animation data required by the game.

## Animation names
Characters: `idle`, `walk`, `treat`, `celebrate`.
Construction: `build`, `complete`.

## Integration rule
Each asset should be usable as a self-contained scene object. The game must remain playable if an optional `.glb` asset fails to load; procedural fallbacks are retained until each asset is verified.

## Next production pass
Replace clinic furniture first, then characters, then construction animations. Keep gameplay logic independent from the asset layer so visual upgrades never break the tycoon simulation.