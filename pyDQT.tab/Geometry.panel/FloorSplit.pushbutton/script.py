"""
Floor Split

Divide floors
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Floor Split!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
