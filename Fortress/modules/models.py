#_*_coding:utf-8*_
#Author:Fiona

from sqlalchemy import create_engine,Table,Column,Integer,String,ForeignKey,DateTime,UnicodeText,UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType,PasswordType


Base = declarative_base()       #生成orm基类

BindHost_Group = Table("BindHost_Group",Base.metadata,
                       Column('bindhost_id',ForeignKey('bind_host.id'),primary_key=True),
                       Column('group_id',ForeignKey('group.id'),primary_key=True),
                       )

BindHost_UserProfile =  Table("BindHost_UserProfile",Base.metadata,
                              Column('bindhost_id',ForeignKey('bind_host.id'),primary_key=True),
                              Column('userprofile_id',ForeignKey('user_profile.id'),primary_key=True),
                              )

Group_UserProfile = Table("Group_UserProfile",Base.metadata,
                          Column('group_id',ForeignKey('group.id'),primary_key=True),
                          Column('userprofile',ForeignKey('user_profile.id'),primary_key=True),
                          )

class UserProfile(Base):
    __tablename__ = "user_profile"
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(32),unique=True,nullable=False)
    password = Column(String(128),unique=True,nullable=False)
    groups = relationship('Group',secondary=Group_UserProfile)
    bind_hosts = relationship('BindHost',secondary=BindHost_UserProfile)
    audit_logs = relationship('AuditLog')

    def __repr__(self):
        return "<UserProfile(id='%s',username='%s')>" % (self.id,self.username)

class RemoteUser(Base):
    __tablename__ = 'remote_user'
    AuthTypes = [
        (u'ssh-passwd',u'SSH/Password'),
        (u'ssh-key',u'SSH/KEY'),
    ]
    id = Column(Integer,primary_key=True,autoincrement=True)
    auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(64),nullable=False)
    password = Column(String(255),nullable=False)

    _table_args_ = (UniqueConstraint('auth_type','username','password',name = '_user_passwd_uc'),)

    def __repr__(self):
        return "<RemoteUser(id='%s',auth_type='%s',username='%s')>" % (self.id,self.auth_type,self.username)

class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(128),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)

    def __repr__(self):
        return "<Host(id='%s',hostname='%s')>" % (self.id,self.hostname)

class Group(Base):
    __tablename__ = 'group'
    id =  Column(Integer,primary_key=True)
    name = Column(String(64),unique=True,nullable=False)

    bind_hosts = relationship("BindHost",secondary=BindHost_Group,back_populates='groups')
    user_profiles = relationship("UserProfile",secondary=Group_UserProfile)

    def __repr__(self):
        return "<HostGroup(id='%s',name='%s')>" % (self.id,self.name)

class BindHost(Base):
    '''Bind host with different remote user,
       eg. 192.168.1.1 mysql passAbc123
       eg. 10.5.1.6    mysql pass532Dr!
       eg. 10.5.1.8    mysql pass532Dr!
       eg. 192.168.1.1 root
    '''
    __tablename__ = 'bind_host'
    id = Column(Integer,primary_key=True,autoincrement=True)
    host_id = Column(Integer,ForeignKey('host.id'))
    remoteuser_id = Column(Integer,ForeignKey('remote_user.id'))

    host = relationship('Host')
    remoteuser = relationship('RemoteUser')
    groups = relationship('Group',secondary=BindHost_Group,back_populates='bind_hosts')
    audit_logs = relationship('AuditLog')

    __table_args__ = (UniqueConstraint('host_id', 'remoteuser_id', name='_bindhost_and_user_uc'),)

    def __repr__(self):
        return "<BindHost(id='%s',hostname='%s',username='%s')>" % (self.id,self.host.hostname,self.remoteuser.username)

class AuditLog(Base):
    __tablename__ = 'audit_log'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user_profile.id'))
    bind_host_id = Column(Integer,ForeignKey('bind_host.id'))
    action_choices = [
        (0,'CMD'),
        (1,'Login'),
        (2,'Logout'),
        (3,'GetFile'),
        (4,'SendFile'),
        (5,'Exception'),
    ]
    action_choices2 = [
        (u'cmd',u'CMD'),
        (u'login',u'Login'),
        (u'logout',u'Logout'),
        (u'getfile',u'GetFile'),
        (u'sendfile',u'SendFile'),
        (u'exception',u'Exception'),
    ]
    action_type = Column(ChoiceType(action_choices2))
    cmd = Column(String(255))
    date = Column(DateTime)

    user_profile = relationship("UserProfile")
    bind_host = relationship("BindHost")

