lint:
	yamllint . --strict

install-pre-commit-hook:
	@if [ ! -f ".git/hooks/pre-commit" ];then \
		pre-commit install; \
	fi
