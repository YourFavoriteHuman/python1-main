# Jaynan Carrasquillo 1/17/2025
# 10 subs
# colors where subbed
# proper capitalization


RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m' # called to return to standard terminal text color



place = input("name a place: ")
color = input("name a color: ")
verb1 = input("name a verb: ")
place2 = input("name another place: ")
action = input("name an action: ")
color2 = input("name another color: ")
adjective = input("name an adjective: ")
feeling = input("name a feeling: ")
sound = input("name a sound: ")
noun = input("name a plural noun: ")
noun2 = input("name another noun: ")
object1 = input("name an object: ")

story = f"""I was the first to step onto the surface of {RED + place.lower() + RESET}, the {GREEN + color.lower() + RESET} dust swirling beneath my boots as {YELLOW + place2.lower() + RESET} seemed a distant memory.
The silence was overwhelming, a vast stillness that made every {BLUE + action.lower() + RESET} feel like a small victory against the void. As I looked up at the {MAGENTA + color2.lower() + RESET} sky,
I realized how {CYAN + adjective.lower() + RESET} I truly was, but the thought didn’t scare me, it made me feel {RED + feeling.lower() + RESET}. A tiny {GREEN + sound.lower() + RESET} from my suit reminded me I had a limited supply of {YELLOW + noun.lower() + RESET}, 
and I smiled, knowing I was part of something greater than a {BLUE + noun2.lower() + RESET}. In that moment, I understood the universe wasn’t just a place to {MAGENTA + verb1.lower() + RESET}, it was a canvas, and I was leaving my {CYAN + object1.lower() + RESET}."""

print(story)