
nome: str = "Mario Rossi"
importo: float = 1250.50
attivo: bool = True

print(f"{nome} ha un importo di {importo:.2f} euro ed è attivo: {attivo}")

importi: list[float] = [1250.50, 980.00, 1750.25, 430.75, 2100.00]

print(f"la lista contiene {len(importi)} importi")
print(f"il primo importo è {importi[0]:.2f} euro")
print(f"l'ultimo importo è {importi[-1]:.2f} euro")
print(f"la somma degli importi è {sum(importi):.2f} euro")

cliente = {
    "id": 1,
    "nome": "Mario Rossi",
    "citta": "Roma",
    "attivo": True,
}
cliente["email"] = "mario.rossi@example.com"

print(f"Cliente: {cliente}")
print(f"Telefono: {cliente.get('telefono', 'non disponibile')}")

# print(cliente["telefono"]) # keyerror