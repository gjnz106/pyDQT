"""
Column Split

Divide columns
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Column Split!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
