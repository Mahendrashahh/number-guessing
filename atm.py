


#mini desi atm system

while True:
    balance = 10000
    print("🙏 Swagat hai bhai! Gareeb ATM mein aaya hai tu 😎")

    pin = int(input("🔐 Pin daal bhai: "))
    if pin == 1234:
        print("💰 Kitna paisa nikaalna chahta hai?")
        amount = int(input("₹ Amount bata de: "))

        if amount <= balance:
            balance -= amount
            print("⏳ Transaction chal rahi hai... ruk zara...")
            print(f"✅ ₹{amount} nikaal liya gaya. Ab bacha hai ₹{balance}")
        else:
            print("❌ Itna paisa nahi hai bhai, thoda kam daal 😅")
    else:
        print("🚫 Galat pin daala re! Aukaat me reh 😤")

    print("\n📊 Balance check karna hai kya?")
    check = input("(y/n): ")
    if check.lower() == 'y':
        dubara = int(input("🔁 Dobara pin daal: "))
        if dubara == 1234:
            print(f" 😅 Tera current balance hai: ₹{balance}")
        else:
            print("❌ Galat pin firse?! Dimaag theek hai? 😑")
    else:
        print(" Thik hai bhai, chalta hu main 😅")

    repeat = input("\n🔁 Dobara try karega ky ATM? (y/n): ")
    if repeat.lower() != 'y':
        print("Bye bhai! Agli baar paisa leke aana 😂")
        break
