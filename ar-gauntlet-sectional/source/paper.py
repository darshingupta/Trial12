# Content of the AR sectional. Each passage: title, kind, intro, conditions, questions.
# Each question: stem, options (4), ans (0-3), why (explanation), trap (what the usual wrong pick does).

CONVENTIONS = [
    "Left and right are always judged from the person's own position, in the direction he or she faces.",
    "'X sits second to the right of Y' means X is the second person counted from Y towards Y's right; one person sits between them.",
    "In a circle, 'n persons sit between X and Y' is true when exactly n persons sit between them along at least one of the two arcs.",
    "Every condition in a passage is true. A question that adds or removes a condition does so for that question only.",
]

P = []

# ---------------------------------------------------------------- Passage I
P.append(dict(
title="Passage I: The Round Table",
kind="Circular arrangement, mixed facing",
intro=("Eight lawyers, Anvi, Bharat, Charu, Dev, Esha, Faiz, Gia and Hari, sit around a circular table at equal distances. "
       "Some of them face the centre of the table and the rest face away from it. Two of them are Judges, two are Advocates, "
       "two are Professors and two are Clerks."),
conds=[
 "Charu sits third to the left of Gia.",
 "As many of the eight face the centre as face away from it.",
 "Faiz sits immediately to the right of Esha, and Esha sits immediately to the right of Faiz.",
 "Exactly one person sits between Dev and Bharat, and that person faces the same direction as Anvi.",
 "Dev faces away from the centre.",
 "Neither of Faiz's immediate neighbours faces the same direction as Faiz.",
 "Bharat faces the same direction as exactly one of Bharat's two immediate neighbours.",
 "Hari sits second to the left of Gia.",
 "The two Judges sit directly opposite each other.",
 "One of Faiz's immediate neighbours is a Clerk who faces the centre; the other is a Professor.",
 "The person sitting second to the left of Hari is an Advocate.",
 "Bharat and Esha have the same profession.",
 "Dev is not a Professor.",
 "No Advocate sits next to a Judge.",
],
solution=("Going clockwise (seen from above): Anvi (faces centre, Judge), Dev (away, Clerk), Gia (centre, Advocate), "
          "Bharat (away, Professor), Hari (away, Judge), Charu (centre, Clerk), Faiz (away, Advocate), Esha (centre, Professor). "
          "This is the only arrangement that satisfies all fourteen conditions."),
key_steps=[
 "Condition 3 is the hinge: Faiz and Esha can each be on the other's right only if they are neighbours facing opposite ways.",
 "Condition 8 says Hari is second to Gia's left. With Condition 11 this makes the pairing mutual, so Gia is the Advocate that Condition 11 names.",
 "Condition 4 puts one seat between Dev and Bharat. That middle seat is Gia, who faces the centre like Anvi.",
],
qs=[
 dict(stem=("Three of the following four pairs are alike: in each, the second person occupies the same position relative to the first person, "
            "judged from the first person's own left and right. Which pair is the odd one out?"),
      opts=["Bharat – Faiz","Esha – Gia","Anvi – Charu","Dev – Hari"], ans=1,
      why=("Bharat (faces away) has Faiz third to his right; Dev (faces away) has Hari third to his right; Anvi (faces the centre) has Charu third to her right, "
           "counted anticlockwise. Esha faces the centre, so her right runs anticlockwise; Gia is three seats clockwise from her, which is third to her LEFT."),
      trap=("On a seating diagram, Esha to Gia is three seats clockwise, exactly like Bharat to Faiz and Dev to Hari, while Anvi to Charu runs the other way. "
            "So anyone who ignores facing marks 'Anvi – Charu'.")),
 dict(stem="For how many of the eight lawyers does the person sitting third to his or her left face the same direction as he or she does?",
      opts=["Two","Four","Six","Eight"], ans=2,
      why=("Count each lawyer's left with that lawyer's own facing. Anvi's third left is Bharat (no). Bharat's is Anvi (no). The other six match: "
           "Dev's third left is Faiz, Gia's Charu, Hari's Dev, Charu's Anvi, Faiz's Hari, Esha's Gia. Charu and Anvi both face the centre; Faiz and Hari both face away."),
      trap=("Counting everyone's left as clockwise, as if all faced the centre, gives a different set. The four people who face away are where solvers slip, "
            "and dropping one or two of them gives 'Four'.")),
 dict(stem=("Which of the following is/are true?\n"
            "I. Exactly three persons sit between the two Professors, whichever way one counts.\n"
            "II. Each Clerk sits immediately to the right of an Advocate.\n"
            "III. Each Judge has a Clerk as an immediate neighbour."),
      opts=["Only I and III","Only I","Only II and III","Only III"], ans=0,
      why=("I: The Professors are Bharat and Esha, who sit opposite each other, so three persons sit between them on each side. True. "
           "II: Dev is immediately to the right of Gia, an Advocate. Charu, however, is immediately to the right of Hari, a Judge. "
           "Charu is next to the Advocate Faiz, but on Faiz's left. False. "
           "III: Anvi is next to Dev and Hari is next to Charu. True."),
      trap="II looks true because each Clerk physically touches an Advocate; only Dev is on an Advocate's right."),
 dict(stem="Which one of the following conditions could be dropped without changing the seat of any person or the direction any person faces?",
      opts=["Condition 2","Condition 7","Condition 10","Condition 11"], ans=3,
      why=("Without Condition 11 there are two solutions with the same seats and facing; only the Judge/Advocate labels of Anvi, Hari, Gia and Faiz swap. "
           "Without 2, Bharat could face the centre. Without 7, Dev and Bharat swap seats. Without 10, two more seatings appear."),
      trap="Condition 11 looks like a seating clue, but once the rest are in place it only fixes professions."),
 dict(stem=("Suppose Charu and Esha exchange seats, each keeping the direction he or she faces, and nothing else changes. "
            "Which of the conditions would then be violated?"),
      opts=["Condition 3 only","Conditions 1 and 3 only","Conditions 1, 3 and 10 only","Conditions 3, 6 and 10 only"], ans=1,
      why=("Charu moves next to Gia, so Charu is no longer third to Gia's left (Condition 1). Esha now sits on Faiz's left, not his right, and Faiz is not on hers (Condition 3). "
           "Faiz's neighbours are still a centre-facing Clerk (Charu) and a Professor (Esha), and both still face the centre, so Conditions 10 and 6 hold. "
           "Nobody's facing or profession changes, so Conditions 2, 9, 12 and 14 hold too."),
      trap="Conditions 6 and 10 are about Faiz's neighbours, so the swap looks as if it must break them. The same two kinds of neighbour simply trade sides."),
]))

# ---------------------------------------------------------------- Passage II
P.append(dict(
title="Passage II: The Two Rings",
kind="Concentric circular arrangement",
intro=("Twelve participants of a mediation workshop, Kabir, Leela, Mohan, Naina, Omkar, Pari, Qadir, Rhea, Sahil, Tara, Uday and Vani, "
       "sit in two concentric circles of six seats each. Everyone in the inner circle faces outward and everyone in the outer circle faces the centre. "
       "The seats are aligned so that each person in the inner circle sits directly facing exactly one person in the outer circle. "
       "'Left', 'right', 'next to', 'between' and 'opposite' refer only to people in the same circle."),
conds=[
 "Rhea sits immediately to the right of Kabir.",
 "Omkar faces the person who sits immediately to the left of Mohan.",
 "Vani and Naina sit in the same circle, with only one person between them.",
 "Leela sits in the outer circle, second to the left of Pari.",
 "Tara faces the person who sits immediately to the left of Rhea.",
 "Qadir faces the person who sits second to the right of Omkar.",
 "Vani faces the person who sits directly opposite Tara.",
 "Uday does not sit next to Kabir, and Sahil does not face Pari.",
],
solution=("Inner circle (facing out), clockwise: Kabir, Rhea, Omkar, Vani, [Sahil or Uday], Naina. "
          "Outer circle (facing in), clockwise and directly facing them: Tara, Mohan, [Uday or Sahil], Pari, Qadir, Leela. "
          "Sahil and Uday can be exchanged, so there are exactly two valid arrangements. Inner-circle people have their right clockwise; "
          "outer-circle people have their right anticlockwise."),
key_steps=[
 "Kabir and Rhea share a circle (1), and Tara faces Kabir (5).",
 "Condition 7 then makes Vani face the person opposite Tara. Condition 2 places Omkar and Mohan, and Condition 6 places Qadir.",
 "No condition separates Sahil from Uday. Condition 8 sounds as if it does, but it holds whichever way they sit.",
],
qs=[
 dict(stem=("Three of the following four groups are alike in the way their three members are placed relative to one another, judged from each person's own left and right. "
            "Which group is the odd one out?"),
      opts=["Kabir, Tara, Qadir","Pari, Vani, Naina","Rhea, Mohan, Leela","Mohan, Rhea, Naina"], ans=3,
      why=("In each group the first person faces the second, and the third sits second to the right of the second. "
           "Kabir faces Tara, and Qadir is second to Tara's right (outer circle, anticlockwise). Pari faces Vani, and Naina is second to Vani's right (inner, clockwise). "
           "Rhea faces Mohan, and Leela is second to Mohan's right. Mohan faces Rhea, but Naina is second to Rhea's LEFT."),
      trap=("Physically, Naina is two seats anticlockwise from Rhea, just as Qadir is from Tara and Leela is from Mohan. "
            "Pari, Vani, Naina looks like the misfit because it goes clockwise. Clockwise means 'right' only in the inner circle.")),
 dict(stem=("Suppose Condition 1 is changed to 'Rhea sits immediately to the left of Kabir', and every other condition stays. "
            "Who would then face Kabir?"),
      opts=["Tara","Qadir","Leela","Pari"], ans=1,
      why=("The whole arrangement has to be rebuilt. Inner circle clockwise: Kabir, Vani, [Sahil or Uday], Naina, Omkar, Rhea. Outer circle, facing them in the same order: "
           "Qadir, Leela, [Uday or Sahil], Mohan, Tara, Pari. Rhea's left neighbour is now Omkar, so Tara faces Omkar (5). Qadir faces Kabir, the seat second to the right of Omkar (6). "
           "Vani faces Leela, who sits opposite Tara (7), and Leela is second to the left of Pari (4)."),
      trap="Carrying over the original 'Tara faces Kabir' gives (A). The change to Condition 1 moves Kabir's whole circle, so nothing from the first solve can be reused."),
 dict(stem="For how many of the twelve participants can the person sitting immediately to his or her right be named with certainty?",
      opts=["Six","Eight","Ten","Twelve"], ans=1,
      why=("Only Sahil and Uday change places, between the inner seat after Vani and the outer seat after Mohan (clockwise). The right-hand neighbour is uncertain for four people: "
           "Vani (her right is that inner seat), Pari (her right runs anticlockwise to that outer seat), and Sahil and Uday themselves, whose right-hand neighbour is Naina "
           "in the inner seat but Mohan in the outer seat. The other eight are certain."),
      trap="'Ten' is the number of people whose seats are fixed. It forgets that Sahil's and Uday's own right-hand neighbours change when they swap."),
 dict(stem="Which of the following must be true?",
      opts=["The person who faces Qadir sits immediately to the right of Vani.","Uday faces Omkar.",
            "Sahil sits second to the left of Kabir.","Exactly one person sits between Tara and Uday."], ans=0,
      why=("Qadir always faces the inner seat after Vani in the clockwise direction, which is Vani's immediate right, whoever sits there. "
           "The other three are true only when Sahil is in the inner circle."),
      trap="(B), (C) and (D) all hold in the first arrangement most solvers find, so they look certain."),
 dict(stem="Which one of the following, if true, would establish that Sahil faces Qadir?",
      opts=["Uday sits immediately to the right of Vani.","Sahil and Uday face in different directions.",
            "The person who faces Uday sits immediately to the left of Vani.","Neither Sahil nor Uday sits next to Tara."], ans=2,
      why=("Sahil faces Qadir only when Sahil takes the inner seat after Vani. Vani's immediate left is Omkar, and Omkar faces Uday only when Uday is in the outer seat, "
           "which puts Sahil in the inner seat facing Qadir. (A) settles the arrangement the other way (Uday faces Qadir). (B) and (D) are true in both arrangements."),
      trap="(A) does fix the arrangement, so it looks like the answer, but it fixes the wrong one: it puts Uday, not Sahil, opposite Qadir."),
]))

# ---------------------------------------------------------------- Passage III
P.append(dict(
title="Passage III: The Five-Storey Block",
kind="Floor-and-flat (tabular) arrangement",
intro=("Eight friends, Ishaan, Juhi, Lalit, Meher, Nikhil, Ojas, Prisha and Ruhi, live in a five-storey building whose floors are numbered 1 (lowest) to 5 (top). "
       "Each floor has two flats, West and East. Every West flat is directly above the West flat of the floor below, and every East flat directly above the East flat. "
       "Each friend lives in a different flat, so exactly two flats are vacant. Each friend plays a different one of eight sports: "
       "Archery, Chess, Hockey, Kabaddi, Polo, Rugby, Squash and Tennis. 'Directly above' means in the same column, exactly one floor higher."),
conds=[
 "Juhi lives in a West flat, directly above Ojas, and nobody else lives on Juhi's floor.",
 "The two vacant flats are on different floors, and exactly one floor lies between those two floors.",
 "Lalit lives directly above the person who plays Polo.",
 "Exactly one floor lies between the Archery player's floor and Prisha's floor.",
 "The Squash player lives in a West flat on a floor that has no vacant flat.",
 "Ruhi lives in a West flat, directly above Nikhil.",
 "Meher lives on a lower floor than Ishaan.",
 "The Tennis player and the Kabaddi player live on the same floor.",
 "The Chess player lives in the same column as the Kabaddi player, at least two floors higher.",
 "The Hockey player lives in an East flat, directly below someone who plays neither Tennis nor Squash.",
 "The Rugby player lives on the floor immediately below the Tennis player's floor.",
],
solution=("Fixed in every case: F5 West Juhi (Archery), F5 East vacant; F4 West Ojas (Squash); F3 West vacant, F3 East Prisha; "
          "F2 West Ruhi (Tennis); F1 West Nikhil (Rugby), F1 East Meher. "
          "Case A: F4 East Lalit (Chess), F2 East Ishaan (Kabaddi), Prisha Polo, Meher Hockey. "
          "Case B: F4 East Ishaan (Chess), F2 East Lalit (Kabaddi), Prisha Hockey, Meher Polo. Both cases satisfy every condition."),
key_steps=[
 "Juhi's floor has a vacancy, so Juhi cannot be on floor 1. Condition 2 then sets the vacancy pattern, and Condition 5 keeps Ojas's floor full.",
 "The Chess and Kabaddi players share the East column (9), and the Kabaddi player's floor also holds Tennis (8). That fixes floors 2 and 4 in the East column.",
 "Lalit's 'directly above Polo' (3) can be met at F4 over F3 or at F2 over F1, and both work. This is where the two cases come from.",
],
qs=[
 dict(stem=("Three of the following four pairs are alike in the way the first-named person's flat is placed relative to the second-named person's flat. "
            "Which pair is the odd one out?"),
      opts=["Juhi – the Chess player","The Chess player – Ruhi","Prisha – the Tennis player","The Squash player – Prisha"], ans=1,
      why=("In each of the other pairs, the first flat is one floor up and diagonally across from the second: F5W to F4E, F3E to F2W, F4W to F3E. "
           "The Chess player (F4E) is two floors above Ruhi (F2W). This holds in both cases, because the Chess player's flat is fixed even though "
           "who plays Chess is not."),
      trap="Solvers who cannot name the Chess player often decide the pair cannot be judged. The Chess player's flat is certain in both cases."),
 dict(stem=("Which of the following can be determined with certainty?\n"
            "I. The floor on which Lalit lives.\n"
            "II. The sport played by the person who lives directly below the Chess player.\n"
            "III. The person who lives directly above the Kabaddi player."),
      opts=["Only I","Only I and III","Only II and III","Only III"], ans=3,
      why=("I: Lalit is on F4 in Case A and F2 in Case B. II: Prisha lives below the Chess player in both cases, but plays Polo in A and Hockey in B. "
           "III: Prisha lives above the Kabaddi player (F2E) in both cases."),
      trap="II looks certain because the person (Prisha) is fixed; her sport is not."),
 dict(stem="If Lalit plays Kabaddi, which of the following must be false?",
      opts=["Prisha plays Hockey.","Ishaan lives directly above Prisha.",
            "The Polo player lives on a floor that has a vacant flat.","Meher lives directly below the Kabaddi player."], ans=2,
      why="Lalit plays Kabaddi only in Case B. There the Polo player is Meher on F1, which has no vacant flat. (A), (B) and (D) are all true in Case B.",
      trap="In Case A, Prisha plays Polo on F3, a floor with a vacancy. Solving only Case A makes (C) look true."),
 dict(stem="For how many of the eight friends can both the flat and the sport be determined with certainty?",
      opts=["Four","Five","Six","Eight"], ans=0,
      why=("Juhi, Ojas, Ruhi and Nikhil: four. Prisha's and Meher's flats are fixed, but their sports swap between Polo and Hockey. "
           "Lalit and Ishaan swap both flat and sport."),
      trap="'Six' counts the six friends whose flats are fixed."),
 dict(stem="Which one of the following, if true, would establish that Meher plays Hockey?",
      opts=["Lalit and Ishaan both live on even-numbered floors.","The Polo player lives directly below the Kabaddi player.",
            "The Hockey player lives on a lower floor than the Chess player.","The Chess player lives directly above the Polo player."], ans=3,
      why=("Meher plays Hockey only in the case where Lalit plays Chess on F4 East and Prisha plays Polo on F3 East, directly below. In the other case Prisha, directly below the Chess player, "
           "plays Hockey, so (D) picks the right case. (B) picks the other case, where Meher plays Polo. (A) and (C) are true in both cases."),
      trap="(B) also settles the arrangement, but in the case where Meher plays Polo. A solver who only asks 'does this fix it?' marks (B)."),
]))

# ---------------------------------------------------------------- Passage IV
P.append(dict(
title="Passage IV: The Lecture Calendar",
kind="Scheduling with unused dates",
intro=("Eight speakers, Sana, Tanay, Urvi, Vihaan, Waseem, Xenia, Yash and Zoya, each deliver exactly one seminar in a lecture series run within one "
       "calendar year that is not a leap year. A seminar can be held only on the 8th or the 23rd of February, April, May, July, September or November, "
       "and no two seminars are held on the same date, so four of these twelve dates go unused. Each seminar is either online or offline. "
       "When the conditions count seminars 'between' two others, or speak of seminars held 'one after the other', they count seminars actually held and ignore unused dates."),
conds=[
 "Only two seminars are held between Sana's seminar and Zoya's seminar.",
 "Tanay's seminar is held in the calendar month that immediately follows the month of Yash's seminar.",
 "No seminar is held after Waseem's.",
 "Xenia and Vihaan speak in the same month, Xenia first.",
 "Urvi's seminar is held in a month that has fewer than 30 days.",
 "No two seminars held one after the other are of the same kind (online or offline).",
 "The first seminar of the series is online.",
 "Tanay's seminar is held on the 23rd.",
 "The number of unused dates before Tanay's seminar equals the number of unused dates after Zoya's seminar.",
 "Urvi's seminar is the only seminar held in its month.",
],
solution=("Urvi: February (8th or 23rd), online. Sana: 8 April, offline. Yash: 23 April, online. Tanay: 23 May, offline. Zoya: 8 July, online. "
          "Xenia: 8 September, offline. Vihaan: 23 September, online. Waseem: November (8th or 23rd), offline. "
          "Fixed unused dates: 8 May and 23 July. The other two unused dates are whichever February and November dates Urvi and Waseem leave free. "
          "That gives four valid schedules."),
key_steps=[
 "Condition 2 forces Yash in April and Tanay in May, the only consecutive calendar months in the list. Condition 8 puts Tanay on 23 May.",
 "Urvi is in February, alone (5, 10), and Waseem is last (3). Xenia and Vihaan need a month to themselves (4).",
 "Conditions 1 and 9 fix Sana in April and Zoya on 8 July. Conditions 6 and 7 then alternate the kinds: online, offline, online, and so on.",
],
qs=[
 dict(stem=("Three of the following four pairs of speakers are alike in where the second-named speaker's seminar falls in the series relative to the first-named speaker's seminar. "
            "Which pair is the odd one out?"),
      opts=["Zoya – the speaker whose seminar is held exactly 46 days away from Zoya's","The first offline speaker – Zoya",
            "Yash – the speaker who speaks immediately after Zoya","The offline speaker whose seminar falls in a 31-day month – Vihaan"], ans=0,
      why=("Decode each description: the first offline speaker is Sana; the speaker after Zoya is Xenia; the offline speaker in a 31-day month is Tanay; "
           "and the only seminar 46 days from 8 July is Tanay's on 23 May (23 August is not a possible date), so that is Tanay too. Sana–Zoya, Yash–Xenia and Tanay–Vihaan each have exactly two seminars between them, "
           "with the first-named speaking earlier. Zoya and Tanay speak one after the other, with Zoya named first though she speaks later."),
      trap="Counting days with 30-day months for May and June gives 45 days, which points to no speaker. Option (A) then seems undecodable and gets skipped."),
 dict(stem=("If the number of days from Urvi's seminar to Sana's seminar is greater than the number of days from Vihaan's seminar to Waseem's seminar, "
            "on which dates are Urvi's and Waseem's seminars held?"),
      opts=["23 February and 8 November","23 February and 23 November","8 February and 23 November","8 February and 8 November"], ans=3,
      why=("8 Feb to 8 Apr is 59 days (February has 28) and 23 Feb to 8 Apr is 44. 23 Sep to 8 Nov is 46 days (October has 31) and 23 Sep to 23 Nov is 61. "
           "Only 59 > 46 works."),
      trap="Giving February 31 days makes 23 Feb to 8 Apr 47 days, which would beat 46 and make (A) look possible as well."),
 dict(stem="Which of the following must be true?",
      opts=["Exactly one unused date lies between Urvi's seminar and Sana's seminar.",
            "As many online seminars are held before Tanay's seminar as offline seminars are held after Zoya's seminar.",
            "Waseem's seminar is held exactly 46 days after Vihaan's seminar.",
            "The last unused date of the year comes after Waseem's seminar."], ans=1,
      why=("Online before Tanay: Urvi and Yash, two. Offline after Zoya: Xenia and Waseem, two. True in all four schedules. "
           "(A), (C) and (D) are each true only when Urvi or Waseem takes the 8th."),
      trap="(A), (C) and (D) are all true in the schedule where both Urvi and Waseem take the 8th, which is the most natural first draft."),
 dict(stem="Suppose Condition 10 is dropped and all the other conditions stay. Which of the following would then be impossible?",
      opts=["Sana's seminar is held on 23 February.","April has an unused date.",
            "Urvi's seminar is held on 23 February and Yash's on 8 April.","Both Urvi's and Waseem's seminars are held on the 8th."], ans=2,
      why=("Without Condition 10, Sana may join Urvi in February, but only if Urvi takes the 8th and Sana the 23rd. "
           "If Urvi takes the 23rd, Sana must still speak on 8 April, which pushes Yash to 23 April. So (C) cannot happen. (A), (B) and (D) can."),
      trap="Once Sana is free to move, it is tempting to think anything in February or April can happen."),
 dict(stem="How many of the speakers could have their seminar held exactly 15 days after one of the twelve possible dates that goes unused?",
      opts=["One","Two","Three","Four"], ans=2,
      why=("Tanay (23 May, after unused 8 May) in every schedule; Urvi, if she speaks on 23 February with 8 February unused; "
           "Waseem, if he speaks on 23 November with 8 November unused. 23 July plus 15 days falls in August, when no seminar can be held."),
      trap="Working from one schedule gives 'One' (only Tanay) or 'Two'. The word 'could' brings in all four schedules."),
]))

# ---------------------------------------------------------------- Passage V (filled in later)
P.append(dict(
title="Passage V: The Family Row",
kind="Blood relations with linear seating, mixed facing",
intro=("Eight members of a three-generation family, B, D, F, G, J, K, S and V, sit in a single row of eight seats numbered 1 to 8 from west to east. "
       "Each faces either north or south. The family is made up of one married couple in the oldest generation, their two children, "
       "the spouse of each of those two children, and two grandchildren, who have the same two parents. Every married couple is one man and one woman. "
       "An aunt is a sister of a parent or the wife of a parent's brother. Nobody's gender is known except as it follows from the conditions."),
conds=[
 "K is the mother-in-law of exactly two members of the family.",
 "J is F's sister.",
 "S is an aunt of J.",
 "The two persons at the ends of the row face opposite directions.",
 "Exactly four members face north.",
 "A grandmother of J sits immediately to J's left.",
 "G sits second to the right of a son-in-law of G.",
 "Exactly three persons sit between D and D's spouse.",
 "F sits at one end of the row and faces the same direction as a grandfather of F.",
 "The person sitting immediately to the right of S is a grandchild of K.",
 "V sits third to the left of J.",
 "G's wife sits third to the right of G.",
 "The person in seat 1 belongs to the youngest generation.",
 "F faces the same direction as F's mother.",
],
solution=("Seats 1 to 8: F (north), S (south), G (north), V (north), B (south), K (south), J (north), D (south). "
          "G and K are the oldest couple. S is their daughter and B is S's husband. D (male) and V (female) are married and are the parents of F and J. "
          "Two things cannot be determined: F's gender, and which of D or V is the child of G and K (the other married into the family). "
          "That makes four valid family trees, all with this seating."),
key_steps=[
 "Seat 1 holds a grandchild (13), and F sits at an end (9). J has a grandmother to her left (6) and V third to her left (11). Together these set the east half of the row.",
 "S's right-hand neighbour is a grandchild (10). Because F is in seat 1, S must be in seat 2 facing south.",
 "Condition 14 needs F's mother to face north like F. That makes V the mother, so D is male. Nothing decides whether D or V is the blood child of G and K.",
],
qs=[
 dict(stem=("Three of the following four pairs are alike: in each, the second person occupies the same position relative to the first person, "
            "judged from the first person's own left and right. Which pair is the odd one out?"),
      opts=["S – B","G – K","B – S","K – G"], ans=0,
      why=("G (seat 3, north) has K third to his right. K (seat 6, south) has G third to her right, since her right runs west. "
           "B (seat 5, south) has S third to his right. S (seat 2, south) has her right running west, where only seat 1 lies. B is third to S's LEFT."),
      trap=("All four are married couples with two people between them, so they look identical. G and K face opposite ways, so 'third to the right' works both ways for them. "
            "B and S face the same way, so it works only one way.")),
 dict(stem="How many members of the family are definitely female?",
      opts=["Three","Four","Five","Cannot be determined"], ans=1,
      why="K, S and J are female by the conditions, and V must be F's mother (Condition 14). F's gender is unknown, but the number of members who are definitely female is four.",
      trap="Since F's gender is open, many mark 'Cannot be determined'. The question asks who is definitely female, and that count is fixed at four."),
 dict(stem="How is the person sitting third to the right of D related to D?",
      opts=["D's sister's husband","D's wife's brother","Either D's brother or D's sister's husband; the conditions do not settle which",
            "Either D's sister's husband or D's wife's sister's husband; the conditions do not settle which"], ans=3,
      why=("D (seat 8) faces south, so his right runs west: J, K, then B. B is S's husband, and S is a daughter of G and K. "
           "If D is G and K's son, S is his sister and B is his sister's husband. If V is their daughter, S is V's sister and B is D's wife's sister's husband. "
           "Nothing in the conditions decides which of D or V is G and K's child."),
      trap="'D's sister's husband' is what the first family tree most solvers draw gives. It assumes the husband is the blood child, which no condition says."),
 dict(stem="Who sits second to the left of the husband of F's aunt?",
      opts=["J","G","K","V"], ans=0,
      why="F's only aunt in the family is S; her husband is B (seat 5, facing south). B's left runs east: K, then J.",
      trap="Treating B as north-facing gives G (seat 3). Reading 'second to the right' instead gives G as well."),
 dict(stem=("Which of the following is/are definitely true?\n"
            "I. G sits second to the right of each of his sons-in-law.\n"
            "II. K's grandchildren face the same direction as each other.\n"
            "III. Exactly one person sits between V and V's mother-in-law."),
      opts=["Only II","Only I and II","Only II and III","I, II and III"], ans=0,
      why=("II: F and J both face north. True in every case. I: if V is G's daughter, D is also G's son-in-law, and D (seat 8, facing south) has K, not G, "
           "second to his right. Not definite. III: true only if D is G's son. If V is G's daughter, V's mother-in-law is not in the family."),
      trap="In the tree most solvers draw first, with D as G's son, all three statements are true."),
]))

# ---------------------------------------------------------------- Passage VI
P.append(dict(
title="Passage VI: The Warehouse Stack",
kind="Vertical (stack) arrangement with weights",
intro=("Seven boxes, E, H, K, M, P, U and W, are stacked one above another in a single stack. Positions are numbered 1 (bottom) to 7 (top). "
       "The boxes weigh 9, 12, 16, 18, 25, 27 and 36 kg, one weight per box, not necessarily in that order."),
conds=[
 "No box is placed above the box that weighs 16 kg.",
 "The weight of K equals the combined weight of the box immediately above K and the box immediately below K.",
 "U weighs exactly twice as much as W.",
 "H is lighter than M but heavier than P.",
 "E weighs exactly as much as the two boxes immediately below E put together.",
 "Exactly two boxes lie between P and the box that weighs 27 kg.",
 "M is placed somewhere above U.",
],
solution="From bottom to top: U 18, K 27, W 9, E 36, P 12, M 25, H 16. This is the only stack that satisfies all seven conditions.",
key_steps=[
 "The only weight pairs that make U twice W are 9 and 18. The only sums of two different weights that equal a third weight are 9+16=25, 9+18=27 and 9+27=36.",
 "K needs two neighbours that add up to its weight, and E needs the two boxes below it to add up to its weight. Each sum uses W at 9, so W sits next to K and two below E.",
 "Condition 4 fixes the order M > H > P. With the 16 kg box on top, the 12/16/25 trio goes to P, H and M. Conditions 6 and 7 then fix the rest.",
],
qs=[
 dict(stem=("Take the boxes of each group below in their order in the stack, from bottom to top, and look at whether the weight rises or falls from one box to the next. "
            "In three of the groups the weights change in the same way. Which group is the odd one out?"),
      opts=["K, P, W","H, K, M","K, M, W","H, K, P"], ans=1,
      why=("Put each group in stack order and read the weights from bottom to top. K, W, P: 27, 9, 12. K, W, M: 27, 9, 25. K, P, H: 27, 12, 16. "
           "In each of these the middle box is the lightest of the three, so the weights fall and then rise. K, M, H gives 27, 25, 16: the middle box is not the lightest, "
           "and the weights fall all the way up."),
      trap=("The letters give nothing away: K is in every group and each other box appears in exactly two. The groups have to be put in stack order first. "
            "Taken in the listed order, K, P, W reads 27, 12, 9, which falls steadily and looks like the misfit.")),
 dict(stem="Suppose Condition 1 is dropped and all the other conditions stay. In how many of the possible stacks would the 16 kg box be placed somewhere below the 25 kg box?",
      opts=["One","Two","Three","Four"], ans=2,
      why=("Without Condition 1 there are four stacks (bottom to top): U K W E P H M; U K W E P M H; H U K W E P M; P H U K W E M. "
           "H is 16 kg and M is 25 kg in all four. H is below M in three of them; only the original stack has H on top."),
      trap="Most solvers find the original stack and one variant with H and M swapped, giving 'One'. The block U-K-W-E can also slide up by one or two places."),
 dict(stem=("Suppose Condition 4 is replaced by: 'H is heavier than M, and M is heavier than P.' All the other conditions stay. "
            "Which of the following could NOT be true?"),
      opts=["H weighs 16 kg.","H is placed at the bottom of the stack.","P is placed immediately below H.","M is placed at the top of the stack."], ans=0,
      why=("The 12/16/25 trio now runs H > M > P, so H is 25, M is 16 and P is 12. M must then be the top box (Condition 1). The stacks are U K W E P H M, "
           "H U K W E P M and P H U K W E M. (B), (C) and (D) each occur; H can never weigh 16 kg."),
      trap="Carrying over the original weights (H 16) makes (A) look like a fixed fact rather than an impossibility."),
 dict(stem="Suppose Condition 7 is dropped and all the other conditions stay. Which of the following would then be true?",
      opts=["Exactly two boxes keep the same position in every possible stack.","P can occupy exactly two different positions.",
            "There are exactly two possible stacks.","All but one of the boxes can each occupy at least two different positions."], ans=3,
      why=("Without Condition 7 there are three stacks (bottom to top): U K W E P M H; M U K W E P H; P M U K W E H. Only H keeps its place. "
           "U, K, W and E each take three positions as their block slides, M takes positions 6, 1 and 2, and P takes 5, 6 and 1. So (D) is true and (A), (B) and (C) are false."),
      trap="Solvers who find only the original stack and the one with M moved to the bottom pick (C), or (B) for P."),
 dict(stem=("Which of the following is/are true?\n"
            "I. The three topmost boxes together weigh more than the three bottommost boxes together.\n"
            "II. Every box whose weight is a perfect square is placed above every box whose weight is not.\n"
            "III. The box in the exact middle of the stack is the heaviest box."),
      opts=["Only II and III","Only I and III","Only III","I, II and III"], ans=2,
      why=("I: top three weigh 12 + 25 + 16 = 53; bottom three weigh 18 + 27 + 9 = 54. False, by 1 kg. "
           "II: W (9, a square) is below P (12, not a square). False. III: position 4 is E, 36 kg. True."),
      trap="I misses by one kilogram, and the four square weights do sit high in the stack, so both I and II feel true."),
]))
