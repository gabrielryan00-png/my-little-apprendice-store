
# Chatbot USF (Telegram) — Protótipo

Este projeto é um protótipo de chatbot para uma Unidade de Saúde da Família (USF), desenvolvido em **Python** usando a biblioteca **python-telegram-bot**.

O objetivo é automatizar respostas frequentes e orientar o paciente sobre horários, vacinação, farmácia, consultas, exames e fluxos específicos.

---

## ✅ Funcionalidades

- Menu principal com botões
- Submenu de consultas (acolhimento e consulta clínica)
- Respostas rápidas para:
  - Horário da unidade
  - Vacinação
  - Farmácia
  - Curativos
  - Exames de sangue
  - Fluxo de gestantes e puericultura
  - Teste de gravidez
  - Orientação de urgência
- Token protegido via variável de ambiente (`BOT_TOKEN`)

---

## Requisitos
- Python 3.10+ (recomendado)
- Telegram Bot Token (via @BotFather)

---

## Como rodar
### 1) Clonar o projeto
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPO.git
cd NOME_DO_REPO
Segurança (importante)

Nunca suba o token no código.

Use sempre variável de ambiente (BOT_TOKEN).

Observação
Este bot é informativo e não realiza diagnóstico nem substitui atendimento médico.
Licença

Este projeto pode ser usado como base educacional e protótipo.


Salve no nano:
- CTRL + O
- Enter
- CTRL + X

---

## 2) Adicione um `.gitignore` (muito importante)
Crie:

```bash
nano .gitignore


Cole isso:

venv/
__pycache__/
*.pyc
.env
.DS_Store
