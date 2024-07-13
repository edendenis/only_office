#!/usr/bin/env python
# coding: utf-8

# # Como instalar/configurar o `OnlyOffice` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para instalar/configurar o `OnlyOffice` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and configurations for installing/configuring `OnlyOffice` on `Linux Ubuntu`._

# ## Descrição [3]
# 
# `OnlyOffice`
# 
# O `OnlyOffice` é uma suíte de escritório online e de código aberto que oferece um conjunto abrangente de aplicativos para edição de documentos, planilhas e apresentações. Ele permite que indivíduos e equipes colaborem em tempo real, criando e editando documentos diretamente no navegador da web. O `OnlyOffice` suporta uma ampla variedade de formatos de arquivo, incluindo Microsoft Office, e oferece recursos avançados de formatação, revisão de documentos e controle de versão. Além disso, ele pode ser implantado em servidores locais ou em nuvem, proporcionando flexibilidade e segurança aos usuários. Com suas funcionalidades de colaboração e edição de documentos, o `OnlyOffice` é uma solução atraente para organizações que buscam uma alternativa de escritório online versátil e de código aberto.
# 

# ## 1. Configurar/Instalar/Usar o `OnlyOffice` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/usar o `OnlyOffice` no `Linux Ubuntu`, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. **Adicionar o repositório `OnlyOffice`:** Use o seguinte comando para adicionar o repositório `OnlyOffice` ao seu sistema: `sudo echo "deb https://download.onlyoffice.com/repo/debian squeeze main" | sudo tee /etc/apt/sources.list.d/onlyoffice.list`
# 
# 4. **Adicionar a chave GPG:** Adicione a chave GPG do repositório `OnlyOffice` com o comando a seguir: `sudo wget https://download.onlyoffice.com/repo/onlyoffice.key`
# 
# 5. **Executar o comando:** `sudo apt-key add onlyoffice.key`
# 
# 6. **Atualizar a lista de pacotes:** Atualize a lista de pacotes do sistema novamente para que o sistema reconheça o novo repositório: `sudo apt update`
# 
# 7. **Instalar o OnlyOffice:** Agora, você pode instalar o `OnlyOffice Community Edition` com o seguinte comando: `sudo snap install onlyoffice-desktopeditors`
# 
#     - Depois de concluída a instalação, você deve ser capaz de acessar o `OnlyOffice` em seu sistema `Linux Ubuntu`.
# 
#     - Lembrando que o uso de `snaps` pode variar dependendo da versão do `Linux Ubuntu` que você está usando, e essa é a forma recomendada de instalar o `OnlyOffice` nas versões mais recentes. Certifique-se de ter o Snap instalado em seu sistema. Se não o tiver, você pode instalá-lo com o seguinte comando: `sudo apt install snapd`
# 
# Após a instalação ser concluída, você pode acessar o `OnlyOffice` em seu sistema. Geralmente, ele estará disponível no menu de aplicativos.
# 
# Isso deve permitir que você instale o `OnlyOffice` no seu sistema Ubuntu.
# 

# 8. Pode ser que aconteça o(s) erro(s): [2]
# 
#     ```
#     W: https://download.onlyoffice.com/repo/debian/dists/squeeze/InRelease: Key is stored in legacy trusted.gpg keyring (`/etc/apt/trusted.gpg`), see the DEPRECATION section in apt-key(8) for details.
#     ```
# 
#     Aviso que você está vendo indica que a chave do repositório do `OnlyOffice` está armazenada no anel de chaves legado (`/etc/apt/trusted.gpg`), que está em desuso. Para resolver esse aviso, você deve mover a chave para um novo local que é mais seguro e recomendado pelas práticas atuais do `Ubuntu`.
# 
# 9. **Remover o repositório existente (opcional)**: Primeiro, você pode remover o repositório existente que está causando o problema. Isso pode ser feito editando o arquivo correspondente em `/etc/apt/sources.list.d/`.
# 
#     9.1 Liste os arquivos em `/etc/apt/sources.list.d/` para encontrar o arquivo do `OnlyOffice`: `ls /etc/apt/sources.list.d/`
# 
#     9.2 Remova ou comente as linhas do repositório problemático. Por exemplo: `sudo nano /etc/apt/sources.list.d/onlyoffice.list`
# 
#     Adicione um # no início da linha para comentá-la.

# ## Referências
# 
# [1] OPENAI. ***Instalação do onlyoffice no ubuntu.*** Disponível em: <https://chat.openai.com/c/4a263fc4-3d7b-4755-854e-74cf83d899cf> (texto adaptado). ChatGPT. Acessado em: 03/10/2023 13:35.]
# 
# [2] OPENAI. ***VS code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 14/11/2023 18:56.
# 
# [3] OPENAI. ***Corrigir erro onlyoffice apt.*** Disponível em: <https://chat.openai.com/c/2e11f074-32f7-4e78-85ca-1443466c9718> (texto adaptado). ChatGPT. Acessado em: 18/10/2023 11:58.
# 
