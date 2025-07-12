# NLP Techniques Explorer

A comprehensive repository exploring various Natural Language Processing (NLP) approaches and techniques, from traditional methods to modern deep learning implementations.

## 🎯 Project Overview

This repository serves as a practical exploration of diverse NLP methodologies, demonstrating both classical and state-of-the-art techniques for text processing, analysis, and understanding. Each implementation includes detailed explanations, code examples, and use cases.


## ✨ Features

- **Distance Metrics**: Pairwise distance calculations for text similarity
- **Dimensionality Reduction**: TF-IDF with t-SNE visualization
- **Linguistic Analysis**: Sentiment analysis using POS tagging and NER
- **Text Generation**: Natural language generation with SimpleNLG
- **Text Preprocessing**: Automated spelling correction implementations
- **Multi-task Processing**: Comprehensive TextBlob applications
- **Deep Learning**: Bidirectional LSTM and CNN implementations
- **Sequence Labeling**: Conditional Random Fields (CRF) for structured prediction

## 🚀 Installation

### Prerequisites

- Python 3.7+
- pip package manager
- Git

### Setup

1. Clone the repository:
```bash
git clone https://github.com/madhur02/nlp-techniques-explorer.git
cd nlp-techniques-explorer
```

2. Create a virtual environment:
```bash
python -m venv nlp_env
source nlp_env/bin/activate  # On Windows: nlp_env\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Download necessary NLTK data:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
```


## 🔍 Techniques Explored

### 1. Pairwise Distance Analysis
- **File**: `src/pairwise_distances.py`
- **Description**: Implementation of various distance metrics (Euclidean, Cosine, Jaccard) for text similarity analysis
- **Use Cases**: Document clustering, duplicate detection, recommendation systems

### 2. TF-IDF with t-SNE Visualization
- **File**: `src/tfidf_tsne.py`
- **Description**: Term Frequency-Inverse Document Frequency vectorization combined with t-SNE for dimensionality reduction and visualization
- **Use Cases**: Document visualization, topic discovery, corpus exploration

### 3. Sentiment Analysis with POS and NER
- **File**: `src/sentiment_pos_ner.py`
- **Description**: Advanced sentiment analysis incorporating Part-of-Speech tagging and Named Entity Recognition
- **Use Cases**: Social media monitoring, product review analysis, opinion mining

### 4. Natural Language Generation (SimpleNLG)
- **File**: `src/nlg_simplenlg.py`
- **Description**: Text generation using SimpleNLG realizer for creating natural language from structured data
- **Use Cases**: Report generation, chatbot responses, automated content creation

### 5. Automated Spelling Correction
- **File**: `src/spell_correction.py`
- **Description**: Multiple approaches to spelling correction including edit distance, phonetic matching, and statistical methods
- **Use Cases**: Text preprocessing, search query correction, user input validation

### 6. TextBlob Multi-task Processing
- **File**: `src/textblob_tasks.py`
- **Description**: Comprehensive TextBlob usage for:
  - Part-of-speech tagging
  - Noun phrase extraction
  - Sentiment analysis
  - Text classification
  - Language translation
- **Use Cases**: Quick NLP prototyping, multilingual text processing

### 7. Bidirectional LSTM Implementation
- **File**: `notebooks/Bidirectional_LSTM.ipynb`
- **Description**: Deep learning approach using bidirectional LSTM networks for sequence modeling
- **Use Cases**: Text classification, sequence labeling, language modeling

### 8. Convolutional Neural Networks
- **File**: `notebooks/Convolutional_Neural_Network.ipynb`
- **Description**: CNN architectures for text classification and feature extraction
- **Use Cases**: Document classification, sentiment analysis, text categorization

### 9. Conditional Random Fields (CRF)
- **File**: `src/crf_implementation.py`
- **Description**: CRF implementation for structured prediction tasks
- **Use Cases**: Named entity recognition, part-of-speech tagging, sequence labeling

## 📁 Repository Structure

```
nlp-techniques-explorer/
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── pairwise_distances.py
│   ├── tfidf_tsne.py
│   ├── sentiment_pos_ner.py
│   ├── nlg_simplenlg.py
│   ├── spell_correction.py
│   ├── textblob_tasks.py
│   ├── crf_implementation.py
│   └── utils/
│       ├── __init__.py
│       ├── data_loader.py
│       └── preprocessing.py
├── notebooks/
│   ├── Bidirectional_LSTM.ipynb
│   ├── Convolutional_Neural_Network.ipynb
│   └── exploratory_analysis.ipynb
├── data/
│   ├── sample_texts/
│   └── datasets/
├── tests/
│   ├── __init__.py
│   └── test_techniques.py
└── docs/
    ├── installation_guide.md
    └── technique_comparisons.md
```



## 🎓 Learning Objectives

By exploring this repository, you will gain hands-on experience with:

- Traditional NLP techniques and their modern applications
- Distance metrics and similarity measures for text analysis
- Dimensionality reduction and visualization techniques
- Deep learning approaches for NLP tasks
- Sequence modeling and structured prediction
- Text preprocessing and normalization methods
- Multi-task learning in NLP contexts

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


**Happy NLP Exploring!** 🚀📚
