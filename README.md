# Recommendation-System-with-Weaviate-Vector-Database

This project is a book recommendation service that suggests books based on a user's inputted genre and book titles. It utilizes a database of 7000 books retrieved from Kaggle. By leveraging **Ada v2** as the large language model, vector embeddings are generated to enable quick vector searches for semantically similar books through natural language input.

---

## 📑 Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data Source](#data-source)
5. [Tech Stack](#tech-stack)
6. [Contributing](#contributing)
7. [License](#license)

---

## 💫 Features
- Input genre and book titles to get book recommendations.
- Vector Search using a **Weaviate Vector Database** with a dataset of 7000 books.
- **Jupyter Notebook workflow** to generate and store vector embeddings in Weaviate.
- Integration with **Ollama** or **OpenAI** for vector generation and inference.

---

## 🛠 Installation

To run the project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/weaviate/BookRecs.git
cd BookRecs
