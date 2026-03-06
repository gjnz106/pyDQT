"""
Level Alignment

Align levels precisely
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Level Alignment!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
