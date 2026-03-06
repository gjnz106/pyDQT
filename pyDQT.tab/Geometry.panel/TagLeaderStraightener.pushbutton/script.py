"""
Tag Leader Straightener

Format orthogonal leaders
"""

from pyrevit import revit, forms

try:
    # Your code here
    forms.alert("Welcome to Tag Leader Straightener!")
    
except Exception as e:
    forms.alert(f"Error: {str(e)}")
