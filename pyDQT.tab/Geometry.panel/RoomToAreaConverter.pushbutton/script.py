"""
Room to Area Converter

Convert rooms to areas
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Room to Area Converter!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
