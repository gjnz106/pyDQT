"""
Gridline Alignment

Align grids precisely
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Gridline Alignment!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
