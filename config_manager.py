# =================================Admin Configuration and Theme Management==================================
# config_manager.py - Centralized configuration and theme management
import json
import os
from datetime import datetime
import hashlib

class ConfigManager:
    def __init__(self):
        self.config_file = "app_config.json"
        self.default_config = {
            "admin": {
                "username": "admin",
                "password_hash": self.hash_password("admin123"),  # Default admin password
                "email": "admin@pythontraining.local",
                "created_date": datetime.now().isoformat()
            },
            "app_settings": {
                "theme": "light",  # light, dark, night
                "window_width": 450,
                "window_height": 700,
                "demo_window_width": 600,
                "auto_advance_delay": 2000,
                "questions_per_level": 15
            },
            "colors": {
                "light": {
                    "primary": "#4CAF50",
                    "secondary": "#2196F3", 
                    "warning": "#FF9800",
                    "danger": "#f44336",
                    "logout": "#9C27B0",
                    "background": "white",
                    "text": "black",
                    "frame_bg": "#f0f0f0",
                    "button_hover": "#45a049"
                },
                "dark": {
                    "primary": "#66BB6A",
                    "secondary": "#42A5F5",
                    "warning": "#FFA726", 
                    "danger": "#EF5350",
                    "logout": "#AB47BC",
                    "background": "#2b2b2b",
                    "text": "#ffffff",
                    "frame_bg": "#404040",
                    "button_hover": "#5cbf60"
                },
                "night": {
                    "primary": "#4CAF50",
                    "secondary": "#1976D2",  # Reduced blue light
                    "warning": "#FF8F00",
                    "danger": "#D32F2F", 
                    "logout": "#7B1FA2",
                    "background": "#1a1a1a",
                    "text": "#ffcc80",  # Warm amber text
                    "frame_bg": "#333333",
                    "button_hover": "#45a049"
                }
            },
            "first_run": True,
            "version": "1.0.0"
        }
        self.config = self.load_config()

    def hash_password(self, password):
        """Hash password for secure storage"""
        return hashlib.sha256(password.encode()).hexdigest()

    def load_config(self):
        """Load configuration from file or create default"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                # Merge with defaults for any missing keys
                return self.merge_configs(self.default_config, config)
            except Exception as e:
                print(f"Error loading config: {e}")
                return self.default_config.copy()
        else:
            # First run - create default config
            self.save_config(self.default_config)
            return self.default_config.copy()

    def merge_configs(self, default, loaded):
        """Merge loaded config with defaults to ensure all keys exist"""
        result = default.copy()
        for key, value in loaded.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self.merge_configs(result[key], value)
            else:
                result[key] = value
        return result

    def save_config(self, config=None):
        """Save configuration to file"""
        if config is None:
            config = self.config
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

    def get_theme_colors(self):
        """Get current theme colors"""
        current_theme = self.config["app_settings"]["theme"]
        return self.config["colors"][current_theme]

    def set_theme(self, theme_name):
        """Set the current theme"""
        if theme_name in self.config["colors"]:
            self.config["app_settings"]["theme"] = theme_name
            self.save_config()
            return True
        return False

    def verify_admin_credentials(self, username, password):
        """Verify admin login credentials"""
        admin_config = self.config["admin"]
        return (admin_config["username"] == username and 
                admin_config["password_hash"] == self.hash_password(password))

    def update_admin_credentials(self, new_username, new_password, new_email):
        """Update admin credentials"""
        self.config["admin"]["username"] = new_username
        self.config["admin"]["password_hash"] = self.hash_password(new_password)
        self.config["admin"]["email"] = new_email
        self.config["admin"]["last_updated"] = datetime.now().isoformat()
        return self.save_config()

    def reset_to_defaults(self):
        """Reset configuration to defaults (for software transfer)"""
        # Keep the current theme preference but reset everything else
        current_theme = self.config["app_settings"]["theme"]
        self.config = self.default_config.copy()
        self.config["app_settings"]["theme"] = current_theme
        self.config["first_run"] = True
        return self.save_config()

    def is_first_run(self):
        """Check if this is the first run"""
        return self.config.get("first_run", True)

    def set_first_run_complete(self):
        """Mark first run as complete"""
        self.config["first_run"] = False
        self.save_config()

    def get_app_setting(self, key, default=None):
        """Get application setting"""
        return self.config["app_settings"].get(key, default)

    def set_app_setting(self, key, value):
        """Set application setting"""
        self.config["app_settings"][key] = value
        self.save_config()

    def export_config(self, filepath):
        """Export configuration for backup"""
        try:
            with open(filepath, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Error exporting config: {e}")
            return False

    def import_config(self, filepath):
        """Import configuration from backup"""
        try:
            with open(filepath, 'r') as f:
                imported_config = json.load(f)
            self.config = self.merge_configs(self.default_config, imported_config)
            return self.save_config()
        except Exception as e:
            print(f"Error importing config: {e}")
            return False


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