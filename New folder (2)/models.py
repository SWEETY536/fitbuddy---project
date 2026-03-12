from sqlalchemy import Column, Integer, String, Text
from database import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    weight = Column(Integer)
    goal = Column(String)
    intensity = Column(String)
    workout_plan = Column(Text, nullable=True)
    nutrition_tip = Column(Text, nullable=True)