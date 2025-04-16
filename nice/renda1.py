from nicegui import ui
i = ui.input(label='Renda anual:')
imposto = ui.label('')

def calculo():
    ui.notify(f"Renda anual: {i.value}")
    ir = float(i.value) * 0.10
    imposto.set_text(f"Valor a pagar: {ir}")

ui.button("clique", on_click=calculo)
ui.run()
