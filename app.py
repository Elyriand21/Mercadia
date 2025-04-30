import os
import time
import sys


def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def loading_text(text, duration, steps=5):
    interval = duration / steps
    for i in range(steps + 1):
        print(f"\r{text}{'.' * i}{' ' * (steps - i)}", end="")
        sys.stdout.flush()
        time.sleep(interval)
    print("\r" + " " * (len(text) + steps + 1) + "\r", end="")


def slow_print(text, delay=0.1):
    """Prints text character by character with a delay.

    Args:
      text: The string to print.
      delay: Time delay in seconds between printing each character.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


name: str = input("Type your name please: ")
print(f"\nHello {name}, welcome to my Choose Your Own Adventure!")

should_start_game = input(
    "Would you like to start the game? (y/n): ").strip().lower()
if should_start_game == "n" or should_start_game == "no":
    print("Okay, maybe next time!")
    exit()
else:
    loading_text("Loading your adventure", 5)
    clear_screen()

    start = ("You wake up in a place that feels unfamiliar — your head throbbing, your memory foggy. The air smells of damp earth and distant smoke. You're lying on a forest floor, a worn leather satchel by your side. \n" +
             "Inside, you find three things: a flickering compass that spins wildly, a weathered journal with half its pages missing, and a small, glass vial filled with a glowing blue liquid.\n" +
             "As you rise to your feet, you notice three paths branching from the clearing. To the north, the forest thickens and a strange humming noise pulses from deep within the trees.\n" +
             "To the east, you see a crumbling stone road leading toward the ruins of what might have once been a city.\n" +
             "A distant rumble shakes the ground.\n\n" +
             "What do you do?\n" +
             "Head" + "\033[1m" + " north " + "\033[0m" + "into the humming forest.\n" +
             "Follow the road" + "\033[1m" + " east " + "\033[0m" + "toward the ruins.\n\n")

    slow_print(start, 0.01)

    direction: str = input("Type your choice: ").strip().lower()
    # User decides to follow the road east
    if direction == "east":
        clear_screen()
        slow_print("\n" + "The road is cracked and overtaken by vines. As you walk, the journal’s pages flutter open to a map that seems to sketch itself in real time—marking a path toward a building labeled “The Archive\".\n" +
                   "Smoke rises faintly from that direction. When you arrive, you find a shattered city swallowed by time. Towering structures lean dangerously, and moss coats everything. Yet, among the rubble, lights flicker in the distance.\n\n" + 
                   "You hear movement — someone… or something… is alive here.\n\n" +
                   "You approach the Archive. Its massive doors are ajar. As you enter, a mechanical eye on the ceiling whirs to life and scans you.", 0.01)
        slow_print("\n\n" + "\x1B[3m" + "Identity: Unknown. Initiating Trial Protocol." + "\x1B[0m\n\n", 0.15)
        slow_print("Metal panels slide open, revealing two corridors — one lined with statues, the other dark and unmarked.\n\n" +
                   "Do you:\n\n" +
                   "Take the " + "\033[1m" + "corridor " + "\033[0m" + "lined with statues.\n" +
                   "\033[1m" + "Enter " + "\033[0m"+ "the dark, unmarked passage.\n" +
                   "Attempt to " + "\033[1m" + "flee" + "\033[0m" + " the Archive.\n\n", 0.01)
    
    # User decides to go into forest
    if direction == "north":
        clear_screen()
        slow_print("\n" + "You begin to walk north beneath the shadowed canopy, the light dimming with every step. The humming grows louder — not mechanical, but", 0.01)
        slow_print ("...alive.\n", 0.15)
        slow_print("The trees here twist unnaturally, their bark veined with faintly glowing lines, pulsing in rhythm with the hum.\n\n" +
                   "Suddenly, your compass jerks in your hand and points directly ahead. The vial in your satchel grows warm.\n\n" +
                   "As you push deeper, the forest opens into a circular glade. Floating in the center is a stone monolith, covered in glowing symbols — the same ones faintly etched in the journal.\n" +
                   "Before you can examine it, the ground trembles, and a voice — neither male nor female — echoes inside your mind:\n\n", 0.01)
        slow_print("\x1B[3m" + "You carry the Key. Speak the truth, or be unmade." + "\x1B[0m\n\n", 0.15)
        slow_print("Do you:\n" +
                   "\033[1m" + "Open " + "\033[0m" + "the journal and attempt to read the symbols aloud.\n" +
                   "\033[1m" + "Drink " + "\033[0m" + "the glowing liquid.\n" +
                   "\033[1m" + "Run " + "\033[0m" + "back the way you came.\n\n", 0.01)
        direction: str = input("Type your choice: ").strip().lower()

        if direction == "run":
            # User decides to run back into clearing
            clear_screen()
            slow_print("\n" + "You turn and sprint back into the forest, the hum fading behind you. The trees seem to close in, branches clawing at your clothes.\n" +
                       "You see the previous two paths branching from the clearing yet, as you enter the clearing - the pathway into the forest you just came from suddenly is encased by vines, growing in grotesque shapes.\n" +
                       "To the east, you see a crumbling stone road leading toward the ruins of what might have once been a city.\n" +
                       "A distant rumble shakes the ground.\n\n" +
                       "What do you do?\n" +
                       "Follow the road" + "\033[1m" + " east " + "\033[0m" + "toward the ruins.\n", 0.01)
