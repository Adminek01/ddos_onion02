# ddos_onion02.

### Instalacja modułów

Aby program działał poprawnie, musisz upewnić się, że masz odpowiednie moduły zainstalowane. W tym przypadku używamy standardowej biblioteki Python, więc nie trzeba nic dodatkowo instalować.

### Komendy

1. **Uruchomienie programu:**
   ```bash
   python3 nazwa_programu.py -t <adres_ip_celu> -p <port_celu> -c <liczba_początkowych_połączeń>
   ```
   - Przykład: `python3 ddos-onion.py -t 192.168.1.1 -p 80 -c 100`

2. **Argumenty:**
   - `-t` lub `--target`: Adres IP celu.
   - `-p` lub `--port`: Port, na którym działa cel.
   - `-c` lub `--connections`: Liczba początkowych połączeń.

### Jak działa program

Program ten implementuje atak Slowloris, który polega na utrzymaniu jak największej liczby niekompletnych połączeń z serwerem docelowym, aby go przeciążyć. Program tworzy początkowe połączenia, utrzymuje je i co pewien czas wysyła "keep-alive headers", co utrzymuje te połączenia otwarte.

### Uwaga

1. **Legalność:**
   - Przeprowadzanie ataków DDoS na systemy, do których nie masz zgody, jest nielegalne. Upewnij się, że masz zgodę przed przeprowadzeniem testów na danej sieci.

2. **Ostrzeżenia:**
   - Program ten jest pokazany jedynie w celach edukacyjnych i nie powinien być używany do celów nielegalnych ani szkodliwych.

3. **Monitoring:**
   - Jeśli używasz tego narzędzia w kontrolowanym środowisku, zawsze monitoruj i testuj na własnej odpowiedzialności.

Pamiętaj, że odpowiedzialne i etyczne korzystanie z takich narzędzi jest kluczowe.
