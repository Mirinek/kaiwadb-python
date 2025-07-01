from __future__ import annotations

from typing import Any, ClassVar

from pydantic import BaseModel
from pydantic import Field as PydanticField


class Document(BaseModel):
    """
    Base class for defining database document schemas in KaiwaDB.

    The Document class enables developers to define clean, readable Python schemas
    that automatically map to database collections/tables with different naming
    conventions. This mapping is handled transparently by the Field() function.

    Class Variables:
        __collection__: MongoDB collection name for this document type
        __table__: SQL table name for this document type (alternative to __collection__)
        __description__: Human-readable description of what this document represents

    Example:
        class User(Document):
            __collection__ = "users"
            __description__ = "Registered platform users"

            user_id: int = Field(..., db_name="id")
            full_name: str = Field(..., db_name="name")

        This creates a clean Python interface while mapping to existing database
        schema where the fields are named "id" and "name".
    """

    __collection__: ClassVar[str] | None = None
    __table__: ClassVar[str] | None = None
    __description__: ClassVar[str] | None = None


def Field(
    default: Any = ...,
    db_name: str | None = None,
    description: str | None = None,
    examples: list[Any] | None = None,
    relation: None | tuple[Document, str] | list[tuple[Document, str]] = None,
):
    """
    Enhanced field definition function for KaiwaDB documents.

    Field() extends Pydantic's Field functionality with database-specific features
    including field name aliasing, relationship definitions, and enhanced metadata
    for natural language query generation.

    The primary purpose is to enable clean, intuitive Python field names while
    maintaining compatibility with existing database schemas through the db_name
    parameter. This allows developers to use readable names like 'first_name'
    while mapping to database fields like 'firstName' or 'fname' or even 'column_4'.

    Args:
        default: Default value for the field. Use ... for required fields,
                or provide a specific default value.
        db_name: The actual field/column name in the database. If None,
                uses the Python field name. This is the key feature that
                enables field name aliasing.
        description: Human-readable description of what this field represents.
                    Used by the natural language query generator to better
                    understand field semantics.
        examples: List of example values for this field. Currently not
                 implemented but reserved for future query optimization.
        relation: Relationship definition to other documents. Currently not implemented.

    Returns:
        PydanticField: A Pydantic field with KaiwaDB-specific metadata.

    Raises:
        NotImplementedError: If examples or relation parameters are provided,
                           as these features are not yet implemented.

    Example:
        class Customer(Document):
            # Maps Python 'customer_id' to database 'id' field
            customer_id: int = Field(..., db_name="id",
                                   description="Unique customer identifier")

            # Maps Python 'full_name' to database 'customerName' field
            full_name: str = Field(..., db_name="customerName",
                                 description="Customer's complete name")

            # Uses Python field name 'email' as-is in database
            email: str = Field(..., description="Customer email address")

        This enables natural queries like "Find customers by full name"
        while working with a database that uses 'customerName' as the actual
        column name.
    """
    if examples is not None:
        raise NotImplementedError("Field examples are not yet implemented")
    if relation is not None:
        raise NotImplementedError("Field relations are not yet implemented")

    return PydanticField(default=default, alias=db_name, description=description)
