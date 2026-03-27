"""
Módulo de Limpeza e Extração Estruturada - Neural Marketing Intelligence
Este módulo contém as funções de Processamento de Linguagem Natural (PLN) baseadas em
Expressões Regulares (Regex) para o Startup Signal Intelligence.

Autor: Renato Assis | Neural Platform Intelligence
"""

import re

def limpar_markdown(texto: str) -> str:
    """
    Remove elementos de formatação Markdown do texto.
    
    Remove: blocos de código, imagens, links, headers, tags HTML e badges.
    
    Args:
        texto (str): O texto bruto em formato Markdown.
        
    Returns:
        str: O texto limpo de marcações.
        
    Exemplo:
        >>> limpar_markdown("# Hello [Link](url)")
        'Hello Link'
    """
    # 1. Remover blocos de código (re.sub)
    texto = re.sub(r'```[\s\S]*?```', '', texto)
    # 2. Remover imagens (re.sub)
    texto = re.sub(r'!\[.*?\]\(.*?\)', '', texto)
    # 3. Remover links mantendo o texto âncora (re.sub)
    texto = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', texto)
    # 4. Remover headers (re.sub)
    texto = re.sub(r'#{1,6}\s', '', texto)
    # 5. Remover tags HTML (re.sub)
    texto = re.sub(r'<.*?>', '', texto)
    # 6. Remover badges específicos (re.sub)
    texto = re.sub(r'\[!\[.*?\]\(.*?\)\]\(.*?\)', '', texto)
    
    return texto.strip()

def extrair_emails(texto: str) -> list:
    """
    Extrai todos os endereços de e-mail válidos do texto.
    
    Args:
        texto (str): Texto para busca.
        
    Returns:
        list: Lista de e-mails encontrados.
        
    Exemplo:
        >>> extrair_emails("Contato: sac@Neural Platform.com.br")
        ['sac@Neural Platform.com.br']
    """
    # Uso de re.findall para capturar padrões de e-mail
    padrao = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(padrao, texto)

def extrair_versoes(texto: str) -> list:
    """
    Extrai números de versão seguindo o padrão Semantic Versioning.
    
    Detecta formatos como v1.0.0, 2.3.4, etc.
    
    Args:
        texto (str): Texto para busca.
        
    Returns:
        list: Lista de versões encontradas.
        
    Exemplo:
        >>> extrair_versoes("Release v2.5.1")
        ['v2.5.1']
    """
    # Uso de re.findall para capturar versões semânticas
    padrao = r'v?\d+\.\d+\.\d+'
    return re.findall(padrao, texto)

def extrair_mentions(texto: str) -> list:
    """
    Extrai menções a usuários no estilo GitHub (@usuario).
    
    Args:
        texto (str): Texto para busca.
        
    Returns:
        list: Lista de menções encontradas.
        
    Exemplo:
        >>> extrair_mentions("cc @renatoassis86")
        ['@renatoassis86']
    """
    # Uso de re.findall para capturar menções
    padrao = r'@[\w-]+'
    return re.findall(padrao, texto)

def extrair_issue_refs(texto: str) -> list:
    """
    Extrai referências a Issues ou Pull Requests (#123).
    
    Args:
        texto (str): Texto para busca.
        
    Returns:
        list: Lista de referências numéricas.
        
    Exemplo:
        >>> extrair_issue_refs("Fixes #45")
        ['#45']
    """
    # Uso de re.findall para capturar referências de issues
    padrao = r'#\d+'
    return re.findall(padrao, texto)

def verificar_qualidade_readme(texto: str) -> dict:
    """
    Verifica a presença de seções vitais para a saúde comunicacional de um README.
    
    Critérios: Badge CI, Instalação, Documentação, Contato, Versão.
    
    Args:
        texto (str): Conteúdo do README.
        
    Returns:
        dict: Dicionário com booleanos para cada critério.
        
    Exemplo:
        >>> verificar_qualidade_readme("## Instalação")
        {'badge': False, 'instalacao': True, ...}
    """
    # Uso de re.search para validar existência de padrões estruturais
    qualidade = {
        "badge": bool(re.search(r'\[!\[.*?\]\(.*?\)\]\(.*?\)', texto)),
        "instalacao": bool(re.search(r'#+\s*Instala[çc][ãa]o', texto, re.IGNORECASE)),
        "docs": bool(re.search(r'https?://[\w.-]+/docs', texto, re.IGNORECASE)),
        "contato": bool(re.search(r'contato|suporte|email|@', texto, re.IGNORECASE)),
        "versao": bool(re.search(r'v?\d+\.\d+\.\d+', texto))
    }
    return qualidade

def split_changelog_por_versao(texto: str) -> list:
    """
    Divide um arquivo de Changelog em blocos baseados na versão.
    
    Args:
        texto (str): Conteúdo do changelog.
        
    Returns:
        list: Lista de blocos de texto por versão.
        
    Exemplo:
        >>> split_changelog_por_versao("## v1.0.0 ... ## v0.9.0")
        ['## v1.0.0 ... ', '## v0.9.0']
    """
    # Uso de re.split para segmentar o texto por headers de versão
    # Capturamos o delimitador para não perdê-lo se necessário, 
    # mas aqui fazemos split simples
    padrao = r'(?=##?\s*v?\d+\.\d+\.\d+)'
    blocos = re.split(padrao, texto)
    return [b.strip() for b in blocos if b.strip()]

def limpar_para_spacy(texto: str) -> str:
    """
    Pipeline completa de limpeza para preparar o texto para processamento no spaCy.
    
    Remove ruído de código, e-mails, URLs e formatação markdown excessiva.
    
    Args:
        texto (str): Texto bruto.
        
    Returns:
        str: Texto limpo e normalizado.
    """
    # 1. Aplicar limpeza de Markdown
    texto = limpar_markdown(texto)
    # 2. Normalizar espaços em branco (re.sub)
    texto = re.sub(r'\s+', ' ', texto)
    # 3. Remover caracteres especiais isolados (re.sub)
    texto = re.sub(r'[^\w\sÀ-ÿ.,!?]', '', texto)
    
    return texto.strip().lower()

def moderar_conteudo(texto: str, palavras_ofensivas: list) -> str:
    """
    Substitui termos sensíveis ou ofensivos por asteriscos.
    
    Args:
        texto (str): Texto a ser moderado.
        palavras_ofensivas (list): Lista de strings proibidas.
        
    Returns:
        str: Texto com as palavras substituídas.
        
    Exemplo:
        >>> moderar_conteudo("Texto ruim", ["ruim"])
        'Texto ***'
    """
    if not palavras_ofensivas:
        return texto
        
    # Uso de re.sub com alternância (|) para moderar múltiplos termos
    padrao = r'\b(?:' + '|'.join(map(re.escape, palavras_ofensivas)) + r')\b'
    return re.sub(padrao, '***', texto, flags=re.IGNORECASE)

if __name__ == "__main__":
    # Simulação de um README de uma Startup Fintech Brasileira (Ex: "Neural PlatformPay")
    readme_simulado = """
    # Neural PlatformPay - API de Pagamentos Instantâneos v1.2.0
    
    [![Build Status](https://img.shields.io/travis/Neural Platform/pay.svg)](url)
    
    Sistema disruptivo para transações B2B. Resolva o problema de fluxo de caixa com @Neural Platformpay.
    
    ## Instalação
    ```bash
    pip install Neural Platformpay
    ```
    
    ### Docs
    Documentação em https://Neural Platform.com.br/docs/api
    
    ## Changelog
    ### v1.2.0
    - Fixes #101 e #102
    - Novo endpoint para Pix
    
    ### v1.1.0
    - Lançamento inicial
    
    Contato: suporte@Neural Platformpay.com.br ou falar com @dev-master.
    """
    
    print("--- Neural Marketing Intelligence - TESTE DE LIMPEZA E EXTRAÇÃO ---")
    
    print(f"E-mails encontrados: {extrair_emails(readme_simulado)}")
    print(f"Versões detectadas: {extrair_versoes(readme_simulado)}")
    print(f"Menções: {extrair_mentions(readme_simulado)}")
    print(f"Referências de Issues: {extrair_issue_refs(readme_simulado)}")
    
    check_qualidade = verificar_qualidade_readme(readme_simulado)
    print(f"Check de Qualidade: {check_qualidade}")
    
    print("\nTexto pronto para spaCy (Snippet):")
    print(limpar_para_spacy(readme_simulado)[:150] + "...")
    
    print("\nModerando conteúdo sensível:")
    print(moderar_conteudo("Essa API é uma porcaria e muito lenta.", ["porcaria", "lenta"]))
    
    print("\nSegmentação de Changelog:")
    blocos = split_changelog_por_versao(readme_simulado)
    print(f"Total de versões no changelog: {len(blocos)}")
