# EthicalHammer.py

### Instalacja 

**Opis:**
"Ethical Hammer" to narzędzie przeznaczone do etycznego testowania penetracyjnego, które skupia się na wykonywaniu powolnych ataków typu POST w celu sprawdzenia odporności serwera internetowego na tego rodzaju działania. Znaczącą cechą narzędzia jest możliwość korzystania z anonimizacji poprzez sieć Tor, co pozwala na dodatkowe zabezpieczenie tożsamości podczas testów.

**Instrukcja użycia:**
```bash
./ethical_hammer.py -t <cel> [-r <wątki> -p <port> -T -h]
```

**Argumenty:**
- `-t` lub `--target`: Określa docelowy adres IP lub nazwę hosta.
- `-r` lub `--threads`: Liczba wątków do użycia (domyślnie 256).
- `-p` lub `--port`: Numer portu serwera internetowego (domyślnie 80).
- `-T` lub `--tor`: Opcjonalne, włącza anonimizację poprzez sieć Tor na adresie 127.0.0.1:9150.
- `-h` lub `--help`: Wyświetla instrukcję użycia.

**Przykład użycia:**
```bash
./ethical_hammer.py -t 192.168.1.100 -r 256
```

**Ważne:**
Zanim zaczniesz używać tego narzędzia, upewnij się, że masz wyraźną zgodę do przeprowadzenia testów penetracyjnych. Używaj narzędzia z odpowiedzialnością i zgodnie z obowiązującymi przepisami prawnymi.


### Uwaga

1. **Legalność:**
   - Przeprowadzanie ataków DDoS na systemy, do których nie masz zgody, jest nielegalne. Upewnij się, że masz zgodę przed przeprowadzeniem testów na danej sieci.

2. **Ostrzeżenia:**
   - Program ten jest pokazany jedynie w celach edukacyjnych i nie powinien być używany do celów nielegalnych ani szkodliwych.

3. **Monitoring:**
   - Jeśli używasz tego narzędzia w kontrolowanym środowisku, zawsze monitoruj i testuj na własnej odpowiedzialności.

Pamiętaj, że odpowiedzialne i etyczne korzystanie z takich narzędzi jest kluczowe.
