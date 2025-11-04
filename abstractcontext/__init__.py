"""
AbstractContext: Redefining Active Token Memory for GenAI

A revolutionary approach to managing context and memory in generative AI systems,
focusing on intelligent token allocation, dynamic context management, and 
efficient memory utilization patterns.

This package provides foundational abstractions and implementations for:
- Dynamic context window management
- Intelligent token prioritization
- Memory-efficient context compression
- Adaptive attention mechanisms
- Context-aware token allocation strategies
"""

__version__ = "0.1.0"
__author__ = "Laurent-Philippe Albou"
__email__ = "contact@abstractcore.ai"
__organization__ = "AbstractCore.ai"

# Core module exports will be added as the package develops
__all__ = [
    "__version__",
]


class AbstractContextError(Exception):
    """Base exception class for AbstractContext package."""
    pass


class ContextMemoryError(AbstractContextError):
    """Raised when context memory operations fail."""
    pass


class TokenAllocationError(AbstractContextError):
    """Raised when token allocation strategies fail."""
    pass


# Placeholder for future core functionality
def get_version() -> str:
    """Return the current version of AbstractContext."""
    return __version__


# Future core components will include:
# - ContextManager: Dynamic context window management
# - TokenAllocator: Intelligent token distribution strategies  
# - MemoryCompressor: Efficient context compression algorithms
# - AttentionOptimizer: Adaptive attention mechanism controllers
# - ContextAnalyzer: Context quality and relevance assessment tools
