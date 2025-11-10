"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Laundry SaaS Schemas

class Customer(BaseModel):
    """Customers collection schema"""
    name: str = Field(..., description="Customer full name")
    phone: str = Field(..., description="Phone number")
    address: Optional[str] = Field(None, description="Address")

class Order(BaseModel):
    """Orders collection schema"""
    customer_name: str = Field(..., description="Name of the customer")
    phone: str = Field(..., description="Customer phone number")
    address: Optional[str] = Field(None, description="Pickup/Delivery address")
    service_type: str = Field(..., description="Service type e.g., Wash & Fold, Dry Clean")
    weight_kg: float = Field(0.0, ge=0, description="Estimated weight in KG")
    price: Optional[float] = Field(None, ge=0, description="Calculated price in local currency")
    status: str = Field("received", description="Order status: received, washing, drying, ready, delivered")

# Auth schema (collection: "account")
class Account(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Unique email")
    hashed_password: str = Field(..., description="BCrypt hashed password")
    role: str = Field("owner", description="Role: owner, staff, admin")
    is_active: bool = Field(True, description="Active status")
