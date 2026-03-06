"""
Quick Element

Fast element selection
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Quick Element!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
