# Friday AI Assistant

A local AI assistant with voice capabilities and MacOS integration, designed for privacy and learning.

## Features (Phase 1)

- Voice-based interaction using OpenAI's Whisper for speech recognition
- MacOS system integration for controlling applications and system functions
- Local language model integration via Ollama (Llama 3.1 8B)
- RAG (Retrieval-Augmented Generation) system using ChromaDB and LangChain
- All data stored locally for privacy

## Prerequisites

- MacOS system (developed on MacBook Pro with M3 chip)
- Conda package manager
- Ollama installed locally

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/friday.git
cd friday

# Create and activate the Conda environment
conda env create -f environment.yml
conda activate friday

# Install the package in development mode
pip install -e .
```
