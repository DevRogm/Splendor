markers = ['emerald', 'sapphire', 'ruby', 'diamond', 'onyx', 'gold']

aristocratic_cards = [
    {'requirements': {'emerald': 3, 'sapphire': 3, 'diamond': 3}, 'points': 3, 'img': ''},
    {'requirements': {'onyx': 4, 'ruby': 4}, 'points': 3, 'img': ''},
    {'requirements': {'onyx': 3, 'sapphire': 3, 'diamond': 3}, 'points': 3, 'img': ''},
    {'requirements': {'onyx': 3, 'ruby': 3, 'emerald': 3}, 'points': 3, 'img': ''},
    {'requirements': {'onyx': 4, 'diamond': 4}, 'points': 3, 'img': ''},
    {'requirements': {'emerald': 3, 'sapphire': 3, 'ruby': 3}, 'points': 3, 'img': ''},
    {'requirements': {'ruby': 4, 'emerald': 4}, 'points': 3, 'img': ''},
    {'requirements': {'sapphire': 4, 'diamond': 4}, 'points': 3, 'img': ''},
    {'requirements': {'onyx': 3, 'ruby': 3, 'diamond': 3}, 'points': 3, 'img': ''},
    {'requirements': {'sapphire': 4, 'emerald': 4}, 'points': 3, 'img': ''}]

# Lvl 3 cards ===============================================================================

# 3 pts, 4 stones
cards_3_3_4 = [
    {'bonus': 'sapphire', 'lvl': 3, 'points': 3, 'requirements': {'diamond': 3, 'emerald': 3, 'ruby': 3, 'onyx': 5},
     'img': '1cs.png'},
    {'bonus': 'ruby', 'lvl': 3, 'points': 3, 'requirements': {'diamond': 3, 'sapphire': 5, 'emerald': 3, 'onyx': 3},
     'img': '2cs.png'},
    {'bonus': 'diamond', 'lvl': 3, 'points': 3, 'requirements': {'sapphire': 3, 'emerald': 3, 'ruby': 5, 'onyx': 3},
     'img': '3cs.png'},
    {'bonus': 'onyx', 'lvl': 3, 'points': 3, 'requirements': {'diamond': 3, 'sapphire': 3, 'emerald': 5, 'ruby': 3},
     'img': '4cs.png'},
    {'bonus': 'emerald', 'lvl': 3, 'points': 3, 'requirements': {'diamond': 5, 'sapphire': 3, 'ruby': 3, 'onyx': 3},
     'img': '5cs.png'},
]

# 4 pts, 1 stone
cards_3_4_1 = {'sapphire': {'pts': 4, 'requirements': {'diamond': 7}, 'img': '6cs.png'},
               'ruby': {'pts': 4, 'requirements': {'emerald': 7}, 'img': '7cs.png'},
               'diamond': {'pts': 4, 'requirements': {'onyx': 7}, 'img': '8cs.png'},
               'onyx': {'pts': 4, 'requirements': {'ruby': 7}, 'img': '9cs.png'},
               'emerald': {'pts': 4, 'requirements': {'sapphire': 7}, 'img': '10cs.png'},
               }

# 4 pts, 3 stones
cards_3_4_3 = {'sapphire': {'pts': 4, 'requirements': {'diamond': 6, 'sapphire': 3, 'onyx': 3}, 'img': '11cs.png'},
               'ruby': {'pts': 4, 'requirements': {'sapphire': 3, 'emerald': 6, 'ruby': 3}, 'img': '12cs.png'},
               'diamond': {'pts': 4, 'requirements': {'diamond': 3, 'ruby': 3, 'onyx': 6}, 'img': '13cs.png'},
               'onyx': {'pts': 4, 'requirements': {'emerald': 3, 'ruby': 6, 'onyx': 3}, 'img': '14cs.png'},
               'emerald': {'pts': 4, 'requirements': {'diamond': 3, 'sapphire': 6, 'emerald': 3}, 'img': '15cs.png'},
               }

# 5 pts, 2 stones
cards_3_5_2 = {'sapphire': {'pts': 5, 'requirements': {'diamond': 7, 'sapphire': 3}, 'img': '16cs.png'},
               'ruby': {'pts': 5, 'requirements': {'emerald': 7, 'ruby': 3}, 'img': '17cs.png'},
               'diamond': {'pts': 5, 'requirements': {'diamond': 3, 'onyx': 7}, 'img': '18cs.png'},
               'onyx': {'pts': 5, 'requirements': {'ruby': 7, 'onyx': 3}, 'img': '19cs.png'},
               'emerald': {'pts': 5, 'requirements': {'sapphire': 7, 'emerald': 3}, 'img': '20cs.png'},
               }
# ===========================================================================================================

# Lvl 2 cards
# 3 pts, 1 stone
cards_2_3_1_v1 = {'sapphire': {'pts': 3, 'requirements': {'sapphire': 6}, 'img': '21cs.png'},
                  'ruby': {'pts': 3, 'requirements': {'ruby': 6}, 'img': '22cs.png'},
                  'diamond': {'pts': 3, 'requirements': {'diamond': 6}, 'img': '23cs.png'},
                  'onyx': {'pts': 3, 'requirements': {'onyx': 6}, 'img': '24cs.png'},
                  'emerald': {'pts': 3, 'requirements': {'emerald': 6}, 'img': '25cs.png'},
                  }

# 2 pts, 1 stone
cards_2_3_1_v2 = {'sapphire': {'pts': 2, 'requirements': {'sapphire': 5}, 'img': '26cs.png'},
                  'ruby': {'pts': 2, 'requirements': {'onyx': 5}, 'img': '27cs.png'},
                  'diamond': {'pts': 2, 'requirements': {'ruby': 5}, 'img': '28cs.png'},
                  'onyx': {'pts': 2, 'requirements': {'diamond': 5}, 'img': '29cs.png'},
                  'emerald': {'pts': 2, 'requirements': {'emerald': 5}, 'img': '30cs.png'},
                  }

# 2 pts, 2 stones
cards_2_2_2 = {'sapphire': {'pts': 2, 'requirements': {'diamond': 5, 'sapphire': 3}, 'img': '31cs.png'},
               'ruby': {'pts': 2, 'requirements': {'diamond': 3, 'onyx': 5}, 'img': '32cs.png'},
               'diamond': {'pts': 2, 'requirements': {'ruby': 5, 'onyx': 3}, 'img': '33cs.png'},
               'onyx': {'pts': 2, 'requirements': {'ruby': 3, 'emerald': 5}, 'img': '34cs.png'},
               'emerald': {'pts': 2, 'requirements': {'sapphire': 5, 'emerald': 3}, 'img': '35cs.png'},
               }

# 1 pts, 3 stones, version 1
cards_2_1_3_v1 = {'sapphire': {'pts': 1, 'requirements': {'emerald': 2, 'sapphire': 2, 'ruby': 3}, 'img': '36cs.png'},
                  'ruby': {'pts': 1, 'requirements': {'diamond': 2, 'onyx': 3, 'ruby': 2}, 'img': '37cs.png'},
                  'diamond': {'pts': 1, 'requirements': {'emerald': 3, 'ruby': 2, 'onyx': 2}, 'img': '38cs.png'},
                  'onyx': {'pts': 1, 'requirements': {'diamond': 3, 'sapphire': 2, 'emerald': 2}, 'img': '39cs.png'},
                  'emerald': {'pts': 1, 'requirements': {'diamond': 2, 'sapphire': 3, 'onyx': 2}, 'img': '40cs.png'},
                  }

# 1 pts, 3 stones, version 2
cards_2_1_3_v2 = {'sapphire': {'pts': 1, 'requirements': {'emerald': 3, 'sapphire': 2, 'onyx': 3}, 'img': '41cs.png'},
                  'ruby': {'pts': 1, 'requirements': {'sapphire': 3, 'onyx': 3, 'ruby': 2}, 'img': '42cs.png'},
                  'diamond': {'pts': 1, 'requirements': {'diamond': 2, 'ruby': 3, 'sapphire': 3}, 'img': '43cs.png'},
                  'onyx': {'pts': 1, 'requirements': {'diamond': 3, 'onyx': 2, 'emerald': 3}, 'img': '44cs.png'},
                  'emerald': {'pts': 1, 'requirements': {'diamond': 3, 'emerald': 2, 'ruby': 3}, 'img': '45cs.png'},
                  }

# 2 pts, 3 stones
cards_2_2_3 = {'sapphire': {'pts': 2, 'requirements': {'diamond': 2, 'ruby': 1, 'onyx': 4}, 'img': '46cs.png'},
               'ruby': {'pts': 2, 'requirements': {'sapphire': 4, 'diamond': 1, 'emerald': 2}, 'img': '47cs.png'},
               'diamond': {'pts': 2, 'requirements': {'emerald': 1, 'ruby': 4, 'onyx': 2}, 'img': '48cs.png'},
               'onyx': {'pts': 2, 'requirements': {'sapphire': 1, 'emerald': 4, 'ruby': 2}, 'img': '49cs.png'},
               'emerald': {'pts': 2, 'requirements': {'diamond': 4, 'sapphire': 2, 'onyx': 1}, 'img': '50cs.png'},
               }

# ===========================================================================================================

# Lvl 1 cards
# 1 pt, 1 stone
cards_1_1_1 = {'sapphire': {'pts': 1, 'requirements': {'ruby': 4}, 'img': '51cs.png'},
               'ruby': {'pts': 1, 'requirements': {'diamond': 4}, 'img': '52cs.png'},
               'diamond': {'pts': 1, 'requirements': {'emerald': 4}, 'img': '53cs.png'},
               'onyx': {'pts': 1, 'requirements': {'sapphire': 4}, 'img': '54cs.png'},
               'emerald': {'pts': 1, 'requirements': {'onyx': 4}, 'img': '55cs.png'},
               }

# 0 pt, 1 stone
cards_1_1_0 = {'sapphire': {'pts': 0, 'requirements': {'onyx': 3}, 'img': '56cs.png'},
               'ruby': {'pts': 0, 'requirements': {'diamond': 3}, 'img': '57cs.png'},
               'diamond': {'pts': 0, 'requirements': {'sapphire': 3}, 'img': '58cs.png'},
               'onyx': {'pts': 0, 'requirements': {'emerald': 3}, 'img': '59cs.png'},
               'emerald': {'pts': 0, 'requirements': {'ruby': 3}, 'img': '60cs.png'},
               }

# 0 pt, 2 stones, version 1
cards_1_2_0_v1 = {'sapphire': {'pts': 0, 'requirements': {'diamond': 1, 'onyx': 2}, 'img': '61cs.png'},
                  'ruby': {'pts': 0, 'requirements': {'sapphire': 2, 'emerald': 1}, 'img': '62cs.png'},
                  'diamond': {'pts': 0, 'requirements': {'ruby': 2, 'onyx': 1}, 'img': '63cs.png'},
                  'onyx': {'pts': 0, 'requirements': {'ruby': 1, 'emerald': 2}, 'img': '64cs.png'},
                  'emerald': {'pts': 0, 'requirements': {'diamond': 2, 'sapphire': 1}, 'img': '65cs.png'},
                  }

# 0 pt, 2 stones, version 2
cards_1_2_0_v2 = {'sapphire': {'pts': 0, 'requirements': {'emerald': 2, 'onyx': 2}, 'img': '66cs.png'},
                  'ruby': {'pts': 0, 'requirements': {'diamond': 2, 'ruby': 2}, 'img': '67cs.png'},
                  'diamond': {'pts': 0, 'requirements': {'sapphire': 2, 'onyx': 2}, 'img': '68cs.png'},
                  'onyx': {'pts': 0, 'requirements': {'diamond': 2, 'emerald': 2}, 'img': '69cs.png'},
                  'emerald': {'pts': 0, 'requirements': {'ruby': 2, 'sapphire': 2}, 'img': '70cs.png'},
                  }

# 0 pt, 3 stones, version 1
cards_1_3_0_v1 = {'sapphire': {'pts': 0, 'requirements': {'diamond': 1, 'emerald': 2, 'ruby': 2}, 'img': '71cs.png'},
                  'ruby': {'pts': 0, 'requirements': {'onyx': 2, 'diamond': 2, 'emerald': 1}, 'img': '72cs.png'},
                  'diamond': {'pts': 0, 'requirements': {'emerald': 2, 'sapphire': 2, 'onyx': 1}, 'img': '73cs.png'},
                  'onyx': {'pts': 0, 'requirements': {'diamond': 1, 'emerald': 2, 'ruby': 2}, 'img': '74cs.png'},
                  'emerald': {'pts': 0, 'requirements': {'sapphire': 1, 'ruby': 2, 'onyx': 2}, 'img': '75cs.png'},
                  }

# 0 pt, 3 stones, version 2
cards_1_3_0_v2 = {'sapphire': {'pts': 0, 'requirements': {'sapphire': 1, 'emerald': 3, 'ruby': 1}, 'img': '76cs.png'},
                  'ruby': {'pts': 0, 'requirements': {'ruby': 1, 'diamond': 1, 'onyx': 3}, 'img': '77cs.png'},
                  'diamond': {'pts': 0, 'requirements': {'diamond': 3, 'sapphire': 1, 'onyx': 1}, 'img': '78cs.png'},
                  'onyx': {'pts': 0, 'requirements': {'onyx': 1, 'emerald': 1, 'ruby': 3}, 'img': '79cs.png'},
                  'emerald': {'pts': 0, 'requirements': {'sapphire': 3, 'diamond': 1, 'emerald': 1}, 'img': '80cs.png'},
                  }

# 0 pt, 4 stones, version 1
cards_1_4_0_v1 = {'sapphire':
                      {'pts': 0, 'requirements': {'diamond': 1, 'emerald': 1, 'ruby': 1, 'onyx': 1}, 'img': '81cs.png'},
                  'ruby':
                      {'pts': 0, 'requirements': {'diamond': 1, 'sapphire': 1, 'emerald': 1, 'onyx': 1},
                       'img': '82cs.png'},
                  'diamond':
                      {'pts': 0, 'requirements': {'sapphire': 1, 'emerald': 1, 'ruby': 1, 'onyx': 1},
                       'img': '83cs.png'},
                  'onyx':
                      {'pts': 0, 'requirements': {'diamond': 1, 'sapphire': 1, 'emerald': 1, 'ruby': 1},
                       'img': '84cs.png'},
                  'emerald':
                      {'pts': 0, 'requirements': {'diamond': 1, 'sapphire': 1, 'ruby': 1, 'onyx': 1},
                       'img': '85cs.png'},
                  }

# 0 pt, 4 stones, version 2
cards_1_4_0_v2 = {'sapphire':
                      {'pts': 0, 'requirements': {'diamond': 1, 'emerald': 1, 'ruby': 2, 'onyx': 1}, 'img': '86cs.png'},
                  'ruby':
                      {'pts': 0, 'requirements': {'diamond': 2, 'sapphire': 1, 'emerald': 1, 'onyx': 1},
                       'img': '87cs.png'},
                  'diamond':
                      {'pts': 0, 'requirements': {'sapphire': 1, 'emerald': 2, 'ruby': 1, 'onyx': 1},
                       'img': '88cs.png'},
                  'onyx':
                      {'pts': 0, 'requirements': {'diamond': 1, 'sapphire': 2, 'emerald': 1, 'ruby': 1},
                       'img': '89cs.png'},
                  'emerald':
                      {'pts': 0, 'requirements': {'diamond': 1, 'sapphire': 1, 'ruby': 1, 'onyx': 2},
                       'img': '90cs.png'},
                  }

cards_lvl_3 = [cards_3_4_1, cards_3_3_4, cards_3_4_3, cards_3_5_2]
cards_lvl_2 = [cards_2_1_3_v1, cards_2_1_3_v2, cards_2_2_3, cards_2_3_1_v1, cards_2_3_1_v2, cards_2_2_2]
cards_lvl_1 = [cards_1_1_0, cards_1_4_0_v2, cards_1_4_0_v1, cards_1_1_1, cards_1_3_0_v2, cards_1_2_0_v2, cards_1_3_0_v1,
               cards_1_2_0_v1]
