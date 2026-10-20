"""Week 04 application package."""

from .api import router
from .services import (
    AIService,
    Classifier,
    KeywordClassifier,
    MLClassifier,
    RuleClassifier,
)

__all__ = [
    "router",
    "AIService",
    "Classifier",
    "KeywordClassifier",
    "MLClassifier",
    "RuleClassifier",
]
