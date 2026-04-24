
---

## ⚙️ Setup

```bash
git clone https://github.com/yourusername/fingpt-pro.git
cd fingpt-pro

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
streamlit run app/streamlit_app.py
pytest
docker-compose up --build

---

# 2. 📄 `.env.example`

```env
OPENAI_API_KEY=
GOOGLE_API_KEY=
ANTHROPIC_API_KEY=

LANGSMITH_API_KEY=
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=fintech-agent
