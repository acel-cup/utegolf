# ACEL CUP

Filer:
- `index.html` – forside / leaderboard
- `register.html` – innlogging, spillerprofil og registrering av runde
- `admin.html` – adminpanel for filtrering og sletting av runder

## Supabase
Prosjektet bruker:
- URL: `https://geduwhzlwdphouslxhsd.supabase.co`
- Publishable key: lagt inn i filene

## Viktig
For at admin-sletting skal fungere, må `admin_users` være satt opp i Supabase.

## Kjør lokalt
Du kan kjøre prosjektet som statiske filer, for eksempel:

```bash
python3 -m http.server 3000
