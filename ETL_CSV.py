import pandas as pd

def calcular_metricas(input_filename, output_filename):
    try:
        # Extração: Ler os dados do arquivo CSV de entrada
        dados_df = pd.read_csv(input_filename)
        
        # Cálculo das métricas de desempenho
        dados_df['preco_unitario'] = dados_df['receita'] / dados_df['quantidade_vendida']
        
        # Carregamento: Salvar os dados com as métricas calculadas em um novo arquivo CSV
        dados_df.to_csv(output_filename, index=False)
        
        print(f"Cálculo de métricas de desempenho concluído. Dados salvos em '{output_filename}'.")
    except Exception as e:
        print("Ocorreu um erro durante o processo:", e)

if __name__ == "__main__":
    input_file = 'dados_vendas.csv'
    output_file = 'metricas_desempenho.csv'
    calcular_metricas(input_file, output_file)
