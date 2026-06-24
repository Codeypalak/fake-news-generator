import random
print("fake news generator")
subjects=["shaharuk khan","salman khan","palak","modi ji","my friend"]
actions=["launches","eat","dance with","celebrate","orders"]
places=["at red fort","a plate of samosa","in station","inside parliament","in park"]
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(places)
    headline=f" Breaking News:{subject} {action} {place} "
    print("\n"+ headline)
    user=input("\nDo You Want a New Headline(yes/no)").strip().lower()
    if user=="no":
        break
print("thanks using fake news generator")
 
