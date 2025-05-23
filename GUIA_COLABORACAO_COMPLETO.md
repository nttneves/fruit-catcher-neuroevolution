# 🤝 GUIA COMPLETO DE COLABORAÇÃO NO PROJETO COM GIT, GITHUB E VS CODE
# ✅ Primeira vez que usas o projeto:

```bash
git clone https://github.com/nttneves/AI-Project.git
cd AI-Project
code .
```

### 🔁 Fluxo de trabalho diário:

1. Atualiza o projeto antes de começares:
   ```bash
   git pull
   ```

2. Trabalha normalmente (edita, testa, etc.)

3. Quando terminares:
   ```bash
   git add .
   git commit -m "Mensagem clara e curta"
   git push
   ```

### ⚠️ Se der erro no `push`:

O erro mais comum será:

```
error: failed to push some refs
```

Isso significa que o repositório remoto tem alterações que tu ainda não tens localmente. Solução:

```bash
git pull
# resolve conflitos, se houver
git push
```

---

## 👥 2. Como colaborar com outros

### Adicionar colaboradores no GitHub:

- Vai a `Settings > Collaborators` no repositório GitHub.
- Adiciona o nome de utilizador GitHub dos teus colegas.

### Regras para colaborar:

- Faz sempre `git pull` **antes de começares a trabalhar**.
- Faz `git add`, `git commit` e `git push` **depois de acabares**.
- Evita alterar os mesmos ficheiros que outra pessoa ao mesmo tempo.
- Usa mensagens de commit descritivas mas curtas.

---

## 🖥️ 3. Como usar o VS Code com Git

### Abrir o projeto:

```bash
cd AI-Project
code .
```

Ou, no VS Code:

- `File > Open Folder` → escolhe a pasta do projeto

### Trabalhar normalmente:

- Edita ficheiros, guarda com `Ctrl+S` ou `Cmd+S`

### Usar o Source Control (Git integrado):

1. Clica no ícone de `Source Control` (símbolo do Git) no lado esquerdo
2. Escreve a mensagem do commit
3. Clica no ✓ para fazer o commit
4. Clica em "Sync Changes" para fazer o `push` e `pull`

---

## ⚔️ 4. Resolução de Conflitos de Merge

### Quando acontece?

- Dois membros editaram o mesmo ficheiro ou linha
- Um faz `push`, o outro tenta depois → erro no push

### O que fazer?

1. O erro ao tentar `push` será algo como:

```
! [rejected] master -> master (non-fast-forward)
```

2. Solução:

```bash
git pull
```

3. O Git pode mostrar:

```
CONFLICT (content): Merge conflict in ficheiro.py
```

4. Abre o ficheiro e vais ver algo como:

```python
<<<<<<< HEAD
versão do código local
=======
versão que veio do GitHub
>>>>>>> abc1234
```

5. Decide o que queres manter (ou junta os dois)

6. Apaga os marcadores `<<<<<<<`, `=======`, `>>>>>>>`

7. Depois de resolver:

```bash
git add .
git commit -m "Conflito resolvido"
git push
```

---

## ✅ Boas práticas finais

| Ação | Porquê |
|------|--------|
| `git pull` antes de começar | Para evitar conflitos |
| Fazer commits pequenos e frequentes | Mais fácil de rever |
| Evitar editar os mesmos ficheiros | Menos conflitos |
| Usar VS Code para ver conflitos | Ajuda visual |
