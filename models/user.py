#!/usr/bin/python3
"""
User Class (inherits from BaseModel)
Author: Mire
"""
from models.base_model import BaseModel

class User(BaseModel):
    email = ''
    password = ''
    first_name = ''
    last_name = ''
