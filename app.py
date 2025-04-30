import os
import time
import sys


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def loading_text(text, duration, steps=5):
    interval = duration / steps
    for i in range(steps + 1):
        print(f"\r{text}{'.' * i}{' ' * (steps - i)}", end="")
        sys.stdout.flush()
        time.sleep(interval)
    print("\r" + " " * (len(text) + steps + 1) + "\r", end="")


def slow_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def intro():
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
        start_game()

def title_screen():
    clear_screen()
    return_to_title = input(
        "\nWould you like to return to the title screen and start again? (y/n): ").strip().lower()
    if return_to_title == "y" or return_to_title == "yes":
            clear_screen()
            start_game()  # Call the game function again to restart
    else:
        print("Thank you for playing! Goodbye.")
        exit()


def start_game():
    start = (
        "You wake up in a place that feels unfamiliar — your head throbbing, your memory foggy. The air smells of damp earth and distant smoke. You're lying on a forest floor, a worn leather satchel by your side. \n"
        "Inside, you find three things: a flickering compass that spins wildly, a weathered journal with half its pages missing, and a small, glass vial filled with a glowing blue liquid.\n"
        "As you rise to your feet, you notice four paths branching from the clearing.\n"
        "To the north, the forest thickens and a strange humming noise pulses from deep within the trees.\n"
        "To the east, you see a crumbling stone road leading toward the ruins of what might have once been a city.\n"
        "To the south, you spot a mist-covered bridge stretching into a canyon.\n"
        "To the west, there's an ancient archway filled with swirling blue mist.\n"
        "A distant rumble shakes the ground.\n\n"
        "What do you do?\n"
        "Head\033[1m north \033[0minto the humming forest.\n"
        "Follow the road\033[1m east \033[0mto the ruins.\n"
        "Venture\033[1m south \033[0mto the misty bridge.\n"
        "Step\033[1m west \033[0mthrough the archway.\n\n")
    slow_print(start, 0.01)
    direction = input("Type your choice: ").strip().lower()

    # EAST: City/Ruins/Archive Path
    if direction == "east":
        clear_screen()
        slow_print("\nThe road is cracked and overtaken by vines...", 0.01)
        slow_print("The journal’s pages flutter open to a map that sketches itself, marking a building labeled 'The Archive'.\n", 0.01)
        slow_print(
            "Smoke rises faintly. You reach a ruined city. Towers lean dangerously.\n", 0.01)
        slow_print(
            "You hear movement. You approach the Archive. A mechanical eye scans you.\n", 0.01)
        slow_print(
            "\n\x1B[3mIdentity: Unknown. Initiating Trial Protocol.\x1B[0m\n\n", 0.15)
        slow_print(
            "Two corridors open: one with statues, the other dark.\nFlee, or choose one?\n\n")
        choice = input("Type your choice: ").strip().lower()

        if choice == "corridor":
            slow_print(
                "\nThe statues seem to whisper. A mural reveals your face among them.\nYou were always part of this place.\n\n\x1B[1mYou have remembered.\x1B[0m\nTHE END.")
            title_screen()
        elif choice == "enter":
            slow_print(
                "\nYou walk into darkness and fall into stars.\nYou are now part of the Archive itself.\n\n\x1B[1mYou fade, but are not gone.\x1B[0m\nTHE END.")
            title_screen()
        elif choice == "flee":
            slow_print(
                "\nYou flee the Archive. The city collapses.\n\n\x1B[1mSome truths are not for the faint.\x1B[0m\nTHE END.")
            title_screen()
        else:
            print("Invalid choice. Game over.")

    # NORTH: Forest/Glade/Monolith Path
    elif direction == "north":
        clear_screen()
        slow_print("\nThe forest hums with life...", 0.01)
        slow_print(
            "Trees glow faintly. The vial grows warm.\nYou enter a glade with a floating stone monolith.\n", 0.01)
        slow_print(
            "A voice echoes: \x1B[3mYou carry the Key. Speak the truth, or be unmade.\x1B[0m\n", 0.15)
        slow_print("\nDo you: Open the journal, Drink the liquid, or Run?\n\n")
        action = input("Type your choice: ").strip().lower()

        if action == "run":
            clear_screen()
            slow_print("\nYou flee back to the clearing. The forest seals itself behind you.\nOnly the road east, the bridge south, and the archway west remain.\n", 0.01)
            direction = input("Do you want to go east, south, or west?: ").strip().lower()
             # SOUTH: The Underbridge
            if direction == "south":
                clear_screen()
                slow_print("\nMist surrounds you as you step onto the bridge. The canyon below whispers your name.\nEach plank creaks with ancient warning.\n", 0.01)
                slow_print(
                    "At the center of the bridge, a cloaked figure blocks your path.\n'To cross, you must give up a memory.'\n\n")
                slow_print("They lift their hood. It is a young woman with sunken eyes and a trembling voice.\n'My name is Elyra. I was once a traveler like you. I gave up my memory of love to cross... but I can't remember who I was crossing for.'\n")
                slow_print("She clutches her arms. 'We met on the cliff's edge, promised to return. But I crossed first, thinking I'd guide the way. Now... I can't remember their face. Only the ache.'\n")
                slow_print(
                    "She hands you a small locket. 'Do you remember them for me? Or do you cross and forget?'\n")
                slow_print("She hesitates. 'Sometimes I dream of their voice. A song in the rain... a hand reaching out. I hold onto that. But dreams fade, don't they?'\n")
                slow_print(
                    "Elyra gazes into the canyon. 'I wonder if they waited. I wonder if they crossed and forgot me too.'\n\n")
                choice = input("Do you (remember / cross / retreat)?: ").strip().lower()
                if choice == "remember":
                    slow_print(
                        "\nYou hold the locket. Her memory floods into you — a lover waiting on the other side.\nTears fill her eyes. 'Thank you...' She fades into mist.\n\x1B[1mYou carry her story now.\x1B[0m\nTHE END.")
                    title_screen()
                elif choice == "cross":
                    slow_print(
                        "\nYou give up your most cherished memory and walk across. Elyra watches, forgotten.\n\x1B[1mYou are free, but hollow.\x1B[0m\nTHE END.")
                    title_screen()
                elif choice == "retreat":
                    slow_print(
                        "\nYou step back. The bridge groans. Elyra remains.\n\x1B[1mSome doors must stay closed.\x1B[0m\nTHE END.")
                    title_screen()
                else:
                    print("Invalid choice. Game over.")

            # WEST: The Whispering Vault
            elif direction == "west":
                clear_screen()
                slow_print("\nYou step through the archway. A thousand voices whisper.\nYou find yourself in a vault where time loops on itself.\n", 0.01)
                slow_print("A boy sits at a table of mirrors, weeping.\n'I tried to find her,' he says.\n'But every door just showed me myself.'\n")
                slow_print("'I'm Lorian. She was my sister. Lost when the vault shifted.'\n")
                slow_print("He shows you a mirror — it flickers through scenes. 'We were orphans. She was all I had. The vault promised a future. But it lied.'\n")
                slow_print("He trembles. 'They said it could undo time. I wanted to undo the day she vanished. The fire. The screaming. I held the door. I thought she was behind me.'\n")
                slow_print("Lorian looks at you, voice cracking. 'But when I turned... she was gone. I gave everything to chase a reflection.'\n")
                slow_print("He points to three doors: Flame, Ice, and Echo.\n'She went into one. I went into all. None led me to her.'\n")
                door = input("Which door do you enter? (flame/ice/echo): ").strip().lower()

                if door == "flame":
                    slow_print(
                        "\nThe door burns away your fear. Inside is a room of fire — and Lorian’s sister, asleep.\nShe wakes and smiles.\n\x1B[1mYou lead her home.\x1B[0m\nTHE END.")
                    title_screen()
                elif door == "ice":
                    slow_print(
                        "\nThe cold steals your breath. You find only a broken mirror and silence.\nLorian collapses.\n\x1B[1mNot every search has an end.\x1B[0m\nTHE END.")
                    title_screen()
                elif door == "echo":
                    slow_print(
                        "\nThe echoes repeat your steps. You see yourself lost in time. Lorian’s voice fades.\n\x1B[1mYou never left.\x1B[0m\nTHE END.")
                    title_screen()
                else:
                    print("Invalid choice. Game over.")
        elif action == "drink":
            slow_print(
                "\nYou drink. Memories flood you. The forest accepts you.\nYou find a hidden city of light.\n\n\x1B[1mYou are now part of its story.\x1B[0m\nTHE END.")
            title_screen()
        elif action == "open":
            slow_print(
                "\nYou speak the truth. The symbols engrave on your skin.\n\x1B[1mYou carry their legacy.\x1B[0m\nTHE END.")
            title_screen()
        else:
            print("Invalid choice. Game over.")

# Start the game
intro()
