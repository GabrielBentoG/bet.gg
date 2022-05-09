import requests

region = ['br1']
america = ['br1', 'la1', 'la2','na1']
asia = ['jp1', 'kr', 'oc', 'tr']
europe = ['eun1', 'euw1', 'ru']
'''
Regions:
br1 - Brazil
eun1 - Europe Nordic
euw1 - Europe West
jp1 - Japan
kr - Korea
la1 or la2 - LAS
na1 - North America
oc1 - Oceania
ru - Russia
tr - Turkey
'''
if region[0] in america:
    region.append('americas')
elif region[0] in asia:
    region.append('asia')
elif region[0] in europe:
    region.append('europe')


nickname = str(input("Nick em jogo: ")).replace(' ', '').lower()


# Nome do jogador
summoner = requests.get(f"https://{region[0]}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{nickname}?api_key=RGAPI-f1949d59-a01b-4b3e-a86b-80a143389c3e")
# Transforma as informações do jogador em um dicionário
summoner = summoner.json()


# RiotID
riotid = requests.get(f"https://{region[1]}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{summoner['puuid']}?api_key=RGAPI-f1949d59-a01b-4b3e-a86b-80a143389c3e")
riotid = riotid.json()


# Rank do jogador
rank = requests.get(f"https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner['id']}?api_key=RGAPI-f1949d59-a01b-4b3e-a86b-80a143389c3e")
rank = rank.json()


# Dicionário do jogador
jogador = {'Nick': summoner['name'], 'Riot ID': riotid['gameName'] + '#' + riotid['tagLine'],
           'Level': summoner['summonerLevel']}
if len(rank) != 0:
    if rank[0]['queueType'] == 'RANKED_SOLO_5x5':
        # Estatísticas rankeada
        jogador['Elo [SOLO/DUO]'] = f"{rank[0]['tier']} {rank[0]['rank']} {rank[0]['leaguePoints']} PDL"
        jogador['Partidas [RANKED]'] = f"{int(rank[0]['wins']) + int(rank[0]['losses'])} PARTIDAS"
        jogador['VITÓRIAS'] = f"{int(rank[0]['wins'])}"
        jogador['DERROTAS'] = f"{int(rank[0]['losses'])}"
    else:
        jogador['Elo'] = f"{summoner['name']} possui rank em outro modo"
else:
    jogador['Elo'] = f"{summoner['name']} não possui rank"

for k, v in jogador.items():
    # Exibe os dados do jogador
    print(f"{k} -> {v}")


#print(jogador)
#print(summoner)
#print(riotid)
#print(rank)
#print(len(rank))


