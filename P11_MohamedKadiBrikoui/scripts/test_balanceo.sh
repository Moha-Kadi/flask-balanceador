#!/bin/bash
echo "Probando balanceo entre instancias..."
for i in {1..10}; do
  curl -s http://localhost:8080/
  echo
done