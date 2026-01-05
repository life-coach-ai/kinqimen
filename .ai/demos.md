## Development Guidelines for Demos/Examples
When adding new demo scripts:

1. **Location**: Place all demo scripts in this `demos/` directory
2. **Naming**: Use the prefix `demo_` for consistency
3. **Imports**: Add the parent directory to path for core imports:
   ```python
   import sys
   from pathlib import Path
   sys.path.insert(0, str(Path(__file__).parent.parent))
   ```
4. **Files** If there are some input or output files needed, place them into `demos/demo_inputs/` or `demos/demo_outputs/`
4. **Documentation**: Add a docstring explaining what the demo shows
5. **Self-contained**: Demos should be runnable independently