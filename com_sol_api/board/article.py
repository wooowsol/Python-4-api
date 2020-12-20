from com_sba_api.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine

class Article(Base):
    __tablename__ = "articles"
    __table_args__={'mysql_collate':'utf8_general_ci'}

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("user.id"))
    item = Column(Integer, ForeignKey("item.id"))
    title = Column(String)
    content = Column(String)