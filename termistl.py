import sys
from pathlib import Path

import numpy as np
from stl import mesh

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class TermiSTLApp(App):
    CSS_PATH = "termistl.css"
    BINDINGS = [
        ("q", "quit_application", "Quit"),
    ]

    def __init__(self, stl_file_path: Path):
        super().__init__()
        self.stl_file_path = stl_file_path
        self.stl_mesh_data = None
        self.information_panel_text = "Loading STL file..."

    def compose(self) -> ComposeResult:
        yield Header("TermiSTL – STL Information")
        yield Static(self.information_panel_text, id="stats")
        yield Footer()

    def on_mount(self):
        stl_load_modes = [("auto_detect", {}), ("binary", {"mode": 2}), ("ascii", {"mode": 1})]
        mesh_loaded_successfully = False
        for mode_name, mode_params in stl_load_modes:
            try:
                loaded_mesh = mesh.Mesh.from_file(self.stl_file_path, **mode_params)
                self.stl_mesh_data = loaded_mesh
                
                model_dimensions_xyz = loaded_mesh.max_ - loaded_mesh.min_
                volume_mm3, center_of_gravity, _ = loaded_mesh.get_mass_properties()
                total_surface_area_mm2 = loaded_mesh.areas.sum()
                
                self.information_panel_text = (
                    f"[bold]File:[/bold] {self.stl_file_path.name}\n"
                    f"[bold]Triangles:[/bold] {len(loaded_mesh.vectors):,}\n"
                    f"[bold]Dimensions (mm):[/bold] X:{model_dimensions_xyz[0]:.2f} Y:{model_dimensions_xyz[1]:.2f} Z:{model_dimensions_xyz[2]:.2f}\n"
                    f"[bold]Volume:[/bold] {volume_mm3 / 1000:.2f} cm³  [bold]Area:[/bold] {total_surface_area_mm2:.2f} mm²"
                )
                self.query_one("#stats", Static).update(self.information_panel_text)
                mesh_loaded_successfully = True
                break
            except Exception:
                continue
        
        if not mesh_loaded_successfully:
            self.query_one("#stats", Static).update("[red]Error: Failed to load STL file.[/red]")
            return

    def action_quit_application(self):
        self.exit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python termistl.py <path_to_model.stl>")
        sys.exit(1)
    
    input_file_path = Path(sys.argv[1])
    if not input_file_path.is_file():
        print(f"Error: File not found at '{input_file_path}'")
        sys.exit(1)
        
    app = TermiSTLApp(input_file_path)
    app.run()