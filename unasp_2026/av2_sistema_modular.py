# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: Mickaell Texeira Medeiros
# Data: 18/09/2026
# Link do Repositório: 
# ==============================================================================

dados_brutos = [
   "  carlos eduardo silva;desenvolvedor;11988887777  ",
   "  ana paula mendes;analista de rh;21977776666  ",
   "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


def limpar_e_formatar_texto(texto):
   texto_limpo = texto.strip()
   texto_formatado = texto_limpo.upper()
   return texto_formatado


def extrair_codigo_ou_ddd(dado):

   dado_limpo = dado.strip()
   codigo = dado_limpo[0:2]
   return codigo


def processar_e_exibir_cadastros(lista_dados):
   total_registros = 0

   for registro in lista_dados:
       partes = registro.split(";")
       nome_bruto = partes[0]
       cargo_bruto = partes[1]
       telefone_bruto = partes[2]

       nome_formatado = limpar_e_formatar_texto(nome_bruto)
       cargo_formatado = limpar_e_formatar_texto(cargo_bruto)
       ddd = extrair_codigo_ou_ddd(telefone_bruto)

       print(f"Nome: {nome_formatado} | Cargo: {cargo_formatado} | DDD: {ddd}")

       total_registros += 1

   return total_registros

def main():
   print("==================================================")
   print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
   print("==================================================\n")

   print("Iniciando o processamento dos dados...\n")

   total_processado = processar_e_exibir_cadastros(dados_brutos)

   print(f"\nTotal de registros processados: {total_processado}")

   print("\n==================================================")
   print("             PROCESSAMENTO CONCLUÍDO              ")
   print("==================================================")

if __name__ == "__main__":
   main()