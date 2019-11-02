import unittest
from RPFunctions import trouverNomRP

class TestRPNominator(unittest.TestCase):

    def setUp(self):
        self.data = {
            'Leprechaun' : {
                'numLettreNom' : 0,
                'numLettrePrenom' : 2,
                'Prenom' : {
                    'A' : 'Sprinkles',  'N' : 'Greenie',
                    'B' : 'Daffodil',   'O' : 'Rusty',
                    'C' : 'Fightin\'',  'P' : 'Lucky',
                    'D' : 'Bunyon',     'Q' : 'Fortune',
                    'E' : 'Warty',      'R' : 'Shillelagh',
                    'F' : 'Toadstool',  'S' : 'Goldie',
                    'G' : 'Wooly',      'T' : 'Peevish',
                    'H' : 'Clover',     'U' : 'Fearsome',
                    'I' : 'Blarney',    'V' : 'Potsy',
                    'J' : 'Clumsy',     'W' : 'Dizzy',
                    'K' : 'Thunderous', 'X' : 'Patty',
                    'L' : 'Tater',      'Y' : 'Stumpy',
                    'M' : 'Bleary',     'Z' : 'Whispers',
                },
                'Nom' : {
                    'A' : 'O\'Blaze',   'N' : 'McCoppertop',
                    'B' : 'McTavern',   'O' : 'O\'Gingerly',
                    'C' : 'O\'Rainbow', 'P' : 'McFeverish',
                    'D' : 'McMuffin',   'Q' : 'O\'Cranky',
                    'E' : 'O\'Wobbles', 'R' : 'McCauldron',
                    'F' : 'McFearsome', 'S' : 'McWoozy',
                    'G' : 'O\'Knuckles','T' : 'O\'Shivers',
                    'H' : 'McDoodles',  'U' : 'McSharmless',
                    'I' : 'McBeauty',   'V' : 'O\'Wickless',
                    'J' : 'McWiskey',   'W' : 'McSpud',
                    'K' : 'McTurnship', 'X' : 'McOutrage',
                    'L' : 'O\'Bourbon', 'Y' : 'O\'Lyin',
                    'M' : 'McSmelly',   'Z' : 'McSullied',
                },
            },
            'Youtuber' : {
                'numLettreNom' : 2,
                'numLettrePrenom' : 0,
                'Prenom' : {
                    'A' : 'Alpaga',     'N' : 'Mega',
                    'B' : 'Piaf',       'O' : 'Ultra',
                    'C' : 'Chien',      'P' : 'Truc',
                    'D' : 'Babouin',    'Q' : 'Cookie',
                    'E' : 'Marsupial',  'R' : 'Super',
                    'F' : 'Chat',       'S' : 'Machin',
                    'G' : 'Minou',      'T' : 'Ecolier',
                    'H' : 'Pépé',       'U' : 'Stylo',
                    'I' : 'The',        'V' : 'Fragile',
                    'J' : 'Code',       'W' : 'Biscuit',
                    'K' : 'Michou',     'X' : 'Pyscho',
                    'L' : 'Lama',       'Y' : 'Ibra',
                    'M' : 'Math',       'Z' : 'Piaf',
                },
                'Nom' : {
                    'A' : 'Mécontent',  'N' : 'Gaming',
                    'B' : 'Shows',      'O' : 'Daddy',
                    'C' : 'FondVert',   'P' : 'Films',
                    'D' : 'Studio',     'Q' : 'Véner',
                    'E' : 'Mécontent',  'R' : 'TV',
                    'F' : 'Faché',      'S' : 'Vidéos',
                    'G' : 'Caméra',     'T' : 'Atomic',
                    'H' : 'Tuber',      'U' : 'Furax',
                    'I' : 'Musclé',     'V' : 'Relaax',
                    'J' : 'Pictures',   'W' : 'Perdu',
                    'K' : 'Désorienté', 'X' : 'Director',
                    'L' : 'Podcast',    'Y' : 'Fatigué',
                    'M' : 'Retraité',   'Z' : 'Abstrait',
                },
            },
            'SuperHero' : {
                'numLettreNom' : 1,
                'numLettrePrenom' : 0,
                'Prenom' : {
                    'A' : 'Captain',    'N' : 'Impossible',
                    'B' : 'Night',      'O' : 'Iron',
                    'C' : 'The',        'P' : 'Rocket',
                    'D' : 'Ancient',    'Q' : 'Human',
                    'E' : 'Spider',     'R' : 'Power',
                    'F' : 'Invisible',  'S' : 'Green',
                    'G' : 'Master',     'T' : 'Super',
                    'H' : 'Mr',         'U' : 'Wonder',
                    'I' : 'Silver',     'V' : 'Metal',
                    'J' : 'Dark',       'W' : 'Doctor',
                    'K' : 'Professor',  'X' : 'Masked',
                    'L' : 'Radioactive','Y' : 'Crimson',
                    'M' : 'Incredible', 'Z' : 'Omega',
                },
                'Nom' : {
                    'A' : 'Lightning',  'N' : 'Dardevil',
                    'B' : 'Knight',     'O' : 'Machine',
                    'C' : 'Hulk',       'P' : 'America',
                    'D' : 'Centurion',  'Q' : 'X',
                    'E' : 'Surfer',     'R' : 'Doom',
                    'F' : 'Girl',       'S' : 'Fist',
                    'G' : 'Warrior',    'T' : 'Shadow',
                    'H' : 'Man',        'U' : 'Patriot',
                    'I' : 'Ghost',      'V' : 'Claw',
                    'J' : 'Master',     'W' : 'Torch',
                    'K' : 'Hornet',     'X' : 'Soldier',
                    'L' : 'Phantom',    'Y' : 'Skull',
                    'M' : 'Crusader',   'Z' : 'Woman',
                },
            },
        }


    def test_trouverNomRP(self):
        self.assertEqual(trouverNomRP('Leprechaun','Mateo','Dupont',self.data),'Peevish McMuffin')
        self.assertEqual(trouverNomRP('Youtuber','Leo','Lafete',self.data),'Lama Faché')
        self.assertEqual(trouverNomRP('SuperHero','Samy','Delahaye',self.data),'Green Surfer')
