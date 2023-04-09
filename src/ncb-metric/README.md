### Scripts da métrica NCB
#### A métrica NCB tem sua própria pasta e scripts em Ruby, pois precisa consultar a GitHub Rest API para ser calculada

> Como
- Adicione a chave de autenticação obtida no GitHub no arquivo `access_token.input`.
- Adicione os hashes dos projetos que quer analisar em arquivos na pasta `input`.
  - Exemplo: `chromium.input`.
- Adicione a pasta em `logs` com o mesmo nome do arquivo adicionado em `input`, sem a extensão do arquivo.
  - Exemplo: `chromium`.
- Execute o script Ruby a partir da pasta `ncb-metric` usando o comando `ruby commits/commit_script.rb`.
- Os resultados estarão disponíveis nas correspondentes em `logs`.
