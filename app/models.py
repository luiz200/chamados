from datetime import datetime
import pytz
from typing import Optional
from sqlalchemy import CheckConstraint
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from enum import Enum
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# def agora_brasil():
#     return datetime.now(pytz.timezone("America/Sao_Paulo"))

#-----Cadastro de Usuário:-----#
class Cargo(str, Enum):

    ANALISTA = 'Analista'
    ASSISTENTE = 'Assistente'
    COORDENADOR = 'Coordenador'
    DIRETOR = 'Diretor'
    ESPECIALISTA = 'Especialista'
    ESTAGIARIO = 'Estagiário'
    GERENTE = 'Gerente'

    def __str__(self):
        return self.value

class Departamento(str, Enum):

    COMERCIAL = 'Comercial'
    DIRETORIA = 'Diretoria'
    EXPEDICAO = 'Expedição'
    EXTERNO = 'Externo'
    FINANCEIRO = 'Financeiro'
    MKT = 'MKT'
    MONITORAMENTO = 'Monitoramento'
    RH = 'R.H'
    TELEVENDAS = 'Televendas'
    TI = 'T.I'

    def __str__(self):
        return self.value

class Cidade(str, Enum):

    BAYEUX = 'Bayeux'
    MOSSORO = 'Mossóro'
    NATAL = 'Natal'
    PATOS = 'Patos'
    PUREZA = 'Pureza'
    SJM = 'São José do Mipibú'

    def __str__(self):
        return self.value

class Unidade(str, Enum):

    EXTREMA = 'Extrema'
    FAALPB = 'Faal PB'
    FAALRN = 'Faal RN'
    LAAFPB = 'Laaf PB'
    LAAFRN = 'Laaf RN'
    POSTAOALTO = 'Postão Alto'
    POSTAOABOLICAO = 'Postão Abolição'
    POSTAOAV2 = 'Postão Av02'
    POSTAOBR = 'Postão BR'
    POSTAOBV = 'Postão Barro Vermelho'
    POSTAOMATRIZ = 'Postão Matriz'
    POSTAOPATOS = 'Postão Patos'
    POSTAOPRUDENTE = 'Postão Prudente'
    POSTAOSJM = 'Postão SJM'
    SABA = 'SABA'

    def __str__(self):
        return self.value
    
class Estado(str, Enum):

    PB = 'Paraíba'
    RN = 'Rio Grande do Norte'

    def __str__(self):
        return self.value

class User(UserMixin, db.Model):

    __tablename__ = 'user'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    cargo: so.Mapped[Cargo] = so.mapped_column(sa.Enum(Cargo))
    cidade: so.Mapped[Cidade] = so.mapped_column(sa.Enum(Cidade))
    uf: so.Mapped[Estado] = so.mapped_column(sa.Enum(Estado))
    unidade: so.Mapped[Unidade] = so.mapped_column(sa.Enum(Unidade))
    departamento: so.Mapped[Departamento] = so.mapped_column(sa.Enum(Departamento))
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
#-----Fim do Cadastro de Usuário-----#

#-----Abertura de OS:-----#

class Status(str, Enum):

    ABERTO = 'Chamado Aberto'
    INICIADO = 'Chamado Iniciado'
    CONCLUIDO = 'Chamado Concluído'

    def __str__(self):
        return self.value

class Categoria(str, Enum):

    HARDWARE = 'Hardware'
    SOFTWARE = 'Software'
    REDES = 'Redes'
    SERVIDORES = 'Servidores'
    APLICACOES = 'Aplicações Corporativa'
    TELEFONIA = 'Telefonia'

    def __str__(self):
        return self.value

class SubCategoria(str, Enum):

    PC = 'pc'
    NOTE = 'Notebook'
    OFFICE = 'Office'
    SISTEMA = 'Sistema Operacional'
    EMAIL = 'Email'
    
    
class Chamados(db.Model):

    __tablename__ = 'chamados'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    data_abertura: so.Mapped[sa.DateTime] = so.mapped_column(sa.DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone("America/Sao_Paulo")))
    data_inicio_atendimento: so.Mapped[sa.DateTime] = so.mapped_column(sa.DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone("America/Sao_Paulo")))
    data_conclusao: so.Mapped[sa.DateTime] = so.mapped_column(sa.DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone("America/Sao_Paulo")))
    id_solicitante: so.Mapped[int] = so.mapped_column(sa.ForeignKey('user.id'), nullable=False)
