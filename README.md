# Enumeracja
Nmap, Vuln skan, Enum4linux, Dirb/Dirbuster, WPScan, SNMPWalk

Enumeracja to prosty skrypt w języku Python, który umożliwia przeprowadzenie różnych rodzajów skanowania i enumeracji na podstawie wyboru użytkownika. 
Skrypt wykorzystuje narzędzia takie jak 
Nmap, enum4linux, Dirb/Dirbuster, WPScan i SNMPWalk do przeprowadzenia skanowania i dostarcza wyniki w konsoli.

Wymagania
Aby uruchomić skrypt, musisz mieć zainstalowane następujące narzędzia:

Nmap
enum4linux
Dirb/Dirbuster
WPScan
SNMPWalk
Instrukcje
Sklonuj repozytorium lub pobierz plik enumeracja.py na swój komputer.

Upewnij się, że wymienione powyżej narzędzia są zainstalowane i dostępne w środowisku.

Uruchom skrypt, wykonując następujące polecenie w terminalu:

Copy code
python enumeracja.py
Na ekranie zostanie wyświetlony baner z nazwą "Enumeracja" oraz lista dostępnych opcji skanowania i enumeracji.

Wybierz odpowiednią opcję, wpisując odpowiedni numer i postępuj zgodnie z dalszymi instrukcjami, aby podać adres IP, URL lub inne dane wymagane przez narzędzie.

Skrypt wykonuje skanowanie lub enumerację przy użyciu wybranego narzędzia i wyświetla wyniki w konsoli.

Wyniki skanowania są również zapisywane w pliku "scan_results.txt".

Po zakończeniu skanowania lub enumeracji skrypt zakończy działanie, a na ekranie zostanie wyświetlony komunikat "Scanning completed!".

Opcje skanowania i enumeracji
Skrypt oferuje następujące opcje skanowania i enumeracji:

OS scan - Przeprowadza skanowanie systemu operacyjnego hosta przy użyciu narzędzia Nmap.

Vulnerability scan - Wykonuje skanowanie podatności przy użyciu narzędzia Nmap.

Enum4linux - Przeprowadza enumerację usług SMB przy użyciu narzędzia enum4linux.

Dirb/Dirbuster - Wykonuje skanowanie katalogów i plików na podanym adresie URL przy użyciu narzędzia Dirb/Dirbuster.

WPScan - Przeprowadza skanowanie podatności na podanym adresie URL przy użyciu narzędzia WPScan.

SNMPWalk - Przeprowadza enumerację usług SNMP na podanym adresie IP przy użyciu narzędzia SNMPWalk.

Uwaga: Upewnij się, że masz odpowiednie uprawnienia i zgody do przeprowadzania skanowania lub enumeracji na danym adresie IP lub URL.
Niezgodne użycie tego skryptu może naruszać prawo i prowadzić do konsekwencji prawnych
