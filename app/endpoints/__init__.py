# app/endpoints/__init__.py

from .base import router as base_router
from .data_search import router as data_search_router
from .faq import router as faq_router
from .transcribe import router as transcribe_router
from .qa import router as qa_router
from .chatbot import router as chatbot_router
from .ingest import router as ingest_router
from .data_delete import router as data_delete_router

__all__ = [
    "base_router", 
    "qa_router", 
    "data_search_router", 
    "faq_router", 
    "transcribe_router", 
    "chatbot_router", 
    "ingest_router",
    "data_delete_router"
    ]
