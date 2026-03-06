"""
IFC-SG Checker

Validate IFC Submission Grade compliance
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to IFC-SG Checker!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
