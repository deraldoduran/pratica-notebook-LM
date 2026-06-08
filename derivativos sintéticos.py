# app.py
# Aplicativo para cálculo de Paridade Put-Call e estratégias sintéticas

import math

class DerivativosSinteticos:
    def __init__(self, S, K, r, T, call_price, put_price):
        """
        S: preço do ativo subjacente
        K: preço de exercício (strike)
        r: taxa de juros livre de risco (anual)
        T: tempo até o vencimento (em anos)
        call_price: preço da opção de compra (call)
        put_price: preço da opção de venda (put)
        """
        self.S = S
        self.K = K
        self.r = r
        self.T = T
        self.call_price = call_price
        self.put_price = put_price

    def valor_presente_strike(self):
        return self.K * math.exp(-self.r * self.T)

    def verificar_paridade(self):
        lhs = self.call_price + self.valor_presente_strike()
        rhs = self.put_price + self.S
        return lhs, rhs, round(lhs - rhs, 4)

    def arbitragem(self):
        lhs, rhs, diff = self.verificar_paridade()
        if diff > 0:
            return f"Arbitragem: Venda Call+PV(K), compre Put+S. Ganho ≈ {diff}"
        elif diff < 0:
            return f"Arbitragem: Venda Put+S, compre Call+PV(K). Ganho ≈ {abs(diff)}"
        else:
            return "Sem oportunidade de arbitragem."

    def futuro_sintetico(self):
        return f"Montagem: Comprar Call (strike {self.K}) + Vender Put (strike {self.K})."

# Exemplo de uso
if __name__ == "__main__":
    # Valores fictícios
    S = 1000       # preço do ativo
    K = 1000       # strike
    r = 0.05       # taxa de juros anual
    T = 0.5        # meio ano
    call_price = 45
    put_price = 40

    app = DerivativosSinteticos(S, K, r, T, call_price, put_price)

    print("=== Paridade Put-Call ===")
    lhs, rhs, diff = app.verificar_paridade()
    print(f"LHS (Call + PV(K)) = {lhs:.2f}")
    print(f"RHS (Put + S) = {rhs:.2f}")
    print(f"Diferença = {diff:.2f}")

    print("\n=== Arbitragem ===")
    print(app.arbitragem())

    print("\n=== Futuro Sintético ===")
    print(app.futuro_sintetico())



