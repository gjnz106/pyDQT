"""
Parameter Manager

Parameter utilities
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Parameter Manager!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
