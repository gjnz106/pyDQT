"""
Smart Delete

Safe element removal
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Smart Delete!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
