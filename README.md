# Finding Similar Songs using Locality-Sensitive Hashing 🎵

A Flask web application that analyzes music similarity using MFCC (Mel-Frequency Cepstral Coefficients) features and Locality-Sensitive Hashing (LSH) techniques.

## 🌟 Features

- **Audio Analysis**: Extract MFCC features from music files
- **Similarity Detection**: Find approximate nearest neighbors using LSH
- **Web Interface**: Simple Flask-based UI for file upload and analysis
- **Similarity Threshold**: Returns matches with Jaccard similarity > 0.5

## 🚀 Getting Started

### Prerequisites

- Python 3
- pip package manager
- Git (for cloning the repository)

### Required Libraries

- Flask: Web application framework
- Pandas: Data manipulation
- NumPy: Numerical computations
- LibROSA: Audio processing
- DataSketch: LSH implementation

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/talalmuzaffar/Finding-Similar-Songs-using-Locality-Sensitive-Hashing.git
   cd Finding-Similar-Songs-using-Locality-Sensitive-Hashing
   ```

2. Install required dependencies:
   ```bash
   pip install flask pandas numpy librosa datasketch
   ```

3. Run the application:
   ```bash
   python3 app.py
   ```

## 💡 Usage

1. Start the Flask application
2. Access the web interface at http://localhost:5000
3. Use the "Choose File" button to select a music file
4. Click "Analyse" to process the file
5. View the list of similar songs based on MFCC features

## 📁 Project Structure

```
Finding-Similar-Songs-using-Locality-Sensitive-Hashing/
├── app.py          # Flask application and core logic
└── README.md       # Project documentation
```

## 👥 Authors

- Talal Muzaffar - [GitHub](https://github.com/talalmuzaffar)
- Faizan Ahmad
- Muhammad Farhan

## 📞 Support

For issues and questions, please [open an issue](https://github.com/talalmuzaffar/Finding-Similar-Songs-using-Locality-Sensitive-Hashing/issues) on GitHub.
