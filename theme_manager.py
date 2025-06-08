# =================================Theme Manager==================================
# theme_manager.py - Advanced theme management with real-time updates
import tkinter as tk

class ThemeManager:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.themed_widgets = []  # Track widgets that need theme updates
        
    def register_widget(self, widget, widget_type="default"):
        """Register a widget for theme updates"""
        self.themed_widgets.append((widget, widget_type))
    
    def apply_theme_to_widget(self, widget, widget_type, colors):
        """Apply theme colors to a specific widget"""
        try:
            if widget_type == "window":
                widget.configure(bg=colors["background"])
            elif widget_type == "frame":
                widget.configure(bg=colors["background"])
            elif widget_type == "label":
                widget.configure(bg=colors["background"], fg=colors["text"])
            elif widget_type == "button_primary":
                widget.configure(bg=colors["primary"], fg="white")
            elif widget_type == "button_secondary":
                widget.configure(bg=colors["secondary"], fg="white")
            elif widget_type == "button_danger":
                widget.configure(bg=colors["danger"], fg="white")
            elif widget_type == "entry":
                widget.configure(bg="white" if colors["background"] == "white" else colors["frame_bg"],
                               fg=colors["text"])
            elif widget_type == "text":
                widget.configure(bg="white" if colors["background"] == "white" else colors["frame_bg"],
                               fg=colors["text"])
        except tk.TclError:
            # Widget might have been destroyed
            pass
    
    def update_all_widgets(self):
        """Update all registered widgets with current theme"""
        colors = self.config_manager.get_theme_colors()
        
        # Remove destroyed widgets
        self.themed_widgets = [(w, t) for w, t in self.themed_widgets 
                              if self.widget_exists(w)]
        
        # Apply theme to remaining widgets
        for widget, widget_type in self.themed_widgets:
            self.apply_theme_to_widget(widget, widget_type, colors)
    
    def widget_exists(self, widget):
        """Check if widget still exists"""
        try:
            widget.winfo_exists()
            return True
        except tk.TclError:
            return False
    
    def set_theme(self, theme_name):
        """Change theme and update all widgets"""
        if self.config_manager.set_theme(theme_name):
            self.update_all_widgets()
            return True
        return False
    
    def get_current_theme(self):
        """Get current theme name"""
        return self.config_manager.get_app_setting("theme", "light")
    
    def get_available_themes(self):
        """Get list of available themes"""
        return list(self.config_manager.config["colors"].keys())