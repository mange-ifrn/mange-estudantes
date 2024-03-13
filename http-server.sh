make clean
make html && \
(cd docs/_build/html; python3 -m http.server)