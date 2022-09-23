stage_descriptions = {
        0:[
    "You're excited about your new seed.",
    "You wonder what kind of plant your seed will grow into.",
    "You're ready for a new start with this plant.",
    "You're tired of waiting for your seed to grow.",
    "You wish your seed could tell you what it needs.",
    "You can feel the spirit inside your seed.",
    "These pretzels are making you thirsty.",
    "Way to plant, Ann!",
    "'To see things in the seed, that is genius' - Lao Tzu",
    ],
        1:[
    "The seedling fills you with hope.",
    "The seedling shakes in the wind.",
    "You can make out a tiny leaf - or is that a thorn?",
    "You can feel the seedling looking back at you.",
    "You blow a kiss to your seedling.",
    "You think about all the seedlings who came before it.",
    "You and your seedling make a great team.",
    "Your seedling grows slowly and quietly.",
    "You meditate on the paths your plant's life could take.",
    ],
        2:[
    "The {} {} makes you feel relaxed.",
    "You sing a song to your {} {}.",
    "You quietly sit with your {} {} for a few minutes.",
    "Your {} {} looks pretty good.",
    "You play loud techno to your {} {}.",
    "You play piano to your {} {}.",
    "You play rap music to your {} {}.",
    "You whistle a tune to your {} {}.",
    "You read a poem to your {} {}.",
    "You tell a secret to your {} {}.",
    "You play your favorite record for your {} {}.",
    ],
        3:[
    "{}Your {} is growing nicely!",
    "{}You're proud of the dedication it took to grow your {}.",
    "{}You take a deep breath with your {}.",
    "{}You think of all the words that rhyme with {}.",
    "{}The {} looks full of life.",
    "{}The {} inspires you.",
    "{}Your {} makes you forget about your problems.",
    "{}Your {} gives you a reason to keep going.",
    "{}Looking at your {} helps you focus on what matters.",
    "{}You think about how nice this {} looks here.",
    "{}The buds of your {} might bloom soon.",
    ],
        4:[
    "The {} flowers look nice on your {}!",
    "The {} flowers have bloomed and fill you with positivity.",
    "The {} flowers remind you of your childhood.",
    "The {} flowers remind you of spring mornings.",
    "The {} flowers remind you of a forgotten memory.",
    "The {} flowers remind you of your happy place.",
    "The aroma of the {} flowers energize you.",
    "The {} {} has grown beautiful flowers."
    "The {} petals remind you of that favorite shirt you lost.",
    "The {} flowers remind you of your crush.",
    "You smell the {} flowers and are filled with peace.",
    ],
        5:[
    "You fondly remember the time you spent caring for your {} {}.",
    "Seed pods have grown on your {} {}.",
    "You feel like your {} {} appreciates your care.",
    "The {} fills you with love.",
    "You're ready for whatever comes after your {} {}.",
    "You're excited to start growing your next plant.",
    "You reflect on when your {} {} was just a seedling.",
    "You grow nostalgic about the early days with your {} {}.",
    ],
        99:[
    "You wish you had taken better care of your plant.",
    "If only you had watered your plant more often..",
    "Your plant is dead, there's always next time.",
    "You cry over the withered leaves of your plant.",
    "Your plant died. Maybe you need a fresh start.",
    ],
}

def get_stage_description(stage: int, number: int, species: str, color: str) -> str:
    return stage_descriptions[stage][number].format(color, species)

plant_art_list = [
    'poppy',
    'cactus',
    'aloe',
    'flytrap',
    'jadeplant',
    'fern',
    'daffodil',
    'sunflower',
    'baobab',
    'lithops',
    'hemp',
    'pansy',
    'iris',
    'agave',
    'ficus',
    'moss',
    'sage',
    'snapdragon',
    'columbine',
    'brugmansia',
    'palm',
    'pachypodium',
    ]

stage_list = [
    'seed',
    'seedling',
    'young',
    'mature',
    'flowering',
    'seed-bearing',
]

color_list = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'indigo',
    'violet',
    'white',
    'black',
    'gold',
    'rainbow',
]

rarity_list = [
    'common',
    'uncommon',
    'rare',
    'legendary',
    'godly',
]

species_list = [
    'poppy',
    'cactus',
    'aloe',
    'venus flytrap',
    'jade plant',
    'fern',
    'daffodil',
    'sunflower',
    'baobab',
    'lithops',
    'hemp',
    'pansy',
    'iris',
    'agave',
    'ficus',
    'moss',
    'sage',
    'snapdragon',
    'columbine',
    'brugmansia',
    'palm',
    'pachypodium',
]

mutation_list = [
    '',
    'humming',
    'noxious',
    'vorpal',
    'glowing',
    'electric',
    'icy',
    'flaming',
    'psychic',
    'screaming',
    'chaotic',
    'hissing',
    'gelatinous',
    'deformed',
    'shaggy',
    'scaly',
    'depressed',
    'anxious',
    'metallic',
    'glossy',
    'psychedelic',
    'bonsai',
    'foamy',
    'singing',
    'fractal',
    'crunchy',
    'goth',
    'oozing',
    'stinky',
    'aromatic',
    'juicy',
    'smug',
    'vibrating',
    'lithe',
    'chalky',
    'naive',
    'ersatz',
    'disco',
    'levitating',
    'colossal',
    'luminous',
    'cosmic',
    'ethereal',
    'cursed',
    'buff',
    'narcotic',
    'gnu/linux',
    'abraxan', # rip dear friend
]