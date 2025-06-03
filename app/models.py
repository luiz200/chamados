from datetime import datetime
from typing import Optional
from sqlalchemy import CheckConstraint
import sqlalchemy.orm as so
from app import db
from enum import Enum
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Cargo(str, Enum):

    ANALISTA = 'Analista'
    ASSISTENTE = 'Assistente'
    COORDENADOR = 'Coordenador'
    DIRETOR = 'Diretor'
    ESPECIALISTA = 'Especialista'
    ESTAGIARIO = 'Estagiário'
    GERENTE = 'Gerente'

class Departamento(str, Enum):

    TI = 'T.I'
    RH = 'R.H'
    MONITORAMENTO = 'Monitoramento'
    


class User(UserMixin, db.Model):

    __tablename__ = 'user'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Chamados(db.Model):

    __tablename__ = 'chamados'