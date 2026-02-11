from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

USF_NOME = "USF Vila Amorim"
ENDERECO = "Professor Jeremias, 456"

def menu_principal():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🕐 Horários da unidade", callback_data="horarios")],
        [InlineKeyboardButton("💉 Vacinação", callback_data="vacina")],
        [InlineKeyboardButton("💊 Farmácia", callback_data="farmacia")],
        [InlineKeyboardButton("🩺 Consultas (acolhimento e clínica)", callback_data="consultas_menu")],
        [InlineKeyboardButton("🩹 Curativos", callback_data="curativos")],
        [InlineKeyboardButton("🧪 Exames de sangue", callback_data="exames")],
        [InlineKeyboardButton("🤰 Gestantes e puericultura", callback_data="gestantes")],
        [InlineKeyboardButton("⚠️ Urgência (UPA)", callback_data="urgencia")],
        [InlineKeyboardButton("🔎 Outras dúvidas", callback_data="outras")],
    ])

def menu_consultas():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("1) Acolhimento", callback_data="acolhimento")],
        [InlineKeyboardButton("2) Consulta clínica (agendada)", callback_data="consulta_clinica")],
        [InlineKeyboardButton("3) Médicos e agenda", callback_data="medicos_agenda")],
        [InlineKeyboardButton("4) Teste de gravidez", callback_data="teste_gravidez")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="voltar_principal")],
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        f"Olá! 👋 Bem-vindo(a) à *{USF_NOME}*\n"
        f"📍 Endereço: {ENDERECO}\n\n"
        "Escolha uma opção:"
    )
    await update.message.reply_text(texto, reply_markup=menu_principal(), parse_mode="Markdown")

async def responder_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    respostas = {
        "horarios": (
            "🕐 *Horários da unidade*\n\n"
            "A USF funciona:\n"
            "📌 07:00 às 17:00"
        ),
        "vacina": (
            "💉 *Vacinação*\n\n"
            "Sala de vacina:\n"
            "📌 08:00 às 16:00\n"
            "✅ Sem horário de almoço"
        ),
        "farmacia": (
            "💊 *Farmácia*\n\n"
            "📌 08:00 às 17:00\n"
            "⏸️ Almoço: 12:00 às 13:00"
        ),
        "curativos": (
            "🩹 *Curativos*\n\n"
            "📌 Realizados todos os dias:\n"
            "08:00 às 16:40"
        ),
        "exames": (
            "🧪 *Exames de sangue*\n\n"
            "📌 Coleta de sangue: todos os dias às 07:00 em ponto.\n\n"
            "📄 Documentos necessários:\n"
            "• Cartão do SUS\n"
            "• RG ou CNH"
        ),
        "gestantes": (
            "🤰 *Gestantes e puericultura (fluxo especial)*\n\n"
            "Esses casos NÃO precisam esperar a abertura da agenda:\n\n"
            "✅ Gestantes: podem marcar direto no balcão.\n"
            "✅ Puericultura: crianças até 1 ano, 11 meses e 29 dias.\n"
            "📌 Marcação feita no dia da consulta."
        ),
        "urgencia": (
            "⚠️ *Urgência*\n\n"
            "Se houver sinais como:\n"
            "• falta de ar\n"
            "• dor no peito\n"
            "• desmaio\n"
            "• sangramento intenso\n"
            "• convulsão\n\n"
            "Procure UPA/Pronto Socorro imediatamente."
        ),
        "acolhimento": (
            "🩺 *Acolhimento*\n\n"
            "O acolhimento é para queixas do momento (ex: gripe, dor de garganta, inflamações e ocorrências não graves).\n\n"
            "📌 Funciona todos os dias:\n"
            "• 08:00 às 10:00\n"
            "• 13:00 às 15:00"
        ),
        "consulta_clinica": (
            "🩺 *Consulta clínica (agendada)*\n\n"
            "As consultas clínicas precisam ser agendadas.\n\n"
            "📌 As agendas abrem sempre na última semana do mês.\n\n"
            "Nessas consultas o médico pode:\n"
            "• solicitar exames\n"
            "• encaminhar para especialistas\n"
            "• acompanhar condições crônicas"
        ),
        "medicos_agenda": (
            "👨‍⚕️ *Médicos e agenda*\n\n"
            "A unidade tem 4 médicos:\n"
            "• João\n"
            "• Rosa\n"
            "• Ana\n"
            "• Claudio\n\n"
            "📌 Na última semana do mês, a agenda de cada médico abre um por dia."
        ),
        "teste_gravidez": (
            "🤰 *Teste de gravidez*\n\n"
            "📌 O teste de gravidez deve ser realizado no dia de acolhimento."
        ),
        "outras": (
            "🔎 *Outras dúvidas*\n\n"
            "Digite sua dúvida.\n\n"
            "⚠️ Observação: este canal é informativo.\n"
            "Para marcação de consulta, gestantes ou puericultura, procure o balcão da unidade."
        )
    }

    if data == "consultas_menu":
        await query.edit_message_text(
            "🩺 *Consultas*\n\nEscolha uma opção:",
            reply_markup=menu_consultas(),
            parse_mode="Markdown"
        )
        return

    if data == "voltar_principal":
        texto = (
            f"Você está na *{USF_NOME}*.\n"
            f"📍 Endereço: {ENDERECO}\n\n"
            "Escolha uma opção:"
        )
        await query.edit_message_text(texto, reply_markup=menu_principal(), parse_mode="Markdown")
        return

    resposta = respostas.get(data, "Opção inválida.")
    await query.edit_message_text(
        resposta,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ Voltar ao menu", callback_data="voltar_principal")]
        ]),
        parse_mode="Markdown"
    )

def main():
    TOKEN = "8510659897:AAFV22YWKpCKRM3kmoZJ5bMg1BiKYhYv6Ko"
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(responder_callback))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()

