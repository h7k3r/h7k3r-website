"""Gear products for h7k3r.com: one page each at /gear/<slug>/ (scripts/build_gear_pages.py).

Names, one-liners and prices must match the cards in the Gear tab of index.html.
Copy rules: say what each item is for and how to check it works; no health claims,
no specs we haven't measured, no "in stock" claims. Images are illustrations.
"""

PRODUCTS = [
    dict(
        slug="faraday-pouch", img="pouch", name="Faraday Pouch", price="25.00",
        line="Stop phone tracking & keyless car theft.",
        title="Faraday Pouch for Phones & Car Keys",
        desc="Faraday pouch for your phone or keyless car fob: blocks its signals while it's closed, so it can't be tracked or relayed by car thieves. £25 from H7K3R Systems.",
        intro="Drop your phone or keyless car fob inside, fold the top over, and it's cut off: no mobile signal, Wi-Fi, Bluetooth, GPS or NFC while the pouch is closed.",
        uses=[
            ("Keyless car theft", "Thieves use a relay box to carry your fob's signal from the hallway to the car on the drive. A fob in a closed pouch has nothing to relay."),
            ("Tracking", "A phone in the pouch can't report its location or be pinged until you take it out."),
            ("Meetings and travel", "Take a phone fully off every network without switching it off."),
        ],
        check=[
            "Put your phone in, close the top and call it from another phone. It should go straight to voicemail.",
            "For a car key: stand next to the car with the fob in the closed pouch and pull the door handle. The car should stay locked.",
            "Repeat the test every few months. Folds and seams wear with daily use.",
        ],
        note="Tell us your phone or key fob when you order and we'll confirm it fits.",
    ),
    dict(
        slug="usb-data-blocker", img="usb-blocker", name="USB Data Blocker", price="15.00",
        line="Safe public charging. Blocks data pins.",
        title="USB Data Blocker for Safe Public Charging",
        desc="USB data blocker: charge at airports, hotels and on trains without the port being able to read or change your phone. Power passes, data doesn't. £15 from H7K3R Systems.",
        intro="It sits between your cable and any USB port you don't control. Power gets through; the data pins don't, so a tampered charging point can't read your phone or install anything on it.",
        uses=[
            ("Public charging", "Airports, hotels, trains, cafés and hire-bike docks: charge from the port without trusting it."),
            ("Hire cars and borrowed laptops", "Charge without your contacts, photos or messages syncing to somebody else's system."),
            ("Work and travel kit", "Small enough to keep with your cables and chargers."),
        ],
        check=[
            "Plug your phone in through the blocker. It should charge, but never ask to \"Trust this computer\" or offer file transfer.",
            "Some fast-charge modes use the data pins, so charging can be slower through a blocker. That's expected.",
        ],
        note="Use it with your own charging cable on the other side.",
    ),
    dict(
        slug="faraday-sleeve", img="sleeve", name="Faraday Sleeve", price="45.00",
        line="Complete offline laptop isolation.",
        title="Faraday Laptop Sleeve",
        desc="Faraday laptop sleeve: zip it shut and the laptop inside can't connect to or be reached over Wi-Fi, Bluetooth or mobile data. £45 from H7K3R Systems.",
        intro="A laptop sleeve lined with signal-blocking fabric. Zip it shut and the machine inside can't connect to Wi-Fi, Bluetooth or mobile data, or be reached through them.",
        uses=[
            ("Travel", "Keep a laptop off every network until you decide to connect it."),
            ("Evidence and data handling", "Keep a device isolated so nothing on it can be changed or wiped remotely."),
            ("Air-gapped machines", "An offline machine stays offline while it's carried around."),
        ],
        check=[
            "Test it with a phone: zip the phone inside and call it. If it rings, the zip isn't fully closed.",
            "Keep the zip clean and fully closed; any gap lets signal through.",
        ],
        note="Send us your laptop model when you order so we can confirm the fit.",
    ),
    dict(
        slug="signal-proof-hat", img="hat", name="Signal-Proof Hat", price="35.00",
        line="Silver-lined EMF protection.",
        title="Signal-Proof Hat with Silver Lining",
        desc="Signal-proof cap with a silver-lined crown, from H7K3R Systems' privacy gear range. £35.",
        intro="A cap with a silver-lined crown that blocks radio signals passing through it. Part of the H7K3R privacy gear range.",
        uses=[
            ("Everyday wear", "A normal-looking cap with a signal-blocking lining."),
            ("Privacy kit", "Pairs with the Faraday Pouch and Stealth Backpack."),
        ],
        check=[
            "The lining blocks signals through the crown only, and it is not a medical device: we don't make any health claims for it.",
        ],
        note="Ask about sizes and colours when you order.",
    ),
    dict(
        slug="stealth-backpack", img="backpack", name="Stealth Backpack", price="120.00",
        line="Built-in Faraday compartments.",
        title="Stealth Backpack with Faraday Compartments",
        desc="Everyday backpack with signal-blocking Faraday compartments for your phone, keys and cards built in. £120 from H7K3R Systems.",
        intro="An everyday backpack with signal-blocking compartments built in, so your phone, keys and cards can be cut off from every network without a separate pouch.",
        uses=[
            ("Commute and travel", "Phone, car key and contactless cards in one shielded compartment, everything else in the main bag."),
            ("Laptop days", "Pairs with the Faraday Sleeve when the laptop needs to stay offline too."),
        ],
        check=[
            "Put a phone in the Faraday compartment, close it and call the phone. It should go straight to voicemail.",
        ],
        note="Ask for dimensions and compartment sizes before you order.",
    ),
    dict(
        slug="faraday-parka", img="parka", name="Faraday Parka", price="185.00",
        line="Full-Body EMF Shielding jacket.",
        title="Faraday Parka",
        desc="Faraday parka lined with signal-blocking fabric, from H7K3R Systems' privacy gear range. £185.",
        intro="A parka lined with signal-blocking fabric. Devices carried inside it are cut off from mobile, Wi-Fi and Bluetooth signals.",
        uses=[
            ("Privacy on the move", "Carry your phone and keys shielded without a separate pouch."),
            ("Winter coat", "A warm parka first, with the lining built in."),
        ],
        check=[
            "Put a phone in an inside pocket, close the jacket and call the phone. It should go straight to voicemail.",
            "It's clothing, not a medical device: we don't make any health claims for it.",
        ],
        note="Ask about sizes when you order.",
    ),
    dict(
        slug="operator-hoodie", img="hoodie", name="Operator Hoodie", price="65.00",
        line="Heavyweight Tactical Cotton.",
        title="Operator Hoodie",
        desc="Heavyweight cotton Operator Hoodie from H7K3R Systems. £65.",
        intro="A heavyweight cotton hoodie in the H7K3R look, made for long sessions at the bench or the keyboard.",
        uses=[
            ("Everyday wear", "Heavyweight cotton in the H7K3R style."),
        ],
        check=[],
        note="Ask about sizes and colours when you order.",
    ),
    dict(
        slug="precision-bit-set", img="bits", name="Precision Bit Set", price="45.00",
        line="S2 Steel Device Teardown Kit.",
        title="Precision Bit Set for Phone, Laptop & Console Repair",
        desc="S2 steel precision bit set for opening phones, laptops, consoles and controllers: the kind of kit used on the H7K3R Systems repair bench. £45.",
        intro="S2 steel precision bits and a driver for opening phones, laptops, consoles and controllers: the kind of kit used on our own repair bench.",
        uses=[
            ("Home repairs", "Battery swaps, cleaning a noisy console, swapping a laptop SSD or fixing a drifting controller stick."),
            ("Hobbyists", "PC builds, retro consoles and modding projects."),
        ],
        check=[
            "Before opening anything, check whether it's still under warranty: opening it can void that.",
            "Disconnect the battery first on phones and laptops before touching the board.",
            "Stuck on a repair? Send us the device instead.",
        ],
        note="",
    ),
]
