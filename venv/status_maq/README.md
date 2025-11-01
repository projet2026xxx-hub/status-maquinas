# Status das Máquinas

Este projeto é uma aplicação web desenvolvida com Streamlit para monitorar o status das máquinas por setor. A aplicação permite que os usuários registrem o status das máquinas, visualize os dados em gráficos interativos e mantenham um histórico dos registros.

## Estrutura do Projeto

- `app.py`: Código principal da aplicação.
- `requirements.txt`: Dependências necessárias para o projeto.
- `dados.csv`: Armazena os registros de status das máquinas.
- `.gitignore`: Arquivos e diretórios a serem ignorados pelo Git.
- `README.md`: Documentação do projeto.
- `LICENSE`: Informações sobre a licença do projeto.
- `scripts/run.sh`: Script para automatizar a execução da aplicação.
- `docs/setup.md`: Instruções detalhadas de configuração do projeto.
- `tests/test_app.py`: Testes unitários para a aplicação.
- `.github/workflows/python-app.yml`: Workflow do GitHub Actions para integração contínua.

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd status_maq
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```
   streamlit run app.py
   ```

## Uso

Após iniciar a aplicação, você poderá registrar o status das máquinas por setor. Os dados serão salvos em `dados.csv` e poderão ser visualizados em gráficos interativos.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).