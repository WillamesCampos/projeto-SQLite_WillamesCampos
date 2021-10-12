from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)

    def __repr__(self):
        return f'ID: {self.id} Nome:{self.nome} '


class Endereco(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key=True)
    nome_rua = Column(String(100))
    bairro = Column(String(100))
    cep = Column(String(20))
    id_pessoa = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship(Pessoa)


engine = create_engine('sqlite:///banco_sql_alchemy.db')

if __name__ == '__main__':
    Base().metadata.create_all(engine)
    pessoa = Pessoa(id=1234, nome='Will')
    print(pessoa)

    Session = sessionmaker(bind=engine)

    session = Session()
    session.add(pessoa)
    session.commit()
