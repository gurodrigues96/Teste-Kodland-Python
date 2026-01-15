# 🎮 Platformer Adventure - Python Project

Este projeto é um jogo de plataforma 2D desenvolvido em **Python** utilizando a biblioteca **PgZero**. O projeto foi criado como parte de um teste técnico para tutores de programação, focando em boas práticas de código, orientação a objetos e implementação de lógica de jogo sem depender de engines complexas.

## 📋 Sobre o Projeto

O objetivo deste projeto foi criar um jogo funcional do gênero *Platformer* seguindo requisitos estritos:
* **Gênero:** Plataforma (visão lateral, gravidade e pulo).
* **Restrições:** Uso exclusivo das bibliotecas `pgzero`, `math` e `random`.
* **Técnicas:** Implementação manual de física, colisão e animação de sprites (sem depender de automações prontas).
* **Código:** Estrutura limpa, em inglês e seguindo o guia de estilo PEP8.

## ✨ Funcionalidades

* **Sistema de Física:** Gravidade customizada e mecânica de pulo fluido.
* **Tilemap Level Design:** O cenário é gerado dinamicamente através de uma matriz de texto, facilitando a edição de fases.
* **Animação de Sprites:** Classes dedicadas para gerenciar a troca de frames de animação (Idle/Walk) para o herói e inimigos.
* **Inimigos com IA Básica:** Inimigos patrulham áreas delimitadas automaticamente.
* **Menu Interativo:** Menu inicial com opções de iniciar jogo, controle de som e sair.
* **Gerenciamento de Áudio:** Sistema de música de fundo e efeitos sonoros com opção de Mute.

## 🚀 Como Executar

### Pré-requisitos
Você precisa ter o **Python 3.x** instalado.

### Passo 1: Instalar Dependências
A única dependência externa é o PgZero. Abra o terminal e execute:

```bash
pip install pgzero

👨‍💻 Autor
Desenvolvido por Gustavo Rodrigues de Oliveira.
