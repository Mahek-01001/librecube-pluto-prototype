# 🚀 LibreCube PLUTO Intelligence System  
### ZED Plugin + API + Neuro-Symbolic Linting Prototype

> Built as part of exploration for LibreCube GSoC (PLUTO Language & ZED Plugin Project)

---

## 📝 Overview

This project is a **modern PLUTO (Procedure Language for Users in Test and Operations) development system** designed for space mission procedures.

It combines:

- ⚡ High-performance editor integration (ZED)
- 🧠 Intelligent parsing & validation (Python backend)
- 🛠️ Auto-formatting aligned with ECSS standards
- 🔍 Semantic linting for mission-critical reliability

The goal is to demonstrate how **space-grade procedural languages** can be enhanced using modern tooling like FastAPI, Tree-sitter, and editor extensions.

---

## 🏗️ Architecture

PLUTO Code (.pluto / .prc)
↓
ZED Extension Layer
(Syntax Highlighting)
↓
FastAPI Backend
(Parsing + Formatting + Linting)
↓
Structured JSON Output
↓
Future: Full LSP Integration


---

## ✨ Key Features & Technical Highlights

### 1. ⚡ High-Performance ZED Integration

- Native extension design for **ZED editor (Rust-based, GPU accelerated)**
- Automatic recognition of:
  - `.pluto`
  - `.prc`
- Instant syntax-aware editing environment for space engineers

---

### 2. 🛠️ Standard-Compliant Auto Formatter

- Aligned with **ECSS-E-ST-70-32C (European Space Standard)**
- Features:
  - ✅ Keyword capitalization (`INITIATE`, `CONFIRM`, `SET VALUE`)
  - ✅ Logical indentation for:
    - `IF-THEN-ELSE`
    - `WHILE`
    - `STEP`
  - ✅ Clean and readable mission procedures

---

### 3. 🧠 Neuro-Symbolic Linter (Semantic Analysis)

- Detects:
  - ❌ Unclosed procedures / blocks
  - ❌ Missing syntax elements (e.g., colons)
  - ❌ Invalid structure definitions

- Provides:
  - Clear, actionable error messages
  - Backend-powered validation (LSP-style simulation)

---

### 4. ⚡ API-First Architecture

- Built using **FastAPI**
- Endpoints:
  - `/parse` → Token classification
  - `/format` → Standard-compliant formatting
  - `/lint` → Semantic validation

- Benefits:
  - High performance
  - Scalable backend
  - Ready for LSP upgrade

---

### 5. 🌲 Tree-sitter Query Engine (Experimental)

- Context-aware highlighting using `.scm` queries
- Differentiates:
  - Structural keywords
  - Actions
  - Logic blocks

> Moves beyond regex → towards real parsing intelligence

---

## 📂 Project Structure

librecube-pluto-prototype/
├── parser/
│ └── pluto_parser.py
├── api.py
├── main.py
├── sample.pluto
├── zed-extension/
│ ├── extension.toml
│ └── syntaxes/
│ └── pluto.tmLanguage.json
├── index.html
├── PROPOSAL_PREVIEW.md
└── README.md


---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install fastapi uvicorn

2. Start Backend
uvicorn api:app --reload

3. Open API Docs
http://127.0.0.1:8000/docs

4. Test Example
{
  "code": "SET TEMP = 25\nWAIT 5"
}

Example Output
[
  [
    {"token": "SET", "type": "actions"},
    {"token": "TEMP", "type": "unknown"}
  ]
]