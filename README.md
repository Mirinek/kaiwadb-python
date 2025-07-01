# KaiwaDB

**Natural Language Database Queries for AI Applications**

KaiwaDB enables AI chatbots and applications to query databases using natural language. Build intelligent data interfaces that understand user questions and translate them into proper database queries, regardless of your schema complexity.

🔒 **Privacy-First**: Your data never leaves your infrastructure. KaiwaDB only processes schema definitions to generate queries.

## 🚀 Quick Start

```python
from kaiwadb import Document, Field, KaiwaDB, engine
import datetime as dt

# Define your database schema for AI understanding
class Customer(Document):
    __collection__ = "customers"

    customer_id: int = Field(..., db_name="id")
    full_name: str = Field(..., db_name="customerName")
    email_address: str = Field(..., db_name="email")
    registration_date: dt.datetime = Field(..., db_name="createdAt")
    total_spent: float = Field(0.0, db_name="totalSpent")

# Initialize KaiwaDB
kdb = KaiwaDB(
    identifier="ecommerce",
    documents=[Customer],
    engine=engine.PostgreSQL(version=15),
    api_key="your-api-key"
)

# AI chatbot can now understand user questions
user_question = "Show me customers who signed up recently and spent a lot"
results = kdb.run(user_question, database_connection)
```

## 🎯 Key Features

### **🤖 AI Chatbot Integration**
Build intelligent chatbots that can answer database questions:

```python
# User asks in natural language
user_input = "What are our best selling products this month?"
results = kdb.run(user_input, db)

# Or more complex questions
user_input = "Show me customers from California who haven't ordered in 3 months"
results = kdb.run(user_input, db)

# AI understands context and relationships
user_input = "Average order value for premium customers in Q4"
results = kdb.run(user_input, db)
```

### **🔧 Multi-Database Support**
Works across different database engines for any AI application:

- **MongoDB** - Document queries with aggregation pipelines
- **PostgreSQL/MySQL** - Advanced SQL generation
- **SQLite** - Development and prototyping
- **MSSQL/Oracle** - Enterprise systems

### **🏷️ Legacy Schema Compatibility**
The key advantage for real-world AI applications - works with any existing database:

```python
# Modern, well-designed schemas work perfectly
full_name: str = Field(..., db_name="customerName")
order_date: dt.datetime = Field(..., db_name="createdAt")

# Legacy schemas with cryptic names? No problem for AI
customer_id: int = Field(..., db_name="cust_id_pk")
registration_date: dt.datetime = Field(..., db_name="reg_dt_tm")
total_spent: float = Field(..., db_name="tot_amt_spent_usd")
order_status: str = Field(..., db_name="stat_cd")
```

**Why This Matters for AI**: Most AI systems fail when encountering cryptic database fields like `tbl_ord_mst`, `amt_tot`, or `stat_cd`, or using numbers as roles (e.g., 1 → "admin", 2 → "manager", etc.). KaiwaDB's mapping layer ensures your AI chatbot understands user questions regardless of how poorly your database was originally designed.

### **🛡️ Type Safety & Context**
Provides AI with proper context for accurate query generation:

```python
class Order(Document):
    __table__ = "ord_mst_tbl"  # Legacy table name

    order_id: int = Field(..., db_name="ord_id_pk")
    customer_reference: int = Field(..., db_name="cust_fk_ref")
    order_total: float = Field(..., db_name="amt_tot")
    order_status: str = Field(..., db_name="stat_cd")
    created_date: dt.datetime = Field(..., db_name="cr_dt_tm")

# AI now understands what each field represents for user queries
```

## 📦 Installation

```bash
pip install kaiwadb
```

## 🏗️ Usage Examples

### Basic Schema Mapping

```python
from kaiwadb import Document, Field, KaiwaDB, engine

class Product(Document):
    __collection__ = "products"

    id: str
    name: str
    price: float
    quantity: int
    category_name: str

kdb = KaiwaDB(
    identifier="inventory",
    documents=[Product],
    engine=engine.Mongo(version=6),
    api_key="your-api-key"
)

# Natural language queries
low_stock = kdb.run("Find products with stock quantity less than 10", db)
top_products = kdb.run("Show top 5 products by unit price in Electronics category", db)
```

### Legacy Schema with Enum Mapping

```python
from enum import Enum

class UserRole(Enum):
    """Maps meaningful roles to database integers"""
    CUSTOMER = 1
    ADMIN = 2
    MODERATOR = 3
    SUPPORT = 9

class User(Document):
    __table__ = "usr_mst_tbl"  # Legacy table name

    # AI understands ←→ Database stores
    user_id: int = Field(..., db_name="usr_id_pk")
    full_name: str = Field(..., db_name="nm_full_txt")
    email_address: str = Field(..., db_name="email_addr")
    user_role: UserRole = Field(..., db_name="role_type")  # Maps to integer
    account_status: str = Field(..., db_name="stat_cd")
    registration_date: dt.datetime = Field(..., db_name="reg_dt_tm")

# AI processes meaningful terms → Generates queries with correct mappings
admin_users = kdb.run("Find all admin users", db)
# Understands "admin users" → WHERE role_type = 2

recent_customers = kdb.run("Show customers who registered this month", db)
# Understands "customers" → WHERE role_type = 1

# Enum mapping handles the complexity automatically
# No need for AI to figure out that admin = 2, customer = 1, etc.
```

## 🔧 Configuration

```bash
export KAIWADB_API_KEY="your-api-key-here"
```

```python
kdb = KaiwaDB(
    identifier="customer_service_bot",
    documents=[Customer, Order, Product],
    engine=engine.PostgreSQL(version=15),
    description="Customer service database with legacy schema",
    verbose=True
)
```

## 🛡️ Privacy & Security

Perfect for AI applications with sensitive data:

```python
# KaiwaDB only processes schema mappings for query generation
# Your actual customer data, orders, etc. never leave your infrastructure
# AI gets the context it needs without exposing sensitive information

results = kdb.run("Find VIP customers", your_secure_database)
# ↑ Query understanding via API
# ↓ Data access stays local
```

## 🆘 Support

- **Documentation**: [docs.kaiwadb.com](https://docs.kaiwadb.com)
- **Issues**: [GitHub Issues](https://github.com/kaiwadb/kaiwadb-python/issues)
- **Email**: support@kaiwadb.com

---

**Build AI applications that understand your database, no matter how it's designed.** 🚀
