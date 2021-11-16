# Aaah!

# Jon Marius shouted too much at the recent Justin Bieber concert, and now needs to go to the doctor 
# because of his sore throat. The doctor’s instructions are to say “aaah”. Unfortunately, the doctors 
# sometimes need Jon Marius to say “aaah” for a while, which Jon Marius has never been good at. Each 
# doctor requires a certain level of “aah” – some require “aaaaaah”, while others can actually diagnose 
# his throat with just a “h”. (They often diagnose wrongly, but that is beyond the scope of this problem.) 
# Since Jon Marius does not want to go to a doctor and have his time wasted, he wants to compare how 
# long he manages to hold the “aaah” with the doctor’s requirements. (After all, who wants to be all 
# like “aaah” when the doctor wants you to go “aaaaaah”?)

# Output “go” if Jon Marius can go to that doctor, and output “no” otherwise.

jonAh = input()
doctorAh = input()
if(len(jonAh) >= len(doctorAh)):
    print('go')
else:
    print('no')