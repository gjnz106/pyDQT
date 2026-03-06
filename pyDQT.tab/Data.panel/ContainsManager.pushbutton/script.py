"""
Contains Manager

Find elements in rooms/areas/spaces
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Contains Manager!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
