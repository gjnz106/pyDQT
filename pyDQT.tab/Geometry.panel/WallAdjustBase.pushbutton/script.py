"""
Wall Adjust Base

Adjust wall base
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Wall Adjust Base!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
