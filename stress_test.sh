#!/bin/bash

TARGET_URL="http://localhost:8000/predict"
TOTAL_REQUESTS=50
CONCURRENT=5
DATA='{"history": [12, 5, 20]}'

echo "[BENCHMARK] Début du test de performance..."
echo "[BENCHMARK] Cible : $TARGET_URL"
echo "[BENCHMARK] Volume : $TOTAL_REQUESTS requêtes (5 en parallèle)"

START_TIME=$(date +%s)
SUCCESS=0
FAILED=0

for ((i=1; i<=TOTAL_REQUESTS; i++)); do
  (
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$TARGET_URL" \
      -H "Content-Type: application/json" \
      -d "$DATA")
    echo "$HTTP_CODE"
  ) &

  # Limiter le parallélisme à 5 requêtes simultanées
  if (( i % CONCURRENT == 0 )); then
    wait
  fi
done > /tmp/stress_results.txt

END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

# Analyse des résultats
SUCCESS=$(grep -c "200" /tmp/stress_results.txt || true)
FAILED=$(grep -v -c "200" /tmp/stress_results.txt || true)

echo "--- RAPPORT DE PERFORMANCE ---"
echo "Temps total d'exécution : ${DURATION}s"
echo "Requêtes réussies (200) : $SUCCESS"
echo "Requêtes échouées       : $FAILED"
echo "-------------------------------"

rm -f /tmp/stress_results.txt

if [ "$FAILED" -gt 0 ]; then
  exit 1
else
  exit 0
fi
