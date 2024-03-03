from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_sentiment_scores(text):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(text)
    return ss['compound']

reviews = [
"The fluffy orange cat napped peacefully in a sunbeam.",
"A forgotten painting sat nestled in the dusty attic.",
"The aroma of freshly baked cookies filled the kitchen.",
"Waves crashed against the rocky shore, their echoes carrying on the salty breeze.",
"He stumbled across an ancient tome filled with cryptic symbols.",
"Laughter and the strumming of a guitar drifted through the open window.",
"The spaceship hurtled through the vast expanse of the cosmos.",
"Rain pattered against the rooftop, creating a soothing rhythm.",
"A vibrant blue butterfly danced among the wildflowers.",
"She whispered her secrets to the old oak tree.",
"The bustling marketplace overflowed with vibrant colors and exotic aromas.",
"His heart fluttered like the wings of a hummingbird.",
"A mischievous grin spread across her face.",
"The clock ticked incessantly, a constant reminder of passing time.",
"Lost in thought, he wandered aimlessly down the winding path.",
"She hummed a forgotten melody as she prepared dinner.",
"His laughter echoed through the empty halls.",
"Shadows danced and flickered in the firelight.",
"The smell of rain-soaked earth hung heavy in the air.",
"With trembling hands, he opened the antique locket.",
"A hidden trail led to an enchanted waterfall.",
"The detective meticulously studied the cryptic message.",
"They shared a secret smile beneath the starry sky.",
"Music pulsated through the crowded nightclub.",
"Sunlight filtering through the leaves created dappled patterns on the ground.",
"The city skyline sparkled with a thousand glittering lights.",
"Whispers of a forgotten legend lingered in the ancient ruins.",
"Intricate carvings adorned the weathered stone walls.",
"A majestic dragon soared through the painted sunset.",
"Their voices blended in a harmonious chorus.",
"Fear gnawed at her as she ventured into the darkened cave.",
"Sand swirled around her bare feet with each step on the windswept beach.",
"The vibrant tapestry depicted a scene from an age-old myth.",
"The scent of lavender carried her back to a cherished childhood memory.",
"His touch was gentle, like the brush of butterfly wings.",
"A playful dolphin leapt from the sparkling waves.",
"The campfire crackled and popped, sending sparks swirling into the night sky.",
"The world faded away as their eyes met across the room.",
"Adventure awaited beyond the distant horizon.",
"Her words flowed effortlessly, painting vivid pictures in his mind.",
"A sense of peace descended upon him as he gazed up at the swirling galaxy.",
"The taste of sweet berries burst on her tongue.",
"Delicate blossoms unfurled their petals beneath the warm sun.",
"The rhythm of the ocean waves provided a sense of tranquility.",
"Her smile radiated warmth and kindness.",
"A lone sailboat drifted gently across the calm lake.",
"The weathered sign creaked in the gentle breeze.",
"Golden leaves swirled and danced in the autumn air.",
"Their eyes locked, sharing a silent understanding.",
"With a sense of determination, she embarked upon her new journey."
]

for i in reviews:
    a = get_sentiment_scores(i)
    print(a)