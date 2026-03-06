"""
Health Check

Detect model issues
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Health Check!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
