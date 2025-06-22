from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
import sys

db = SQLAlchemy()

class User(db.Model):
    _tablename_ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    is_active = Column(Boolean(), nullable=False)

    favorites = relationship("Favorite", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
        }

class Character(db.Model):
    _tablename_ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    gender = Column(String(20))
    species = Column(String(50))

    favorites = relationship("Favorite", back_populates="character")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "species": self.species,
        }

class Planet(db.Model):
    _tablename_ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(50))
    population = Column(String(50))

    favorites = relationship("Favorite", back_populates="planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
        }

class Favorite(db.Model):
    _tablename_ = "favorite"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    character_id = Column(Integer, ForeignKey("character.id"), nullable=True)
    planet_id = Column(Integer, ForeignKey("planet.id"), nullable=True)

    user = relationship("User", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }

# 👇 ESTA PARTE GENERA EL DIAGRAMA AUTOMÁTICAMENTE CUANDO SE LLAMA EL SCRIPT
try:
    from eralchemy2 import render_er
    render_er(db.Model, 'diagram.png')
    print("✅ Diagrama generado correctamente como 'diagram.png'")
except Exception as e:
    print("❌ Error al generar el diagrama:")
    print(e)
    sys.exit(1)
