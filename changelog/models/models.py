from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class SiteModel(Base):
    __tablename__ = 'Sites'
    id = Column(Integer, primary_key=True)
    Name = Column(Text)
    
    def __init__(self, name):
        self.Name = name

class SystemModel(Base):
    __tablename__ = 'Systems'
    id = Column(Integer, primary_key=True)
    Name = Column(Text)

    def __init__(self, name):
        self.Name = name

class UserModel(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    email = Column(Text)

class TagModel(Base):
    __tablename__ = 'Tags'
    id = Column(Integer, primary_key=True)
    Name = Column(Text)

    def __init__(self, name):
        self.Name=name

class TagAssociationModel(Base):
    __tablename__ = 'TagAssociation'
    id = Column(Integer, primary_key=True)
    Entry = Column(Integer, ForeignKey("ChangelogEntry.id"))
    Tag = Column(Integer, ForeignKey("Tags.id"))

    def __init__(self, entry, tag):
        self.Entry = entry
        self.Tag = tag

class SystemAssociationModel(Base):
    __tablename__ = 'SystemAssociation'
    id = Column(Integer, primary_key=True)
    Entry = Column(Integer, ForeignKey("ChangelogEntry.id"))
    System = Column(Integer,ForeignKey("Systems.id"))

    def __init__(self, entry, system):
        self.Entry = entry
        self.System = system

class SiteAssociationModel(Base):
    __tablename__ = 'SiteAssociation'
    id = Column(Integer, primary_key=True)
    Entry = Column(Integer, ForeignKey("ChangelogEntry.id"))
    Site = Column(Integer,ForeignKey("Sites.id"))

    def __init__(self, entry, site):
        self.Entry = entry
        self.Site = site


class ChangeLogEntryModel(Base):
    __tablename__ = 'ChangelogEntry'
    id = Column(Integer, primary_key=True)
    ParentList = Column(Integer, ForeignKey("ChangeLogLists.id"))
    User = Column(Integer, ForeignKey("Users.id"))
    DateCreated = Column(DateTime)
    DateEdited = Column(DateTime)
    Change = Column(Text)

    def __init__(self, user, system, site, create, edit, change):
        self.User = user
        self.DateCreated = create
        self.DateEdited = edit
        self.Change = change


class ChangeLogListModel(Base):
    __tablename__ = 'ChangeLogLists'
    id = Column(Integer, primary_key=True)
    Name = Column(Text)
    User = Column(Integer, ForeignKey("Users.id"))

    def __init__(self, name, user):
        self.User=user
        self.Name=name


