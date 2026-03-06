"""
Advanced Purge

Granular cleanup with safety
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Advanced Purge!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
