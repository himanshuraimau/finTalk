# FinTalk - Financial Advisor AI Chatbot

## Overview
FinTalk is an AI-powered financial assistant specialized in providing loan advisory services. It offers personalized financial guidance based on user profiles and can interact through both text and voice inputs in multiple languages.

## Features
- **Multilingual Support**: Communicate in multiple Indian languages including Hindi, Bengali, Tamil, Telugu, and more
- **Voice Interaction**: Speak directly to the chatbot with real-time speech-to-text processing
- **Personalized Financial Profiles**: Create and update your financial profile through the FinCard system
- **Intelligent Loan Advisory**: Get customized loan eligibility assessment, application guidance, and financial literacy tips
- **Audio Responses**: Receive spoken responses for a more accessible experience

## Installation

### Prerequisites
- Python 3.8 or higher
- Virtual environment (recommended)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fintalk.git
   cd fintalk
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv fintalk
   source fintalk/bin/activate  # On Windows: fintalk\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure API keys:
   - Create a `.env` file in the root directory
   - Add the required API keys (see Configuration section)

## Usage

1. Start the application:
   ```bash
   streamlit run home.py
   ```

2. Click "Start Chatting" to begin the conversation

3. Interact via:
   - Text: Type your questions about loans or financial advice
   - Voice: Click the microphone button and speak your queries

4. Update your financial profile using the FinCard form in the sidebar for more personalized advice

## Configuration

Create a `.env` file with the following API keys:
```
API_KEY="your-sarvam-ai-api-key"
GOOGLE_API_KEY="your-google-ai-api-key"
```

## API Services
This application uses the following API services:
- **Google Generative AI** (Gemini): For intelligent chat responses
- **Sarvam AI**: For speech-to-text, text-to-speech, and language translation

## Features in Detail

### Loan Eligibility Assessment
The AI can evaluate your loan eligibility based on:
- Income and expenses
- Credit score
- Existing debt and EMIs
- Employment type and stability

### Loan Application Guidance
Receive step-by-step instructions for loan applications including:
- Required documentation
- Application procedures
- Timeline expectations
- Fee structures

### Financial Literacy
Get practical financial advice on:
- Improving credit scores
- Debt reduction strategies
- Saving techniques
- Budget management

## Dependencies
- streamlit: Web application framework
- google-generativeai: AI response generation
- pydub: Audio processing
- langdetect/langid: Language detection
- requests: API communication
- python-dotenv: Environment variable management
- numpy: Numerical processing
- streamlit-mic-recorder: Voice input recording

## Project Structure
```
fintalk/
├── home.py               # Main entry point
├── pages/
│   └── main.py           # Chat interface and logic
├── finCard_data.json     # User financial profiles
├── requirements.txt      # Dependencies
└── .env                  # API keys and configuration
```

## License
This project is available under the MIT License.
