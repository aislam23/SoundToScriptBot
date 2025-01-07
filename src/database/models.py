from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, BigInteger
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    is_subscribed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_activity = Column(DateTime, default=datetime.utcnow)
    referrer_id = Column(BigInteger, ForeignKey('users.id'), nullable=True)
    
    # Отношения
    referrals = relationship('User', backref='referrer', remote_side=[id])
    voice_messages = relationship('VoiceMessage', back_populates='user')
    
    def __repr__(self):
        return f"<User {self.id}>"

class VoiceMessage(Base):
    __tablename__ = 'voice_messages'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    file_id = Column(String, nullable=False)
    duration = Column(Integer)  # в секундах
    text_result = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Отношения
    user = relationship('User', back_populates='voice_messages')
    
    def __repr__(self):
        return f"<VoiceMessage {self.id}>" 