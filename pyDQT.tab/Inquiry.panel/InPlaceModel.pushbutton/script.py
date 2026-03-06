"""
In-Place Model

Analyze in-place family elements
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to In-Place Model!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
