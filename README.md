# 📈 Estratégias com Derivativos Sintéticos

Este repositório apresenta conceitos e estratégias de **derivativos sintéticos** utilizando opções de compra (**call**) e venda (**put**), fundamentados no princípio da **Paridade Put-Call**.  

A paridade estabelece que, em mercados eficientes, existe uma relação fixa entre o preço da call, da put, do ativo subjacente e o valor presente do preço de exercício.

---

## 🚀 Formas de Ganho

### 1. Arbitragem (Lucro Sem Risco)
A arbitragem ocorre quando a equação da paridade está desalinhada:



\[
C + PV(K) \neq P + S
\]



- **Arbitragem Fiduciária vs. Venda Protegida:**  
  Se uma *Married Put* (ativo + put) estiver mais cara que uma *Fiduciary Call* (caixa + call), o arbitrador vende a primeira e compra a segunda, embolsando a diferença.

- **Arbitragem Centesimal:**  
  Exemplo: Call strike 1000 custa 45 e Put strike 1000 custa 40 → preço justo do futuro = 1005.  
  Se o futuro estiver a 1006, é possível lucrar 1 centavo por contrato comprando a call, vendendo o futuro e vendendo a put.

---

### 2. Criação de Posições Sintéticas (Alavancagem)
Os sintéticos permitem replicar o comportamento de ativos com menor capital inicial, ampliando retornos.

- **Futuro Comprado Sintético:**  
  Comprar uma call e vender uma put do mesmo strike e vencimento → comportamento idêntico ao contrato futuro.

- **Alavancagem Extrema:**  
  Relações de até **33:1 a 99:1**, onde pequenas variações no ativo resultam em grandes ganhos percentuais sobre a margem.

---

### 3. Eficiência de Custos e Gestão de Fluxo
Institucionais usam sintéticos para otimizar portfólios sem atritos do mercado à vista.

- **Substituição de Ativos:**  
  Ajuste de duração de carteiras de títulos via sintéticos, reduzindo custos de transação.

- **Geração de Renda com Puts:**  
  *Cash-Secured Put* ≡ *Covered Call*. Estratégia popular para gerar renda passiva com prêmios de opções.

---

## ⚠️ Riscos Críticos

- **Espiral de Perdas e Liquidação Forçada:**  
  Em alta volatilidade, posições sintéticas alavancadas sofrem chamadas de margem agressivas.

- **Risco de Contraparte:**  
  Em derivativos OTC, depende da capacidade da contraparte honrar o contrato.

- **Regulação:**  
  A **Regra 18f-4 da SEC** limita alavancagem sintética em fundos, com base no cálculo de **VaR (Valor em Risco)**.

---

## 📚 Objetivo do Repositório
- Documentar estratégias de arbitragem, alavancagem e eficiência de custos com derivativos sintéticos.  
- Servir como guia para estudantes, traders e analistas interessados em finanças quantitativas.  
- Destacar riscos e boas práticas na utilização dessas estruturas.

---

## 🛠️ Próximos Passos
- Exemplos numéricos de montagem de futuros sintéticos.  
- Simulações de arbitragem com dados históricos.  
- Scripts em Python para cálculo automático da paridade put-call.

---

## 📜 Licença
Este projeto está sob a licença MIT.  
Sinta-se livre para usar, modificar e compartilhar.
