from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Define custom naming conventions for constraints
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Initialize SQLAlchemy with custom metadata
db = SQLAlchemy(metadata=metadata)

# Define the Message model
class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)  # Message content
    username = db.Column(db.String, nullable=False)  # User who created the message
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for creation
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Timestamp for updates

    # Serialization rules
    serialize_rules = ('-updated_at',)  # Exclude 'updated_at' from serialized output
