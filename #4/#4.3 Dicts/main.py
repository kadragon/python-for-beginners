player = {
    'name': 'nico',
    'age': 12,
    'alive': True,
    'fav_food': ["🍕", "🍔", "🍟"],
}

print(player.get('age'))
print(player.get('fav_food')[0])

print(player['fav_food'])

player.pop("age")
player['xp'] = 1500

print(player)

player['fav_food'].append("🍘")
