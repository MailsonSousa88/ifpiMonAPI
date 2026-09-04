# Como contribuir

Este guia deve ser seguido em qualquer alteração feita no projeto.

## Branches

Use nomes em letras minúsculas, sem espaços ou acentos, no formato:

```text
prefixo/titulo-curto
```

Prefixos recomendados:

- `add`: nova funcionalidade ou documentação;
- `fix`: correção de erro;
- `docs`: alteração somente na documentação;
- `refactor`: melhoria interna sem mudança de comportamento;
- `test`: criação ou alteração de testes;
- `chore`: manutenção do projeto.

Exemplos: `add/listagem-de-monstros` e `fix/erro-na-busca`.

## Commits

Escreva mensagens objetivas, no imperativo, seguindo o formato:

```text
prefixo(contexto): titulo resumido
```

Use os mesmos prefixos das branches. O contexto deve identificar a parte
alterada.

Exemplos:

```text
add(api): cria rota de listagem
fix(busca): trata resultado inexistente
docs(readme): atualiza instrucoes de instalacao
```

## Issues

Antes de abrir uma issue, verifique se já existe outra sobre o mesmo assunto.
Na página de criação, escolha o modelo adequado:

- **FIX** para relatar um erro;
- **ADD** para sugerir uma adição, como funcionalidade, novo IFPI Mon ou
  documentação.

Preencha todos os campos obrigatórios com informações suficientes para que
outra pessoa consiga entender a solicitação.

## Pull requests

Abra o pull request usando o modelo do repositório, mantenha a alteração focada
em um único objetivo e:

1. descreva o que foi alterado;
2. relacione a issue correspondente, quando houver;
3. informe como a alteração foi testada;
4. confirme os itens da lista de verificação.

Ao enviar uma contribuição, você concorda em seguir estas regras.
