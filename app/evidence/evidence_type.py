from enum import Enum


class EvidenceType(Enum):
    EMAIL = "email"
    WHATSAPP = "whatsapp"
    TEXT_MESSAGE = "text_message"
    PDF = "pdf"
    IMAGE = "image"
    WORD_DOCUMENT = "word_document"
    ATTACHMENT = "attachment"
    COURT_DOCUMENT = "court_document"
    CALENDAR_EVENT = "calendar_event"
    CONVERSATION = "conversation"