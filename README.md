# NEXUS - AI Agent Orchestration System

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

> **An intelligent multi-agent orchestration system that separates natural language directives from deterministic execution, combining the flexibility of LLMs with the reliability of Python scripts.**

---

## 🎯 Overview

NEXUS is a three-layer architecture designed to maximize reliability in AI agent systems. It solves the fundamental mismatch between probabilistic LLMs and deterministic business logic by separating concerns across distinct layers: directives, orchestration, and execution.

### Key Innovation

Traditional LLM systems suffer from compounding errors—90% accuracy per step results in only 59% success over 5 steps. NEXUS addresses this by pushing complexity down to deterministic code while keeping LLMs focused on what they do best: decision-making and routing.

---

## ⚠️ IMPORTANT SECURITY NOTICE

> **🔐 This project uses API keys and access tokens. Before uploading to GitHub:**
> 1. ✅ Verify `.gitignore` includes `.env` files
> 2. ✅ Never commit your actual API credentials
> 3. ✅ Use `.env.example` for documentation only (with placeholder values)
> 4. ✅ Run `git status` to ensure `.env` is excluded before pushing
>
> **Your `.env` file with real credentials should NEVER be committed to version control.**

---

## 🏗️ Architecture

### Three-Layer System

```
┌─────────────────────────────────────────────────────┐
│  Layer 1: DIRECTIVES (What to do)                   │
│  • Natural language SOPs in Markdown                │
│  • Define goals, inputs, tools, outputs             │
├─────────────────────────────────────────────────────┤
│  Layer 2: ORCHESTRATOR (Decision Making)            │
│  • Intelligent routing & workflow management        │
│  • Error handling & clarification requests          │
│  • Self-annealing and directive updates             │
├─────────────────────────────────────────────────────┤
│  Layer 3: EXECUTION (Doing It)                      │
│  • Deterministic Python scripts                     │
│  • API calls, data processing, file operations      │
│  • Reliable, testable, fast                         │
└─────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
NEXUS/
├── main.py                    # Entry point - CLI interface
├── orchestrator.py            # Core routing and decision logic
├── requirements.txt           # Python dependencies
├── run_nexus.bat             # Windows startup script
├── .env.example              # Environment variable template
├── GEMINI.md                 # Architecture documentation
├── directives/               # Natural language agent instructions
│   ├── academic_teacher.md
│   ├── ghost_writer.md
│   ├── prompt_engineer.md
│   ├── visual_generator.md
│   ├── ai_editor.md
│   ├── linkedin_agent.md
│   ├── instagram_agent.md
│   └── social_media_scheduler.md
└── execution/                # Deterministic Python tools
    ├── academic_tutor.py
    ├── ghost_writer_tool.py
    ├── visual_generator.py
    ├── ai_editor.py
    ├── social_manager.py
    ├── scheduler.py
    └── utils.py
```

---

## 🔧 How It Works

### 1. User Input
User provides natural language request through CLI interface.

### 2. Intent Classification
The Orchestrator analyzes input and routes to appropriate agent:

| Intent | Keywords | Agent |
|--------|----------|-------|
| `ACADEMIC` | formula, solve, study, paper | Academic Teacher |
| `CREATIVE_WRITING` | write, essay, draft, story | Ghost Writer |
| `VISUAL_GEN` | image, generate, visual, poster | Visual Generator |
| `EDITING` | edit image, change background | AI Editor |
| `SOCIAL_LINKEDIN` | LinkedIn, professional post | LinkedIn Agent |
| `SOCIAL_INSTAGRAM` | Instagram, crochet, shop | Instagram Agent |
| `GENERAL` | Other queries | Direct handling |

### 3. Workflow Execution
The Orchestrator:
1. Reads relevant directive from `/directives/`
2. Calls appropriate execution tool from `/execution/`
3. Handles errors and retries
4. Returns formatted response

### 4. Self-Annealing Loop
When errors occur, NEXUS:
1. Analyzes error and stack trace
2. Fixes the execution script
3. Tests the fix
4. Updates directive with learnings
5. System becomes more robust

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- API keys for services you plan to use

### Step 1: Clone Repository
```bash
git clone <your-repo-url>
cd NEXUS
```

### Step 2: Set Up Virtual Environment
```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies include:**
- `python-dotenv` - Environment variable management
- `requests` - HTTP requests
- `pillow` - Image processing
- `openai` - OpenAI API integration
- `google-generativeai` - Google Gemini API integration

### Step 4: Configure Environment Variables ⚠️

> **🔒 CRITICAL SECURITY WARNING**: Never commit your `.env` file to version control. The `.gitignore` file is configured to protect your credentials, but always verify before pushing to GitHub.

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your **actual API keys** (keep this file private):
   ```env
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   LINKEDIN_ACCESS_TOKEN=AQVxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   INSTAGRAM_ACCESS_TOKEN=IGQxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

3. **Verify `.gitignore` protection**:
   ```bash
   git status
   # Ensure .env is NOT listed in files to be committed
   ```

**Security Checklist:**
- ✅ `.env` file is in `.gitignore`
- ✅ Never share screenshots containing API keys
- ✅ Rotate keys immediately if accidentally exposed
- ✅ Use separate keys for development/production
- ✅ Never hardcode credentials in Python files

### Step 5: Run NEXUS

**Windows (using batch file):**
```bash
run_nexus.bat
```

**Manual launch:**
```bash
python main.py
```

---

## 🚀 Usage Examples

### Starting NEXUS
```
$ python main.py
Welcome to NEXUS (Local Execution Mode)
Type 'exit' to quit.

You: _
```

### Example Interactions

**Academic Help:**
```
You: Solve 5 + 3 * 2
NEXUS: [Calculation result: 11]
```

**Creative Writing:**
```
You: Write a short essay about artificial intelligence
NEXUS: [Generated essay content...]
```

**Visual Generation:**
```
You: Generate an image of a sunset over mountains
NEXUS: [Image generation process initiated...]
```

**Social Media (LinkedIn Chain):**
```
You: Create a LinkedIn post about productivity tips
NEXUS: [Draft created → Post formatted → Scheduled]
```

**Exit:**
```
You: exit
[Session terminated]
```

---

## 🎨 Features

### ✅ Multi-Agent Support
- **Academic Teacher**: Formula solving, concept explanation
- **Ghost Writer**: Essays, stories, creative content
- **Visual Generator**: Image creation using AI APIs
- **AI Editor**: Image editing and manipulation
- **LinkedIn Agent**: Professional content creation
- **Instagram Agent**: Visual social media posts
- **Scheduler**: Content scheduling and automation

### ✅ Intelligent Routing
Keyword-based intent classification with extensibility for LLM-powered routing

### ✅ Self-Healing System
Automatic error detection, script correction, and directive updates

### ✅ Modular Architecture
Easy to add new agents, directives, and execution tools

### ✅ Environment Management
Secure API key storage using `.env` files

### ✅ Logging System
All actions logged to `system.log` for debugging and analysis

---

## 🔍 Key Components Explained

### `main.py`
- Entry point for the application
- Provides CLI interface
- Handles user input/output loop
- Manages graceful shutdown

### `orchestrator.py`
- **Core intelligence** of the system
- Routes requests based on intent classification
- Chains multiple agents for complex workflows
- Implements error handling and recovery

### `directives/`
- Markdown files containing **natural language instructions**
- Define agent goals, inputs, expected outputs
- Living documents that improve over time
- Human-readable SOPs for each agent

### `execution/`
- **Deterministic Python scripts** for reliable execution
- Handle API calls, data processing, file operations
- Testable, fast, and maintainable
- Called by Orchestrator based on directives

### `utils.py`
- Helper functions shared across execution tools
- Directive loading and parsing
- Action logging functionality

---

## 🛡️ Error Handling & Reliability

### Built-in Safety
- Input validation before routing
- Exception catching at multiple levels
- Graceful degradation when services unavailable
- User clarification requests for ambiguous input

### Self-Annealing Process
When errors occur:
1. Error detected and logged
2. Stack trace analyzed
3. Script automatically corrected
4. Fix tested before deployment
5. Directive updated with new learnings

**Result:** System becomes more robust with each error encountered.

---

## 🔐 Security Considerations

### 🔒 Protecting API Credentials (CRITICAL)

**Never Expose Your API Keys:**
- ❌ **NEVER** commit `.env` file to GitHub or any version control
- ❌ **NEVER** hardcode API keys directly in Python files
- ❌ **NEVER** share screenshots containing visible credentials
- ❌ **NEVER** post logs that might contain API keys
- ❌ **NEVER** include `.env` in Docker images or deployments

**Best Practices:**
- ✅ Always use `.gitignore` to exclude `.env` files (already configured)
- ✅ Use environment variables loaded via `python-dotenv`
- ✅ Rotate API keys immediately if accidentally exposed
- ✅ Use separate API keys for development and production
- ✅ Set up API key spending limits on provider platforms
- ✅ Review GitHub commits before pushing: `git diff --cached`

**If You Accidentally Expose Keys:**
1. **Immediately revoke** the exposed keys on provider platforms
2. **Generate new keys** and update your `.env` file
3. **Audit usage logs** for unauthorized access
4. **Enable 2FA** on all API provider accounts

### Additional Security Measures

- **Input Sanitization**: Validate user input before processing
- **Logging**: System logs never contain sensitive credentials
- **Permissions**: Execution scripts run with minimal required permissions
- **Network Security**: Use HTTPS for all API communications
- **Code Review**: Review execution scripts before adding new agents

---

## 🤝 Contributing

To add a new agent:

1. **Create directive**: Add `your_agent.md` to `directives/`
2. **Write execution tool**: Add `your_agent.py` to `execution/`
3. **Update orchestrator**: Add intent keyword and routing logic
4. **Test**: Verify end-to-end workflow
5. **Document**: Update README with new agent details

---

## 📝 License

[Specify your license here - e.g., MIT, Apache 2.0, etc.]

---

## 👤 Author

**Kusumita**
- Email: kusumitagunnam@gmail.com

---

## 🐛 Troubleshooting

### Common Issues

**"Module not found" error:**
```bash
# Ensure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

**"API key not found" error:**
```bash
# Check .env file exists and contains valid keys
# Ensure .env is in the same directory as main.py
```

**"Permission denied" on Windows:**
```bash
# Run as administrator or use:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📚 Additional Resources

- [GEMINI.md](GEMINI.md) - Detailed architecture documentation
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Google Gemini API Docs](https://ai.google.dev/)

---

## 🎯 Roadmap

- [ ] LLM-powered intent classification (replace keyword matching)
- [ ] Web interface (Flask/FastAPI)
- [ ] Database integration for persistent storage
- [ ] Multi-user support
- [ ] Real-time collaboration features
- [ ] Plugin system for community agents
- [ ] Comprehensive test suite

---

**Built with ❤️ using the power of modular AI orchestration**
