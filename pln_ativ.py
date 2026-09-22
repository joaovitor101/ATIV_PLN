import nltk
#tirar pontuação
import string

avaliacoes = [
    #5 estrelas
    
    """ Envio muito rápido (apenas 4 dias), a caixa chegou um pouco danificada, o que é 
típico do AliExpress. Quanto ao teclado, é muito bom e confortável de usar, parece 
uma teclado mecânico, mas não é, não tem aquele som típico (clack clack) ao digitar. 
Mas, para mim, isso é até melhor, trabalho com um PC e esse som pode ser irritante, 
este teclado é perfeito para mim. 100 por cento recomendado. Ótimo custo-benefício. """,


    """Bonito, com uma qualidade muito boa, até acima da minha expectativa, e por um 
preço justo. Realmente fiquei impressionado. Os botões são muito bons e o toque é 
bem agradável. O mouse também achei muito bonito e gostei bastante dele. O som 
também é muito bom. Ainda estou testando, porque acabou de chegar, então não 
posso falar sobre a durabilidade ou o uso a longo prazo. Mas, até agora, estou muito 
satisfeito e recomendo bastante!""",


    """Impecável 10/10, bonito e confortável, boa cor, chegou em perfeito estado, a caixa 
chegou sem nenhum dano... muito satisfeito, recomendado, peso 0,75 kg = 750 
gramas. """,

    """Não é ruim pelo preço. É de plástico, mas eu gosto, é simples. É uma membrana, 
como esperado pelo visual. Ideal para iniciantes! """,

    """Muito satisfeito. É melhor do que eu esperava pelo preço que paguei. Estou muito 
feliz com minha compra. O processo de compra e entrega foi rápido. A qualidade do 
produto é satisfatória. Sim, eu recomendo.""",


    #4 estrelas
    
    """A caixa chegou em mau estado, mas o produto está em boas condições. Funciona 
perfeitamente, emitindo um som muito suave ao usar as teclas. Não fica muito 
firme; balança um pouco. Tem pernas extras para elevá-lo, mas, mesmo assim, o 
conjunto não se mantém estável. As luzes iluminam muito bem e é muito 
confortável de usar; as teclas podem ser removidas sem muita dificuldade, e tanto o 
mouse quanto o teclado são bastante leves.""",

    """Um teclado muito funcional. Uma boa alternativa aos teclados gamer mais caros 
disponíveis no mercado. Infelizmente, possui apenas 2 modos de iluminação RGB 
(estacionário e piscando lentamente), sem efeito de respiração ou algo equivalente. """,


    """Um teclado e mouse muito legais. Qualidade média, mas para o uso que vamos dar, 
é suficiente ou mais do que suficiente. Mas eu realmente gostei disso.""",

    """Este teclado é uma verdadeira joia, que beleza, e acima de tudo, é excelente para 
jogos. Altamente recomendado pela relação custo-benefício, 8/10. """,

    """É bom pelo preço, tal como está, mas o material é um pouco fino.""",
    
    #3 estrelas
    
    """O produto não é ruim pelo preço, mas o envio precisa melhorar. Há pouca proteção, 
ou seja, nada além de uma caixa dentro de um saco, como mostrado nas imagens. A 
caixa está amassada. """,

    """O teclado não é nada ruim. Pelo preço que pagamos, seria ótimo se as teclas fossem 
iluminadas em vez de apenas a caixa, mas, no geral, está tudo bem. Pelo preço, é 
perfeito, não tenho do que reclamar. """,

    """ O produto chegou em uma caixa amassada. O mouse está quebrado em algumas 
partes. Além disso, parece que já havia sido colocado lá, pois não foram encontrados 
fragmentos ou peças do mouse dentro da caixa. """,

    """O teclado é muito bom para começar, mas devido à qualidade do plástico barato, 
não é recomendado se você planeja usá-lo por um longo período. Mas, fora isso, é 
muito bom e se ajusta muito bem. """,

    """Dou 3 estrelas, não porque seja um produto ruim em si, mas porque os materiais de 
fabricação são realmente baratos. Se você está com uma situação financeira difícil, 
não tenha receio de comprá-lo; se puder economizar no curto prazo, procure uma 
opção de maior qualidade. """,

    #2 estrelas
    
    """ trava da tecla esc quebrada e o trocador de dpi está quebrado, caixa amassada """,
    
    """A velocidade de resposta das teclas é terrível, e depois de alguns usos, todas as 
teclas se soltam. A estrutura parece ter sido impressa em 3D. É mal feita. Se vocês já 
vão fazer algo tão mal, não vendam, seus malditos idiotas.""",

    """Embora diga ser mecânico e pareça ser, na verdade é baseado em membrana, e os 
materiais parecem ser de baixa qualidade.""",

    """Assim que recebi o item, ele estava todo rasgado e quebrado, e eu nem sequer o 
levei para dentro de casa. É realmente irritante. O produto foi enviado de forma tão 
descuidada que acabou sendo danificado. Isso é uma piada ou o que? """,

    """É simples, diferente dos teclados vendidos nas lojas da mesma marca. Acho que o 
Bamba tem um pouco mais de qualidade, mas não o recomendo; é muito básico 
para uso contínuo em cabines. Não recomendo; é péssimo. Sinto que fui enganado.""",

    #1 estrela
    
    """O item é bom para uso em jogos, muito leve e esteticamente agradável. A única 
desvantagem, além da embalagem de baixa qualidade, é que o vendedor não 
responde quando você tenta obter informações sobre o produto.""",

    """Fiz o pedido e, para minha grande surpresa, recebi um pequeno pôster!!!!!! É a 
primeira vez que isso acontece comigo depois de anos comprando no Aliexpress. """,

    """Chegou quebrado, e o material é de baixa qualidade. A conexão USB falhou após 2 
dias. Não jogue seu dinheiro fora. Caro e ruim!""",

    """Infelizmente, o pedido chegou de forma incorreta, o teclado estava quebrado ao 
meio, o mouse faz um barulho estranho por dentro e desconecta do PC de vez em 
quando. Eu estava muito animado com esses produtos, mas eles não funcionaram 
para mim.""",

    """Mouse e teclado chegaram quebrados. O teclado RGB não liga de jeito nenhum, e o 
mouse não faz clique direito porque veio com o botão descolado. É uma pena, 
porque eu realmente gosto do fato de o teclado ser silencioso ao digitar."""
]


artigos = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
           'the', 'a', 'an']

stopwords = nltk.corpus.stopwords.words('portuguese')

import nltk
import string

artigos = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
           'the', 'an']

stopwords = nltk.corpus.stopwords.words('portuguese')

qtd_tokens_inicial = 0
qtd_tokens_sem_artigos = 0
qtd_tokens_sem_pontuacao = 0
qtd_tokens_sem_numeros = 0
qtd_tokens_sem_stopwords = 0

# tokenização das avaliações
for avaliacao in avaliacoes:

    tokens = nltk.word_tokenize(avaliacao.lower())

    # quantidade inicial
    qtd_tokens_inicial += len(tokens)

    # tirar artigos
    tokens = [token for token in tokens if token not in artigos]
    qtd_tokens_sem_artigos += len(tokens)

    # tirar pontuação
    tokens = [token for token in tokens if token not in string.punctuation]
    qtd_tokens_sem_pontuacao += len(tokens)

    # tirar números
    tokens = [token for token in tokens if not token.isdigit()]
    qtd_tokens_sem_numeros += len(tokens)

    # tirar stopwords
    tokens = [token for token in tokens if token not in stopwords]
    qtd_tokens_sem_stopwords += len(tokens)

    print(tokens)

print(f"Quantidade de tokens inicialmente: {qtd_tokens_inicial}")
print(f"Quantidade de tokens após remover artigos: {qtd_tokens_sem_artigos}")
print(f"Quantidade de tokens após remover pontuação: {qtd_tokens_sem_pontuacao}")
print(f"Quantidade de tokens após remover números: {qtd_tokens_sem_numeros}")
print(f"Quantidade de tokens após remover stopwords: {qtd_tokens_sem_stopwords}")