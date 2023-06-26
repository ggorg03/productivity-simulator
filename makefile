EXEC = python

TESTS_PATH = tests/

all: tests

test: test-tarefa test-pilha-tarefas test-trabalhador

test-tarefa:
	@$(EXEC) $(TESTS_PATH)test_tarefa.py

test-pilha-tarefas:
	@$(EXEC) $(TESTS_PATH)test_pilha_tarefas.py

test-trabalhador:
	@$(EXEC) $(TESTS_PATH)test_trabalhador.py