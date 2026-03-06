"""
Family Manager

Family management
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Family Manager!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
