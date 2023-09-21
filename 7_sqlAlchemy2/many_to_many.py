from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base,relationship

# Relationships 
#initialize with decrative base
    #Properties

    # session.add_all([nmeal,ning,r])
    # session.commit()